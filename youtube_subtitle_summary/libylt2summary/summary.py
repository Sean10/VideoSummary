import os
import json
import jsonlines
from .utils import sanitize_filename
import asyncio
from openai import AsyncOpenAI
import datetime

# 设置OpenAI API密钥
YOUR_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if YOUR_OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

client = AsyncOpenAI(
    api_key = f"{YOUR_OPENAI_API_KEY}",
    base_url = "http://localhost:3000/v1",
)

model = "deepseek-ai/DeepSeek-V2-Chat"
# model = "THUDM/glm-4-9b-chat"

async def call_openai_api(func, *args, **kwargs):
    MAX_RETRIES = 10
    RETRY_DELAY = 10
    MAX_RETRY_DELAY = 60
    retries = 0
    delay = RETRY_DELAY
    while retries < MAX_RETRIES:
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            print(f"Error occurred: {e}. Retrying in {delay} seconds...")
            await asyncio.sleep(delay)
            retries += 1
            delay = min(delay * 2, MAX_RETRY_DELAY)
    
    print(f"Task failed after {MAX_RETRIES} attempts.")
    return None

async def summary(subtitle_file, mode="summary", history=None):
    if history is None:
        history = []

    if mode == "summary" or mode == "translation":
        fullpath = os.path.join("subtitles_origin", subtitle_file)
        if not os.path.exists(fullpath):
            print(f"文件不存在: {fullpath}")
            return history
        with open(fullpath, 'r', encoding='utf-8') as file:
            text = file.read()

    if mode == "summary":
        prompt = """你是专业的存储领域分布式存储ceph的研发人员, 也是视频会议字幕翻译(负责英译中)及总结人员, 麻烦将下文内容用中文总结, 编写出优质的会议纪要（会议记录）
        注意保留部分计算机科学/ceph相关领域英文原文的关键词.
        需要涵盖会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划.
        再次重复, 必须用中文回答.

        以下是ceph相关的保留关键字. 
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
        """
    elif mode == "translation":
        prompt = """你是专业的存储领域分布式存储ceph的研发人员, 也是计算机专业+英语专业的翻译人员, 麻烦将下文内容用中文翻译, 编写出优质的会议中文对话内容
        注意保留部分计算机科学/ceph相关领域英文原文的关键词.
        注意按照内容主题划分段落章节.
        如果会议内容过长，可按照3000字一次进行回复, 在最后翻译结束时返回END。不要在未结束时重复我的问题时回复END该词. 注意回复的翻译结果一定需要是中文

        以下是ceph相关的保留关键字. 
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
        """
    elif mode == "translation_continue":
        prompt = """你是专业的存储领域分布式存储ceph的研发人员, 也是计算机专业+英语专业的翻译人员, 麻烦将下文内容用中文翻译, 编写出优质的会议中文对话内容
        注意保留部分计算机科学/ceph相关领域英文原文的关键词.
        注意按照内容主题划分段落章节.
        如果会议内容过长，可按照3000字一次进行回复, 在最后翻译结束时返回END。不要在未结束时重复我的问题时回复END该词. 注意回复的翻译结果一定需要是中文
        """
        text = "请从上次最后一个字后继续回复, 如果输出��束，结束时返回END。不要在未结束时重复我的问题时回复END该词. 注意回复的翻译结果一定需要是中文"
    else:
        print("mode error")
        import sys
        sys.exit(1)

    current = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": text}
    ]
    messages = history + current
    history = messages

    completion = await call_openai_api(
        client.chat.completions.create,
        model=model,
        messages=messages,
        temperature=0.5,
        max_tokens=4096,
    )
    
    if completion.choices[0].message.content is None:
        print(completion)
        print(messages)
        import sys
        sys.exit(1)
    response_content = completion.choices[0].message.content
    history.append({"role": "assistant", "content": response_content})

    title = subtitle_file.replace(".en.ttml", "")
    if mode == "summary":
        output_file = os.path.join("summary", f"{title}.md")
    else:
        output_file = os.path.join("translations", f"{title}.md")

    with open(output_file, "a+", encoding='utf-8') as f:
        f.write(response_content)
    print(response_content)
    print(datetime.datetime.now())
    if "END" in response_content:
        print("翻译结束")
        return []
    
    return history

async def main_summary():
    sorted_file_names = show_summary_diff()
    for file in sorted_file_names:
        history = await summary(file, "summary")

def show_summary_diff():
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

if __name__ == "__main__":
    asyncio.run(main_summary())