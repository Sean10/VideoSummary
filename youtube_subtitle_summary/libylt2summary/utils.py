import os
import aiohttp
import asyncio
import json
import datetime
from asyncio import Queue, Semaphore
from openai import AsyncOpenAI
import re
from yt_dlp import utils as yt_utils

YOUR_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if YOUR_OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

model = "THUDM/glm-4-9b-chat"
client = AsyncOpenAI(
    api_key=f"{YOUR_OPENAI_API_KEY}",
    base_url="http://localhost:3000/v1",
)

MAX_RETRIES = 10
RETRY_DELAY = 10
MAX_RETRY_DELAY = 60

class RetryQueue:
    def __init__(self):
        self.queue = Queue()
        self.processing = set()

    async def add(self, task):
        await self.queue.put(task)

    async def get(self):
        return await self.queue.get()

    def task_done(self, task):
        self.queue.task_done()
        self.processing.remove(task)

    def is_empty(self):
        return self.queue.empty() and len(self.processing) == 0

retry_queue = RetryQueue()

async def retry_with_exponential_backoff(func, *args, **kwargs):
    retries = 0
    delay = RETRY_DELAY
    while retries < MAX_RETRIES:
        try:
            return await func(*args, **kwargs)
        except aiohttp.ClientResponseError as e:
            if e.status == 429:
                print(f"遇到 429 错误（Too Many Requests）。等待 {RETRY_DELAY} 秒后重试...")
                await asyncio.sleep(RETRY_DELAY)
                retries += 1
            else:
                print(f"遇到错误: {e}. 重试中...")
                await asyncio.sleep(delay)
                retries += 1
                delay = min(delay * 2, MAX_RETRY_DELAY)
        except Exception as e:
            print(f"Error occurred: {e}. Retrying in {delay} seconds...")
            await asyncio.sleep(delay)
            retries += 1
            delay = min(delay * 2, MAX_RETRY_DELAY)
    
    print(f"任务在 {MAX_RETRIES} 次尝试后失败。")
    return None

async def process_retry_queue():
    while not retry_queue.is_empty():
        task = await retry_queue.get()
        func, args, kwargs = task
        retry_queue.processing.add(task)
        result = await retry_with_exponential_backoff(func, *args, **kwargs)
        if result is not None:
            retry_queue.task_done(task)
        await asyncio.sleep(asyncio.uniform(1, 5))

async def call_openai_api(func, *args, **kwargs):
    return await retry_with_exponential_backoff(func, *args, **kwargs)

def full_to_half(s):
    full_to_half_map = {
        ord(f): ord(h) for f, h in zip(
            '　！＂＃＄％＆＇（）＊＋，－．／０１２３４５６７８９：；＜＝？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［＼］＾＿｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝～',
            ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
        )
    }
    return s.translate(full_to_half_map)

def escape_title(title):
    return title.replace(' ', '_').replace('|', '_').replace(':', '_')

def render_template(title, date, updated, tags):
    tags_str = "\n".join(f"- {tag}" for tag in tags)
    template = f"""---
title: {title}
date: {date}
updated: {updated}
tags:
{tags_str}
categories:
- "视频总结"
subtitle: tech
---
"""
    return template

def clean_subtitles(info):
    try:
        filepath = info['info_dict']['requested_subtitles']['en']['filepath']
    except Exception as e:
        with open("error.log", "w") as f:
            f.write(json.dumps(info))
            f.write(str(e))
        return
    
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    cleaned_content = re.sub(r'^[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9] --> [0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]$', '', content, flags=re.MULTILINE)
    cleaned_content = re.sub(r'^[[:digit:]]\{1,5\}$', '', cleaned_content, flags=re.MULTILINE)
    cleaned_content = re.sub(r'<[^>]*>', '', cleaned_content)
    cleaned_content = re.sub(r'^[[:space:]]*$', '', cleaned_content, flags=re.MULTILINE)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

def get_latest_file(path, filter="*"):
    from pathlib import Path
    directory = Path(path)
    files = directory.glob(filter)
    sorted_files = sorted(files, key=lambda f: f.stat().st_mtime)
    sorted_file_names = [file.name for file in sorted_files]
    return sorted_file_names

def sanitize_filename(filename):
    return yt_utils.sanitize_filename(filename, restricted=True)

def load_metadata_to_dict():
    metadata_dict = {}
    with open('videos_meta.jsonl', 'r') as file:
        for line in file:
            data = json.loads(line)
            key = sanitize_filename(data['title']) + '.md'
            metadata_dict[key] = {
                'title': '"' + data['title'] + '"',
                'date': datetime.datetime.strptime(data['upload_date'], '%Y%m%d').strftime('%Y-%m-%d'),
                'updated': datetime.datetime.fromtimestamp(data['timestamp']).strftime('%Y-%m-%d') if data['timestamp'] else None
            }
    return metadata_dict

metadata_dict = load_metadata_to_dict()

def get_metadata_from_jsonl(filename):
    return metadata_dict.get(filename)

def get_quarter(date):
    return (date.month - 1) // 3 + 1