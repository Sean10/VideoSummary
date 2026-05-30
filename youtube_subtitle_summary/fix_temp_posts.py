"""
修复 temp_posts/ 里的格式问题：
1. 删除 [改进后的中文总结内容] 占位符行
2. 删除正文中多余的 --- 分隔符（front matter 之后的）
3. 报告无 front matter 的文件（不自动修复，需人工处理）
"""
import os
import re

POSTS_DIR = "temp_posts"
PLACEHOLDER = "[改进后的中文总结内容]"


def fix_file(path: str) -> tuple[bool, str]:
    """
    修复单个文件。返回 (changed, reason)。
    """
    content = open(path, encoding="utf-8").read()
    changed = False

    # strip 开头的空行
    stripped = content.lstrip("\n")
    if stripped != content:
        content = stripped
        changed = True

    if not content.startswith("---"):
        return False, "no_frontmatter"

    # 1. 删除占位符行（整行，允许行首有 # 等前缀）
    if PLACEHOLDER in content:
        new_content = re.sub(
            r"^[#\s]*\[改进后的中文总结内容\]\s*\n?",
            "",
            content,
            flags=re.MULTILINE,
        )
        if new_content != content:
            content = new_content
            changed = True

    # 2. 删除正文中多余的 --- （front matter 之后的第3个及以上）
    parts = content.split("---")
    # parts[0] 是空串（文件以 --- 开头）
    # parts[1] 是 front matter 内容
    # parts[2] 是正文（可能包含更多 ---）
    if len(parts) > 3:
        # 把 parts[2:] 合并，去掉其中的 ---
        body = "".join(parts[2:])
        new_content = f"---{parts[1]}---{body}"
        if new_content != content:
            content = new_content
            changed = True

    if changed:
        open(path, "w", encoding="utf-8").write(content)

    return changed, "ok"


def main():
    fixed = 0
    skipped_no_fm = []

    files = [f for f in os.listdir(POSTS_DIR) if f.endswith(".md")]
    for fname in sorted(files):
        path = os.path.join(POSTS_DIR, fname)
        changed, reason = fix_file(path)
        if reason == "no_frontmatter":
            skipped_no_fm.append(fname)
        elif changed:
            fixed += 1

    print(f"修复: {fixed} 个文件")
    print(f"跳过（无 front matter）: {len(skipped_no_fm)} 个")
    if skipped_no_fm:
        for f in skipped_no_fm:
            print(f"  {f}")


if __name__ == "__main__":
    main()
