"""
清理旧的总结文章：
- 删除所有季度总结（保留 2026Q2_Ceph社区季度总结.md）
- 删除所有月度总结（如有）
- 删除所有年度总结（如有）
让用户重新触发生成带章节内链接的新版本。
"""
import os
import sys

POSTS_DIR = "../source/_posts"
KEEP = {"2026Q2_Ceph社区季度总结.md"}


def main(dry_run: bool = False):
    to_delete = []
    for fname in sorted(os.listdir(POSTS_DIR)):
        if fname in KEEP:
            continue
        if any(tag in fname for tag in ("季度总结", "月度总结", "年度总结")):
            to_delete.append(fname)

    if not to_delete:
        print("没有需要清理的文件。")
        return

    print(f"将删除 {len(to_delete)} 个文件（保留 {sorted(KEEP)}）：")
    for f in to_delete:
        print(f"  {f}")

    if dry_run:
        print("\n[dry-run 模式，未实际删除]")
        return

    confirm = input("\n确认删除？(y/N) ").strip().lower()
    if confirm != "y":
        print("已取消。")
        return

    for fname in to_delete:
        os.remove(os.path.join(POSTS_DIR, fname))
        print(f"  deleted: {fname}")

    print(f"\n完成，删除了 {len(to_delete)} 个文件。")


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    main(dry_run=dry_run)
