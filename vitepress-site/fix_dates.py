#!/usr/bin/env python3
"""Fix article dates by extracting real dates from titles/filenames."""
import os
import re

posts_dir = '/Users/sean10/Self_Code/VideoSummary/vitepress-site/docs/posts'
fixed = 0

for year_dir in sorted(os.listdir(posts_dir)):
    year_path = os.path.join(posts_dir, year_dir)
    if not os.path.isdir(year_path):
        continue
    for fname in os.listdir(year_path):
        if not fname.endswith('.md') or fname == 'index.md':
            continue
        fpath = os.path.join(year_path, fname)
        with open(fpath, 'r') as f:
            content = f.read()

        # Extract frontmatter
        fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            continue
        fm = fm_match.group(1)

        date_match = re.search(r'^date:\s*(.+?)\s*$', fm, re.MULTILINE)
        if not date_match:
            continue
        current_date = date_match.group(1).strip()

        # Try to find a real date in the title
        real_date = None
        title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
        if title_match:
            title = title_match.group(1)
            dm = re.search(r'(\d{4}-\d{2}-\d{2})', title)
            if dm:
                real_date = dm.group(1)

        # Fallback: check filename
        if not real_date:
            dm = re.search(r'(\d{4}-\d{2}-\d{2})', fname)
            if dm:
                real_date = dm.group(1)

        # Fix if different
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

print(f'Fixed dates for {fixed} articles')
