import os
import sys
from pyzotero import zotero
from pathlib import Path

# Zotero API 设置
LIBRARY_ID = 'your_library_id'
LIBRARY_TYPE = 'user'  # 或 'group'
API_KEY = 'your_api_key'

# 初始化 Zotero 客户端
zot = zotero.Zotero(LIBRARY_ID, LIBRARY_TYPE, API_KEY)

def create_zotero_item(file_path):
    file_name = os.path.basename(file_path)
    file_ext = os.path.splitext(file_name)[1].lower()

    if file_ext == '.md':
        item_type = 'note'
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        template = zot.item_template(item_type)
        template['note'] = content
    elif file_ext == '.pdf':
        item_type = 'document'
        template = zot.item_template(item_type)
        template['title'] = os.path.splitext(file_name)[0]
    else:
        print(f"不支持的文件类型: {file_ext}")
        return None

    return template

def upload_file_to_zotero(file_path):
    item = create_zotero_item(file_path)
    if item is None:
        return

    # 创建 Zotero 条目
    resp = zot.create_items([item])
    
    if resp['success']:
        key = resp['successful']['0']['key']
        print(f"成功创建条目: {key}")

        # 上传附件
        if os.path.splitext(file_path)[1].lower() == '.pdf':
            zot.attachment_simple([file_path], parentid=key)
            print(f"成功上传附件: {file_path}")
    else:
        print(f"创建条目失败: {resp}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.md', '.pdf')):
                file_path = os.path.join(root, file)
                print(f"处理文件: {file_path}")
                upload_file_to_zotero(file_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("请提供要处理的目录路径")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"无效的目录路径: {directory}")
        sys.exit(1)

    process_directory(directory)