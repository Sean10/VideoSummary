#!/usr/bin/env python3
"""Fix article dates using real YouTube upload_date from videos_meta.jsonl."""
import os
import json
import re
from datetime import datetime

META_FILE = '/Users/sean10/Self_Code/VideoSummary/youtube_subtitle_summary/videos_meta.jsonl'
DOCS_DIR = '/Users/sean10/Self_Code/VideoSummary/vitepress-site/docs/posts'

# 1. Build title -> upload_date mapping
title_to_date = {}
with open(META_FILE) as f:
    for line in f:
        data = json.loads(line)
        title = data.get('title', '').strip()
        upload = data.get('upload_date', '')
        ts = data.get('timestamp')
        if not upload and ts:
            upload = datetime.fromtimestamp(ts).strftime('%Y%m%d')
        if title and upload and len(upload) == 8:
            formatted = f'{upload[:4]}-{upload[4:6]}-{upload[6:8]}'
            title_to_date[title] = formatted

print(f'Loaded {len(title_to_date)} title->date mappings')

# 2. Walk all posts and fix dates
fixed = 0
total = 0

for year_dir in sorted(os.listdir(DOCS_DIR)):
    year_path = os.path.join(DOCS_DIR, year_dir)
    if not os.path.isdir(year_path):
        continue
    for fname in os.listdir(year_path):
        if not fname.endswith('.md') or fname == 'index.md':
            continue
        total += 1
        fpath = os.path.join(year_path, fname)
        with open(fpath, 'r') as f:
            content = f.read()

        fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            continue
        fm = fm_match.group(1)

        # Get current date
        date_match = re.search(r'^date:\s*(.+?)\s*$', fm, re.MULTILINE)
        if not date_match:
            continue
        current_date = date_match.group(1).strip()

        # Get title from frontmatter
        title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
        if not title_match:
            continue
        title = title_match.group(1).strip()

        # Try to match against YouTube metadata
        real_date = title_to_date.get(title)

        if real_date and real_date != current_date:
            new_fm = re.sub(
                r'^date:\s*.+$',
                f'date: {real_date}',
                fm, count=1, flags=re.MULTILINE
            )
            new_content = content[:fm_match.start(1)] + new_fm + content[fm_match.end(1):]
            with open(fpath, 'w') as f:
                f.write(new_content)
            fixed += 1

print(f'Checked {total} articles')
print(f'Fixed dates for {fixed} articles')
