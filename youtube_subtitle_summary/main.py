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

# 从环境变量中获取API密钥
YOUR_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if YOUR_OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

start=0
TIME_INTERVAL=30
client = OpenAI(
    api_key = f"{YOUR_OPENAI_API_KEY}",
    base_url = "http://localhost:3000/v1",
)

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

def summary(subtitle_file, mode="summary", history=None):
    """
    本函数支持基于历史上下文进行问答，第一次调用时进行总结，第二次调用时进行翻译。
    """
    if history is None:
        history = []

    # 星火 api乱, oneapi暂时不太好用
    # model = "SparkDesk-v3.5"
    # model = "generalv3.5"
    # model = "deepseek-chat"
    # model = "Qwen/Qwen1.5-7B-Chat"
    model = "THUDM/glm-4-9b-chat"
    if mode == "summary" or mode == "translation":
        fullpath = os.path.join("subtitles_origin", subtitle_file)
        with open(fullpath, 'r', encoding='utf-8') as file:
            text = file.read()

    if mode == "summary":
        prompt = """你是专业的存储领域分布式存储ceph的研发人员, 也是视频会议字幕翻译(负责英译中)及总结人员, 麻烦将下文内容用中文总结, 编写出优质的会议纪要（会议记录）
        注意保留部分计算机科学/ceph相关领域英文原文的关键词.
        需要涵盖会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划.
        再次重复, 必须用中文回答.
        """
    elif mode == "translation":
        prompt = """你是专业的存储领域分布式存储ceph的研发人员, 也是计算机专业+英语专业的翻译人员, 麻烦将下文内容用中文翻译, 编写出优质的会议中文对话内容
        注意保留部分计算机科学/ceph相关领域英文原文的关键词.
        注意按照内容主题划分段落章节.
        如果会议内容过长，可按照3000字一次进行回复, 在最后翻译结束时返回END。不要在未结束时重复我的问题时回复END该词. 注意回复的翻译结果一定需要是中文
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

    completion = client.chat.completions.create(
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


# 主函数
def main():
    parser = argparse.ArgumentParser(description="YouTube Subtitle Summary Tool")
    parser.add_argument('--fetch', action='store_true', help='Fetch videos from channel')
    parser.add_argument('--fetch-diff', action='store_true', help='Fetch videos from channel')
    parser.add_argument('--summarize', action='store_true', help='Summarize subtitles')
    parser.add_argument('--summarize-diff', action='store_true', help='Summarize subtitles')
    parser.add_argument('--translate', type=str, help='Translate a specific subtitle file')
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

if __name__ == "__main__":
    main()