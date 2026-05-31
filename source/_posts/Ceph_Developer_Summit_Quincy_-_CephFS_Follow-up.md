---
categories:
- 视频总结
date: 2021-04-28
subtitle: Ceph开发者峰会Quincy：CephFS跟进
tags:
- CephFS
title: "'Ceph Developer Summit Quincy: CephFS Follow-up'"
updated: 2021-04-29
---



Ceph开发者峰会的Quincy版本跟进会议主要讨论了CephFS项目的上游Trello backlog board，并规划了即将到来的Quincy版本的工作内容。

**会议要点**：

* **Trello Backlog**: 会议回顾了Trello backlog中的各项任务，包括多MDS导出冲突、MDS版本检查、碎片处理、MDS内存目标等。
* **Quincy版本工作内容**： 
    * 多MDS导出冲突的PR因MDS相关问题失败，需要先解决MDS问题。
    * MDS版本检查将发出健康警告，继续跟踪此问题。
    * 碎片处理需要基于最新代码进行调整，并进行审查。
    * MDS内存目标考虑采用优先级缓存方法。
    * 客户端Lazy IO支持因实现难度和需求不明确，决定不作为Quincy版本的工作内容。
    * Root Squash via MDS Capability已在Pacific版本中实现。
    * HSM Support因缺乏下游需求，决定不作为Quincy版本的工作内容。
    * Optimized Rsync因CephFS Mirror的存在，决定关闭此优化需求。
    * Multi-FS Shared Pools因技术限制和需求变化，决定关闭此需求。
    * Snapshots File Level Snapshots因技术挑战和实际需求，决定暂时不作为Quincy版本的工作内容。
    * Background Fored Scrub Scheduling计划在Quincy版本中实现。
    * CephFS Notify Support因在VFS层实现通知支持的难度，决定暂时不作为Quincy版本的工作内容。
    * MDS Star因需要大规模重写MDS，决定暂时不作为Quincy版本的工作内容。
    * Libs CephFS PP因C API与C++ API分离的需求，决定暂时不作为Quincy版本的工作内容。
    * Ceph Top MultiFS Support需改进mgr stats模块以支持多文件系统，计划在Quincy版本中实现。
    * Recursive Unlink RPC计划在Quincy版本中实现。
    * AHA Support计划在Quincy版本中实现。
    * CephFS Cache等待内核补丁的进展，计划在Quincy版本中实现。
    * Client Expose Auth MDS for Fileder讨论了在客户端暴露权威MDS的需求，决定暂时不作为Quincy版本的工作内容。
* **后续行动计划**： 
    * 继续跟踪和更新Trello board，确保所有工作内容和进度得到准确反映。
    * 对于标记为Quincy版本的工作内容，需尽快找到负责人并开始实施。
    * 对于暂时不作为Quincy版本的工作内容，将继续在backlog中跟踪，等待合适的时机再进行处理。

**关键词**： CephFS, Quincy版本, Trello Backlog, 开发者会议, Ceph生态系统