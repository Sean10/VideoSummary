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
            summary_file_path = f"source/_posts/{escaped_title}"
            
            if not os.path.exists(summary_file_path):
                print(summary_file_path+ " not exists")
                continue
            rendered_template = render_template(title, upload_date, updated_date)
            with open(summary_file_path, 'r+') as summary_file:
                content = summary_file.read()
                summary_file.seek(0, 0)
                summary_file.write(rendered_template +'\n\n'+ content)
            print("succeed to insert to "+ summary_file_path)

# Example usage
process_jsonlines_file('youtube_subtitle_summary/videos_meta.jsonl')
