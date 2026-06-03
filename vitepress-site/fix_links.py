#!/usr/bin/env python3
"""Fix internal links in migrated VitePress posts.

Converts Hexo-style permalink URLs to VitePress file-based paths.
Old: (/VideoSummary/2020/01/11/some-title/)
New: (/posts/2020/some-title)
"""
import os
import re

DOCS = '/Users/sean10/Self_Code/VideoSummary/vitepress-site/docs'
POSTS_DIR = os.path.join(DOCS, 'posts')

# Build a lookup: slug -> (year, filename)
slug_map = {}
for year_dir in os.listdir(POSTS_DIR):
    year_path = os.path.join(POSTS_DIR, year_dir)
    if not os.path.isdir(year_path):
        continue
    for fname in os.listdir(year_path):
        if not fname.endswith('.md') or fname == 'index.md':
            continue
        slug = fname[:-3]  # Remove .md
        slug_map[slug] = year_dir

print(f'Built slug map with {len(slug_map)} entries')

# Pattern to match Hexo-style absolute links in markdown:
# [text](/VideoSummary/2023/10/04/Some_Title/)
# The link part: /VideoSummary/YYYY/MM/DD/SLUG/ or /VideoSummary/YYYY/MM/DD/SLUG
hexo_link_re = re.compile(
    r'\(/VideoSummary/(\d{4})/\d{2}/\d{2}/([^/\s\)]+?)/?(?=\))'
)

# Pattern to match relative links like [text](./Some_Title)
# within annual/quarterly summaries
relative_link_re = re.compile(
    r'\]\(\./([^/\s\)\.]+)\)'
)

fixed_count = 0
file_count = 0

def fix_file(filepath, year_hint=None):
    global fixed_count, file_count
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return

    original = content

    # Fix absolute Hexo links
    def fix_absolute(m):
        global fixed_count
        year_str, slug = m.group(1), m.group(2)
        if slug in slug_map:
            actual_year = slug_map[slug]
            fixed_count += 1
            return f'(/posts/{actual_year}/{slug})'
        # Slug not found, rewrite to year-based path anyway
        fixed_count += 1
        return f'(/posts/{year_str}/{slug})'

    content = hexo_link_re.sub(fix_absolute, content)

    # Fix relative links (within same year)
    def fix_relative(m):
        global fixed_count
        slug = m.group(1)
        if slug in slug_map:
            actual_year = slug_map[slug]
            fixed_count += 1
            return f'](/posts/{actual_year}/{slug})'
        return m.group(0)

    content = relative_link_re.sub(fix_relative, content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        file_count += 1

# Process all posts
for year_dir in sorted(os.listdir(POSTS_DIR)):
    year_path = os.path.join(POSTS_DIR, year_dir)
    if not os.path.isdir(year_path):
        continue
    for fname in os.listdir(year_path):
        if not fname.endswith('.md'):
            continue
        filepath = os.path.join(year_path, fname)
        fix_file(filepath, year_hint=int(year_dir))

# Process quarterly reports
quarterly_dir = os.path.join(DOCS, 'quarterly')
if os.path.isdir(quarterly_dir):
    for fname in os.listdir(quarterly_dir):
        if not fname.endswith('.md') or fname == 'index.md':
            continue
        filepath = os.path.join(quarterly_dir, fname)
        fix_file(filepath)

print(f'Fixed {fixed_count} links in {file_count} files')
