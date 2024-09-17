---
title: "CDS G/H (Day 2) - CephFS: forward scrub"
date: 2014-06-26
updated: 2014-06-26
tags:
categories:
- "视频总结"
subtitle: tech
---



**会议纪要**

**会议主题**： 分布式存储Ceph文件系统一致性检查系统（forward scrub）方案讨论

**会议时间**： 2023年11月某日

**参会人员**：  （此处应列出参会人员名单）

**会议内容**：

* **议题背景**：
    * 会议讨论了Ceph文件系统一致性检查系统（forward scrub）的方案，该方案旨在确保文件系统的数据一致性。
    * 该方案分为两部分：第一部分是forward scrub，从文件系统的根节点开始，向下检查所有文件和目录的一致性；第二部分是反向检查，检查所有rados pool中的对象是否与文件系统相关联。

* **forward scrub方案细节**：
    * forward scrub将创建一个独立的scrub线程，运行在MJS（Metadata Server）上。
    * scrub线程从scrub iode函数开始，维护一个inode栈，用于记录需要检查的inode。
    * scrub node函数会检查inode，如果是文件，则检查其元数据一致性；如果是目录，则检查目录内容与元数据的一致性。
    * 对于远程inode（硬链接），需要验证其存在性和链接计数正确性。
    * scrub过程中，会对inode设置scrub start stamp和scrub start version，用于记录scrub的开始时间和版本。
    * scrub完成后，会标记scrub finish，并记录scrub结束时间和版本。

* **讨论要点**：
    * scrub过程中如何处理远程inode的链接计数问题。
    * 是否有必要在内存中设置scrub start stamp和scrub start version。
    * 是否可以将scrub分为阻塞和非阻塞两种模式。
    * 是否可以将scrub分为不同的级别，例如快速内存scrub和完整文件scrub。

* **行动计划**：
    * 进一步完善forward scrub方案，包括处理远程inode链接计数问题和scrub级别划分。
    * 制定详细的技术方案和实施计划。
    * 在Ceph社区中讨论和评估该方案。

**关键词**： forward scrub, distributed SE FS, consistency check, scrub thread, MJS, inode, metadata, rados pool, object, link count, scrub start stamp, scrub start version, scrub finish, block, non-block, scrub level