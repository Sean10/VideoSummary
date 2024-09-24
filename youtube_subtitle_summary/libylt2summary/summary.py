import os
import json
import jsonlines
from .utils import sanitize_filename

async def summary(subtitle_file, mode="summary", history=None):
    # 这个函数的实现保持不变，但需要确保它是异步的
    # 如果需要，可以将其中的 OpenAI API 调用改为异步
    pass

def main_summary():
    sorted_file_names = main_summary_diff()
    for file in sorted_file_names:
        history = summary(file, "summary")

def main_summary_diff():
    need_summary = []
    summary_files = os.listdir("summary")
    summaryed = [title.replace(".md", "") for title in summary_files]

    downloaded = {}
    with jsonlines.open("videos_meta.jsonl", "r") as reader:
        for item in reader:
            title = sanitize_filename(item['title']).replace(".en.ttml", "")
            if title in downloaded:
                print(f"已下载过: {title}")
                continue
            downloaded[title] = item

            if title not in summaryed:
                print(f"未总结: {title}")
                need_summary.append(title+".en.ttml")
            else:
                print(f"已总结: {title}")
    
    return list(reversed(need_summary))