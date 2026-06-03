#!/usr/bin/env python3
"""Generate tag index pages for VitePress from article frontmatter.

Scans all posts and quarterly articles, extracts tags from frontmatter,
and generates:
  - docs/tags/index.md  — overview page with all tags
  - docs/tags/TAG.md    — per-tag article listing
"""
import os
import re
import unicodedata
from collections import defaultdict

DOCS = '/Users/sean10/Self_Code/VideoSummary/vitepress-site/docs'
POSTS_DIR = os.path.join(DOCS, 'posts')
QUARTERLY_DIR = os.path.join(DOCS, 'quarterly')
TAGS_DIR = os.path.join(DOCS, 'tags')


def parse_frontmatter(content):
    """Extract frontmatter from markdown content."""
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return {}
    fm_str = fm_match.group(1)
    result = {}
    current_key = None
    current_list = None

    for line in fm_str.split('\n'):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        if stripped.startswith('- '):
            if current_key and current_list is not None:
                val = stripped[2:].strip().strip('"').strip("'")
                current_list.append(val)
            continue
        if current_key and current_list is not None:
            result[current_key] = current_list
            current_list = None
            current_key = None
        if ':' in stripped:
            key, val = stripped.split(':', 1)
            key = key.strip()
            val = val.strip()
            if not val:
                current_key = key
                current_list = []
            else:
                result[key] = val.strip('"').strip("'")
                current_key = key
                current_list = None
    if current_key and current_list is not None:
        result[current_key] = current_list
    return result


def tag_to_slug(tag):
    """Convert tag to URL-safe slug."""
    # Replace spaces and special chars
    slug = tag.lower().strip()
    slug = re.sub(r'[^\w\u4e00-\u9fff-]', '-', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug or 'untagged'


def scan_articles():
    """Scan all articles and return tag -> [article_info] mapping."""
    tag_articles = defaultdict(list)

    # Scan posts by year
    if os.path.isdir(POSTS_DIR):
        for year_dir in sorted(os.listdir(POSTS_DIR)):
            year_path = os.path.join(POSTS_DIR, year_dir)
            if not os.path.isdir(year_path):
                continue
            for fname in sorted(os.listdir(year_path)):
                if not fname.endswith('.md') or fname == 'index.md':
                    continue
                fpath = os.path.join(year_path, fname)
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        content = f.read()
                except Exception:
                    continue

                fm = parse_frontmatter(content)
                title = fm.get('title', fname.replace('.md', '').replace('_', ' '))
                date = fm.get('date', '')
                tags = fm.get('tags', [])
                if isinstance(tags, str):
                    tags = [tags]

                link = f'/posts/{year_dir}/{fname[:-3]}'

                for tag in tags:
                    tag_articles[tag].append({
                        'title': title,
                        'date': date,
                        'link': link,
                        'year': year_dir,
                    })

    # Scan quarterly
    if os.path.isdir(QUARTERLY_DIR):
        for fname in sorted(os.listdir(QUARTERLY_DIR)):
            if not fname.endswith('.md') or fname == 'index.md':
                continue
            fpath = os.path.join(QUARTERLY_DIR, fname)
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue

            fm = parse_frontmatter(content)
            title = fm.get('title', fname.replace('.md', '').replace('_', ' '))
            date = fm.get('date', '')
            tags = fm.get('tags', [])
            if isinstance(tags, str):
                tags = [tags]

            link = f'/quarterly/{fname[:-3]}'

            for tag in tags:
                tag_articles[tag].append({
                    'title': title,
                    'date': date,
                    'link': link,
                    'year': '季度报告',
                })

    return tag_articles


def generate_tag_index(tag_articles):
    """Generate the main tags/index.md overview page."""
    lines = [
        '---',
        'title: "按标签浏览"',
        'layout: page',
        'outline: deep',
        '---',
        '',
        '# 按标签浏览',
        '',
        f'共 **{len(tag_articles)}** 个标签，涵盖 Ceph 各个技术方向。',
        '',
    ]

    # Sort tags by article count (descending)
    sorted_tags = sorted(tag_articles.items(), key=lambda x: -len(x[1]))

    # Group into tiers for better readability
    hot_tags = [(t, arts) for t, arts in sorted_tags if len(arts) >= 50]
    medium_tags = [(t, arts) for t, arts in sorted_tags if 10 <= len(arts) < 50]
    niche_tags = [(t, arts) for t, arts in sorted_tags if len(arts) < 10]

    if hot_tags:
        lines.append('## 热门标签')
        lines.append('')
        for tag, arts in hot_tags:
            slug = tag_to_slug(tag)
            lines.append(f'- [{tag}](./{slug}.md) — {len(arts)} 篇')
        lines.append('')

    if medium_tags:
        lines.append('## 专题标签')
        lines.append('')
        for tag, arts in medium_tags:
            slug = tag_to_slug(tag)
            lines.append(f'- [{tag}](./{slug}.md) — {len(arts)} 篇')
        lines.append('')

    if niche_tags:
        lines.append('## 其他标签')
        lines.append('')
        for tag, arts in niche_tags:
            slug = tag_to_slug(tag)
            lines.append(f'- [{tag}](./{slug}.md) — {len(arts)} 篇')
        lines.append('')

    return '\n'.join(lines)


def generate_tag_page(tag, articles):
    """Generate a per-tag article listing page."""
    slug = tag_to_slug(tag)

    # Sort articles by date descending
    sorted_arts = sorted(articles, key=lambda a: a.get('date', ''), reverse=True)

    lines = [
        '---',
        f'title: "{tag}"',
        'layout: page',
        'outline: deep',
        '---',
        '',
        f'# {tag}',
        '',
        f'共 **{len(sorted_arts)}** 篇文章',
        '',
        f'[← 返回标签列表](./index.md)',
        '',
    ]

    # Group by year
    by_year = defaultdict(list)
    for art in sorted_arts:
        by_year[art['year']].append(art)

    for year in sorted(by_year.keys(), reverse=True):
        lines.append(f'## {year}')
        lines.append('')
        for art in by_year[year]:
            date_str = f' `{art["date"]}`' if art.get('date') else ''
            lines.append(f'- [{art["title"]}]({art["link"]}){date_str}')
        lines.append('')

    lines.append('[← 返回标签列表](./index.md)')
    lines.append('')

    return '\n'.join(lines)


# === Main ===
print('Scanning articles for tags...')
tag_articles = scan_articles()
print(f'Found {len(tag_articles)} unique tags across {sum(len(v) for v in tag_articles.values())} tag-article pairs')

# Create tags directory
os.makedirs(TAGS_DIR, exist_ok=True)

# Clean old tag pages (keep only ones we generate)
for f in os.listdir(TAGS_DIR):
    if f.endswith('.md'):
        os.remove(os.path.join(TAGS_DIR, f))

# Generate index page
print('Generating tags/index.md...')
index_content = generate_tag_index(tag_articles)
with open(os.path.join(TAGS_DIR, 'index.md'), 'w', encoding='utf-8') as f:
    f.write(index_content)

# Generate per-tag pages
for tag, articles in tag_articles.items():
    slug = tag_to_slug(tag)
    content = generate_tag_page(tag, articles)
    with open(os.path.join(TAGS_DIR, f'{slug}.md'), 'w', encoding='utf-8') as f:
        f.write(content)

print(f'Generated {len(tag_articles) + 1} tag pages in {TAGS_DIR}')
