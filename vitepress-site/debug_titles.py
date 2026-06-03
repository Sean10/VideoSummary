#!/usr/bin/env python3
"""Debug title matching between frontmatter and YouTube metadata."""
import json
import re

META_FILE = '/Users/sean10/Self_Code/VideoSummary/youtube_subtitle_summary/videos_meta.jsonl'

# Load YouTube titles
yt_titles = {}
with open(META_FILE) as f:
    for line in f:
        data = json.loads(line)
        title = data.get('title', '').strip()
        upload = data.get('upload_date', '')
        if title and upload:
            yt_titles[title] = upload

# Search for RGW Refactoring in YouTube titles
rgw = {k: v for k, v in yt_titles.items() if 'RGW Refactoring' in k}
print('YouTube RGW Refactoring titles:')
for k, v in sorted(rgw.items()):
    print(f'  {v} | [{k}]')

# Check frontmatter titles for problem files
test_files = [
    'Ceph_RGW_Refactoring_Meeting_2026-03-04.md',
    'Ceph_RGW_Refactoring_Meeting_2026-02-25.md',
    'Ceph_RGW_Refactoring_Meeting_2026-04-01.md',
]
base = '/Users/sean10/Self_Code/VideoSummary/vitepress-site/docs/posts/2026/'

print('\nFrontmatter titles:')
for fname in test_files:
    try:
        with open(base + fname) as f:
            content = f.read()
        m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
        ft = m.group(1) if m else 'N/A'
        matched = ft in yt_titles
        print(f'  [{ft}] -> match={matched}')
    except FileNotFoundError:
        print(f'  {fname} not found')
