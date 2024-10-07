import os
import json
import datetime
import asyncio
from asyncio import Semaphore
from .utils import call_openai_api, sanitize_filename, logger, render_template

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
                model="THUDM/glm-4-9b-chat",
                messages=messages,
                temperature=0.7,
                max_tokens=100,
                response_format={"type": "json_object"}
            )
            response_content = completion.choices[0].message.content
            return json.loads(response_content)
        except Exception as e:
            logger.error(f"生成标签时出错: {e}")
            return []

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
                    logger.error(f"处理元数据时出错: {e}")
                    logger.error(f"问题数据: {data}")
                    continue

            escaped_title = sanitize_filename(title + ".md")
            original_file_path = f"summary/{escaped_title}"
            summary_file_path = f"../source/_posts/{escaped_title}"
            
            if escaped_title in current_post_title:
                logger.info(f"{summary_file_path} 已经发布")
                continue
            if not os.path.exists(original_file_path):
                logger.warning(f"{summary_file_path} 不存在")
                continue
            
            with open(original_file_path, 'r') as summary_file:
                content = summary_file.read()

            tags = await generate_tags(content, semaphore)
            rendered_template = render_template(title, upload_date, updated_date, tags)
            need_insert_post.append((original_file_path, summary_file_path, rendered_template))
            logger.info(f"需要插入到 {summary_file_path}")

    for post in need_insert_post:
        with open(post[0], 'r') as summary_file:
            content = summary_file.read()
        with open(post[1], 'w') as summary_file:
            summary_file.seek(0, 0)
            summary_file.write(post[2] + '\n\n' + content)
            logger.info(f"成功插入到 {post[1]}")
    
    logger.info(f"处理了 {len(need_insert_post)} 个文件")