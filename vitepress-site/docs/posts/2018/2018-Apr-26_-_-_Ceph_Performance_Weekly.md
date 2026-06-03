---
title: "2018-Apr-26 :: Ceph Performance Weekly"
date: 2018-04-26
updated: 2018-04-27
tags:
  - "Ceph"
  - "分布式存储"
  - "BlueStore"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2023年某月某日

**参会人员**： Josh, Sage, CJ, Igor, Adam, Virata 等

**会议主题**： Ceph 分布式存储项目进展讨论

**会议内容**：

**1. 编译与代码问题**

- Josh 分享了代码编译过程中遇到的问题，并提到在修复编译错误后，系统似乎运行良好，但他对此感到怀疑，担心可能存在更复杂的问题。

**2. 项目进展**

- **Osteen Mapping Encoding**： Sage 介绍了 Osteen Mapping Encoding 的进展，该功能即将合并，但需要回滚到 Luminous 版本。
- **Slav Pull Requests**： Sage 提到了 Slav 的几个 pull requests，旨在加快加密操作，并提到正在使用 OpenSSL 进行更大规模的更改。
- **其他合并项**： 包括 Creek assist 和 Shin 等功能。
- **Blue Store**： 讨论了 Blue Store 的巨大页面使用情况，以及如何优化内存使用和减少同步开销。
- **Recovery Optimization**： Josh 表示该功能尚未准备好，将联系 Young 了解更多信息。
- **OpenSSL**： CJ 认为使用 OpenSSL 的改动很有前景。
- **内存分配和释放列表管理**： Igor 正在研究新的位图分配方法，Adam 正在研究碎片化问题。
- **Blue Store Cash Balancing**： John 讨论了 Blue Store Cash Balancing 的设置方式，认为当前的设置不够直观，并建议简化缓存调整过程。

**3. 决定事项**

- 将 Osteen Mapping Encoding 功能回滚到 Luminous 版本。
- 关注 Slav 的 pull requests，并跟踪 OpenSSL 改动的进展。
- 进一步优化 Blue Store 的巨大页面使用。
- 跟踪 Recovery Optimization 和内存分配相关问题的进展。
- 简化 Blue Store Cash Balancing 的设置过程。

**4. 后续行动计划**

- Josh 将联系 Young 了解 Recovery Optimization 的进展。
- CJ 将关注 OpenSSL 改动的进展。
- John 将准备相关 pull requests，以简化 Blue Store Cash Balancing 的设置过程。

**5. 其他事项**

- 会议讨论了其他一些议题，但没有形成明确的行动计划。

**会议结束**。