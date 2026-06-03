#!/usr/bin/env python3
"""
Hybrid date strategy:
1. If article title contains a date (meeting date), use it — most meaningful for meeting summaries
2. Otherwise, use YouTube upload_date
3. Fallback: keep existing frontmatter date
"""
import os
import json
import re

META_FILE = '/Users/sean10/Self_Code/VideoSummary/youtube_subtitle_summary/videos_meta.jsonl'
DOCS_DIR = '/Users/sean10/Self_Code/VideoSummary/vitepress-site/docs/posts'

# Load YouTube metadata: title -> upload_date
yt_dates = {}
with open(META_FILE) as f:
    for line in f:
        data = json.loads(line)
        title = data.get('title', '').strip()
        upload = data.get('upload_date', '')
        if title and upload and len(upload) == 8:
            yt_dates[title] = f'{upload[:4]}-{upload[4:6]}-{upload[6:8]}'

print(f'Loaded {len(yt_dates)} YouTube dates')

# Date pattern in titles: YYYY-MM-DD
DATE_RE = re.compile(r'(\d{4}-\d{2}-\d{2})')

fixed = 0
by_title = 0
by_youtube = 0

for year_dir in sorted(os.listdir(DOCS_DIR)):
    year_path = os.path.join(DOCS_DIR, year_dir)
    if not os.path.isdir(year_path):
        continue
    for fname in os.listdir(year_path):
        if not fname.endswith('.md') or fname == 'index.md':
            continue
        fpath = os.path.join(year_path, fname)
        with open(fpath, 'r') as f:
            content = f.read()

        fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            continue
        fm = fm_match.group(1)

        date_m = re.search(r'^date:\s*(.+?)\s*$', fm, re.MULTILINE)
        title_m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
        if not date_m or not title_m:
            continue

        current_date = date_m.group(1).strip()
        title = title_m.group(1).strip()

        # Strategy 1: date in title (meeting date)
        new_date = None
        title_date_m = DATE_RE.search(title)
        if title_date_m:
            new_date = title_date_m.group(1)
            source = 'title'

        # Strategy 2: YouTube upload date (if different from batch date)
        if not new_date and title in yt_dates:
            yt_date = yt_dates[title]
            if yt_date != current_date:
                new_date = yt_date
                source = 'youtube'

        # Strategy 3: date in filename as last resort
        if not new_date:
            fn_date_m = DATE_RE.search(fname)
            if fn_date_m:
                fn_date = fn_date_m.group(1)
                if fn_date != current_date:
                    new_date = fn_date
                    source = 'filename'

        if new_date and new_date != current_date:
            new_fm = re.sub(r'^date:\s*.+$', f'date: {new_date}', fm, count=1, flags=re.MULTILINE)
            new_content = content[:fm_match.start(1)] + new_fm + content[fm_match.end(1):]
            with open(fpath, 'w') as f:
                f.write(new_content)
            fixed += 1
            if source == 'title':
                by_title += 1
            elif source == 'youtube':
                by_youtube += 1

print(f'Fixed {fixed} articles: {by_title} from title, {by_youtube} from YouTube')
