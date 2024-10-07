import os
import asyncio
from langchain.document_loaders import BiliBiliLoader
from bilibili_api import video, sync

# 从环境变量获取B站认证信息
BILIBILI_SESSDATA = os.getenv("BILIBILI_SESSDATA")
BILIBILI_JCT = os.getenv("BILIBILI_JCT")
BILIBILI_BUVID3 = os.getenv("BILIBILI_BUVID3")

async def fetch_subtitles(channel_id):
    # 创建channel实例
    c = channel.Channel(channel_id, credential={
        "sessdata": BILIBILI_SESSDATA,
        "bili_jct": BILIBILI_JCT,
        "buvid3": BILIBILI_BUVID3
    })
    
    # 获取频道信息
    channel_info = await c.get_channel_info()
    channel_name = channel_info['name']
    
    # 创建存储目录
    os.makedirs(channel_name, exist_ok=True)
    
    # 获取频道视频列表
    video_list = await c.get_videos()
    
    for video_info in video_list:
        video_id = video_info['bvid']
        video_title = video_info['title']
        video_url = f"https://www.bilibili.com/video/{video_id}"
        
        # 创建BiliBiliLoader实例
        loader = BiliBiliLoader(
            video_urls=[video_url],
            credential={
                "sessdata": BILIBILI_SESSDATA,
                "bili_jct": BILIBILI_JCT,
                "buvid3": BILIBILI_BUVID3
            }
        )
        
        # 获取字幕
        try:
            documents = loader.load()
            if documents:
                save_subtitles(channel_name, video_title, documents[0].page_content)
            else:
                print(f"视频 {video_title} 没有可用的字幕")
        except Exception as e:
            print(f"处理视频 {video_title} 时出错: {str(e)}")

def save_subtitles(channel_name, video_title, subtitles):
    # 清理文件名
    safe_title = "".join([c for c in video_title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
    filename = f"{channel_name}/{safe_title}.md"
    
    # 将字幕内容写入文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# {video_title}\n\n")
        f.write(subtitles)
    
    print(f"已保存字幕: {filename}")

async def main():
    channel_id = 1206844881  # 替换为目标B站频道ID
    await fetch_subtitles(channel_id)

if __name__ == "__main__":
    asyncio.run(main())