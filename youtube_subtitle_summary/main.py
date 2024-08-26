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

# 从环境变量中获取API密钥
YOUR_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if YOUR_OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

start=290
client = OpenAI(
    api_key = f"{YOUR_OPENAI_API_KEY}",
    base_url = "http://localhost:3000/v1",
    
)



def get_channel_videos(channel_url, begin, end):
    ydl_opts = {
        'ignoreerrors': True,  # Continue on download errors
        # 'quiet': True,         # Suppress output
        'daterange': utils.DateRange(begin, end),
        'sleep_interval': 60,
        'cachedir': "cache",
        'verbose': True,
        # 这条导致拿到的info只有标题和url了
        'extract_flat': True
    }
    
    downloaded = {}
    with jsonlines.open("videos_meta.jsonl", "r") as reader:
        for item in reader:
            downloaded[item['webpage_url']] = item


    with YoutubeDL(ydl_opts) as ydl:
        channel_info = ydl.extract_info(channel_url, download=False)
        
        with open('channel_info.json', 'w', encoding='utf-8') as f:
            json.dump(channel_info, f, ensure_ascii=False, indent=4)
        # 将20240101 这个日期格式转换为 utc时间戳
        # end_date_timestamp = int(datetime.datetime.strptime(end_date, '%Y%m%d').timestamp())

        if 'entries' not in channel_info:
            return []
        
        videos = []
        for entry in channel_info['entries']:
            if entry is not None:
                video_info = {
                    'title': entry.get('title', ''),
                    'upload_date': entry.get('upload_date', ''),
                    'webpage_url': entry.get('webpage_url', ''),
                    'playlist_title': entry.get('playlist_title', ''),
                    'timestamp': entry.get('timestamp', '')
                }
                # if end_date_timestamp > int(video_info['timestamp']):
                #     print(f"达到日期, 结束")
                #     break

                if entry['webpage_url'] not in downloaded:
                    # videos.append(video_info)
                    print(f"Title: {video_info['title']}, Upload Date: {video_info['upload_date']}, URL: {video_info['webpage_url']}")

                    with jsonlines.open("videos_meta.jsonl", "a") as writer:
                        writer.write(video_info)
                        writer.flush()
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
    model = "deepseek-chat"

    if mode == "summary" or mode == "translation":
        fullpath = os.path.join("subtitles_origin", subtitle_file)
        with open(fullpath, 'r', encoding='utf-8') as file:
            text = file.read()

    if mode == "summary":
        prompt = """你是专业的存储领域分布式存储ceph的研发人员, 也是视频会议字幕总结人员, 麻烦将下文内容用中文总结, 编写出优质的会议纪要（会议记录）
        注意保留部分计算机科学/ceph相关领域英文原文的关键词.
        需要涵盖会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划.
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
        # temperature=0.5,
        max_tokens=2048,
        # 以下为deepseek可用
        # temperature=1.1,
        # max_tokens=4096,
    )

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
        time.sleep(60)

# 主函数
def main():
    # channel_id = 'YOUR_CHANNEL_ID'
    # video_urls = get_video_urls(channel_id)
    # download_subtitles(video_urls)
    # video_urls = [""]
    # summaries = summarize_and_translate(video_urls)
    # print(summaries)

    # channel_url = 'https://www.youtube.com/@Cephstorage'
    ## channel_url = 'https://www.youtube.com/watch?v=U9Qgq6HqN6c&list=PLrBUGiINAakMz4n_oOeiueeUkGynQZCbK'
    # videos = get_channel_videos(channel_url, "20240101", "today")
    # "https://www.youtube.com/watch?v=bByZZk3DiXU",

    # 目前主要实现方案
    # with open("channel_info.json", "r") as f:
    #     channel_info = json.load(f)
    # urls = channel_info['entries']
    # urls = [item['url'] for item in channel_info['entries']]
    # urls = urls[start:]
    # get_subtitles(urls)


    # subtitle_file = "Ceph Developer Monthly ｜ 2024-08-07 [bByZZk3DiXU].en.srt"
    # subtitle_file = "2015-APR-23_--_Ceph_Tech_Talks_-_Calamari.en.ttml"
    # summary
    # 按照时间顺序排序列出指定目录下所有文件名
    from pathlib import Path
    # 指定目录
    directory = Path("subtitles_origin")

    # 获取目录下的所有文件
    files = directory.glob("*")

    # 根据文件的修改时间排序
    sorted_files = sorted(files, key=lambda f: f.stat().st_mtime)

    # 只保留文件名
    sorted_file_names = [file.name for file in sorted_files]
    # files = os.listdir("subtitles_origin")
    cnt = start
    for file in sorted_file_names[start:700]:
        print(cnt)
        history = summary(file, "summary")
        cnt += 1

    # translate
    # if not history:
    #     print("返回了END, 错了")
    #     import sys;sys.exit(1)
    # history = summary(subtitle_file, "translation")
    
    # while history:
    #     history = summary(subtitle_file, "translation_continue", history)
    #     print("try first")
    # print("end")


    # summary('MicroCeph from Development to Solutions ｜ Ceph Days NYC 2024.en.ttml')



if __name__ == "__main__":
    main()