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
MAX_CONCURRENT_REQUESTS = 5
REQUEST_DELAY = 1  # 秒

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
            print("start")
            pr = await github.rest.pulls.get(owner=owner, repo=repo, pull_number=pr_number)
            with open("temp_pr.txt", "w") as f:
                f.write(json.dumps(pr))
            file_name = escape_title(f"{pr.data.base.repo.full_name}_PR_{pr.data.number}.md")
            output_path = output_dir / file_name
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"# {pr.data.title}\n\n")
                f.write(f"PR URL: {pr_url}\n\n")
                f.write(f"## Description\n\n{pr.data.body}\n\n")
                f.write(f"## Files Changed\n\n")
                for file in pr.data.changed_files:
                    f.write(f"- {file.filename}\n")
            
            print(f"已保存 PR 内容: {output_path}")
            fetched_prs.add(pr_url)
            save_fetched_prs(fetched_prs)
            import sys
            sys.exit(1)
            await asyncio.sleep(REQUEST_DELAY)  # 添加延迟以遵守速率限制

        except RequestFailed as e:
            print(f"Failed to fetch PR {pr_url}: {e}")
        
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
    output_dir.mkdir(exist_ok=True)

    await process_reference_files(reference_dir, output_dir)
    print(f"PR contents have been saved to the '{output_dir}' directory.")