import os
import subprocess
from openai import OpenAI
from yt_dlp import YoutubeDL, utils
import json
import jsonlines
import datetime
from typing_extensions import List
import time
import re
import shlex
import argparse
import asyncio
import aiohttp
from openai import AsyncOpenAI
from asyncio import Semaphore
import yaml
import asyncio
from asyncio import Queue
import random

# 从环境变量中获取API密钥
YOUR_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if YOUR_OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# 星火 api乱, oneapi暂时不太好用
# model = "SparkDesk-v3.5"
# model = "generalv3.5"
# model = "deepseek-chat"
# model = "Qwen/Qwen2.5-7B-Instruct"
model = "THUDM/glm-4-9b-chat"
# model = "internlm/internlm2_5-7b-chat"
start=0
TIME_INTERVAL=30
client = AsyncOpenAI(
    api_key = f"{YOUR_OPENAI_API_KEY}",
    base_url = "http://localhost:3000/v1",
)

MAX_RETRIES = 10
RETRY_DELAY = 10  # 初始重试延迟（秒）
MAX_RETRY_DELAY = 60  # 最大重试延迟（秒）

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
        await asyncio.sleep(random.uniform(1, 5))  # 添加随机延迟以避免突发请求

# 修改现有的 OpenAI 调用函数
async def call_openai_api(func, *args, **kwargs):
    return await retry_with_exponential_backoff(func, *args, **kwargs)

def get_channel_videos(channel_url, begin, end):
    ydl_opts = {
        'ignoreerrors': True,  # Continue on download errors
        # 'quiet': True,         # Suppress output
        'daterange': utils.DateRange(begin, end),
        'sleep_interval': 30,
        'cachedir': "cache",
        'verbose': True,
        # 这条导致拿到的info只有标题和url了
        'extract_flat': True
    }
    


    with YoutubeDL(ydl_opts) as ydl:
        channel_info = ydl.extract_info(channel_url, download=False)
        with open('channel_info.json', 'w', encoding='utf-8') as f:
            json.dump(channel_info, f, ensure_ascii=False, indent=4)
    # with open('channel_info.json', 'r', encoding='utf-8') as f:
    #     channel_info = json.load(f)

        # 将20240101 这个日期格式转换为 utc时间戳
        # end_date_timestamp = int(datetime.datetime.strptime(end_date, '%Y%m%d').timestamp())

        if 'entries' not in channel_info:
            return []
        
        videos = []
        # for entry in channel_info['entries']:
            
        #         # if end_date_timestamp > int(video_info['timestamp']):
        #         #     print(f"达到日期, 结束")
        #         #     break

                

        #             with jsonlines.open("videos_meta.jsonl", "a") as writer:
        #                 writer.write(video_info)
                        # writer.flush()
        return videos


def full_to_half(s):
    # 全角字符到半角字符的映射表
    full_to_half_map = {
        ord(f): ord(h) for f, h in zip(
            '　！＂＃＄％＆＇（）＊＋，－．／０１２３４５６７８９：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［＼］＾＿｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝～',
            ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
        )
    }
    return s.translate(full_to_half_map)



# 4. 对每个视频URL进行总结并获取翻译
SUMMARY_PREFIX = "summary"
TRANSLATION_PREFIX = "translations"

async def summary(subtitle_file, mode="summary", history=None):
    """
    本函数支持基于历史上下文进行问答，第一次调用时进行总结，第二次调用时进行翻译。
    """
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
        text = "请从上次最后一个字后继续回复, 如果输出结束，结束时返回END。不要在未结束时重复我的问题时回复END该词. 注意回复的翻译结果一定需要是中文"
    else:
        print("mode error")
        import sys
        sys.exit(1)

    
    # if mode == "summary":
    current = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ]
    # else:
    #     current = [{"role": "user", "content": text}]
    messages = history + current
    history = messages
    # with open("temp.json", "a+") as f:
    #     json.dump(messages, f, ensure_ascii=False, indent=4)

    completion = await call_openai_api(
        client.chat.completions.create,
        model=model,
        messages=messages,
        temperature=0.5,
        max_tokens=4096,
        # 以下为deepseek可用
        # temperature=1.1,
        # max_tokens=4096,
    )
    # 如果completion 报错
    if completion.choices[0].message.content is None:
        print(completion)
        print(messages)
        import sys
        sys.exit(1)
    response_content = completion.choices[0].message.content
    # history.append({"role": "user", "content": text})
    history.append({"role": "assistant", "content": response_content})

    title = subtitle_file.replace(".en.ttml", "")
    if mode == "summary":
        output_file = os.path.join(SUMMARY_PREFIX, f"{title}.md")
    else:
        output_file = os.path.join(TRANSLATION_PREFIX, f"{title}.md")

    with open(output_file, "a+", encoding='utf-8') as f:
        # f.write(f"## {title}\n\n")
        f.write(response_content)
    print(response_content)
    print(datetime.datetime.now())
    if "END" in response_content:
        print("翻译结束")
        # 列表为空代表结束
        return []
    
    return history




def clean_subtitles(info):
    # print(info)
    with open("info", "w") as f:
        f.write(json.dumps(info, indent=4))
    try:
        filepath = info['info_dict']['requested_subtitles']['en']['filepath']
    except Exception as e:
        with open("error.log", "w") as f:
            f.write(json.dumps(info))
            f.write(str(e))
        return
    # filepath = utils._utils.sanitize_filename(filepath, True)
    # os.rename(filepath, full_to_half(filepath))
    # filepath = full_to_half(filepath)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    # 使用正则表达式清理字幕文件
    cleaned_content = re.sub(r'^[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9] --> [0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]$', '', content, flags=re.MULTILINE)
    cleaned_content = re.sub(r'^[[:digit:]]\{1,5\}$', '', cleaned_content, flags=re.MULTILINE)
    cleaned_content = re.sub(r'<[^>]*>', '', cleaned_content)
    cleaned_content = re.sub(r'^[[:space:]]*$', '', cleaned_content, flags=re.MULTILINE)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

def sed_command(filepath):
    return "sed -e '/^[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9] --> [0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]$/d' -e '/^[[:digit:]]\{1,5\}$/d' -e 's/<[^>]*>//g' -e '/^[[:space:]]*$/d' -i '' %s".format(filepath)


def get_subtitles(urls: List):
    def my_hook(d):
        with open("d", "w") as f:
            f.write(json.dumps(d, indent=4))
        if d['status'] == 'finished' and 'requested_subtitles' in d:
            for lang, info in d['requested_subtitles'].items():
                if info['ext'] == 'ttml':
                    ttml_path = info['filepath']
                    srt_path = ttml_path.replace('.ttml', '.srt')
                    # os.system(f'ffmpeg -i "{ttml_path}" "{srt_path}"')
                    clean_subtitles(srt_path)

    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'subtitlesformat': 'ttml',
        'convertsubtitles': 'srt',
        # 'progress_hooks': [my_hook],
        'outtmpl': 'subtitles_origin/%(title)s.%(ext)s', # 指定字幕文件存放路径,
        # 'exec_cmd': sed_command,
        'postprocessor_hooks': [clean_subtitles],
        'restrictfilenames': True,
        # 'sleep_interval_subtitles': 60,
    }
    cnt = start
    for url in urls:

        with YoutubeDL(ydl_opts) as ydl:
            video_info = ydl.extract_info(url, download=False)
            title = video_info["title"]
            # 用这个函数来做转换
            title = utils._utils.sanitize_filename(title, True)
            with open(f'video_infos/{title}.json', 'w', encoding='utf-8') as f:
                json.dump(video_info, f, ensure_ascii=False, indent=4)
            entry = video_info
            video_info = {
                'title': entry.get('title', ''),
                'upload_date': entry.get('upload_date', ''),
                'webpage_url': entry.get('webpage_url', ''),
                'playlist_title': entry.get('playlist_title', ''),
                'timestamp': entry.get('timestamp', '')
            }
            print(f"Title: {video_info['title']}, Upload Date: {video_info['upload_date']}, URL: {video_info['webpage_url']}")

            with jsonlines.open("videos_meta.jsonl", "a") as writer:
                writer.write(video_info)
            # if end_date_timestamp > int(video_info['timestamp']):
            #     print(f"达到日期, 结束")
            #     break

            # if entry['webpage_url'] not in downloaded:
                # videos.append(video_info)
            
                # writer.flush()
            ydl.download([url])
            print(cnt)
            cnt += 1
        # if cnt < 40:
        #     summary(full_to_half(f"{title}.en.ttml"))
        time.sleep(TIME_INTERVAL)

# 实现一个队videos_meta.jsonl的遍历, 然后获取到url作为主键, 然后进行去重. 输出一个没有重复的原内容的列表

def main_fectch_subtitle():
    """
    TODO:这里当前仅实现了根据之前获取的一次channel_info.json按顺序遍历的动作
    需要考虑增加, 每次更新一次channel_info, 然后检测其中url比我已经触发过保存呃videos_meta.jsonl新的内容. 或者有差异的内容?
    """
    with open("channel_info.json", "r") as f:
        channel_info = json.load(f)

    downloaded = {}
    with jsonlines.open("videos_meta.jsonl", "r") as reader:
        for item in reader:
            downloaded[item['webpage_url']] = item
    urls = []
    for entry in channel_info['entries']:
        if entry is not None:
            video_info = {
                'title': entry.get('title', ''),
                'upload_date': entry.get('upload_date', ''),
                # 'webpage_url': entry.get('webpage_url', ''),
                'webpage_url': entry.get('url', ''),

                'playlist_title': entry.get('playlist_title', ''),
                'timestamp': entry.get('timestamp', '')
            }
        
        if entry['url'] not in downloaded:
            urls.append(entry['url'])
            print(f"Title: {video_info['title']}, Upload Date: {video_info['upload_date']}, URL: {video_info['webpage_url']}")
    # urls = [item['url'] for item in channel_info['entries']]
    print(urls)
    urls = urls[start:]
    get_subtitles(urls)

def get_latest_file(path, filter="*"):
    from pathlib import Path
    # 指定目录
    directory = Path(path)

    # 获取目录下的所有文件
    files = directory.glob(filter)

    # 根据文件的修改时间排序
    sorted_files = sorted(files, key=lambda f: f.stat().st_mtime)

    # 只保留文件名
    sorted_file_names = [file.name for file in sorted_files]
    return sorted_file_names

def main_translate(subtitle_file):
    # 功能5. 支持上下文翻译
    # translate
    if not history:
        print("返回了END, 错了")
        import sys;sys.exit(1)
    history = summary(subtitle_file, "translation")
    
    while history:
        history = summary(subtitle_file, "translation_continue", history)
        print("try first")
    print("end")

def main_summary():
    """
    最好支持根据文件存在, 获取哪些是未触发过总结的, 发起一次总结.
    """

    sorted_file_names = main_summary_diff()
    # cnt = start
    for file in sorted_file_names:
        # print(cnt)
        history = summary(file, "summary")
        # cnt += 1

# 实现一个扫描目录, 识别哪些文件已经被总结过
# 扫描summary目录下, 哪些文件已经存在, 然后videos_meta.jsonl中的title中存在的文件, 后者应该是包含前者的关系, 取差
def main_summary_diff():
    need_summary = []
    # 获取summary目录下所有文件
    summary_files = os.listdir("summary")
    # summary_files = sorted_file_names
    summaryed = []
    for title in summary_files:
        title = title.replace(".md", "")
        summaryed.append(title)

    # 获取已下载的字幕文件列表
    downloaded = {}
    with jsonlines.open("videos_meta.jsonl", "r") as reader:
        for item in reader:
            title = utils._utils.sanitize_filename(item['title'], True)
            title = title.replace(".en.ttml", "")
            if title in downloaded:
                print(f"已下载过: {title}")
                continue
            downloaded[title] = item

            if title not in summaryed:
                print(f"未总结: {title}")
                need_summary.append(title+".en.ttml")
            else:
                print(f"已总结: {title}")
        # title = utils._utils.sanitize_filename(file, True)
        
    return list(reversed(need_summary))

def get_quarter(date):
    return (date.month - 1) // 3 + 1

async def classify_batch(batch, session, semaphore):
    async with semaphore:
        prompt = """你是一个专业的 Ceph 存储专家和内容分类专家。请根据以下文章标题列表，将它们分类到适当的类别中。使用以下分类方案：

        1. 内容类型：技术深度探讨、新特性介绍、用户案例分享、社区更新和路线图、性能优化和调优、故障排除和最佳实践、集成和互操作性
        2. Ceph 组件：RADOS 核心、RGW (对象存储)、RBD (块存储)、CephFS (文件系统)、监控和管理工具
        3. 应用场景：云原生存储、大数据和分析、备份和归档、高性能计算 (HPC)、边缘计算存储
        4. 技术主题：扩展性和性能、数据安全和加密、多站点和灾难恢复、自动化和编排、监控和可观察性
        5. 会议类型：Ceph 月度社区会议、Ceph 开发者峰会、用户组会议、技术研讨会、行业会议演讲
        6. 时间线：季度更新、年度总结、版本发布说明

        返回一个 JSON 格式的结果，其中键是上述分类方案中的具体类别，值是属于该类别的文章标题列表。每篇文章应至少分到一个类别，但可以分到多个相关类别。以下是文章标题列表：

        {}

        请确保返回有效的 JSON 格式。
        """.format("\n".join(batch))

        messages = [
            {"role": "system", "content": "You are a helpful assistant that classifies articles."},
            {"role": "user", "content": prompt}
        ]

        try:
            completion = await call_openai_api(
                client.chat.completions.create,
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=4096,
                response_format={"type": "json_object"}
            )
            response_content = completion.choices[0].message.content
            return json.loads(response_content)
        except json.JSONDecodeError:
            print(f"JSON 解析失败，响应内容：")
            print(response_content)
            return {}
        except Exception as e:
            print(f"处理批次时出错: {e}")
            return {}

async def classify_posts_by_content():
    posts_dir = "source/_posts"
    post_titles = [f for f in os.listdir(posts_dir) if f.endswith('.md')]
    
    batch_size = 50  # 每批处理的文章数量
    max_concurrent_requests = 15  # 最大并发请求数
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
                        # print(f"Type of metadata['date']: {type(metadata['date'])}")
                        if isinstance(metadata['date'], datetime.date):
                            date = metadata['date']
                        else:
                            date = datetime.datetime.strptime(metadata['date'], '%Y-%m-%d').date()
                        year = date.year
                        quarter = get_quarter(date)
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

async def generate_tags(content, semaphore):
    async with semaphore:
        prompt = f"""作为一个 Ceph 存储专家，请为以下内容生成 3-5 个相关的标签。这些标签应该反映文章的主要主题和技术焦点。请以 JSON 数组格式返回标签。

        内容摘要：
        {content[:1000]}  # 只使用内容的前1000个字符

        请返回格式如下的 JSON：
        ["tag1", "tag2", "tag3"]
        """

        messages = [
            {"role": "system", "content": "You are a helpful assistant that generates tags for technical articles."},
            {"role": "user", "content": prompt}
        ]

        try:
            completion = await call_openai_api(
                client.chat.completions.create,
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=100,
                response_format={"type": "json_object"}
            )
            response_content = completion.choices[0].message.content
            return json.loads(response_content)
        except Exception as e:
            print(f"生成标签时出错: {e}")
            return []

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

async def add_hexo_metadata():
    file_path = 'videos_meta.jsonl'
    current_post = os.listdir("../source/_posts")
    current_post_title = current_post
    need_insert_post = []

    semaphore = Semaphore(15)  # 限制并发请求数

    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            try:
                title = '"' + data['title'] + '"'
                upload_date = datetime.datetime.strptime(data['upload_date'], '%Y%m%d').strftime('%Y-%m-%d')
                updated_date = datetime.datetime.fromtimestamp(data['timestamp']).strftime('%Y-%m-%d')
            except Exception as e:
                if data['timestamp'] is None:
                    updated_date = upload_date
                else:
                    print(data)
                    print(e)
                    continue

            escaped_title = utils._utils.sanitize_filename(title+".md", restricted=True)
            original_file_path = f"summary/{escaped_title}"
            summary_file_path = f"../source/_posts/{escaped_title}"
            
            if escaped_title in current_post_title:
                print(summary_file_path+ " already posted")
                continue
            if not os.path.exists(original_file_path):
                print(summary_file_path+ " not exists")
                continue
            
            with open(original_file_path, 'r') as summary_file:
                content = summary_file.read()

            tags = await generate_tags(content, semaphore)
            rendered_template = render_template(title, upload_date, updated_date, tags)
            need_insert_post.append((original_file_path, summary_file_path, rendered_template))
            print(f"need to insert to {summary_file_path}")

    for post in need_insert_post:
        with open(post[0], 'r') as summary_file:
            content = summary_file.read()
        with open(post[1], 'w') as summary_file:
            summary_file.seek(0, 0)
            summary_file.write(post[2] +'\n\n'+ content)
            print("succeed to insert to "+ post[1])
    
    print(f"处理了 {len(need_insert_post)} 个文件")

async def reflect_and_summarize(summary_file, original_file, semaphore):
    start_time = time.time()
    async with semaphore:
        print(f"开始处理文件: {summary_file}")
        with open(summary_file, 'r', encoding='utf-8') as f:
            summary_content = f.read()
        
        with open(original_file, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # 获取元数据
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
{original_content}  # 限制字数以避免超过 token 限制



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
不要修改---中间模板的date,updated和title,subtitle内容. 也不要重复我的问题. 
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
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=4096
            )
            api_end_time = time.time()
            api_duration = api_end_time - api_start_time
            print(f"API 调用耗时: {api_duration:.2f} 秒")
            return completion.choices[0].message.content
        except Exception as e:
            print(f"反思总结时出错: {e}")
            return None
        
        finally:
            end_time = time.time()
            total_duration = end_time - start_time
            print(f"处理文件 {summary_file} 总耗时: {total_duration:.2f} 秒")

def load_metadata_to_dict():
    metadata_dict = {}
    with open('videos_meta.jsonl', 'r') as file:
        for line in file:
            data = json.loads(line)
            key = utils._utils.sanitize_filename(data['title'], True) + '.md'
            metadata_dict[key] = {
                'title': '"' + data['title'] + '"',
                'date': datetime.datetime.strptime(data['upload_date'], '%Y%m%d').strftime('%Y-%m-%d'),
                'updated': datetime.datetime.fromtimestamp(data['timestamp']).strftime('%Y-%m-%d') if data['timestamp'] else None
            }
    return metadata_dict

# 全局变量，用于存储元数据字典
metadata_dict = load_metadata_to_dict()

def get_metadata_from_jsonl(filename):
    return metadata_dict.get(filename)

# 在主函数或初始化部分调用 load_metadata_to_dict
async def main_async():
    global metadata_dict
    metadata_dict = load_metadata_to_dict()
    # ... 其余代码保持不变 ...

async def process_reflections():
    summary_dir = "summary"
    original_dir = "subtitles_origin"
    output_dir = "temp_posts"
    # output_dir = "../source/_posts"
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

    start_time = time.time()
    for task, output_path in tasks:
        reflected_content = await task
        if reflected_content:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(reflected_content)
            print(f"已生成反思后的文章: {output_path}")
    
    end_time = time.time()
    total_duration = end_time - start_time
    print(f"处理所有文件总耗时: {total_duration:.2f} 秒")
    print(f"平均每个文件耗时: {total_duration / len(tasks):.2f} 秒")

async def generate_quarterly_summary(quarter, post_titles, semaphore):
    async with semaphore:
        summaries = []
        for post_title in post_titles:
            with open(os.path.join("source/_posts", post_title), 'r', encoding='utf-8') as f:
                summaries.append(f.read())
        
        combined_summary = "\n\n".join(summaries)
        
        prompt = f"""作为专业的存储领域分布式存储Ceph的研发人员，请对以下{quarter}季度的会议总结进行综合分析，生成一份季度总结报告。
        
        请包含以下内容：
        1. 本季度Ceph社区的主要活动和重点议题
        2. 技术发展和创新亮点
        3. 重要的决策和里程碑
        4. 社区贡献和合作情况
        5. 下一季度的展望和计划

        以下是本季度的会议总结：

        {combined_summary}  # 限制字数以避免超过token限制

        请以Markdown格式输出季度总结报告，包含适当的标题和分段。
        """

        messages = [
            {"role": "system", "content": "You are a helpful assistant that generates quarterly summary reports for Ceph community."},
            {"role": "user", "content": prompt}
        ]

        try:
            completion = await call_openai_api(
                client.chat.completions.create,
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=4096
            )
            return completion.choices[0].message.content
        except Exception as e:
            print(f"生成季度总结报告时出错: {e}")
            return None

async def process_quarterly_summaries():
    with open("post_classification_by_quarter.json", "r", encoding="utf-8") as f:
        quarterly_reports = json.load(f)
    
    semaphore = Semaphore(15)  # 限制并发请求数
    
    for quarter, post_titles in quarterly_reports.items():
        summary = await generate_quarterly_summary(quarter, post_titles, semaphore)
        if summary:
            # output_file = f"posts_quarter/{quarter}_Ceph社区季度总结.md"
            output_file = f"source/_posts/{quarter}_Ceph社区季度总结.md"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"""---
title: "{quarter} Ceph社区季度总结"
date: {quarter[:4]}-{int(quarter[5])*3}-01
updated: {quarter[:4]}-{int(quarter[5])*3}-01
categories:
- "季度总结"
tags:
- Ceph
- 社区动态
- 技术发展
subtitle: quarterly-summary
---

{summary}
""")
            print(f"已生成季度总结报告: {output_file}")

# 修改主函数以支持异步
async def main_async():
    parser = argparse.ArgumentParser(description="YouTube Subtitle Summary Tool")
    parser.add_argument('--fetch', action='store_true', help='Fetch videos from channel')
    parser.add_argument('--fetch-diff', action='store_true', help='Fetch videos from channel')
    parser.add_argument('--summarize', action='store_true', help='Summarize subtitles')
    parser.add_argument('--summarize-diff', action='store_true', help='Summarize subtitles')
    parser.add_argument('--translate', type=str, help='Translate a specific subtitle file')
    parser.add_argument('--classify-content', action='store_true', help='Classify posts by content')
    parser.add_argument('--classify-quarter', action='store_true', help='Classify posts by quarter')
    parser.add_argument('--add-metadata', action='store_true', help='Add Hexo metadata to summary files')
    parser.add_argument('--reflect', action='store_true', help='Reflect on and improve existing summaries')
    parser.add_argument('--quarterly-summary', action='store_true', help='Generate quarterly summary reports')
    args = parser.parse_args()

    if args.fetch:
        # 功能1. 采集channel_info.json中用于后续去重
        channel_url = 'https://www.youtube.com/@Cephstorage'
        videos = get_channel_videos(channel_url, "20220101", "today")
    if args.fetch_diff:
        # 功能2. 采集剩余范围内文件字幕
        main_fectch_subtitle()

    if args.summarize_diff:
        # 功能3. 扫描哪些文件未总结
        main_summary_diff()

    if args.summarize:
        # 功能4. 触发总结
        main_summary()

    if args.translate:
        # 功能6, 指定文件进行总结输出
        summary(args.translate)

    if args.classify_content:
        await classify_posts_by_content()

    if args.classify_quarter:
        classify_posts_by_quarter()

    if args.add_metadata:
        await add_hexo_metadata()

    if args.reflect:
        await process_reflections()

    if args.quarterly_summary:
        await process_quarterly_summaries()

    # 在所有任务完成后，处理重试队列
    await process_retry_queue()

# 修改程序入口点
if __name__ == "__main__":
    asyncio.run(main_async())