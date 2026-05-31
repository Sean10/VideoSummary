---
categories:
- 会议纪要
date: 2014-10-30
subtitle: CephFS forward scrub 方案讨论会议总结
tags:
- CephFS
- 分布式存储
title: "'CDS G/H (Day 2) - CephFS: forward scrub'"
updated: 2014-10-30
---




**会议纪要**

**会议主题**： CephFS文件系统一致性检查系统（forward scrub）方案讨论

**会议时间**： 2023年11月某日

**参会人员**： （此处应列出参会人员名单）

**会议内容**：

* **议题背景**：
    会议重点讨论了Ceph文件系统一致性检查系统中的forward scrub方案，此方案旨在确保文件系统的数据一致性。该方案分为两部分：forward scrub和反向检查。forward scrub从文件系统的根节点开始，向下检查所有文件和目录的一致性；反向检查则检查所有rados pool中的对象是否与文件系统相关联。
* **forward scrub方案细节**：
    - forward scrub将在MJS（Metadata Server）上创建一个独立的scrub线程。
    - scrub线程从scrub iode函数开始，维护一个inode栈，记录需要检查的inode。
    - scrub node函数将检查inode，如果是文件，则检查其元数据一致性；如果是目录，则检查目录内容与元数据的一致性。
    - 对于远程inode（硬链接），需要验证其存在性和链接计数正确性。
    - scrub过程中，会对inode设置scrub start stamp和scrub start version，记录scrub的开始时间和版本。
    - scrub完成后，会标记scrub finish，并记录scrub结束时间和版本。
* **讨论要点**：
    - 如何处理远程inode的链接计数问题。
    - 是否有必要在内存中设置scrub start stamp和scrub start version。
    - 是否可以将scrub分为阻塞和非阻塞两种模式。
    - 是否可以将scrub分为不同的级别，例如快速内存scrub和完整文件scrub。
* **行动计划**：
    - 进一步完善forward scrub方案，包括处理远程inode链接计数问题和scrub级别划分。
    - 制定详细的技术方案和实施计划。
    - 在Ceph社区中讨论和评估该方案。

**关键词**： CephFS, forward scrub, distributed storage, consistency check, scrub thread, MJS, inode, metadata, rados pool, object, link count, scrub start stamp, scrub start version, scrub finish, block, non-block, scrub level