---
title: "Ceph Crimson/SeaStor OSD Weekly 2020-06-03"
date: 2020-06-03
updated: 2020-06-04
tags:
  - "Ceph"
  - "分布式存储"
  - "CRUSH算法"
  - "高可用性"
  - "可扩展性"
  - "对象存储"
  - "块存储"
  - "文件系统存储"
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
  - "复制"
  - "快照"
  - "克隆"
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
  - "虚拟化"
  - "云计算"
  - "AWS"
  - "Azure"
  - "Google Cloud"
  - "混合云"
  - "多云"
  - "存储集群"
  - "SSD"
  - "HDD"
  - "SAN"
  - "NAS"
  - "网络"
  - "弹性"
  - "恢复"
  - "负载均衡"
  - "缓存"
  - "压缩"
  - "去重"
  - "分层"
  - "测试"
categories:
  - "视频总结"
outline: deep
---
本次会议主要讨论了以下议题：

1. **PR更新与同步**：会议开始时，讨论了上周的PR更新情况，特别是关于同步版本的问题。讨论了如何获取同步版本以及后续的审查和合并流程。

2. **代码重构与实现细节**：讨论了提取公共代码的问题，特别是关于extended map tree和IRB tree的实现细节差异。决定暂时不停止提取公共代码。

3. **Transaction Manager与Cache**：解释了transaction manager如何通过cache进行操作，并强调了transaction manager在系统中的重要性。

4. **测试与性能评估**：讨论了如何处理重复的crimson实例，并计划实施单元测试。提到了关于active item的单元测试问题，并计划在不同环境下实施测试。

5. **Recovery测试**：讨论了如何在现有QA框架内进行recovery测试，特别是涉及OSD的关闭和启动。建议先进行单元测试和手动测试，然后集成crimson到QA框架中。

6. **内存分配器问题**：讨论了内存分配器的问题，特别是关于使用Liberty allocator的必要性。强调了需要一个单一的二进制文件，而不是根据不同的存储后端提供不同的二进制文件。

会议决定：

- 继续推进PR的同步和审查工作。
- 暂时不停止提取公共代码。
- 实施单元测试和手动测试，以验证recovery机制。
- 解决内存分配器的问题，确保最终提供一个单一的二进制文件。

后续行动计划：

- 完成PR的同步和审查工作，并解决相关的评论问题。
- 继续实施extended tree和key system的简化工作。
- 实施单元测试和手动测试，确保recovery机制的正确性。
- 评估内存分配器的性能影响，并寻找解决方案以提供单一的二进制文件。