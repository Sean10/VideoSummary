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


import math


def generate_tag_index(tag_articles):
    """Generate the main tags/index.md overview page with tag cloud."""
    sorted_tags = sorted(tag_articles.items(), key=lambda x: -len(x[1]))
    counts = [len(arts) for _, arts in sorted_tags]
    min_count = min(counts) if counts else 1
    max_count = max(counts) if counts else 1

    # Font size range (px): small tags 14px, biggest 48px
    MIN_SIZE = 14
    MAX_SIZE = 48

    def calc_size(count):
        if max_count == min_count:
            return (MIN_SIZE + MAX_SIZE) / 2
        # Logarithmic scale for smoother distribution
        log_min = math.log(min_count)
        log_max = math.log(max_count)
        ratio = (math.log(count) - log_min) / (log_max - log_min)
        return round(MIN_SIZE + ratio * (MAX_SIZE - MIN_SIZE))

    # Color tiers based on popularity
    def calc_color(count):
        if count >= 200:
            return 'var(--indigo-dark)'      # Deep indigo
        elif count >= 100:
            return 'var(--indigo-primary)'    # Primary indigo
        elif count >= 50:
            return 'var(--vp-c-brand-2)'     # Medium
        elif count >= 20:
            return 'var(--vp-c-text-2)'      # Gray
        else:
            return 'var(--vp-c-text-3)'      # Light gray

    # Build tag cloud HTML
    cloud_items = []
    for tag, arts in sorted_tags:
        slug = tag_to_slug(tag)
        size = calc_size(len(arts))
        color = calc_color(len(arts))
        weight = '700' if len(arts) >= 100 else '500' if len(arts) >= 30 else '400'
        cloud_items.append(
            f'<a href="./{slug}" '
            f'class="tag-cloud-link" '
            f'style="font-size:{size}px;color:{color};font-weight:{weight}" '
            f'title="{tag} ({len(arts)} 篇)">{tag}</a>'
        )
    cloud_html = '<div class="tag-cloud">' + '\n'.join(cloud_items) + '</div>'

    lines = [
        '---',
        'title: "按标签浏览"',
        'outline: deep',
        '---',
        '',
        '# 按标签浏览',
        '',
        f'共 **{len(tag_articles)}** 个标签，涵盖 Ceph 各个技术方向。',
        '',
        cloud_html,
        '',
    ]

    # Group into tiers for detailed listing
    hot_tags = [(t, arts) for t, arts in sorted_tags if len(arts) >= 50]
    medium_tags = [(t, arts) for t, arts in sorted_tags if 10 <= len(arts) < 50]
    niche_tags = [(t, arts) for t, arts in sorted_tags if len(arts) < 10]

    if hot_tags:
        lines.append('## 热门标签')
        lines.append('')
        for tag, arts in hot_tags:
            slug = tag_to_slug(tag)
            lines.append(f'- [{tag}](./{slug}) — {len(arts)} 篇')
        lines.append('')

    if medium_tags:
        lines.append('## 专题标签')
        lines.append('')
        for tag, arts in medium_tags:
            slug = tag_to_slug(tag)
            lines.append(f'- [{tag}](./{slug}) — {len(arts)} 篇')
        lines.append('')

    if niche_tags:
        lines.append('## 其他标签')
        lines.append('')
        for tag, arts in niche_tags:
            slug = tag_to_slug(tag)
            lines.append(f'- [{tag}](./{slug}) — {len(arts)} 篇')
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
        'outline: deep',
        '---',
        '',
        f'# {tag}',
        '',
        f'共 **{len(sorted_arts)}** 篇文章',
        '',
        f'[← 返回标签列表](./)',
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

    lines.append('[← 返回标签列表](./)')
    lines.append('')

    return '\n'.join(lines)


# === Main ===
MIN_ARTICLES = 5  # Only generate pages for tags with at least this many articles

print('Scanning articles for tags...')
tag_articles = scan_articles()
print(f'Found {len(tag_articles)} unique tags across {sum(len(v) for v in tag_articles.values())} tag-article pairs')

# Filter tags by minimum article count
filtered_tags = {tag: arts for tag, arts in tag_articles.items() if len(arts) >= MIN_ARTICLES}
skipped = len(tag_articles) - len(filtered_tags)
print(f'Keeping {len(filtered_tags)} tags with >= {MIN_ARTICLES} articles (skipping {skipped} low-frequency tags)')

# Create tags directory
os.makedirs(TAGS_DIR, exist_ok=True)

# Clean old tag pages (keep only ones we generate)
for f in os.listdir(TAGS_DIR):
    if f.endswith('.md'):
        os.remove(os.path.join(TAGS_DIR, f))

# Generate index page (use filtered tags)
print('Generating tags/index.md...')
index_content = generate_tag_index(filtered_tags)
with open(os.path.join(TAGS_DIR, 'index.md'), 'w', encoding='utf-8') as f:
    f.write(index_content)

# Generate per-tag pages (only for filtered tags)
for tag, articles in filtered_tags.items():
    slug = tag_to_slug(tag)
    content = generate_tag_page(tag, articles)
    with open(os.path.join(TAGS_DIR, f'{slug}.md'), 'w', encoding='utf-8') as f:
        f.write(content)

print(f'Generated {len(filtered_tags) + 1} tag pages in {TAGS_DIR}')
