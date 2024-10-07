import os
import json
import jsonlines
import datetime
import time
import asyncio
from yt_dlp import YoutubeDL, utils
from typing import List
from .utils import clean_subtitles, sanitize_filename, logger

TIME_INTERVAL = 30

def get_channel_videos(channel_url, begin, end):
    ydl_opts = {
        'ignoreerrors': True,
        'daterange': utils.DateRange(begin, end),
        'sleep_interval': 30,
        'cachedir': "cache",
        'verbose': True,
        'extract_flat': True
    }

    with YoutubeDL(ydl_opts) as ydl:
        channel_info = ydl.extract_info(channel_url, download=False)
        with open('channel_info.json', 'w', encoding='utf-8') as f:
            json.dump(channel_info, f, ensure_ascii=False, indent=4)

        if 'entries' not in channel_info:
            return []
        
        return []

def get_subtitles(urls: List):
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'subtitlesformat': 'ttml',
        'convertsubtitles': 'srt',
        'outtmpl': 'subtitles_origin/%(title)s.%(ext)s',
        'postprocessor_hooks': [clean_subtitles],
        'restrictfilenames': True,
        # 'ignoreerrors': True,  # 添加这个选项来忽略错误
    }
    cnt = 0
    for url in urls:
        try:
            with YoutubeDL(ydl_opts) as ydl:
                video_info = ydl.extract_info(url)
                if video_info is None:
                    logger.warning(f"无法获取视频信息: {url}")
                    continue
                
                title = video_info["title"]
                title = sanitize_filename(title)
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
                logger.info(f"Title: {video_info['title']}, Upload Date: {video_info['upload_date']}, URL: {video_info['webpage_url']}")

                with jsonlines.open("videos_meta.jsonl", "a") as writer:
                    writer.write(video_info)
                
                # 尝试下载字幕
                try:
                    ydl.download(url)
                except Exception as e:
                    logger.error(f"下载字幕时出错: {e}")
                    logger.info(f"跳过此视频并继续: {url}")
                
                logger.debug(f"处理视频计数: {cnt}")
                cnt += 1
        except Exception as e:
            logger.error(f"处理视频时出错: {e}")
            logger.info(f"跳过此视频并继续: {url}")
        
        time.sleep(TIME_INTERVAL)

def main_fectch_subtitle():
    logger.info("开始执行 main_fectch_subtitle 函数")
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
                'webpage_url': entry.get('url', ''),
                'playlist_title': entry.get('playlist_title', ''),
                'timestamp': entry.get('timestamp', '')
            }
        
        if entry['url'] not in downloaded:
            urls.append(entry['url'])
            logger.info(f"新视频: Title: {video_info['title']}, Upload Date: {video_info['upload_date']}, URL: {video_info['webpage_url']}")
    
    logger.info(f"找到 {len(urls)} 个新视频需要处理")
    urls = urls[0:]
    get_subtitles(urls)
    logger.info("main_fectch_subtitle 函数执行完毕")