import asyncio
import argparse
import os
from pathlib import Path
from libylt2summary import (
    get_channel_videos,
    main_fectch_subtitle,
    show_summary_diff,
    main_summary,
    summary,
    classify_posts_by_content,
    classify_posts_by_quarter,
    add_hexo_metadata,
    process_reflections,
    process_quarterly_summaries,
    collect_prompt_info,
    split_reference_files,
    process_retry_queue,
    github_fetch_prs,
    load_metadata_to_dict,
    generate_article,
    html_to_markdown,
)
from libylt2summary.pdf_to_markdown import convert_pdfs_in_directory

# 设置OpenAI API密钥和基础URL
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# 设置Kimi API密钥
KIMI_API_KEY = os.getenv("KIMI_API_KEY")
if not KIMI_API_KEY:
    raise ValueError("KIMI_API_KEY environment variable is not set")

model = "moonshot-v1-32k"
base_url = "https://api.moonshot.cn/v1"

async def main():
    global metadata_dict
    metadata_dict = load_metadata_to_dict()

    parser = argparse.ArgumentParser(description="YouTube Subtitle Summary Tool")
    parser.add_argument('--fetch', action='store_true', help='Fetch videos from channel')
    parser.add_argument('--fetch-diff', action='store_true', help='Fetch videos from channel')
    parser.add_argument('--summarize', action='store_true', help='Summarize subtitles')
    parser.add_argument('--show-summarize-diff', action='store_true', help='Summarize subtitles')
    parser.add_argument('--translate', type=str, help='Translate a specific subtitle file')
    parser.add_argument('--classify-content', action='store_true', help='Classify posts by content')
    parser.add_argument('--classify-quarter', action='store_true', help='Classify posts by quarter')
    parser.add_argument('--add-metadata', action='store_true', help='Add Hexo metadata to summary files')
    parser.add_argument('--reflect', action='store_true', help='Reflect on and improve existing summaries')
    parser.add_argument('--quarterly-summary', action='store_true', help='Generate quarterly summary reports')
    parser.add_argument('--collect-prompt', action='store_true', help='Collect prompt information from specified URLs')
    parser.add_argument('--split-reference', action='store_true', help='Split reference files into sections')
    parser.add_argument('--fetch-github-prs', action='store_true', help='Fetch GitHub PR contents from reference files')
    parser.add_argument('--generate-article', type=str, help='Generate an article based on the given topic')
    parser.add_argument('--convert-pdfs', action='store_true', help='Convert PDFs to Markdown')
    parser.add_argument('--pdf-input-dir', type=str, default='pdf_input', help='Input directory for PDF files')
    parser.add_argument('--html-to-md', nargs=2, metavar=('INPUT', 'OUTPUT'),
                        help='Convert HTML file to Markdown. Specify input and output file paths.')
    args = parser.parse_args()

    # 检查是否有任何参数被指定
    if not any(vars(args).values()):
        parser.print_help()
        return

    if args.fetch:
        channel_url = 'https://www.youtube.com/@Cephstorage'
        videos = get_channel_videos(channel_url, "20220101", "today")
    if args.fetch_diff:
        main_fectch_subtitle()
    if args.show_summarize_diff:
        show_summary_diff()
    if args.summarize:
        await main_summary()
    if args.translate:
        await summary(args.translate, mode="translation")
    if args.classify_content:
        await classify_posts_by_content()
    if args.classify_quarter:
        classify_posts_by_quarter()
    if args.add_metadata:
        await add_hexo_metadata()
    if args.reflect:
        await process_reflections()
    if args.quarterly_summary:
        await process_quarterly_summaries()
    if args.collect_prompt:
        urls = [
            'https://pad.ceph.com/p/ceph-user-dev-monthly-minutes/export/txt',
            'https://pad.ceph.com/p/performance_weekly/export/txt',
            'https://pad.ceph.com/p/performance_weekly_2014/export/txt',
            'https://pad.ceph.com/p/performance_weekly_2015/export/txt',
            'https://pad.ceph.com/p/performance_weekly_2016/export/txt',
            'https://pad.ceph.com/p/performance_weekly_2017/export/txt',
            'https://pad.ceph.com/p/performance_weekly_2018/export/txt',
            'https://pad.ceph.com/p/performance_weekly_2019/export/txt',
            'https://pad.ceph.com/p/performance_weekly_2020/export/txt',
            'https://pad.ceph.com/p/performance_weekly_2022/export/txt',
        ]
        prompt_info = await collect_prompt_info(urls)
        print("Collected prompt information:")
        print(prompt_info)
        print("Content has been saved to the 'reference' directory.")
    if args.split_reference:
        split_reference_files()
    if args.fetch_github_prs:
        await github_fetch_prs()
    if args.generate_article:
        reference_dir = Path("reference_md")  # 使用转换后的 Markdown 文件
        reference_files = [str(reference_dir / file) for file in os.listdir(reference_dir) if file.endswith('.md')]
        await generate_article(args.generate_article, KIMI_API_KEY, base_url, model, reference_files)
    if args.convert_pdfs:
        input_directory = args.pdf_input_dir
        output_directory = "reference_md"
        convert_pdfs_in_directory(input_directory, output_directory)
    if args.html_to_md:
        input_file, output_file = args.html_to_md
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            markdown_content = html_to_markdown(html_content)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            print(f"HTML文件已成功转换为Markdown。输出文件: {output_file}")
        except Exception as e:
            print(f"转换过程中发生错误: {str(e)}")

    await process_retry_queue()

if __name__ == "__main__":
    asyncio.run(main())