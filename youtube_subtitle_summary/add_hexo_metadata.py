import os
import json
from datetime import datetime
from yt_dlp import utils

def escape_title(title):
    return title.replace(' ', '_').replace('|', '_').replace(':', '_')

def render_template(title, date, updated):
    template = """---
title: {title}
date: {date}
updated: {updated}
tags:
categories:
- "视频总结"
subtitle: tech
---
"""
    return template.format(title=title, date=date, updated=updated)

def process_jsonlines_file(file_path):
    current_post = os.listdir("../source/_posts")
    current_post_title = [file.replace(".md", "") for file in current_post]

    need_insert_post = []
    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            try:
                title = '"' + data['title'] + '"'
                upload_date = datetime.strptime(data['upload_date'], '%Y%m%d').strftime('%Y-%m-%d')
                updated_date = datetime.fromtimestamp(data['timestamp']).strftime('%Y-%m-%d')
            except Exception as e:
                if data['timestamp'] is None:
                    updated_date = upload_date
                else:
                    print(data)
                    print(e)
                    break
            escaped_title = utils._utils.sanitize_filename(title+".md", restricted=True)
            original_file_path = f"summary/{escaped_title}"
            summary_file_path = f"../source/_posts/{escaped_title}"
            
            if escaped_title in current_post_title:
                print(summary_file_path+ " already posted")
                continue
            if not os.path.exists(original_file_path):
                print(summary_file_path+ " not exists")
                continue
            rendered_template = render_template(title, upload_date, updated_date)
            need_insert_post.append((original_file_path, summary_file_path, rendered_template))
            print(f"need to insert to {summary_file_path}")

    # 正式修正文档
    for post in need_insert_post:
        with open(post[0], 'r') as summary_file:
            # if "subtitle: tech" in summary_file.read():
            #     continue
            content = summary_file.read()
        with open(post[1], 'w') as summary_file:
            summary_file.seek(0, 0)
            summary_file.write(post[2] +'\n\n'+ content)
            print("succeed to insert to "+ summary_file_path)

# Example usage
process_jsonlines_file('videos_meta.jsonl')
# process_jsonlines_file('youtube_subtitle_summary/videos_meta.jsonl')
