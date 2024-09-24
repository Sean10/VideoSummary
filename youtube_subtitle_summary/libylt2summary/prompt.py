import os
import re
import asyncio
import aiohttp
from asyncio import Semaphore
from urllib.parse import urlparse
from pathlib import Path

async def fetch_webpage(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_and_parse(session, url, semaphore):
    async with semaphore:
        try:
            content = await fetch_webpage(session, url)
            return {'url': url, 'content': content}
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return {'url': url, 'content': None}

async def crawl_webpages(urls, semaphore):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_and_parse(session, url, semaphore)) for url in urls]
        results = await asyncio.gather(*tasks)
    return results

async def collect_prompt_info(urls):
    semaphore = Semaphore(15)  # 限制并发请求数
    results = await crawl_webpages(urls, semaphore)
    
    reference_dir = "reference"
    os.makedirs(reference_dir, exist_ok=True)
    
    prompt_info = ""
    for result in results:
        if result['content']:
            parsed_url = urlparse(result['url'])
            title = re.search(r'/p/(.*?)/export', parsed_url.path)
            if title:
                file_name = f"{title.group(1)}.md"
            else:
                file_name = os.path.basename(parsed_url.path) or 'index.md'
            
            file_path = os.path.join(reference_dir, file_name)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(result['content'])
            prompt_info += f"Content from {result['url']} saved to {file_path}\n"
    
    return prompt_info

def split_reference_files():
    reference_dir = Path("reference")
    after_reference_dir = Path("after_reference")
    after_reference_dir.mkdir(exist_ok=True)

    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}')
    special_char_pattern = re.compile(r'^\*')

    for file in reference_dir.glob('*.md'):
        with file.open('r', encoding='utf-8') as f:
            content = f.read()

        sections = []
        current_section = []
        current_date = None

        for line in content.split('\n'):
            date_match = date_pattern.match(line)
            special_char_match = special_char_pattern.match(line)

            if date_match or special_char_match:
                if current_section:
                    sections.append((current_date, '\n'.join(current_section)))
                    current_section = []
                if date_match:
                    current_date = date_match.group()
                else:
                    current_date = None
            
            current_section.append(line)

        if current_section:
            sections.append((current_date, '\n'.join(current_section)))

        for date, section_content in sections:
            if date:
                output_file = after_reference_dir / f"{file.stem}_{date}.md"
            else:
                output_file = after_reference_dir / f"{file.stem}_no_date_{len(sections)}.md"
            
            with output_file.open('w', encoding='utf-8') as f:
                f.write(f"# {date if date else 'No Date'}\n\n")
                f.write(section_content)

    print(f"Split {len(list(reference_dir.glob('*.md')))} files into {len(list(after_reference_dir.glob('*.md')))} sections.")