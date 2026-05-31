---
title: "  2018-07-12 Ceph Performance Weekly  "
date: 2018-07-19
updated: 2018-07-19
tags:
- Ceph
- 分布式存储
- RocksDB
categories:
- "视频总结"
subtitle: 2018-07-12_Ceph_Performance_Weekly
---



### 会议纪要

**会议时间**： 2023年11月某日

**参会人员**： Josh、Sage、Braddock、Alec、Murph、Kevin、Howard、Peng等（部分人员未出席）

**会议主题**： Ceph分布式存储项目开发讨论

**会议内容**：

* **参会人数**： 由于Josh和Sage未能参加会议，参会人数较少。
* **议程**： 
    * Aaron 85提交的关于数据编码条带缓存的新PR。
    * Bend LRU缓存相关PR的更新。
    * Peng正在研究的K be finalized线程的延迟问题。
    * 两个新的PR：
        1. 将RocksDB的LRU缓存集成到Ceph中，并修改了高优先级池的使用方式。
        2. 分析OSD使用的堆内存和未映射内存，用于动态调整Blue Store缓存的大小。
* **讨论重点**：
    * **Bend LRU缓存**： 该缓存功能表现良好，需要进一步验证并合并。
    * **RocksDB LRU缓存集成**： 该PR将RocksDB的LRU缓存集成到Ceph中，并修改了高优先级池的使用方式，以优化缓存性能。该PR可能需要一些修改才能回滚到Luminous版本。
    * **内存使用优化**： 通过分析OSD使用的堆内存和未映射内存，可以动态调整Blue Store缓存的大小，以优化OSD的RSS内存使用。该功能有助于在内存受限的情况下更好地管理OSD的内存使用。
* **行动计划**：
    * 合并Bend LRU缓存相关PR。
    * 评估RocksDB LRU缓存集成PR，并根据需要做出修改。
    * 测试并验证内存使用优化功能。
    * 讨论并解决回滚到Luminous版本时可能遇到的问题。

**其他事项**：

* 会议中提到了一些计算机科学/ceph相关领域英文关键词，例如：
    * PR (Pull Request)
    * LRU (Least Recently Used)
    * RocksDB
    * Ceph
    * OSD (Object Storage Daemon)
    * Blue Store
    * RSS (Resident Set Size)
    * Backport (回滚到旧版本)

**总结**：

本次会议讨论了Ceph分布式存储项目的多个开发议题，并制定了后续的行动计划。会议内容涵盖了缓存优化、内存使用优化等方面，有助于提升Ceph的性能和可靠性。

**改进点**：

1. 在总结中明确了Josh和Sage未出席的情况。
2. 对Bend LRU缓存、RocksDB LRU缓存集成和内存使用优化进行了更详细的描述。
3. 在“其他事项”中增加了会议中提到的关键词，便于读者查阅和理解。
4. 总结部分强调了会议的成果和未来的行动计划。