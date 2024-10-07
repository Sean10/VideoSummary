import os
import re
import asyncio
import json
from pathlib import Path
from typing import Set
from urllib.parse import urlparse
from githubkit import GitHub
from githubkit.exception import RequestFailed
from .utils import escape_title

# 设置 GitHub 访问令牌
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable is not set")

github = GitHub(GITHUB_TOKEN)

# 设置限速参数
MAX_CONCURRENT_REQUESTS = 2
REQUEST_DELAY = 2  # 秒

FETCHED_PRS_FILE = "fetched_prs.json"

async def extract_github_pr_links(file_path: Path) -> Set[str]:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # 匹配 GitHub PR 链接的正则表达式
    pr_pattern = r'https://github\.com/[^/]+/[^/]+/pull/\d+'
    return set(re.findall(pr_pattern, content))

async def fetch_pr_content(pr_url: str, semaphore: asyncio.Semaphore, output_dir: Path, fetched_prs: Set[str], progress: asyncio.Queue) -> None:
    if pr_url in fetched_prs:
        await progress.put(1)  # 即使跳过也要更新进度
        return

    async with semaphore:
        parsed_url = urlparse(pr_url)
        path_parts = parsed_url.path.split('/')
        owner, repo, _, pr_number = path_parts[1], path_parts[2], path_parts[3], int(path_parts[4])
        
        try:
            print(f"开始获取 PR {pr_number} 的内容和评论")
            pr = await github.rest.pulls.async_get(owner=owner, repo=repo, pull_number=pr_number)
            comments = await github.rest.issues.async_list_comments(owner=owner, repo=repo, issue_number=pr_number)
            # with open("temp.json", "w") as f:
            #     f.write(json.dumps(pr.json(), indent=4))

            # print(f"准备创建目录: {output_dir}")
            # output_dir.mkdir(parents=True, exist_ok=True)
            # print(f"目录创建成功: {output_dir}")
        
            
            file_name = escape_title(f"{pr.parsed_data.base.repo.full_name}_PR_{pr.parsed_data.number}.md")
            output_path = output_dir / file_name
            base_path = output_path.parent
            base_path.mkdir(parents=True, exist_ok=True)
            print(f"目录创建成功: {base_path}")

            print(f"准备写入文件: {output_path}")

            if not output_dir.exists():
                print(f"警告：目录 {output_dir} 不存在，尝试再次创建")
                output_dir.mkdir(parents=True, exist_ok=True)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"# {pr.parsed_data.title}\n\n")
                f.write(f"PR URL: {pr_url}\n\n")
                f.write(f"## Description\n\n{pr.parsed_data.body}\n\n")
                # f.write(f"## Files Changed\n\n")
                # for file in pr.parsed_data.changed_files:
                #     f.write(f"- {file.filename}\n")
                
                f.write("\n## Comments\n\n")
                for comment in comments.parsed_data:
                    f.write(f"### {comment.user.login} - {comment.created_at}\n\n")
                    f.write(f"{comment.body}\n\n")
            
            print(f"已保存 PR 内容和评论: {output_path}")
            fetched_prs.add(pr_url)
            save_fetched_prs(fetched_prs)
            await asyncio.sleep(REQUEST_DELAY)  # 添加延迟以遵守速率限制

        except RequestFailed as e:
            print(f"Failed to fetch PR {pr_url}: {e}")
        except FileNotFoundError as e:
            print(f"处理 PR {pr_url} 时发生错误: {e}")
            print(f"当前工作目录: {os.getcwd()}")
            print(f"output_dir 是否存在: {output_dir.exists()}")
            print(f"output_dir 的权限: {oct(output_dir.stat().st_mode)[-3:]}")
        finally:
            await progress.put(1)  # 无论成功与否，都更新进度

def save_fetched_prs(fetched_prs: Set[str]) -> None:
    with open(FETCHED_PRS_FILE, 'w', encoding='utf-8') as f:
        json.dump(list(fetched_prs), f, ensure_ascii=False, indent=2)

def load_fetched_prs() -> Set[str]:
    if os.path.exists(FETCHED_PRS_FILE):
        with open(FETCHED_PRS_FILE, 'r', encoding='utf-8') as f:
            return set(json.load(f))
    return set()

async def process_reference_files(reference_dir: Path, output_dir: Path):
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    all_pr_links: Set[str] = set()
    fetched_prs = load_fetched_prs()

    # 提取所有 PR 链接
    for file in reference_dir.glob('*.md'):
        pr_links = await extract_github_pr_links(file)
        all_pr_links.update(pr_links)

    # all_pr_links = list(all_pr_links)[:3]
    total_prs = len(all_pr_links)
    progress_queue = asyncio.Queue()

    # 创建任务
    tasks = [asyncio.create_task(fetch_pr_content(pr_url, semaphore, output_dir, fetched_prs, progress_queue)) 
             for pr_url in all_pr_links]

    # 创建进度跟踪任务
    progress_task = asyncio.create_task(track_progress(progress_queue, total_prs))

    # 等待所有任务完成，包括进度更新
    await asyncio.gather(*tasks, progress_task)

async def track_progress(progress_queue: asyncio.Queue, total: int):
    processed = 0
    while processed < total:
        await progress_queue.get()
        processed += 1
        print(f"进度: {processed}/{total} ({processed/total*100:.2f}%)")
        progress_queue.task_done()

async def github_fetch_prs():
    reference_dir = Path("reference")
    output_dir = Path("reference_gh")
    output_dir.mkdir(parents=True, exist_ok=True)  # 添加这行来创建目录

    await process_reference_files(reference_dir, output_dir)
    print(f"PR contents have been saved to the '{output_dir}' directory.")
    
    import sys
    sys.exit(1)