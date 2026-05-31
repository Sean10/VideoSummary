"""
修复现有季度总结文章：追加"参考文章"章节。
不重新调用 Claude，只在文件末尾追加链接列表。
"""
import os
import re
import sys

# 需要在 youtube_subtitle_summary 目录下运行
POSTS_DIR = "temp_posts"
QUARTERLY_DIR = "../source/_posts"
SITE_ROOT = "/VideoSummary"


def build_post_url(fname: str, posts_dir: str) -> str:
    path = os.path.join(posts_dir, fname)
    try:
        content = open(path, encoding="utf-8").read()
        m = re.search(r"^date:\s*(\d{4})-(\d{2})-(\d{2})", content, re.MULTILINE)
        if not m:
            return ""
        year, month, day = m.group(1), m.group(2), m.group(3)
        title = fname.replace(".md", "")
        return f"{SITE_ROOT}/{year}/{month}/{day}/{title}/"
    except Exception:
        return ""


def get_post_title(fname: str, posts_dir: str) -> str:
    try:
        content = open(os.path.join(posts_dir, fname), encoding="utf-8").read()
        m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    except Exception:
        pass
    return fname.replace(".md", "").replace("_", " ")


def get_quarter(year: int, month: int) -> str:
    return f"{year}Q{(month - 1) // 3 + 1}"


def get_quarter_posts(quarter: str, posts_dir: str) -> list:
    """从 temp_posts 里找属于该季度的所有文章。"""
    result = []
    for fname in os.listdir(posts_dir):
        if not fname.endswith(".md"):
            continue
        content = open(os.path.join(posts_dir, fname), encoding="utf-8").read()
        m = re.search(r"^date:\s*(\d{4})-(\d{2})", content, re.MULTILINE)
        if not m:
            continue
        year, month = int(m.group(1)), int(m.group(2))
        if get_quarter(year, month) == quarter:
            result.append(fname)
    return result


def fix_file(quarterly_path: str, quarter: str, posts_dir: str) -> bool:
    content = open(quarterly_path, encoding="utf-8").read()

    # 已有参考文章章节则跳过
    if "## 参考文章" in content:
        return False

    post_files = get_quarter_posts(quarter, posts_dir)
    if not post_files:
        return False

    ref_lines = ["\n\n---\n\n## 参考文章\n"]
    for fname in sorted(post_files):
        url = build_post_url(fname, posts_dir)
        if not url:
            continue
        title = get_post_title(fname, posts_dir)
        ref_lines.append(f"- [{title}]({url})")

    ref_section = "\n".join(ref_lines)
    with open(quarterly_path, "a", encoding="utf-8") as f:
        f.write(ref_section + "\n")
    return True


def main():
    fixed = 0
    skipped = 0

    for fname in sorted(os.listdir(QUARTERLY_DIR)):
        if "季度总结" not in fname or not fname.endswith(".md"):
            continue
        quarter = fname.replace("_Ceph社区季度总结.md", "")
        path = os.path.join(QUARTERLY_DIR, fname)
        changed = fix_file(path, quarter, POSTS_DIR)
        if changed:
            fixed += 1
            print(f"  fixed  {quarter}")
        else:
            skipped += 1

    print(f"\n修复: {fixed} 个，跳过: {skipped} 个")


if __name__ == "__main__":
    main()
