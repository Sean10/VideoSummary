---
title: "Ceph Crimson/SeaStore 2021-10-03"
date: 2021-10-03
updated: 2021-11-05
tags:
  - "Ceph"
  - "分布式存储"
  - "CRUSH算法"
  - "高可用性"
  - "可扩展性"
  - "对象存储"
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
  - "Erasure Coding"
  - "iSCSI"
  - "NFS"
  - "CIFS"
  - "POSIX"
  - "监控"
  - "Dashboard"
  - "编排"
  - "自动化"
  - "容器化"
  - "Kubernetes"
  - "Docker"
  - "云计算"
  - "AWS"
  - "Azure"
  - "Google Cloud"
  - "存储集群"
  - "SSD"
  - "HDD"
  - "SAN"
  - "NAS"
categories:
  - "视频总结"
outline: deep
---
在2021年10月3日的Ceph Crimson/SeaStore会议中，与会人员讨论了Ceph项目的多个关键议题和进展情况。以下是会议的主要内容和决定事项：

**主要议题**：

1. **Ceph相关工作进展**：
   - 完成对“Journal Badging PR for Young Gem”的评审。
   - “C-Star Metadata PR for May”正在进行中。
   - “Cache LRU”项目因其他事务被打断。
   - 建立过程中遇到问题，需要进一步调查。
   - 发现不同构建选项对性能测试结果有影响，需进一步验证。
   - “Make FS”问题，Ceph启动和停止正常，但使用特定命令启动OSD时出现问题。
   - 讨论了FSID的设置和随机化问题。
   - 计划将“Spread LFS Strategy Work”合并到主分支，但上周因其他工作未能推进。
   - 修复了“Journal Committer Management”相关问题，并进行了性能测试。

**决定事项**：

- 需要进一步调查和解决“Build”问题。
- 需要验证不同构建选项对性能测试结果的影响。
- 需要调查“Make FS”问题。
- 决定在Ceph存储初始化时随机化FSID，避免写入零值。
- 决定合并“Journal Committer Management”相关PR，尽管在特定环境中存在性能问题。

**后续行动计划**：

- 继续调查并解决“Build”问题。
- 验证并分析不同构建选项的影响。
- 调查“Make FS”问题。
- 在Ceph存储初始化时随机化FSID。
- 继续推进“Spread LFS Strategy Work”并将工作合并到主分支。
- 合并“Journal Committer Management”相关PR，并后续解决性能问题。

**其他**：

- 会议中提到了一些技术细节和具体代码问题，需要相关人员进一步跟进和处理。

会议在讨论完所有议题后结束，祝大家一周愉快。