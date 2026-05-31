"""
清洗 source/_posts/ 里所有文章的 tags：
1. 通过 ALIAS_MAP 规范化 tag（统一大小写变体、中英文重复）
2. 只保留白名单中的 tag
3. 清洗后为空则兜底保留 ["Ceph"]
4. 重写 front matter 中的 tags 字段

用法：
  python clean_tags.py           # 实际执行
  python clean_tags.py --dry-run # 只预览，不修改文件
"""
import os
import re
import sys

POSTS_DIR = "../source/_posts"

# 语义别名映射：将变体统一到标准形式
ALIAS_MAP = {
    "Distributed Storage": "分布式存储",
    "distributed storage": "分布式存储",
    "Bluestore": "BlueStore",
    "bluestore": "BlueStore",
    "Blue Store": "BlueStore",
    "CRUSH Algorithm": "CRUSH算法",
    "CRUSH algorithm": "CRUSH算法",
    "CRUSH 算法": "CRUSH算法",
    "Performance Optimization": "性能优化",
    "性能调优": "性能优化",
    "Ceph性能优化": "性能优化",
    "High Availability": "高可用性",
    "Scalability": "可扩展性",
    "可伸缩性": "可扩展性",
    "Rocksdb": "RocksDB",
    "rocksdb": "RocksDB",
    "Bluefs": "BlueFS",
    "bluefs": "BlueFS",
    "Rados": "RADOS",
    "rbd": "RBD",
    "radosgw": "RGW",
    "[Ceph]": "Ceph",
    "[分布式存储]": "分布式存储",
    "object storage": "对象存储",
    "Object Storage": "对象存储",
    "Storage Optimization": "存储优化",
    "Storage Cluster": "存储集群",
    "Monitoring": "监控",
    "Automation": "自动化",
    "Performance": "性能",
    "Containerization": "容器化",
    "Cloud Computing": "云计算",
    "Orchestration": "编排",
    "Orchestrator": "编排",
    "Security": "安全性",
    "Open Source": "开源",
    "Storage": "存储",
    "Ceph性能": "性能",
    "Ceph RGW": "RGW",
    "Ceph Orchestrator": "编排",
    "软件定义存储": "软件定义存储",
    "自动化测试": "测试",
    "Performance Testing": "测试",
    "性能测试": "测试",
    "故障域": "弹性",
    "失败域": "弹性",
    "网络拓扑": "网络",
    "内存管理": "性能优化",
    "仪表板": "Dashboard",
    "管理": "编排",
    "编排": "编排",
    "Cephadm": "Cephadm",
    "去中心化": "分布式存储",
    "一致性": "高可用性",
    "SD": None,  # 无意义，丢弃
    "Multi": None,
    # 小写变体补充
    "high availability": "高可用性",
    "performance tuning": "性能优化",
    "performance optimization": "性能优化",
    "erasure coding": "Erasure Coding",
    "object storage": "对象存储",
    "block storage": "块存储",
    "distributed storage": "分布式存储",
    "cloud computing": "云计算",
    "high performance": "性能优化",
    "scalability": "可扩展性",
    "monitoring": "监控",
    "automation": "自动化",
    "security": "安全性",
    "storage": "存储",
    "performance": "性能",
    "testing": "测试",
    "containerization": "容器化",
    "orchestration": "编排",
    "open source": "开源",
    "replication": "复制",
    "encryption": "加密",
    "compression": "压缩",
    "deduplication": "去重",
    "caching": "缓存",
    "snapshots": "快照",
    "clones": "克隆",
    "authentication": "认证",
    "authorization": "授权",
    "virtualization": "虚拟化",
    "load balancing": "负载均衡",
    "recovery": "恢复",
    "network": "网络",
}

TAG_WHITELIST = {
    # 核心组件
    "Ceph", "RGW", "CephFS", "OSD", "MON", "MDS", "RBD", "RADOS",
    "BlueStore", "BlueFS", "RocksDB", "Crimson", "Cephadm",
    # 存储类型
    "分布式存储", "对象存储", "块存储", "文件系统存储", "存储集群", "存储优化",
    # 技术特性
    "性能优化", "高可用性", "可扩展性", "CRUSH算法", "Erasure Coding",
    "加密", "快照", "克隆", "复制", "认证", "授权", "压缩", "去重", "缓存", "分层",
    "PG", "librados", "libcephfs", "RESTful API", "NFS", "iSCSI", "POSIX", "CIFS",
    # 生态集成
    "Kubernetes", "Rook", "OpenStack", "Docker", "AWS", "Azure", "Google Cloud",
    "云计算", "混合云", "多云", "容器化", "虚拟化",
    # 运维管理
    "监控", "自动化", "编排", "Dashboard", "Teuthology", "CI/CD",
    "负载均衡", "恢复", "弹性", "网络", "NVMe", "HDD", "SSD", "SAN", "NAS",
    # 社区/报告类
    "社区动态", "季度报告", "年度报告", "月度报告", "会议纪要",
    "开源", "安全性", "性能", "测试", "存储",
    # 其他高频
    "CERN", "软件定义存储",
}


def normalize_tag(tag: str) -> str | None:
    """规范化单个 tag，返回白名单中的标准形式，或 None 表示丢弃。"""
    tag = tag.strip()
    # 先查别名映射
    if tag in ALIAS_MAP:
        return ALIAS_MAP[tag]
    # 在白名单中直接返回
    if tag in TAG_WHITELIST:
        return tag
    return None


def parse_tags_from_frontmatter(content: str) -> list[str]:
    """从 front matter 中提取 tags 列表。"""
    m = re.search(r'^tags:\s*\n((?:[ \t]*- .+\n?)+)', content, re.MULTILINE)
    if not m:
        return []
    tags = []
    for line in m.group(1).split('\n'):
        tag = re.sub(r'^[ \t]*- ', '', line).strip()
        if tag:
            tags.append(tag)
    return tags


def replace_tags_in_content(content: str, new_tags: list[str]) -> str:
    """替换 front matter 中的 tags 字段，保持其他内容不变。"""
    tags_block = "tags:\n" + "".join(f"- {t}\n" for t in new_tags)
    # 匹配 tags: 后跟列表项的整个块
    new_content = re.sub(
        r'^tags:\s*\n(?:[ \t]*- .+\n?)+',
        tags_block,
        content,
        flags=re.MULTILINE,
    )
    return new_content


def process_file(path: str, dry_run: bool) -> tuple[int, int]:
    """处理单个文件，返回 (原始tag数, 清洗后tag数)。"""
    content = open(path, encoding="utf-8").read()
    original_tags = parse_tags_from_frontmatter(content)
    if not original_tags:
        return 0, 0

    # 规范化并过滤
    new_tags_set = []
    seen = set()
    for tag in original_tags:
        normalized = normalize_tag(tag)
        if normalized and normalized not in seen:
            new_tags_set.append(normalized)
            seen.add(normalized)

    # 兜底
    if not new_tags_set:
        new_tags_set = ["Ceph"]

    if set(original_tags) == set(new_tags_set) and len(original_tags) == len(new_tags_set):
        return len(original_tags), len(new_tags_set)

    if not dry_run:
        new_content = replace_tags_in_content(content, new_tags_set)
        open(path, "w", encoding="utf-8").write(new_content)

    return len(original_tags), len(new_tags_set)


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("[dry-run 模式，不修改文件]\n")

    total_files = 0
    changed_files = 0
    total_before = 0
    total_after = 0

    for fname in sorted(os.listdir(POSTS_DIR)):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(POSTS_DIR, fname)
        before, after = process_file(path, dry_run)
        total_files += 1
        total_before += before
        total_after += after
        if before != after or (before > 0 and after < before):
            changed_files += 1
            if dry_run and before > 0:
                # 显示变化详情
                content = open(path, encoding="utf-8").read()
                orig = parse_tags_from_frontmatter(content)
                new_t = []
                seen = set()
                for t in orig:
                    n = normalize_tag(t)
                    if n and n not in seen:
                        new_t.append(n)
                        seen.add(n)
                if not new_t:
                    new_t = ["Ceph"]
                removed = set(orig) - set(new_t)
                if removed:
                    print(f"  {fname}: {before}→{after} tags, 移除: {sorted(removed)[:5]}{'...' if len(removed)>5 else ''}")

    print(f"\n{'[dry-run] ' if dry_run else ''}处理完成:")
    print(f"  总文件数: {total_files}")
    print(f"  变更文件数: {changed_files}")
    print(f"  tag 总数: {total_before} → {total_after}")
    print(f"  减少: {total_before - total_after} 个 tag 实例")


if __name__ == "__main__":
    main()
