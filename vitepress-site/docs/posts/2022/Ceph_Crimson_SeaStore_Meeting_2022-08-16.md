---
title: "Ceph Crimson/SeaStore Meeting 2022-08-16"
date: 2022-10-20
updated: 2022-10-21
tags:
  - "Ceph"
  - "分布式存储"
  - "CRUSH算法"
  - "高可用性"
  - "可扩展性"
  - "对象存储"
  - "块存储"
  - "性能"
  - "BlueStore"
  - "BlueFS"
  - "RocksDB"
  - "OSD"
  - "MON"
  - "MDS"
  - "PG"
  - "RADOS"
  - "librados"
  - "libcephfs"
  - "RBD"
  - "RGW"
  - "RESTful API"
  - "认证"
  - "授权"
  - "加密"
  - "Erasure Coding"
  - "复制"
  - "快照"
  - "克隆"
  - "iSCSI"
  - "NFS"
  - "CIFS"
  - "POSIX"
  - "监控"
  - "编排"
  - "自动化"
  - "容器化"
  - "Kubernetes"
  - "Docker"
  - "虚拟化"
  - "云计算"
  - "AWS"
  - "Azure"
  - "Google Cloud"
  - "SSD"
  - "HDD"
  - "SAN"
  - "NAS"
  - "网络"
  - "恢复"
  - "负载均衡"
  - "缓存"
  - "压缩"
  - "去重"
  - "性能优化"
  - "测试"
categories:
  - "视频总结"
outline: deep
---
在 2022 年 8 月 16 日的 Ceph Crimson/SeaStore 会议中，团队讨论了一系列技术议题和后续行动计划。以下是对会议内容的总结：

### 会议主要内容：

1. **OSD Map 共享优化**：讨论了创建外部指针模拟以高效共享 OSD Maps 的解决方案，并进行了多核处理优化。

2. **GNS 补丁更新**：Aaron 提交了 GNS 补丁的第二版，解决了评审意见，并讨论了 `advance` 函数的使用和命名问题。

3. **ZNS 测试进展**：Aaron 报告了在物理 ZNS 驱动上的测试情况，并计划进行更长时间的测试。

4. **事务管理器优化**：讨论了事务管理器中的特定机制，包括设备清除和异步清理接口的优化。

5. **Key Range Remove 和 Omap 合并策略**：讨论了 Key Range Remove 的复杂性，并找到了更好的 Omap 合并策略。

6. **测试环境更新**：报告了测试环境中的进展，目前 60% 的测试已通过，正在解决系统挂起的问题。

7. **其他更新**：讨论了 Fish Bay Tree 代码的优化，并提交了两个 PR 以修复发现的次要问题。

### 决定事项：

- Aaron 将发送邮件给 Seth 和 David Galloway，请求更新 CI 机器上的内核版本以支持 ZNS。
- 确定 `advance` 函数的使用和命名问题，将其分为两个调用：`advance` 和 `write`。

### 后续行动计划：

- Aaron 将继续进行 ZNS 的长时间测试。
- 继续优化事务管理器和异步清理接口。
- 完成 Key Range Remove 和 Omap 合并策略的改进。
- 解决测试环境中的系统挂起问题，并完成剩余的测试。

会议在讨论了所有议题后结束，所有参会人员祝大家一周愉快。