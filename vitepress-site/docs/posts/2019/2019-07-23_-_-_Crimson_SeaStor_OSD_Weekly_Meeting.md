---
title: "2019-07-23 :: Crimson SeaStor OSD Weekly Meeting"
date: 2019-07-24
updated: 2019-07-24
tags:
  - "Ceph"
  - "BlueStore"
  - "RocksDB"
categories:
  - "视频总结"
outline: deep
---
会议纪要：

**会议时间**： 2019年7月23日
**会议主题**： Ceph存储系统相关技术讨论

**关键细节**：

* **会议背景**： 会议主要讨论了Ceph存储系统中BlueStore与CRimsonOS的兼容性、RocksDB的移植、性能优化以及功能扩展等议题。
* **主要议题**：
    * **Ceph BlueStore 与 CRimsonOS 的兼容性**： 讨论了将BlueStore移植到CRimsonOS的不同方案，包括代码修改、进程分离等，并分析了每种方案的优缺点。
    * **RocksDB 与 CRimsonOS 的兼容性**： 讨论了如何将RocksDB移植到CRimsonOS，并分析了可能遇到的问题。
    * **Ceph存储系统性能优化**： 讨论了如何优化Ceph存储系统的性能，包括I/O性能、内存使用率和网络带宽等。
    * **Ceph存储系统功能扩展**： 讨论了如何扩展Ceph存储系统的功能，例如支持新的存储介质、提供更多存储服务等。
* **讨论的主要议题**：
    * **Ceph BlueStore 与 CRimsonOS 的兼容性**： 包括方案一至四，以及它们各自的优势和劣势。
    * **RocksDB 与 CRimsonOS 的兼容性**： 讨论了移植过程中可能遇到的问题。
    * **Ceph存储系统性能优化**： 讨论了优化I/O性能、内存使用率和网络带宽等。
    * **Ceph存储系统功能扩展**： 讨论了支持新的存储介质和提供更多存储服务。
* **决定的事项**：
    * 继续讨论BlueStore与CRimsonOS的兼容性问题，并评估不同方案的可行性。
    * 将RocksDB移植到CRimsonOS，并分析移植过程中可能遇到的问题。
    * 优化Ceph存储系统的性能，并扩展其功能。
* **后续行动计划**：
    * 继续讨论BlueStore与CRimsonOS的兼容性问题。
    * 将RocksDB移植到CRimsonOS。
    * 优化Ceph存储系统的性能。
    * 扩展Ceph存储系统的功能。

**其他事项**：
* 讨论了Ceph存储系统与其他技术的兼容性。
* 讨论了Ceph存储系统的性能优化和功能扩展方案。

**关键词**：
* Ceph
* BlueStore
* CRimsonOS
* RocksDB
* 性能优化
* 稳定性提升
* 功能扩展
* 共享内存
* 命名空间
* 链接器魔法