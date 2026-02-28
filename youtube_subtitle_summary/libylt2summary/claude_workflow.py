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
from .utils import sanitize_filename

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
