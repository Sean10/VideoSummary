import os
from pathlib import Path
from gptpdf import parse_pdf

model = "qwen-vl-max"
base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"

def convert_pdf_to_markdown(pdf_path, output_dir):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    content, image_paths = parse_pdf(pdf_path, api_key=api_key, output_dir=str(output_dir), base_url=base_url, model=model)
    
    # 保存 Markdown 内容
    output_file = output_dir / f"{Path(pdf_path).stem}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"转换完成：{output_file}")
    print(f"生成的图片文件：{image_paths}")

def convert_pdfs_in_directory(input_dir, output_dir):
    input_dir = Path(input_dir)
    for pdf_file in input_dir.glob('*.pdf'):
        print(f"正在转换：{pdf_file}")
        convert_pdf_to_markdown(str(pdf_file), output_dir)

if __name__ == "__main__":
    input_directory = "reference_cloud"
    output_directory = "reference_md"
    convert_pdfs_in_directory(input_directory, output_directory)