import os
import re

def clean_yaml_frontmatter(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 提取YAML front matter
            yaml_match = re.search(r'---\n([\s\S]*?)(---)?\n\n', content, re.DOTALL)
            if yaml_match:
                yaml_content = yaml_match.group(1)
                rest_content = content[yaml_match.end():]

                # 清理YAML内容
                cleaned_yaml = clean_yaml_content(yaml_content)
                
                # 重建文件内容
                new_content = f"---\n{cleaned_yaml}\n---\n\n{rest_content}"

                # 写回文件
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                
                print(f"Processed: {filename}")
            else:
                print(f"No YAML front matter found in {filename}")
        # break

def clean_yaml_content(yaml_content):
    lines = yaml_content.split('\n')
    cleaned_lines = []
    current_key = None
    current_value = []

    for line in lines:
        stripped_line = line.strip()
        if re.match(r'^[\w-]+:', line) and not stripped_line.startswith('-'):
            if current_key:
                cleaned_lines.append(process_key_value(current_key, current_value))
                current_value = []
            current_key, value = line.split(':', 1)
            current_key = current_key.strip()
            current_value = [value.strip()]
        elif current_key:
            current_value.append(stripped_line)
        else:
            cleaned_lines.append(line)

    if current_key:
        cleaned_lines.append(process_key_value(current_key, current_value))

    return '\n'.join(cleaned_lines)

def process_key_value(key, value):
    if key in ['categories', 'tags']:
        # 确保categories和tags是列表格式
        value = [v.strip() for v in ' '.join(value).split('-') if v.strip()]
        return f"{key}:\n" + '\n'.join(f"- {v}" for v in value)
    elif key == 'title':
        # 处理标题中的特殊字符
        title = ' '.join(value).strip().replace('"', ' ')
        return f'{key}: "{title}"'
    else:
        # 其他键值对
        return f"{key}: {' '.join(value).strip()}"

if __name__ == "__main__":
    temp_posts_dir = "temp_posts"
    clean_yaml_frontmatter(temp_posts_dir)