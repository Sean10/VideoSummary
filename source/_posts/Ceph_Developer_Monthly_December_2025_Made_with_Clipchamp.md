---
title: Ceph Developer Monthly   December 2025   Made with Clipchamp
date: 2025-12-04
updated: 2025-12-04
tags:
- Ceph
- libcephfs
- BlueStore
- RocksDB
categories: 
- "视频总结"
- "Ceph 社区"
- "存储技术"
- "软件开发"
- "系统架构"
subtitle: Ceph_Developer_Monthly_December_2025_Made_with_Clipchamp
---

## 改进后的中文总结内容

本次 Ceph 开发者月度会议主要讨论了 EC Direct Reads 的优化与 Exec 操作安全性的改进。

**会议要点**：

1. **EC Direct Reads 优化**：
   - 目标：提升性能，客户端直接从多个 OSD 读取数据并拼接结果。
   - 风险：Exec 操作可能因重试导致重复写入，数据损坏。
   - 改进方向：OSD 端强化检查，明确返回错误以便调试；版本控制，避免破坏旧集群。

2. **Exec 操作的安全性**：
   - 现状问题：客户端可能通过标记为读的 Exec 执行写入操作。
   - 解决方案：C++ API 改进，引入编译时安全的接口；废弃旧接口；运行时检查，OSD 对含写入的 read_op 返回错误。

3. **C/C++ API 兼容性**：
   - C++ API：共识为直接移除不安全接口，维持 ABI 兼容性已无实际维护。
   - C API：保留现有接口，但依赖 OSD 端强制检查，避免破坏外部绑定。

4. **后续行动计划**：
   - 短期：提交 PR 实现 OSD 端强化检查，更新 C++ API并提供编译时安全接口。
   - 长期：评估外部用户对 C API 的依赖，讨论 Exec 接口的公开性。

**其他议题**：

- Casey 的 "Fast Clones" 提案：新增 RADOS 操作返回写入空间分配信息，支持 CephFS 快照克隆；RGW 对 `return_ve` 大小限制的改进需求。

**会议结论**：

- 通过：OSD 端强制检查 + C++ API 安全改造。
- 搁置：完全隐藏 Exec 接口的提议。
- 下一步：在 dev mailing list 同步方案细节，收集社区反馈。

## 关键词保留（Ceph 术语）

- **EC (Erasure Coding)** | **CRUSH Algorithm** | **OSD/MON/MDS**  
- **PG (Placement Group)** | **RADOS** | **librados/libcephfs**  
- **Bluestore/RocksDB** | **Thin Provisioning** | **iSCSI/NFS**  
- **Exec Operation** | **C++ API** | **C API**  
- **Compatibility** | **Rados API** | **libcephfs**  
- **Fast Clones** | **CephFS** | **Snapshots**  
- **Object Class API** | **Exec Interface** | **Safety**  
- **Compile-time Safety** | **Runtime Check** | **Error Handling**