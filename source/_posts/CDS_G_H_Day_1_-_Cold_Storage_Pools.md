---
title: "CDS G/H (Day 1) - Cold Storage Pools"
date: 2014-06-24
updated: 2014-06-25
tags:
categories:
- "视频总结"
subtitle: tech
---



### 会议纪要

**会议主题**： 冷存储池讨论

**参会人员**： Roger Weeks（HGST），Samuel Saguy，以及其他未具名参与者

**会议内容**：

* **背景**： 
    * 讨论如何实现一个存储池，其中的数据可以被写入且几乎不会进行重平衡或重写，或者重写非常不频繁。
    * 旨在为冷存储提供解决方案，即介于磁带和活跃访问数据之间的存储层。
    * 目标是提高数据访问速度，同时减少数据移动和存储成本。
* **主要议题**：
    * 如何实现数据在写入后几乎不会移动？
    * 如何平衡数据移动和冗余性？
    * 如何实现高效的数据访问？
* **讨论要点**：
    * **冷存储池**： 将冷数据存储在一个独立的池中，并使用特定的策略来管理数据移动和冗余性。
    * **PG温映射**： 使用PG温映射来限制数据移动，并确保数据在写入后几乎不会移动。
    * **PG强制映射**： 为管理员提供一个工具，可以强制将PG映射到特定的位置，从而实现更精细的控制。
    * **Silo架构**： 将存储部署为多个独立的池，每个池用于存储特定类型的数据。
    * **缓存层**： 使用缓存层来缓冲数据，并减少对冷存储的访问频率。
    * **RAID方法**： 使用RAID方法来提高数据冗余性，并实现更静态的数据映射。
* **决定事项**：
    * 探索使用PG温映射和PG强制映射来实现数据几乎不会移动。
    * 考虑使用Silo架构来存储不同类型的数据。
    * 研究使用缓存层来减少对冷存储的访问频率。
    * 考虑使用RAID方法来提高数据冗余性。
* **后续行动计划**：
    * Roger将撰写有关冷存储池的详细文档。
    * 团队将研究不同的实现方案，并选择最适合Ceph的方案。
    * 团队将与其他Ceph社区成员合作，以推动冷存储池的实现。

**关键术语**：

* 冷存储
* 数据移动
* 冗余性
* PG温映射
* PG强制映射
* Silo架构
* 缓存层
* RAID方法