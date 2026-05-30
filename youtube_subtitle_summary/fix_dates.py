"""
修复 temp_posts/ 里 front matter 的 date/updated 字段：
- 优先从文件名提取日期（如 Meeting_2025-12-10）
- 否则用 videos_meta.jsonl 的 upload_date
"""
import os
import re
from libylt2summary.utils import get_metadata_from_jsonl

POSTS_DIR = "temp_posts"
DATE_IN_NAME = re.compile(r"(\d{4}-\d{2}-\d{2})")
VALID_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def resolve_date(filename: str) -> str | None:
    """返回应使用的日期，优先文件名，其次 upload_date。"""
    m = DATE_IN_NAME.search(filename)
    if m:
        return m.group(1)
    meta = get_metadata_from_jsonl(filename)
    if meta and meta.get("date"):
        return meta["date"]
    return None


def fix_file(path: str, filename: str) -> tuple[bool, str]:
    content = open(path, encoding="utf-8").read()

    # 取 front matter 里的 date
    m = re.search(r"^(date:\s*)(.+)$", content, re.MULTILINE)
    if not m:
        return False, "no_date_field"

    current_date = m.group(2).strip()
    correct_date = resolve_date(filename)
    if not correct_date:
        return False, "no_metadata"

    # 判断是否需要修复：格式不合法，或年份不符
    needs_fix = (
        not VALID_DATE.match(current_date)
        or current_date[:4] != correct_date[:4]
    )
    if not needs_fix:
        return False, "ok"

    # 替换 date 和 updated
    new_content = re.sub(
        r"^(date:\s*).+$", f"date: {correct_date}", content, flags=re.MULTILINE
    )
    new_content = re.sub(
        r"^(updated:\s*).+$", f"updated: {correct_date}", new_content, flags=re.MULTILINE
    )

    open(path, "w", encoding="utf-8").write(new_content)
    return True, f"{current_date} → {correct_date}"


def main():
    fixed = 0
    skipped = []

    for f in sorted(os.listdir(POSTS_DIR)):
        if not f.endswith(".md"):
            continue
        path = os.path.join(POSTS_DIR, f)
        changed, reason = fix_file(path, f)
        if changed:
            fixed += 1
            print(f"  fixed  {reason:40s}  {f}")
        elif reason not in ("ok",):
            skipped.append((f, reason))

    print(f"\n修复: {fixed} 个")
    if skipped:
        print(f"跳过: {len(skipped)} 个")
        for f, r in skipped[:5]:
            print(f"  {r}: {f}")


if __name__ == "__main__":
    main()
