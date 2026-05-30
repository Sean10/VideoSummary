"""
修复 temp_posts/ 里 front matter 的 title 字段：
- 如果 title 含中文，说明是 LM 翻译/编造的，用 metadata 里的原始英文 title 替换
- subtitle 字段如果也是中文或不是文件名格式，一并修复
"""
import os
import re
from libylt2summary.utils import get_metadata_from_jsonl, sanitize_yaml_string

POSTS_DIR = "temp_posts"


def fix_file(path: str, filename: str) -> tuple[bool, str]:
    content = open(path, encoding="utf-8").read()

    m = re.search(r"^title:\s*(.+)$", content, re.MULTILINE)
    if not m:
        return False, "no_title"

    fm_title = m.group(1).strip().strip("'").strip('"').strip()

    # 只处理含中文的 title
    if not re.search(r"[一-鿿]", fm_title):
        return False, "ok"

    meta = get_metadata_from_jsonl(filename)
    if not meta:
        return False, "no_metadata"

    correct_title = sanitize_yaml_string(meta["title"])
    if not correct_title:
        return False, "empty_meta_title"

    # 替换 title
    new_content = re.sub(
        r"^title:\s*.+$",
        f"title: {correct_title}",
        content,
        flags=re.MULTILINE,
    )

    # 同时修复 subtitle（如果也含中文，改为文件名 id）
    subtitle_id = filename.replace(".md", "")
    new_content = re.sub(
        r"^subtitle:\s*.+$",
        f"subtitle: {subtitle_id}",
        new_content,
        flags=re.MULTILINE,
    )

    if new_content == content:
        return False, "no_change"

    open(path, "w", encoding="utf-8").write(new_content)
    return True, f"{fm_title!r} → {correct_title!r}"


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
            print(f"  fixed  {reason}")
        elif reason not in ("ok",):
            skipped.append((f, reason))

    print(f"\n修复: {fixed} 个")
    if skipped:
        print(f"跳过: {len(skipped)} 个")
        for f, r in skipped[:5]:
            print(f"  {r}: {f}")


if __name__ == "__main__":
    main()
