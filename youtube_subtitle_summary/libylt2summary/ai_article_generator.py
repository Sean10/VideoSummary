import os
import asyncio
import aiohttp
import httpx
from openai import AsyncOpenAI
from pathlib import Path
import json
import time
import re

# 设置OpenAI API密钥和基础URL
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# 设置Kimi API密钥
KIMI_API_KEY = os.getenv("KIMI_API_KEY")
if not KIMI_API_KEY:
    raise ValueError("KIMI_API_KEY environment variable is not set")

# model = "moonshot-v1-32k"
model = "ep-20240926005025-6ght9"
# base_url = "https://api.moonshot.cn/v1"
base_url = "https://ark.cn-beijing.volces.com/api/v3"

# 重试设置
MAX_RETRIES = 50
INITIAL_RETRY_DELAY = 1
MAX_RETRY_DELAY = 60

client = AsyncOpenAI(api_key=KIMI_API_KEY, base_url=base_url)

async def retry_with_exponential_backoff(func, *args, **kwargs):
    retries = 0
    delay = INITIAL_RETRY_DELAY
    while retries < MAX_RETRIES:
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            retries += 1
            if retries == MAX_RETRIES:
                raise e
            print(f"Error occurred: {e}. Retrying in {delay} seconds...")
            await asyncio.sleep(delay)
            delay = min(delay * 2, MAX_RETRY_DELAY)

async def web_search(query, KIMI_API_KEY, base_url, model):
    url = f"{base_url}/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {KIMI_API_KEY}",
    }
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query},
        ],
        "temperature": 0.7,
        "tools": [
            {
                "type": "builtin_function",
                "function": {
                    "name": "$web_search",
                },
            }
        ],
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            result = await response.json()
            with open("temp_kimi.json", "w") as f:
                f.write(json.dumps(result, indent=4))
            if "choices" not in result:
                print("Unexpected API response format")
                return "Error: Unexpected API response format"
            try:
                message = result["choices"][0]["message"]
                if "tool_calls" in message:
                    for tool_call in message["tool_calls"]:
                        if (
                            tool_call["type"] == "function"
                            and tool_call["function"]["name"] == "$web_search"
                        ):
                            search_results = json.loads(
                                tool_call["function"]["arguments"]
                            )
                            return json.dumps(
                                search_results, ensure_ascii=False, indent=2
                            )
                return message["content"]
            except KeyError as e:
                print(f"KeyError: {e}")
                print("Full response:", json.dumps(result, indent=2))
                return f"Error: {e}"

async def upload_files(files, cache_tag=None):
    """
    注意：由于 QoS 限制和缓存权限问题，此功能暂时被弃用。
    此代码保留以供将来可能的使用。
    """
    messages = []
    for file in files:
        file_object = await client.files.create(file=Path(file), purpose="file-extract")
        file_content = (await client.files.content(file_id=file_object.id)).text
        messages.append({
            "role": "system",
            "content": file_content,
        })

    if cache_tag:
        async with httpx.AsyncClient() as async_client:
            r = await async_client.post(
                f"{client.base_url}caching",
                headers={"Authorization": f"Bearer {client.api_key}"},
                json={
                    "model": model,
                    "messages": messages,
                    "ttl": 3000,
                    "tags": [cache_tag],
                }
            )
        if r.status_code != 200:
            raise Exception(r.text)
        print(f"success upload file. {messages}")
        return [{
            "role": "cache",
            "content": f"tag={cache_tag};reset_ttl=3000",
        }]
    else:
        return messages

async def generate_outline(topic, client, model, KIMI_API_KEY, base_url, reference_files=None, cache_tag=None):
    """根据主题生成大纲"""
    search_results = await retry_with_exponential_backoff(web_search, f"Generate an outline for the topic: {topic}", KIMI_API_KEY, base_url, model)
    
    messages = [
        {"role": "system", "content": """你是一个专业的文章大纲生成器。请使用Markdown格式生成大纲,
# 一级标题
## 二级标题

以此类推。主要不要返回markdown```转义, 直接正文是markdown格式即可,
         
"""},
        {
            "role": "user",
            "content": f"请为主题'{topic}'生成一个详细的文章大纲。以下是一些相关的搜索结果，可以参考：\n\n{search_results}",
        },
    ]

    if reference_files:
        file_messages = await upload_files(reference_files, cache_tag)
        messages = file_messages + messages

    response = await retry_with_exponential_backoff(
        client.chat.completions.create,
        model=model,
        messages=messages,
        temperature=1.0,
        tools=[
            {
                "type": "builtin_function",
                "function": {
                    "name": "$web_search",
                },
            }
        ],
    )
    return response.choices[0].message.content

def parse_outline(outline):
    """解析大纲，将其分组为一级标题及其下属的所有子标题"""
    lines = outline.split('\n')
    sections = {}
    current_section = None

    for line in lines:
        if line.startswith('## '):
            current_section = line.strip()
            sections[current_section] = []
        elif current_section and line.strip():
            sections[current_section].append(line.strip())

    return sections

async def generate_section_content(section_title, section_outline, full_outline, client, model, KIMI_API_KEY, base_url, reference_files=None, cache_tag=None):
    """根据大纲和章节标题生成章节内容"""
    # search_results = await retry_with_exponential_backoff(
        # web_search, f"Information about {section_title} in the context of {full_outline}", KIMI_API_KEY, base_url, model
    # )
    search_results = ""
    print(reference_files)
    section_outline_str = '\n'.join([section_title] + section_outline)
    messages = [
        {"role": "system", "content": "你是一个专业的文章作者。"},
        {
            "role": "user",
            "content": f"这是文章的完整大纲：\n\n{full_outline}\n\n请根据这个大纲，详细展开以下章节的内容：\n\n{section_outline_str}\n\n以下是一些相关的搜索结果，可以参考：\n\n{search_results}",
        },
    ]

    if reference_files:
        file_messages = await upload_files(reference_files, cache_tag)
        messages = file_messages + messages
        print(f"file upload: {file_messages}")
    print(messages)
    response = await retry_with_exponential_backoff(
        client.chat.completions.create,
        model=model,
        messages=messages,
        temperature=1.0,
        tools=[
            {
                "type": "builtin_function",
                "function": {
                    "name": "$web_search",
                },
            }
        ],
    )
    return response.choices[0].message.content

async def generate_article(topic, KIMI_API_KEY, base_url, model, reference_files=None):
    client = AsyncOpenAI(api_key=KIMI_API_KEY, base_url=base_url)
    cache_tag = None
    # cache_tag = f"article_gen_{int(time.time())}" if reference_files else None

    try:
        # 生成并保存大纲
        # outline = await generate_outline(topic, client, model, KIMI_API_KEY, base_url, reference_files, cache_tag)
        # if outline.startswith("Error:"):
        #     print("Failed to generate outline:", outline)
        #     return
        # save_outline(outline)

        # input("请修正outline.txt 文件中的大纲，完成后按回车键继续...")

        # 读取修改后的大纲
        modified_outline = read_outline()

        # 解析大纲，将其分组为一级标题及其下属的所有子标题
        sections = parse_outline(modified_outline)

        # 创建最终文章文件
        final_article_path = "generated_article_full.md"
        with open(final_article_path, "w", encoding="utf-8") as f:
            f.write(f"# {topic}\n\n")
            f.write(modified_outline + "\n\n")

        # 生成每个章节的内容并直接追加到最终文件
        for i, (section_title, section_outline) in enumerate(sections.items()):
            print(f"正在生成章节：{section_title}")
            content = await generate_section_content(
                section_title, section_outline, modified_outline, client, model, KIMI_API_KEY, base_url, reference_files, cache_tag
            )
            if content.startswith("Error:"):
                print(f"Failed to generate content for section '{section_title}': {content}")
                continue
            
            # 直接追加内容到最终文件
            with open(final_article_path, "a", encoding="utf-8") as f:
                f.write(f"\n\n{section_title}\n\n{content}\n")
            
            print(f"章节 {i+1} 已追加到 {final_article_path}")

        print(f"完整文章生成完成，已保存到 {final_article_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def save_outline(outline, filename="outline.txt"):
    """保存大纲到文件"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(outline)
    print(f"大纲已保存到 {filename}。请修改此文件，然后继续。")

def read_outline(filename="outline.txt"):
    """从文件读取修改后的大纲"""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

# 示例使用
if __name__ == "__main__":
    topic = "边缘云,专属云,超融合的市场行业调研报告"
    reference_dir = Path("reference_cloud")  # 使用 Path 对象来处理路径
    reference_files = [str(reference_dir / file) for file in os.listdir(reference_dir)]  # 只包含 .md 文件
    asyncio.run(generate_article(topic, KIMI_API_KEY, base_url, model, reference_files))
