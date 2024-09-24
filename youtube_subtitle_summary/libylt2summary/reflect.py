import os
import asyncio
from asyncio import Semaphore
from .utils import call_openai_api, get_metadata_from_jsonl

async def reflect_and_summarize(summary_file, original_file, semaphore):
    async with semaphore:
        print(f"开始处理文件: {summary_file}")
        with open(summary_file, 'r', encoding='utf-8') as f:
            summary_content = f.read()
        
        with open(original_file, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        metadata = get_metadata_from_jsonl(os.path.basename(summary_file))
        if not metadata:
            print(f"无法获取元数据: {summary_file}")
            return None

        title = metadata['title']
        date = metadata['date']
        updated = metadata['updated']
        
        prompt = f"""作为专业的存储领域分布式存储ceph的研发人员和内容审核专家，请仔细审阅以下内容：

0. 原文件名: {title}
        
1. 现有总结：
{summary_content}

2. 原始字幕内容：
{original_content[:1000]}  # 限制字数以避免超过 token 限制

请执行以下任务：
1. 检查总结是否准确反映了原始内容的要点，涵盖会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。
2. 识别任何可能的错误、误解或遗漏的重要信息。
3. 提供一个改进的、更准确的中文总结，确保保留计算机科学/ceph相关领域的英文原文关键词。
4. 生成 3-5 个相关的标签，反映文章的主要主题和技术焦点。

请以以下格式返回你的分析和改进后的总结：

---
title: "{title}"
date: {date}
updated: {updated}
tags:
- [tag1]
- [tag2]
- [tag3]
categories:
- "视频总结"
subtitle: {os.path.basename(summary_file).replace('.md', '')}
---

[改进后的中文总结内容]

请确保你的回答是 Markdown 格式，并包含上述所有元素。
不要修改---中间模板的date,updated和title,subtitle内容。也不要重复我的问题。
"""

        messages = [
            {"role": "system", "content": "You are a helpful assistant that reflects on and improves article summaries."},
            {"role": "user", "content": prompt}
        ]

        try:
            completion = await call_openai_api(
                client.chat.completions.create,
                model="THUDM/glm-4-9b-chat",
                messages=messages,
                temperature=0.7,
                max_tokens=4096
            )
            return completion.choices[0].message.content
        except Exception as e:
            print(f"反思总结时出错: {e}")
            return None

async def process_reflections():
    summary_dir = "summary"
    original_dir = "subtitles_origin"
    output_dir = "temp_posts"
    semaphore = Semaphore(15)  # 限制并发请求数

    tasks = []
    for summary_file in os.listdir(summary_dir):
        if summary_file.endswith('.md'):
            original_file = summary_file.replace('.md', '.en.ttml')
            summary_path = os.path.join(summary_dir, summary_file)
            original_path = os.path.join(original_dir, original_file)
            output_path = os.path.join(output_dir, summary_file)

            if os.path.exists(original_path):
                task = asyncio.create_task(reflect_and_summarize(summary_path, original_path, semaphore))
                tasks.append((task, output_path))
            else:
                print(f"原始文件不存在: {original_path}")

    for task, output_path in tasks:
        reflected_content = await task
        if reflected_content:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(reflected_content)
            print(f"已生成反思后的文章: {output_path}")

    print(f"处理了 {len(tasks)} 个文件")