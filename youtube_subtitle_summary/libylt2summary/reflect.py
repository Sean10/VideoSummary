import os
import asyncio
from asyncio import Semaphore
from .utils import call_openai_api, get_metadata_from_jsonl, logger, sanitize_filename
import time
from openai import AsyncOpenAI

# 设置OpenAI API密钥
YOUR_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if YOUR_OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set")


model = "THUDM/glm-4-9b-chat"
client = AsyncOpenAI(
    api_key=f"{YOUR_OPENAI_API_KEY}",
    base_url="http://localhost:3000/v1",
)

async def reflect_and_summarize(summary_file, original_file, semaphore):
    start_time = time.time()
    async with semaphore:
        logger.info(f"开始处理文件: {summary_file}")
        with open(summary_file, 'r', encoding='utf-8') as f:
            summary_content = f.read()
        
        with open(original_file, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        metadata = get_metadata_from_jsonl(os.path.basename(summary_file))
        if not metadata:
            logger.warning(f"无法获取元数据: {summary_file}")
            return None

        title = sanitize_yaml_string(metadata['title'])
        date = metadata['date']
        updated = metadata['updated']
        
        prompt = f"""作为专业的存储领域分布式存储ceph的研发人员和内容审核专家，请仔细审阅以下内容：

0. 原文件名: {title}
        
1. 现有总结：
{summary_content}

2. 原始字幕内容：
{original_content}

请执行以下任务：
1. 检查总结是否准确反映了原始内容的要点，涵盖会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。
2. 识别任何可能的错误、误解或遗漏的重要信息。
3. 提供一个改进的、更准确的中文总结，确保保留计算机科学/ceph相关领域的英文原文关键词。
4. 生成 3-5 个相关的标签，反映文章的主要主题和技术焦点。

请以以下格式返回你的分析和改进后的总结：

---
title: {title}
date: {date}
updated: {updated}
tags:
- tag1
- tag2
- tag3
categories:
- "视频总结"
subtitle: {os.path.basename(summary_file).replace('.md', '')}
---

[改进后的中文总结内容]

请确保你的回答是 Markdown 格式，并包含上述所有元素。
不要修改---中间模板的date,updated和title,subtitle内容。但如果标题中含有双引号或单引号导致无法满足yaml语法时, 需要去除或替换为适当的字符. 
也不要重复我的问题。
确保生成的tag不包含任何引号或特殊字符。
除了上面样例的yaml front matter外, 请不要额外添加---标记

"""

        messages = [
            {"role": "system", "content": """You are a helpful assistant that reflects on and improves article summaries. 
            注意原始字幕是音译, 可能有错误的文本关键词, 其实际是下文中给出的关键词.
            在总结中，请注意保留以下 Ceph 相关的关键字（如果出现）：
Ceph, distributed storage, CRUSH algorithm, high availability, scalability, object storage,
block storage, file system storage, consistency, decentralization, performance, bluestore,
bluefs, rocksdb, OSD, MON, MDS, PG, RADOS, librados, libcephfs, cephfs, rbd, radosgw, RGW,
RESTful API, authentication, authorization, encryption, erasure coding, replication, 
snapshots, clones, thin provisioning, iSCSI, Fibre Channel, NFS, CIFS, POSIX, monitoring, 
dashboard, management, orchestration, automation, integration, containerization, 
Kubernetes, Docker, virtualization, cloud computing, AWS, Azure, Google Cloud, 
hybrid cloud, multi-cloud, storage cluster, node, disk, SSD, HDD, JBOD, SAN, NAS, 
network, topology, failure domain, recovery, resilience, load balancing, caching, 
compression, deduplication, tiering, performance tuning, benchmarking, testing, validation 
             """},
            {"role": "user", "content": prompt}
        ]

        try:
            api_start_time = time.time()
            completion = await call_openai_api(
                client.chat.completions.create,
                model="THUDM/glm-4-9b-chat",
                messages=messages,
                temperature=0.7,
                max_tokens=4096
            )
            api_end_time = time.time()
            api_duration = api_end_time - api_start_time
            logger.info(f"API 调用耗时: {api_duration:.2f} 秒")
            
            # 检查和修复YAML front matter
            content = completion.choices[0].message.content
            return content
        except Exception as e:
            logger.error(f"反思总结时出错: {e}")
            return None
        
        finally:
            end_time = time.time()
            total_duration = end_time - start_time
            logger.info(f"处理文件 {summary_file} 总耗时: {total_duration:.2f} 秒")

def sanitize_yaml_string(s):
    # 移除或替换可能导致YAML解析错误的字符
    return s.replace('"', '').replace("'", "").replace(":", "-").strip()

async def process_reflections():
    summary_dir = "summary"
    original_dir = "subtitles_origin"
    output_dir = "temp_posts"
    semaphore = Semaphore(15)  # 限制并发请求数

    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 获取已经存在的输出文件列表
    existing_outputs = set(os.listdir(output_dir))

    tasks = []
    for summary_file in os.listdir(summary_dir):
        if summary_file.endswith('.md'):
            original_file = summary_file.replace('.md', '.en.ttml')
            summary_path = os.path.join(summary_dir, summary_file)
            original_path = os.path.join(original_dir, original_file)
            output_path = os.path.join(output_dir, summary_file)

            # 检查文件是否为新增文件
            if summary_file not in existing_outputs and os.path.exists(original_path):
                logger.info(f"发现新文件需要处理: {summary_file}")
                task = asyncio.create_task(reflect_and_summarize(summary_path, original_path, semaphore))
                tasks.append((task, output_path))
            elif summary_file in existing_outputs:
                logger.info(f"文件已存在，跳过处理: {summary_file}")
            else:
                logger.warning(f"原始文件不存在: {original_path}")

    if not tasks:
        logger.info("没有新的文件需要处理")
        return

    start_time = time.time()
    for task, output_path in tasks:
        reflected_content = await task
        if reflected_content:
            # 在写入文件之前，再次检查和清理front matter
            cleaned_content = clean_front_matter(reflected_content)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            logger.info(f"已生成反思后的文章: {output_path}")
    
    end_time = time.time()
    total_duration = end_time - start_time
    logger.info(f"处理所有新文件总耗时: {total_duration:.2f} 秒")
    logger.info(f"平均每个新文件耗时: {total_duration / len(tasks):.2f} 秒")

def clean_front_matter(content):
    lines = content.split('\n')
    in_front_matter = False
    cleaned_lines = []
    for line in lines:
        if line.strip() == '---':
            in_front_matter = not in_front_matter
            cleaned_lines.append(line)
        elif in_front_matter:
            if ':' in line:
                key, value = line.split(':', 1)
                cleaned_value = sanitize_yaml_string(value)
                cleaned_lines.append(f"{key}: {cleaned_value}")
            else:
                cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)
    return '\n'.join(cleaned_lines)