#!/usr/bin/env python3
"""Migrate Hexo posts to VitePress structure."""
import os
import shutil
import re
from datetime import datetime

PROJECT = '/Users/sean10/Self_Code/VideoSummary'
HEXO_POSTS = os.path.join(PROJECT, 'source', '_posts')
QUARTER_POSTS = os.path.join(PROJECT, 'posts_quarter')
DOCS = os.path.join(PROJECT, 'vitepress-site', 'docs')

# Output dirs
POSTS_BY_YEAR = os.path.join(DOCS, 'posts')
QUARTERLY_DIR = os.path.join(DOCS, 'quarterly')

# Stats
stats = {'video': 0, 'quarterly': 0, 'translation': 0, 'summary': 0, 'other': 0, 'errors': 0}
year_counts = {}

def extract_year_from_name(name):
    """Extract year from filename like 2014Q2_xxx or 2015-JAN-22_xxx."""
    m = re.match(r'(\d{4})', name)
    if m:
        return int(m.group(1))
    return None

def parse_frontmatter(content):
    """Simple frontmatter parser."""
    if not content.startswith('---'):
        return {}, content

    end = content.find('---', 3)
    if end == -1:
        return {}, content

    fm_str = content[3:end].strip()
    body = content[end+3:].lstrip('\n')
    fm = {}

    current_key = None
    current_list = None

    for line in fm_str.split('\n'):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue

        # List item
        if stripped.startswith('- '):
            if current_key and current_list is not None:
                current_list.append(stripped[2:].strip().strip('"').strip("'"))
            continue

        # Save previous list
        if current_key and current_list is not None:
            fm[current_key] = current_list
            current_list = None
            current_key = None

        # Key-value
        if ':' in stripped:
            parts = stripped.split(':', 1)
            key = parts[0].strip()
            val = parts[1].strip()

            if not val:
                # Next lines might be a list
                current_key = key
                current_list = []
            else:
                val = val.strip('"').strip("'")
                fm[key] = val
                current_key = key
                current_list = None

    if current_key and current_list is not None:
        fm[current_key] = current_list

    return fm, body

def clean_title(title):
    """Remove problematic characters from title for display."""
    if not title:
        return 'Untitled'
    # Remove outer quotes
    title = title.strip().strip('"').strip("'").strip('"').strip('"')
    return title

def migrate_file(src, dest_dir, filename, section='video'):
    """Migrate a single file."""
    try:
        with open(src, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        try:
            with open(src, 'r', encoding='gbk') as f:
                content = f.read()
        except Exception:
            stats['errors'] += 1
            return

    fm, body = parse_frontmatter(content)

    # Determine year
    year = None
    if 'date' in fm:
        try:
            year = datetime.strptime(str(fm['date'])[:10], '%Y-%m-%d').year
        except Exception:
            pass
    if not year:
        year = extract_year_from_name(filename)
    if not year:
        try:
            mtime = os.path.getmtime(src)
            year = datetime.fromtimestamp(mtime).year
        except Exception:
            year = 2024

    # Ensure title
    title = clean_title(fm.get('title', filename.replace('.md', '').replace('_', ' ')))

    # Build clean frontmatter
    tags = fm.get('tags', [])
    if isinstance(tags, str):
        tags = [tags]
    categories = fm.get('categories', [])
    if isinstance(categories, str):
        categories = [categories]

    date_str = fm.get('date', '')
    updated_str = fm.get('updated', '')

    # Build new frontmatter
    fm_lines = ['---']
    fm_lines.append(f'title: "{title}"')
    if date_str:
        fm_lines.append(f'date: {date_str}')
    if updated_str:
        fm_lines.append(f'updated: {updated_str}')
    if tags:
        fm_lines.append('tags:')
        for t in tags:
            fm_lines.append(f'  - "{t}"')
    if categories:
        fm_lines.append('categories:')
        for c in categories:
            fm_lines.append(f'  - "{c}"')
    # Add outline for VitePress TOC
    fm_lines.append('outline: deep')
    fm_lines.append('---')

    new_content = '\n'.join(fm_lines) + '\n' + body

    # Write
    year_dir = os.path.join(dest_dir, str(year))
    os.makedirs(year_dir, exist_ok=True)

    dest_path = os.path.join(year_dir, filename)
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    year_counts[year] = year_counts.get(year, 0) + 1
    return year

# === Main migration ===
print('Starting migration...\n')

# 1. Migrate main posts
print(f'Scanning {HEXO_POSTS}...')
for filename in sorted(os.listdir(HEXO_POSTS)):
    if not filename.endswith('.md') or filename.startswith('.'):
        continue
    src = os.path.join(HEXO_POSTS, filename)
    year = migrate_file(src, POSTS_BY_YEAR, filename, 'video')

    # Classify for stats
    try:
        with open(src, 'r', encoding='utf-8') as f:
            head = f.read(500)
    except Exception:
        head = ''

    if '季度总结' in head or '阶段总结' in head:
        stats['summary'] += 1
    elif '翻译' in head:
        stats['translation'] += 1
    else:
        stats['video'] += 1

# 2. Migrate quarterly posts
print(f'Scanning {QUARTER_POSTS}...')
os.makedirs(QUARTERLY_DIR, exist_ok=True)
for filename in sorted(os.listdir(QUARTER_POSTS)):
    if not filename.endswith('.md') or filename.startswith('.'):
        continue
    src = os.path.join(QUARTER_POSTS, filename)
    try:
        with open(src, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        try:
            with open(src, 'r', encoding='gbk') as f:
                content = f.read()
        except Exception:
            stats['errors'] += 1
            continue

    fm, body = parse_frontmatter(content)
    title = clean_title(fm.get('title', filename.replace('.md', '').replace('_', ' ')))

    # Extract year from filename like 2014Q4_Ceph社区季度总结.md
    m = re.match(r'(\d{4})Q(\d)', filename)
    if m:
        year_label = f'{m.group(1)} Q{m.group(2)}'
    else:
        year_label = filename.replace('.md', '')

    tags = fm.get('tags', [])
    if isinstance(tags, str):
        tags = [tags]
    date_str = fm.get('date', '')

    fm_lines = ['---']
    fm_lines.append(f'title: "{title}"')
    if date_str:
        fm_lines.append(f'date: {date_str}')
    if tags:
        fm_lines.append('tags:')
        for t in tags:
            fm_lines.append(f'  - "{t}"')
    fm_lines.append('outline: deep')
    fm_lines.append('---')

    new_content = '\n'.join(fm_lines) + '\n' + body
    dest = os.path.join(QUARTERLY_DIR, filename)
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(new_content)
    stats['quarterly'] += 1

# 3. Print summary
print(f'\n=== Migration Complete ===')
print(f'  Video summaries: {stats["video"]}')
print(f'  Quarterly reports: {stats["quarterly"]}')
print(f'  Translations: {stats["translation"]}')
print(f'  Other summaries: {stats["summary"]}')
print(f'  Errors: {stats["errors"]}')
print(f'  Total: {sum(stats.values())}')
print(f'\nBy year:')
for y in sorted(year_counts):
    print(f'  {y}: {year_counts[y]} posts')
