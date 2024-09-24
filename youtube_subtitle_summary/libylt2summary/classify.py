import os
import json
import yaml
import re
import datetime
import asyncio
import aiohttp
from asyncio import Semaphore
from .utils import call_openai_api

async def classify_posts_by_content():
    posts_dir = "source/_posts"
    post_titles = [f for f in os.listdir(posts_dir) if f.endswith('.md')]
    
    batch_size = 50
    max_concurrent_requests = 15
    classifications = {}

    semaphore = Semaphore(max_concurrent_requests)

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(0, len(post_titles), batch_size):
            batch = post_titles[i:i+batch_size]
            task = asyncio.create_task(classify_batch(batch, session, semaphore))
            tasks.append(task)
        
        for completed_task in asyncio.as_completed(tasks):
            batch_classification = await completed_task
            for category, titles in batch_classification.items():
                if category not in classifications:
                    classifications[category] = []
                classifications[category].extend(titles)

    with open("post_classification_by_content.json", "w", encoding="utf-8") as f:
        json.dump(classifications, f, ensure_ascii=False, indent=4)
    print("文章内容分类完成，结果已保存到 post_classification_by_content.json")

def classify_posts_by_quarter():
    posts_dir = "source/_posts"
    post_titles = [f for f in os.listdir(posts_dir) if f.endswith('.md')]
    quarterly_reports = {}

    for post_title in post_titles:
        with open(os.path.join(posts_dir, post_title), 'r', encoding='utf-8') as f:
            content = f.read()
            yaml_match = re.search(r'---\n(.*?)\n---', content, re.DOTALL)
            if yaml_match:
                yaml_content = yaml_match.group(1)
                try:
                    metadata = yaml.safe_load(yaml_content)
                    if 'date' in metadata:
                        if isinstance(metadata['date'], datetime.date):
                            date = metadata['date']
                        else:
                            date = datetime.datetime.strptime(metadata['date'], '%Y-%m-%d').date()
                        year = date.year
                        quarter = (date.month - 1) // 3 + 1
                        quarter_key = f"{year}Q{quarter}"
                        if quarter_key not in quarterly_reports:
                            quarterly_reports[quarter_key] = []
                        quarterly_reports[quarter_key].append(post_title)
                except yaml.YAMLError as e:
                    print(f"Error parsing YAML in {post_title}: {e}")
                    break

    with open("post_classification_by_quarter.json", "w", encoding="utf-8") as f:
        json.dump(quarterly_reports, f, ensure_ascii=False, indent=4)
    print("文章季度分类完成，结果已保存到 post_classification_by_quarter.json")