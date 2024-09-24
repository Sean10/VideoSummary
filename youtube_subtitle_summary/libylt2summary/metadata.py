import os
import json
import datetime
import asyncio
from asyncio import Semaphore
from .utils import call_openai_api, sanitize_filename

async def add_hexo_metadata():
    file_path = 'videos_meta.jsonl'
    current_post = os.listdir("../source/_posts")
    current_post_title = current_post
    need_insert_post = []

    semaphore = Semaphore(15)

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

            escaped_title = sanitize_filename(title + ".md", restricted=True)
            original_file_path = f"summary/{escaped_title}"
            summary_file_path = f"../source/_posts/{escaped_title}"
            
            if escaped_title in current_post_title:
                print(summary_file_path + " already posted")
                continue
            if not os.path.exists(original_file_path):
                print(summary_file_path + " not exists")
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
            summary_file.write(post[2] + '\n\n' + content)
            print("succeed to insert to " + post[1])
    
    print(f"处理了 {len(need_insert_post)} 个文件")