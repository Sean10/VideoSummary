"""
修正 source/_posts/ 里 CephFS 相关的字幕误写：
- SEFS → CephFS
- CFS  → CephFS
- SFS  → CephFS
- FFS  → CephFS（Loops FFS → libcephfs）

保留不替换：
- SDFS（IBM 软件定义存储）
- HDFS（Hadoop）
- VFS（Linux 虚拟文件系统层）
- NFS / CIFS / XFS / ZFS / LFS / COHORTFS（各自独立含义）
"""
import os
import re
import sys

POSTS_DIR = "../source/_posts"


def fix_file(path: str, dry_run: bool) -> list[str]:
    """返回该文件的变更描述列表，空列表表示无变化。"""
    content = open(path, encoding="utf-8").read()
    original = content

    # Loops FFS → libcephfs（先处理，避免被后面的规则误伤）
    content = re.sub(r'(?<![A-Za-z])Loops FFS(?![A-Za-z])', 'libcephfs', content)

    # SEFS / CFS / SFS / FFS → CephFS
    # 用 (?<![A-Za-z]) 和 (?![A-Za-z]) 替代 \b，兼容中文紧邻的情况
    for pattern in (r'(?<![A-Za-z])SEFS(?![A-Za-z])',
                    r'(?<![A-Za-z])CFS(?![A-Za-z])',
                    r'(?<![A-Za-z])SFS(?![A-Za-z])',
                    r'(?<![A-Za-z])FFS(?![A-Za-z])'):
        content = re.sub(pattern, 'CephFS', content)

    if content == original:
        return []

    changes = []
    orig_lines = original.splitlines()
    new_lines = content.splitlines()
    for i, (ol, nl) in enumerate(zip(orig_lines, new_lines), 1):
        if ol != nl:
            changes.append(f"  L{i}: {ol.strip()[:80]}")

    if not dry_run:
        open(path, "w", encoding="utf-8").write(content)

    return changes


def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("[dry-run 模式，不修改文件]\n")

    total_files = 0
    changed_files = 0

    for fname in sorted(os.listdir(POSTS_DIR)):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(POSTS_DIR, fname)
        changes = fix_file(path, dry_run)
        total_files += 1
        if changes:
            changed_files += 1
            print(f"{fname} ({len(changes)} 处):")
            for c in changes[:5]:
                print(c)
            if len(changes) > 5:
                print(f"  ... 还有 {len(changes)-5} 处")
            print()

    print(f"{'[dry-run] ' if dry_run else ''}完成: {total_files} 个文件，{changed_files} 个有变更")


if __name__ == "__main__":
    main()
