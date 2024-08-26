---
title: "Ceph Developer Summit Quincy: CephFS Follow-up"
date: 2021-04-28
updated: 2021-04-29
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题
本次会议主要讨论了Ceph项目的上游Trello backlog board，并计划了即将到来的Quincy版本的工作内容。

#### 会议链接
会议中提供了Trello board和Quincy feature search的链接，确保所有参与者都能访问相关资源。

#### 主要议题及讨论内容
1. **Multi-MDS Export Thrashing**
   - PR已准备好，但因MDS相关问题导致测试失败，需先解决该问题。
   - 该PR已被标记为Quincy版本的工作内容。

2. **MDS Check for Mixed Versions**
   - 讨论了是否需要对MDS demons版本不匹配的情况发出健康警告。
   - 决定继续跟踪此问题，并计划在Quincy版本中解决。

3. **Threshing Fragments**
   - 需要重新基于最新代码进行调整，并进行审查。
   - 该问题也被标记为Quincy版本的工作内容。

4. **MDS Memory Target**
   - 由于当前方法不满足需求，正在考虑采用优先级缓存方法。
   - 该问题将在后续讨论中进一步探讨。

5. **Client Complete Support for Lazy IO**
   - 讨论了Lazy IO的实际需求和实现难度，最终决定不将其作为Quincy版本的工作内容。

6. **Root Squash via MDS Capability**
   - 该功能已在Pacific版本中实现，因此从Quincy版本的工作内容中移除。

7. **HSM Support**
   - 由于缺乏下游需求，决定不将其作为Quincy版本的工作内容。

8. **Optimized Rsync**
   - 由于CephFS Mirror的存在，决定关闭此优化需求。

9. **Multi-FS Shared Pools**
   - 由于技术限制和需求变化，决定关闭此需求。

10. **Snapshots File Level Snapshots**
    - 讨论了文件级快照的技术挑战和实际需求，决定暂时不作为Quincy版本的工作内容。

11. **Background Fored Scrub Scheduling**
    - 需要创建相关跟踪票并找到负责人，计划在Quincy版本中实现。

12. **FFS Notify Support**
    - 讨论了在VFS层实现通知支持的难度，决定暂时不作为Quincy版本的工作内容。

13. **MDS Star**
    - 由于需要大规模重写MDS，决定暂时不作为Quincy版本的工作内容。

14. **Libs FFS PP**
    - 讨论了将C API与C++ API分离的需求，决定暂时不作为Quincy版本的工作内容。

15. **Ceph Top MultiFS Support**
    - 需要改进mgr stats模块以支持多文件系统，计划在Quincy版本中实现。

16. **Recursive Unlink RPC**
    - 计划在Quincy版本中实现。

17. **AHA Support**
    - 计划在Quincy版本中实现。

18. **SFS Cache**
    - 等待内核补丁的进展，计划在Quincy版本中实现。

19. **Client Expose Auth MDS for Fileder**
    - 讨论了在客户端暴露权威MDS的需求，决定暂时不作为Quincy版本的工作内容。

#### 后续行动计划
- 继续跟踪和更新Trello board，确保所有工作内容和进度得到准确反映。
- 对于标记为Quincy版本的工作内容，需尽快找到负责人并开始实施。
- 对于暂时不作为Quincy版本的工作内容，将继续在backlog中跟踪，等待合适的时机再进行处理。

#### 会议总结
本次会议对Ceph项目的多个关键议题进行了深入讨论，并制定了相应的行动计划。通过Trello board的持续更新和跟踪，确保项目按计划推进，并为即将到来的Quincy版本做好充分准备。