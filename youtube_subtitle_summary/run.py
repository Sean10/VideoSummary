import asyncio
import argparse
from libylt2summary import (
    get_channel_videos,
    main_fectch_subtitle,
    main_summary_diff,
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
    load_metadata_to_dict
)

async def main():
    global metadata_dict
    metadata_dict = load_metadata_to_dict()

    parser = argparse.ArgumentParser(description="YouTube Subtitle Summary Tool")
    parser.add_argument('--fetch', action='store_true', help='Fetch videos from channel')
    parser.add_argument('--fetch-diff', action='store_true', help='Fetch videos from channel')
    parser.add_argument('--summarize', action='store_true', help='Summarize subtitles')
    parser.add_argument('--summarize-diff', action='store_true', help='Summarize subtitles')
    parser.add_argument('--translate', type=str, help='Translate a specific subtitle file')
    parser.add_argument('--classify-content', action='store_true', help='Classify posts by content')
    parser.add_argument('--classify-quarter', action='store_true', help='Classify posts by quarter')
    parser.add_argument('--add-metadata', action='store_true', help='Add Hexo metadata to summary files')
    parser.add_argument('--reflect', action='store_true', help='Reflect on and improve existing summaries')
    parser.add_argument('--quarterly-summary', action='store_true', help='Generate quarterly summary reports')
    parser.add_argument('--collect-prompt', action='store_true', help='Collect prompt information from specified URLs')
    parser.add_argument('--split-reference', action='store_true', help='Split reference files into sections')
    parser.add_argument('--fetch-github-prs', action='store_true', help='Fetch GitHub PR contents from reference files')
    args = parser.parse_args()

    if args.fetch:
        channel_url = 'https://www.youtube.com/@Cephstorage'
        videos = get_channel_videos(channel_url, "20220101", "today")
    if args.fetch_diff:
        await main_fectch_subtitle()
    if args.summarize_diff:
        main_summary_diff()
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

    await process_retry_queue()

if __name__ == "__main__":
    asyncio.run(main())