import asyncio
import argparse
import os
import logging
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
    load_metadata_to_dict,
    generate_article,
    html_to_markdown,
)
from libylt2summary import claude_workflow

# API keys are loaded lazily — only required for legacy (non-Claude) code paths
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
KIMI_API_KEY = os.getenv("KIMI_API_KEY")

model = "moonshot-v1-32k"
base_url = "https://api.moonshot.cn/v1"


def _configure_logging(verbose: int) -> None:
    """Configure root logging level from CLI verbosity."""
    if verbose >= 2:
        level = logging.DEBUG
    elif verbose == 1:
        level = logging.INFO
    else:
        level = logging.WARNING

    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def _require_api_keys():
    """Validate that legacy API keys are set before using legacy code paths."""
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    if not KIMI_API_KEY:
        raise ValueError("KIMI_API_KEY environment variable is not set")

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
    # Claude Code based processing options
    parser.add_argument('--claude-summarize', action='store_true',
                        help='Summarize using Claude Code CLI (instead of direct API)')
    parser.add_argument('--claude-reflect', action='store_true',
                        help='Reflect using Claude Code CLI (instead of direct API)')
    parser.add_argument('--claude-classify', action='store_true',
                        help='Classify using Claude Code CLI (instead of direct API)')
    parser.add_argument('--claude-process', action='store_true',
                        help='One-step: subtitle → hexo post via Claude (replaces --claude-summarize + --claude-reflect)')
    parser.add_argument('--claude-quarterly', action='store_true',
                        help='Generate missing quarterly summary posts via Claude')
    parser.add_argument('--quarters', type=str, default=None,
                        help='Comma-separated quarters to generate, e.g. 2025Q1,2025Q2 (default: all missing)')
    parser.add_argument('--batch-size', type=int, default=10,
                        help='Batch size for Claude Code processing (default: 10)')
    parser.add_argument('--max-workers', type=int, default=1,
                        help='并发 CLI 进程数 (default: 1 串行)')
    parser.add_argument('--timeout', type=int, default=300,
                        help='Timeout per batch in seconds (default: 300)')
    parser.add_argument('--backend', type=str, default='claude',
                        choices=['claude', 'kiro'],
                        help='AI CLI backend: claude (default) or kiro')
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='Increase logging verbosity (-v: INFO, -vv: DEBUG)')
    args = parser.parse_args()
    _configure_logging(args.verbose)

    # 设置 AI CLI 后端
    claude_workflow.set_backend(args.backend)

    # 检查是否有任何实际业务动作被指定（verbose/batch/timeout等不算动作）
    has_action = any((
        args.fetch,
        args.fetch_diff,
        args.summarize,
        args.show_summarize_diff,
        args.translate,
        args.classify_content,
        args.classify_quarter,
        args.add_metadata,
        args.reflect,
        args.quarterly_summary,
        args.collect_prompt,
        args.split_reference,
        args.fetch_github_prs,
        args.generate_article,
        args.convert_pdfs,
        args.html_to_md,
        args.claude_summarize,
        args.claude_reflect,
        args.claude_classify,
        args.claude_process,
        args.claude_quarterly,
    ))
    if not has_action:
        parser.print_help()
        return

    if args.fetch:
        channel_url = 'https://www.youtube.com/@Cephstorage'
        videos = get_channel_videos(channel_url, "20220101", "today")
    if args.fetch_diff:
        main_fectch_subtitle()
    if args.show_summarize_diff:
        show_summary_diff()
    # Legacy paths that require API keys
    legacy_api_actions = (
        args.summarize or args.translate or args.classify_content or
        args.add_metadata or args.reflect or args.quarterly_summary or
        args.generate_article
    )
    if legacy_api_actions:
        _require_api_keys()

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
        from libylt2summary import github_fetch_prs
        await github_fetch_prs()
    if args.generate_article:
        reference_dir = Path("reference_md")  # 使用转换后的 Markdown 文件
        reference_files = [str(reference_dir / file) for file in os.listdir(reference_dir) if file.endswith('.md')]
        await generate_article(args.generate_article, KIMI_API_KEY, base_url, model, reference_files)
    if args.convert_pdfs:
        from libylt2summary.pdf_to_markdown import convert_pdfs_in_directory

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

    # Claude Code based processing
    if args.claude_summarize:
        await claude_workflow.main_claude_summarize(
            batch_size=args.batch_size,
            timeout=args.timeout,
            max_workers=args.max_workers
        )
    if args.claude_reflect:
        await claude_workflow.main_claude_reflect(
            batch_size=args.batch_size,
            timeout=args.timeout,
            max_workers=args.max_workers
        )
    if args.claude_classify:
        await claude_workflow.main_claude_classify(
            batch_size=args.batch_size,
            timeout=args.timeout,
            max_workers=args.max_workers
        )
    if args.claude_process:
        await claude_workflow.main_claude_process(
            timeout=args.timeout,
            max_workers=args.max_workers
        )
    if args.claude_quarterly:
        quarters = [q.strip() for q in args.quarters.split(',')] if args.quarters else None
        await claude_workflow.main_claude_quarterly(
            quarters=quarters,
            timeout=args.timeout,
        )

    await process_retry_queue()

if __name__ == "__main__":
    asyncio.run(main())