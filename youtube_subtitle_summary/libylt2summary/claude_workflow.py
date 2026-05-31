"""
Claude Code Workflow Integration
Provides workflow functions that use Claude Code CLI for AI processing
"""
import os
import json
import logging
import asyncio
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime

from . import claude_invoker as _claude_backend
from . import kiro_invoker as _kiro_backend
from .jsonl_handler import jsonl_reader, jsonl_writer, create_error_entry
from .utils import sanitize_filename, sanitize_yaml_string, clean_front_matter

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Backend 切换: "claude" (默认) 或 "kiro"
# 通过 set_backend() 在 run.py 中设置，workflow 函数内部透明使用
# ---------------------------------------------------------------------------
_backend_name: str = "claude"


def set_backend(name: str) -> None:
    """设置 AI CLI 后端 ("claude" 或 "kiro")。"""
    global _backend_name
    if name not in ("claude", "kiro"):
        raise ValueError(f"Unknown backend: {name!r}, expected 'claude' or 'kiro'")
    _backend_name = name
    logger.info(f"AI backend set to: {name}")


def _backend():
    """返回当前后端模块 (claude_invoker 或 kiro_invoker)。"""
    return _kiro_backend if _backend_name == "kiro" else _claude_backend


# 便捷访问 — 这些函数签名在两个 invoker 中完全一致
def invoke_claude(**kwargs):
    return _backend().invoke_claude(**kwargs)

def invoke_skill(**kwargs):
    return _backend().invoke_skill(**kwargs)

def load_skill(*args, **kwargs):
    return _backend().load_skill(*args, **kwargs)

def build_skill_prompt(*args, **kwargs):
    return _backend().build_skill_prompt(*args, **kwargs)

# Change to the youtube_subtitle_summary directory
WORK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def prepare_summarize_input(
    subtitles_dir: str = "subtitles_origin",
    videos_meta: str = "videos_meta.jsonl",
    output_file: str = "temp_input/summarize_input.jsonl"
) -> List[Dict[str, Any]]:
    """
    Prepare input JSONL for summarize skill.

    Args:
        subtitles_dir: Directory containing subtitle files
        videos_meta: Path to videos metadata JSONL
        output_file: Path to output input file

    Returns:
        List of input items
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Get list of already summarized files
    summary_dir = "summary"
    summarized = set()
    if os.path.exists(summary_dir):
        summarized = {f.replace(".md", "") for f in os.listdir(summary_dir) if f.endswith(".md")}

    # Read video metadata
    video_metadata = {}
    if os.path.exists(videos_meta):
        for item in jsonl_reader(videos_meta):
            title = sanitize_filename(item.get('title', '')).replace(".en.ttml", "")
            video_metadata[title] = item

    # Prepare input items
    items = []
    subtitles_path = Path(subtitles_dir)

    if not subtitles_path.exists():
        logger.warning(f"Subtitles directory not found: {subtitles_dir}")
        return items

    for subtitle_file in subtitles_path.glob("*.ttml"):
        # subtitles use "<name>.en.ttml", while summary files are "<name>.md"
        # normalize to the same id format so incremental skip works.
        title = subtitle_file.stem.removesuffix(".en")

        # Skip if already summarized
        if title in summarized:
            logger.info(f"Skipping already summarized: {title}")
            continue

        # Read subtitle content
        try:
            with open(subtitle_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            logger.error(f"Error reading {subtitle_file}: {e}")
            continue

        # Get video metadata
        metadata = video_metadata.get(title, {})

        item = {
            'id': title,
            'content': content[:50000],  # Limit content length
            'video_title': metadata.get('title', title),
            'metadata': {
                'published_at': metadata.get('published_at'),
                'channel': metadata.get('channel'),
                'duration': metadata.get('duration')
            }
        }
        items.append(item)

    # Write input file
    if items:
        jsonl_writer(output_file, items)
        logger.info(f"Prepared {len(items)} items for summarization: {output_file}")

    return items


def _summarize_one_item(item, base_prompt, output_dir, timeout):
    """处理单条 summarize 任务，返回 (result_dict, is_error)。"""
    item_id = item.get("id", "unknown")
    subtitle_content = item.get("content", "")
    video_title = item.get("video_title", item_id)
    metadata = item.get("metadata", {})

    full_prompt = f"""{base_prompt}

请基于以下输入生成完整会议纪要，并严格遵循：
1) 只输出 Markdown 正文，不要输出 JSON，不要用 ``` 包裹。
2) 必须包含这些二级标题：## 摘要、## 关键议题、## 决定事项、## 行动项。
3) 对每个议题给出充分细节，优先使用条目列表表达技术讨论点。
4) 若某信息缺失，请在对应小节写"未在字幕中明确提及"。
5) 保留 Ceph/计算机领域关键英文术语（如 RGW、S3、ETag、KMS）。

视频标题: {video_title}
元数据: {json.dumps(metadata, ensure_ascii=False)}

字幕内容:
{subtitle_content}
"""
    response = invoke_claude(prompt=full_prompt, timeout=timeout)
    if not response.get("success"):
        return create_error_entry(item_id, response.get("error", "Unknown error")), True

    markdown_content = (response.get("output") or "").strip()
    if not markdown_content:
        return create_error_entry(item_id, "Empty markdown output"), True

    output_path = os.path.join(output_dir, f"{item_id}.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content + "\n")

    return {
        "id": item_id,
        "status": "success",
        "result": {"summary_markdown": markdown_content}
    }, False


def run_summarize_workflow(
    input_file: str = "temp_input/summarize_input.jsonl",
    output_dir: str = "summary",
    batch_size: int = 10,
    timeout: int = 300,
    max_workers: int = 1,
) -> Dict[str, Any]:
    """
    Run the summarize workflow using Claude Code.

    Args:
        input_file: Path to input JSONL file
        output_dir: Directory for output summaries
        batch_size: Items per batch
        timeout: Timeout per batch
        max_workers: 并发 CLI 进程数 (默认 1 串行)

    Returns:
        Processing result statistics
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(input_file):
        logger.error(f"Input file not found: {input_file}")
        return {'success': False, 'error': 'Input file not found'}

    # Load input
    input_data = jsonl_reader(input_file)
    if not input_data:
        logger.info("No items to process")
        return {'success': True, 'processed': 0, 'errors': 0}

    # Prepare output file for results
    output_file = os.path.join(output_dir, "results.jsonl")
    skill = load_skill("summarize")

    skill_vars = {}
    if 'variables' in skill:
        for var in skill['variables']:
            skill_vars[var['name']] = var.get('default', '')

    base_prompt = build_skill_prompt(skill, skill_vars)
    results = []
    processed = 0
    errors = 0

    effective_workers = min(max_workers, len(input_data)) if max_workers > 1 else 1
    logger.info(f"Summarizing {len(input_data)} items with max_workers={effective_workers}")

    if effective_workers <= 1:
        for item in input_data:
            result_item, is_err = _summarize_one_item(item, base_prompt, output_dir, timeout)
            results.append(result_item)
            if is_err:
                errors += 1
            else:
                processed += 1
    else:
        with ThreadPoolExecutor(max_workers=effective_workers) as executor:
            future_to_item = {
                executor.submit(
                    _summarize_one_item, item, base_prompt, output_dir, timeout
                ): item
                for item in input_data
            }
            for future in as_completed(future_to_item):
                try:
                    result_item, is_err = future.result()
                except Exception as e:
                    item = future_to_item[future]
                    result_item = create_error_entry(item.get("id", "unknown"), str(e))
                    is_err = True
                results.append(result_item)
                if is_err:
                    errors += 1
                else:
                    processed += 1

    jsonl_writer(output_file, results)
    result = {
        'success': errors == 0,
        'processed': processed,
        'errors': errors,
        'total': len(input_data)
    }

    logger.info(f"Summarize workflow complete: {result}")
    return result


def prepare_reflect_input(
    summary_dir: str = "summary",
    subtitles_dir: str = "subtitles_origin",
    videos_meta: str = "videos_meta.jsonl",
    output_file: str = "temp_input/reflect_input.jsonl"
) -> List[Dict[str, Any]]:
    """
    Prepare input JSONL for reflect skill.

    Args:
        summary_dir: Directory containing summary files
        subtitles_dir: Directory containing subtitle files
        videos_meta: Path to videos metadata JSONL
        output_file: Path to output input file

    Returns:
        List of input items
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Get list of already reflected files
    output_dir = "temp_posts"
    reflected = set()
    if os.path.exists(output_dir):
        reflected = {f.replace(".md", "") for f in os.listdir(output_dir) if f.endswith(".md")}

    # Read video metadata
    video_metadata = {}
    if os.path.exists(videos_meta):
        for item in jsonl_reader(videos_meta):
            title = sanitize_filename(item.get('title', '')).replace(".en.ttml", "")
            video_metadata[title] = item

    # Prepare input items
    items = []
    summary_path = Path(summary_dir)

    if not summary_path.exists():
        logger.warning(f"Summary directory not found: {summary_dir}")
        return items

    for summary_file in summary_path.glob("*.md"):
        title = summary_file.stem

        # Skip if already reflected
        if title in reflected:
            logger.info(f"Skipping already reflected: {title}")
            continue

        # Read summary content
        try:
            with open(summary_file, 'r', encoding='utf-8') as f:
                summary_content = f.read()
        except Exception as e:
            logger.error(f"Error reading {summary_file}: {e}")
            continue

        # Read original subtitle content
        original_file = os.path.join(subtitles_dir, f"{title}.en.ttml")
        original_content = ""
        if os.path.exists(original_file):
            try:
                with open(original_file, 'r', encoding='utf-8') as f:
                    original_content = f.read()
            except Exception as e:
                logger.warning(f"Could not read original: {original_file}")

        # Get video metadata
        metadata = video_metadata.get(title, {})
        date_str = metadata.get('published_at', '')[:10] if metadata.get('published_at') else datetime.now().strftime('%Y-%m-%d')

        item = {
            'id': title,
            'summary_content': summary_content[:30000],
            'original_content': original_content[:50000],
            'video_title': metadata.get('title', title),
            'date': date_str,
            'updated': datetime.now().strftime('%Y-%m-%d'),
            'subtitle': title
        }
        items.append(item)

    # Write input file
    if items:
        jsonl_writer(output_file, items)
        logger.info(f"Prepared {len(items)} items for reflection: {output_file}")

    return items


def run_reflect_workflow(
    input_file: str = "temp_input/reflect_input.jsonl",
    output_dir: str = "temp_posts",
    batch_size: int = 10,
    timeout: int = 300,
    max_workers: int = 1,
) -> Dict[str, Any]:
    """
    Run the reflect workflow using Claude Code.

    Args:
        input_file: Path to input JSONL file
        output_dir: Directory for output posts
        batch_size: Items per batch
        timeout: Timeout per batch

    Returns:
        Processing result statistics
    """
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(input_file):
        logger.error(f"Input file not found: {input_file}")
        return {'success': False, 'error': 'Input file not found'}

    # Load input
    input_data = jsonl_reader(input_file)
    if not input_data:
        logger.info("No items to process")
        return {'success': True, 'processed': 0, 'errors': 0}

    # Prepare output file for results
    output_file = os.path.join(output_dir, "results.jsonl")

    # Invoke skill
    result = invoke_skill(
        skill_name="reflect",
        input_data=input_data,
        output_file=output_file,
        batch_size=batch_size,
        timeout=timeout,
        max_retries=3,
        max_workers=max_workers,
    )

    # Process results - write individual post files
    if os.path.exists(output_file):
        results = jsonl_reader(output_file)
        for item in results:
            if item.get('status') == 'success':
                # Extract the full content with front matter
                full_content = item.get('result', {}).get('full_content', '')
                if full_content:
                    output_path = os.path.join(output_dir, f"{item['id']}.md")
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(full_content)

    logger.info(f"Reflect workflow complete: {result}")
    return result


def run_classify_workflow(
    posts_dir: str = "source/_posts",
    output_file: str = "post_classification_by_content.json",
    batch_size: int = 50,
    timeout: int = 300,
    max_workers: int = 1,
) -> Dict[str, Any]:
    """
    Run the classify workflow using Claude Code.

    Args:
        posts_dir: Directory containing post files
        output_file: Path to output classification JSON
        batch_size: Items per batch
        timeout: Timeout per batch

    Returns:
        Processing result statistics
    """
    if not os.path.exists(posts_dir):
        logger.error(f"Posts directory not found: {posts_dir}")
        return {'success': False, 'error': 'Posts directory not found'}

    # Get post titles
    post_files = [f for f in os.listdir(posts_dir) if f.endswith('.md')]
    if not post_files:
        logger.info("No posts to classify")
        return {'success': True, 'processed': 0, 'errors': 0}

    # Prepare input - group into batches
    input_data = []
    for i in range(0, len(post_files), batch_size):
        batch = post_files[i:i + batch_size]
        input_data.append({
            'id': f'batch_{i // batch_size}',
            'post_titles': batch
        })

    # Output file for this workflow
    temp_output = "temp_classify_results.jsonl"

    # Invoke skill
    result = invoke_skill(
        skill_name="classify",
        input_data=input_data,
        output_file=temp_output,
        batch_size=1,  # Each batch is already grouped
        timeout=timeout,
        max_retries=3,
        max_workers=max_workers,
    )

    # Merge batch results into final output
    if os.path.exists(temp_output):
        final_classification = {}
        results = jsonl_reader(temp_output)
        for item in results:
            if item.get('status') == 'success':
                batch_result = item.get('result', {})
                for category, titles in batch_result.items():
                    if category not in final_classification:
                        final_classification[category] = []
                    final_classification[category].extend(titles)

        # Write final classification
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(final_classification, f, ensure_ascii=False, indent=4)

        logger.info(f"Classification complete: {output_file}")

    return result


async def main_claude_summarize(batch_size: int = 10, timeout: int = 300, max_workers: int = 1):
    """Main function for Claude Code-based summarization."""
    logger.info("Starting Claude Code summarize workflow...")

    # Step 1: Prepare input
    items = prepare_summarize_input()
    if not items:
        logger.info("No new videos to summarize")
        return

    # Step 2: Run workflow
    result = run_summarize_workflow(batch_size=batch_size, timeout=timeout, max_workers=max_workers)

    logger.info(f"Summarize workflow result: {result}")


async def main_claude_reflect(batch_size: int = 10, timeout: int = 300, max_workers: int = 1):
    """Main function for Claude Code-based reflection."""
    logger.info("Starting Claude Code reflect workflow...")

    # Step 1: Prepare input
    items = prepare_reflect_input()
    if not items:
        logger.info("No new summaries to reflect")
        return

    # Step 2: Run workflow
    result = run_reflect_workflow(batch_size=batch_size, timeout=timeout, max_workers=max_workers)

    logger.info(f"Reflect workflow result: {result}")


async def main_claude_classify(batch_size: int = 50, timeout: int = 300, max_workers: int = 1):
    """Main function for Claude Code-based classification."""
    logger.info("Starting Claude Code classify workflow...")

    result = run_classify_workflow(batch_size=batch_size, timeout=timeout, max_workers=max_workers)

    logger.info(f"Classify workflow result: {result}")


# ---------------------------------------------------------------------------
# Process workflow: subtitle → hexo post (one-step, replaces summarize+reflect)
# ---------------------------------------------------------------------------

import re as _re


def prepare_process_input(
    subtitles_dir: str = "subtitles_origin",
    videos_meta: str = "videos_meta.jsonl",
    output_file: str = "temp_input/process_input.jsonl",
) -> List[Dict[str, Any]]:
    """
    Prepare input JSONL for the process skill (subtitle → hexo post).
    Skips files already present in temp_posts/.
    """
    import datetime as _dt

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # 已处理过的文件（temp_posts 里已有的）
    processed = set()
    if os.path.exists("temp_posts"):
        processed = {f.replace(".md", "") for f in os.listdir("temp_posts") if f.endswith(".md")}

    # 读取 video metadata
    video_metadata = {}
    if os.path.exists(videos_meta):
        for item in jsonl_reader(videos_meta):
            raw_title = item.get("title", "")
            key = sanitize_filename(raw_title)
            upload_date = item.get("upload_date", "")
            timestamp = item.get("timestamp")
            try:
                date_str = _dt.datetime.strptime(upload_date, "%Y%m%d").strftime("%Y-%m-%d")
            except (ValueError, TypeError):
                date_str = _dt.datetime.now().strftime("%Y-%m-%d")
            updated_str = (
                _dt.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
                if timestamp
                else date_str
            )
            video_metadata[key] = {
                "title": sanitize_yaml_string(raw_title),
                "date": date_str,
                "updated": updated_str,
            }

    items = []
    subtitles_path = Path(subtitles_dir)
    if not subtitles_path.exists():
        logger.warning(f"Subtitles directory not found: {subtitles_dir}")
        return items

    for subtitle_file in subtitles_path.glob("*.ttml"):
        # 文件名格式: <name>.en.ttml → id = <name>
        title_id = subtitle_file.stem.removesuffix(".en")

        if title_id in processed:
            logger.info(f"Skipping already processed: {title_id}")
            continue

        try:
            content = subtitle_file.read_text(encoding="utf-8")
        except Exception as e:
            logger.error(f"Error reading {subtitle_file}: {e}")
            continue

        meta = video_metadata.get(title_id, {})
        today = datetime.now().strftime("%Y-%m-%d")

        items.append({
            "id": title_id,
            "content": content[:50000],
            "video_title": meta.get("title", title_id),
            "date": meta.get("date", today),
            "updated": meta.get("updated", today),
            "subtitle": title_id,
        })

    if items:
        jsonl_writer(output_file, items)
        logger.info(f"Prepared {len(items)} items for processing: {output_file}")

    return items


def _process_one_item(
    item: Dict[str, Any],
    base_prompt: str,
    output_dir: str,
    timeout: int,
) -> tuple:
    """处理单条 process 任务，返回 (result_dict, is_error)。"""
    item_id = item.get("id", "unknown")

    response = invoke_claude(prompt=base_prompt, timeout=timeout)
    if not response.get("success"):
        return create_error_entry(item_id, response.get("error", "Unknown error")), True

    raw = (response.get("output") or "").strip()
    if not raw:
        return create_error_entry(item_id, "Empty output"), True

    # 后处理
    raw = _re.sub(r"\x1b\[[0-9;]*m", "", raw)   # strip ANSI
    raw = raw.lstrip("\n")
    raw = clean_front_matter(raw)

    # 检查残留占位符
    if "[改进后的中文总结内容]" in raw or "[此处直接输出" in raw:
        return create_error_entry(item_id, "Output contains unfilled placeholder"), True

    output_path = os.path.join(output_dir, f"{item_id}.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(raw + "\n")

    return {"id": item_id, "status": "success"}, False


def run_process_workflow(
    input_file: str = "temp_input/process_input.jsonl",
    output_dir: str = "temp_posts",
    timeout: int = 300,
    max_workers: int = 1,
) -> Dict[str, Any]:
    """
    Run the one-step process workflow: subtitle → hexo post.
    Each item is processed individually (not batched JSONL) so Claude
    outputs plain Markdown directly.
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(input_file):
        logger.error(f"Input file not found: {input_file}")
        return {"success": False, "error": "Input file not found"}

    input_data = jsonl_reader(input_file)
    if not input_data:
        logger.info("No items to process")
        return {"success": True, "processed": 0, "errors": 0}

    skill = load_skill("process")
    skill_vars = {
        var["name"]: var.get("default", "")
        for var in skill.get("variables", [])
    }
    base_prompt_template = build_skill_prompt(skill, skill_vars)

    processed = 0
    errors = 0
    effective_workers = min(max_workers, len(input_data)) if max_workers > 1 else 1
    logger.info(f"Processing {len(input_data)} items with max_workers={effective_workers}")

    def _run_item(item):
        # 把 item 的字段替换进 prompt 模板
        from .claude_invoker import substitute_variables
        item_vars = {**skill_vars, **{k: str(v) for k, v in item.items()
                                       if k in ("video_title", "date", "updated", "subtitle")}}
        item_vars["subtitle_content"] = item.get("content", "")
        prompt = substitute_variables(base_prompt_template, item_vars)
        return _process_one_item(item, prompt, output_dir, timeout)

    if effective_workers <= 1:
        for item in input_data:
            result, is_err = _run_item(item)
            if is_err:
                errors += 1
                logger.error(f"Error processing {item.get('id')}: {result.get('error')}")
            else:
                processed += 1
    else:
        with ThreadPoolExecutor(max_workers=effective_workers) as executor:
            future_to_item = {executor.submit(_run_item, item): item for item in input_data}
            for future in as_completed(future_to_item):
                item = future_to_item[future]
                try:
                    result, is_err = future.result()
                except Exception as e:
                    is_err = True
                    logger.error(f"Exception for {item.get('id')}: {e}")
                if is_err:
                    errors += 1
                else:
                    processed += 1

    result = {"success": errors == 0, "processed": processed, "errors": errors, "total": len(input_data)}
    logger.info(f"Process workflow complete: {result}")
    return result


async def main_claude_process(timeout: int = 300, max_workers: int = 1):
    """Main function for one-step subtitle → hexo post processing."""
    logger.info("Starting Claude Code process workflow...")

    items = prepare_process_input()
    if not items:
        logger.info("No new videos to process")
        return

    result = run_process_workflow(timeout=timeout, max_workers=max_workers)
    logger.info(f"Process workflow result: {result}")


# ---------------------------------------------------------------------------
# Quarterly / Monthly summary workflow
# ---------------------------------------------------------------------------

def _get_quarter(year: int, month: int) -> str:
    return f"{year}Q{(month - 1) // 3 + 1}"


def _build_post_url(fname: str, posts_dir: str, site_root: str = "/VideoSummary") -> str:
    """根据文件名和 front matter date 构建 hexo permalink。"""
    path = os.path.join(posts_dir, fname)
    try:
        content = open(path, encoding="utf-8").read()
        m = _re.search(r"^date:\s*(\d{4})-(\d{2})-(\d{2})", content, _re.MULTILINE)
        if not m:
            return ""
        year, month, day = m.group(1), m.group(2), m.group(3)
        title = fname.replace(".md", "")
        return f"{site_root}/{year}/{month}/{day}/{title}/"
    except Exception:
        return ""


def _get_post_title(fname: str, posts_dir: str) -> str:
    """从 front matter 读取 title 字段，fallback 到文件名。"""
    try:
        content = open(os.path.join(posts_dir, fname), encoding="utf-8").read()
        m = _re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, _re.MULTILINE)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    except Exception:
        pass
    return fname.replace(".md", "").replace("_", " ")


def _replace_placeholder_links(body: str, post_files: list, posts_dir: str) -> str:
    """
    把 Claude 输出中的占位符链接 [title](filename) 替换为真实 hexo URL。
    只替换 href 部分是纯文件名（不含 / 和 http）的链接。
    """
    fname_to_url = {
        fname.replace(".md", ""): _build_post_url(fname, posts_dir)
        for fname in post_files
    }

    def replace_link(m):
        text, href = m.group(1), m.group(2)
        if "/" not in href and not href.startswith("http"):
            url = fname_to_url.get(href, "")
            if url:
                return f"[{text}]({url})"
        return m.group(0)

    return _re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, body)


def _quarter_date(quarter: str) -> str:
    """Return the last month of the quarter as YYYY-MM-01."""
    year = int(quarter[:4])
    q = int(quarter[5])
    last_month = q * 3
    return f"{year}-{last_month:02d}-01"


def _get_month(year: int, month: int) -> str:
    return f"{year}-{month:02d}"


def _month_date(month_str: str) -> str:
    return f"{month_str}-01"


def _year_date(year: str) -> str:
    return f"{year}-12-01"


def _is_summary_stale(summary_path: str, post_files: list, posts_dir: str) -> bool:
    """
    检测总结文件是否过期：temp_posts 中该时间段内有任何文章的 mtime 比总结更新则过期。
    """
    if not os.path.exists(summary_path):
        return True
    summary_mtime = os.path.getmtime(summary_path)
    for fname in post_files:
        fpath = os.path.join(posts_dir, fname)
        if os.path.exists(fpath) and os.path.getmtime(fpath) > summary_mtime:
            return True
    return False


def _build_summary_body(
    skill_name: str,
    period_key: str,
    period_var: str,
    post_files: list,
    posts_dir: str,
    timeout: int,
    max_chars: int,
) -> tuple:
    """
    共用的 Claude 调用逻辑：加载 skill、拼接内容、调用 Claude、后处理。
    返回 (body, ref_section) 或 (None, None) 表示失败。
    """
    from .claude_invoker import substitute_variables

    skill = load_skill(skill_name)
    base_template = skill.get("system_prompt", "")

    parts = []
    total = 0
    for fname in sorted(post_files):
        path = os.path.join(posts_dir, fname)
        try:
            text = open(path, encoding="utf-8").read()
            body_text = text.split("---", 2)[-1].strip() if text.count("---") >= 2 else text
            snippet = f"### {fname.replace('.md', '')}\n{body_text[:2000]}\n"
            if total + len(snippet) > max_chars:
                break
            parts.append(snippet)
            total += len(snippet)
        except Exception as e:
            logger.warning(f"Could not read {fname}: {e}")

    posts_content = "\n\n".join(parts)
    item_vars = {period_var: period_key, "post_count": str(len(post_files)), "posts_content": posts_content}
    prompt = substitute_variables(base_template, item_vars)

    response = invoke_claude(prompt=prompt, timeout=timeout)
    if not response.get("success"):
        logger.error(f"Failed to generate {period_key}: {response.get('error')}")
        return None, None

    body = (response.get("output") or "").strip()
    body = _re.sub(r"\x1b\[[0-9;]*m", "", body).lstrip("\n")
    body = _replace_placeholder_links(body, post_files, posts_dir)

    ref_lines = ["\n\n---\n\n## 参考文章\n"]
    for fname in sorted(post_files):
        url = _build_post_url(fname, posts_dir)
        if not url:
            continue
        title = _get_post_title(fname, posts_dir)
        ref_lines.append(f"- [{title}]({url})")
    ref_section = "\n".join(ref_lines)

    return body, ref_section


def run_quarterly_workflow(
    posts_dir: str = None,
    output_dir: str = None,
    quarters: list = None,
    timeout: int = 600,
    max_chars_per_quarter: int = 60000,
    force_update: bool = False,
) -> Dict[str, Any]:
    """
    Generate quarterly summary posts from existing temp_posts.

    Args:
        posts_dir: Directory with processed posts (default: temp_posts)
        output_dir: Where to write quarterly posts (default: ../source/_posts)
        quarters: List of quarter strings to generate, e.g. ['2025Q1']. None = all missing.
        timeout: Timeout per Claude call
        max_chars_per_quarter: Max chars of post content fed to Claude per quarter
    """
    import re as _re2

    if posts_dir is None:
        posts_dir = "temp_posts"
    if output_dir is None:
        output_dir = os.path.join(WORK_DIR, "..", "source", "_posts")
    output_dir = os.path.normpath(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    # 按季度分组 temp_posts 文件
    by_quarter: Dict[str, list] = {}
    for fname in os.listdir(posts_dir):
        if not fname.endswith(".md"):
            continue
        content = open(os.path.join(posts_dir, fname), encoding="utf-8").read()
        m = _re.search(r"^date:\s*(\d{4})-(\d{2})", content, _re.MULTILINE)
        if not m:
            continue
        year, month = int(m.group(1)), int(m.group(2))
        q = _get_quarter(year, month)
        by_quarter.setdefault(q, []).append(fname)

    # 已存在的季度总结
    existing = {
        f.replace("_Ceph社区季度总结.md", "")
        for f in os.listdir(output_dir)
        if "季度总结" in f
    }

    def _should_gen(q: str) -> bool:
        if q not in existing:
            return True
        if force_update:
            return True
        summary_path = os.path.join(output_dir, f"{q}_Ceph社区季度总结.md")
        return _is_summary_stale(summary_path, by_quarter.get(q, []), posts_dir)

    target_quarters = quarters if quarters else [
        q for q in sorted(by_quarter) if _should_gen(q)
    ]

    if not target_quarters:
        logger.info("All quarters already have summaries (and none are stale)")
        return {"success": True, "processed": 0, "skipped": len(existing)}

    processed = 0
    errors = 0

    for quarter in target_quarters:
        post_files = by_quarter.get(quarter, [])
        if not post_files:
            logger.warning(f"No posts found for {quarter}, skipping")
            continue

        logger.info(f"Generating quarterly summary for {quarter} ({len(post_files)} posts)")

        body, ref_section = _build_summary_body(
            "quarterly", quarter, "quarter", post_files, posts_dir, timeout, max_chars_per_quarter
        )
        if body is None:
            errors += 1
            continue

        date_str = _quarter_date(quarter)
        front_matter = f"""---
title: "{quarter} Ceph社区季度进展报告"
date: {date_str}
updated: {date_str}
categories:
- 季度总结
tags:
- Ceph
- 社区动态
- 季度报告
subtitle: {quarter}_quarterly_summary
---

"""
        out_path = os.path.join(output_dir, f"{quarter}_Ceph社区季度总结.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(front_matter + body + ref_section + "\n")

        logger.info(f"Written: {out_path}")
        processed += 1

    result = {"success": errors == 0, "processed": processed, "errors": errors}
    logger.info(f"Quarterly workflow complete: {result}")
    return result


async def main_claude_quarterly(quarters: list = None, timeout: int = 600, force_update: bool = False):
    """Generate quarterly summary posts (missing or stale)."""
    logger.info("Starting quarterly summary workflow...")
    result = run_quarterly_workflow(quarters=quarters, timeout=timeout, force_update=force_update)
    logger.info(f"Quarterly result: {result}")


# ---------------------------------------------------------------------------
# Monthly summary workflow
# ---------------------------------------------------------------------------

def run_monthly_workflow(
    posts_dir: str = None,
    output_dir: str = None,
    months: list = None,
    timeout: int = 600,
    max_chars_per_month: int = 40000,
    force_update: bool = False,
) -> Dict[str, Any]:
    """Generate monthly summary posts from existing temp_posts."""
    if posts_dir is None:
        posts_dir = "temp_posts"
    if output_dir is None:
        output_dir = os.path.join(WORK_DIR, "..", "source", "_posts")
    output_dir = os.path.normpath(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    by_month: Dict[str, list] = {}
    for fname in os.listdir(posts_dir):
        if not fname.endswith(".md"):
            continue
        content = open(os.path.join(posts_dir, fname), encoding="utf-8").read()
        m = _re.search(r"^date:\s*(\d{4})-(\d{2})", content, _re.MULTILINE)
        if not m:
            continue
        year, month = int(m.group(1)), int(m.group(2))
        key = _get_month(year, month)
        by_month.setdefault(key, []).append(fname)

    existing = {
        f.replace("_Ceph社区月度总结.md", "")
        for f in os.listdir(output_dir)
        if "月度总结" in f
    }

    def _should_gen(k: str) -> bool:
        if k not in existing:
            return True
        if force_update:
            return True
        return _is_summary_stale(
            os.path.join(output_dir, f"{k}_Ceph社区月度总结.md"),
            by_month.get(k, []), posts_dir
        )

    target_months = months if months else [k for k in sorted(by_month) if _should_gen(k)]

    if not target_months:
        logger.info("All months already have summaries (and none are stale)")
        return {"success": True, "processed": 0, "skipped": len(existing)}

    processed = 0
    errors = 0

    for month_key in target_months:
        post_files = by_month.get(month_key, [])
        if not post_files:
            logger.warning(f"No posts found for {month_key}, skipping")
            continue

        logger.info(f"Generating monthly summary for {month_key} ({len(post_files)} posts)")

        body, ref_section = _build_summary_body(
            "monthly", month_key, "month", post_files, posts_dir, timeout, max_chars_per_month
        )
        if body is None:
            errors += 1
            continue

        date_str = _month_date(month_key)
        front_matter = f"""---
title: "{month_key} Ceph社区月度进展报告"
date: {date_str}
updated: {date_str}
categories:
- 月度总结
tags:
- Ceph
- 社区动态
- 月度报告
subtitle: {month_key}_monthly_summary
---

"""
        out_path = os.path.join(output_dir, f"{month_key}_Ceph社区月度总结.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(front_matter + body + ref_section + "\n")

        logger.info(f"Written: {out_path}")
        processed += 1

    result = {"success": errors == 0, "processed": processed, "errors": errors}
    logger.info(f"Monthly workflow complete: {result}")
    return result


async def main_claude_monthly(months: list = None, timeout: int = 600, force_update: bool = False):
    """Generate monthly summary posts (missing or stale)."""
    logger.info("Starting monthly summary workflow...")
    result = run_monthly_workflow(months=months, timeout=timeout, force_update=force_update)
    logger.info(f"Monthly result: {result}")


# ---------------------------------------------------------------------------
# Yearly summary workflow
# ---------------------------------------------------------------------------

def run_yearly_workflow(
    posts_dir: str = None,
    output_dir: str = None,
    years: list = None,
    timeout: int = 900,
    max_chars_per_year: int = 80000,
    force_update: bool = False,
) -> Dict[str, Any]:
    """Generate yearly summary posts from existing temp_posts."""
    if posts_dir is None:
        posts_dir = "temp_posts"
    if output_dir is None:
        output_dir = os.path.join(WORK_DIR, "..", "source", "_posts")
    output_dir = os.path.normpath(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    by_year: Dict[str, list] = {}
    for fname in os.listdir(posts_dir):
        if not fname.endswith(".md"):
            continue
        content = open(os.path.join(posts_dir, fname), encoding="utf-8").read()
        m = _re.search(r"^date:\s*(\d{4})-(\d{2})", content, _re.MULTILINE)
        if not m:
            continue
        year = m.group(1)
        by_year.setdefault(year, []).append(fname)

    existing = {
        f.replace("_Ceph社区年度总结.md", "")
        for f in os.listdir(output_dir)
        if "年度总结" in f
    }

    def _should_gen(k: str) -> bool:
        if k not in existing:
            return True
        if force_update:
            return True
        return _is_summary_stale(
            os.path.join(output_dir, f"{k}_Ceph社区年度总结.md"),
            by_year.get(k, []), posts_dir
        )

    target_years = years if years else [k for k in sorted(by_year) if _should_gen(k)]

    if not target_years:
        logger.info("All years already have summaries (and none are stale)")
        return {"success": True, "processed": 0, "skipped": len(existing)}

    processed = 0
    errors = 0

    for year_key in target_years:
        post_files = by_year.get(year_key, [])
        if not post_files:
            logger.warning(f"No posts found for {year_key}, skipping")
            continue

        logger.info(f"Generating yearly summary for {year_key} ({len(post_files)} posts)")

        body, ref_section = _build_summary_body(
            "yearly", year_key, "year", post_files, posts_dir, timeout, max_chars_per_year
        )
        if body is None:
            errors += 1
            continue

        date_str = _year_date(year_key)
        front_matter = f"""---
title: "{year_key} Ceph社区年度进展报告"
date: {date_str}
updated: {date_str}
categories:
- 年度总结
tags:
- Ceph
- 社区动态
- 年度报告
subtitle: {year_key}_yearly_summary
---

"""
        out_path = os.path.join(output_dir, f"{year_key}_Ceph社区年度总结.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(front_matter + body + ref_section + "\n")

        logger.info(f"Written: {out_path}")
        processed += 1

    result = {"success": errors == 0, "processed": processed, "errors": errors}
    logger.info(f"Yearly workflow complete: {result}")
    return result


async def main_claude_yearly(years: list = None, timeout: int = 900, force_update: bool = False):
    """Generate yearly summary posts (missing or stale)."""
    logger.info("Starting yearly summary workflow...")
    result = run_yearly_workflow(years=years, timeout=timeout, force_update=force_update)
    logger.info(f"Yearly result: {result}")
