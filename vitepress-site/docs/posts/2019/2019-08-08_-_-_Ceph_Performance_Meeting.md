---
title: "2019-08-08 -- Ceph Performance Meeting"
date: 2019-08-08
updated: 2019-08-12
tags:
  - "性能"
  - "存储优化"
  - "分布式存储"
  - "BlueStore"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2023年11月某日

**参会人员**： 核心团队成员

**会议主题**： 讨论Ceph项目的最新进展、关键性能问题及后续行动计划。

**关键细节**：

* **Alec尺寸变更**： 
    * 由于碎片化导致的空间浪费，团队成员正在讨论将Alec尺寸从64k调整到更大的值，以优化存储效率。
    * 讨论中提出了两个PR：一个将Alec尺寸设置为64k，另一个在共享设备上使用64k的Alec尺寸，但在Blue Store TV或Well设备上不使用。
* **异步读取PR**：
    * 讨论了一个实现异步读取的OSD PR，但需要进一步的性能和剖析数据来评估其影响。
* **其他PR**：
    * Jinping的PR：优化了IO通知解锁操作，提高了性能。
    * Igor的PR：减少了锁获取的开销。
    * Champagne的PR：减少了不必要的通知，可能略微提高了性能。
    * Eric的PR：合并了一个小的RG w PR qualms PR，可能没有太大影响，但有助于提高性能。
* **Blue Store Alexeyes**：
    * Neha的PR：针对Blue Store Alexeyes进行了一些调整。
    * Adam的PR：对Boost和元数据进行了研究，并将其组织到不同的列族中。
    * 讨论了将PG日志信息存储在单独的列族中的利弊，以及如何优化存储和内存缓冲区。
* **其他议题**：
    * MDS和Mon内存限制的优化。
    * 自动化Rocks DB文件在BlueFS设备之间移动的PR。
    * IOU ring和messenger的PR。
    * op tracker PR。
    * cash bidding rebase。

**讨论的主要议题**：

* **Alec尺寸变更**：
    * 讨论了将Alec尺寸从64k调整到更大的值的利弊。
    * 分析了不同Alec尺寸对性能的影响。
    * 讨论了是否应该将PG日志信息存储在单独的列族中。
* **其他议题**：
    * 讨论了如何优化存储和内存缓冲区。
    * 讨论了如何将Rocks DB文件在BlueFS设备之间移动。

**决定的事项**：

* 继续讨论Alec尺寸变更，并收集更多数据。
* 对异步读取PR进行进一步的分析。
* 对其他PR进行审查和合并。
* 继续优化MDS和Mon内存限制。
* 完成其他议题的相关工作。

**后续行动计划**：

* 收集更多数据以评估Alec尺寸变更的影响。
* 对异步读取PR进行进一步的分析。
* 完成其他PR的审查和合并。
* 完成MDS和Mon内存限制的优化。
* 完成其他议题的相关工作。

**备注**：

* 会议中提到了一些计算机科学/ceph相关领域英文关键词，例如Alec、Blue Store、RocksDB、OSD、PG、column family等。
* 会议中讨论了一些具体的性能测试和实验，例如迭代测试、写入测试等。