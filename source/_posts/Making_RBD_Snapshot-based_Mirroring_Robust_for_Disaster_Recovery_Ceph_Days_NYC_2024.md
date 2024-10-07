---
title: "Making RBD Snapshot-based Mirroring Robust for Disaster Recovery | Ceph Days NYC 2024"
date: 2024-06-18
updated: 2024-06-18
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：RBD快照基础镜像功能的改进与灾难恢复解决方案

#### 主讲人：Raman Raja，IBM软件工程师

#### 会议内容概述：
Raman Raja介绍了RBD（RADOS Block Device）快照基础镜像功能的最新改进，旨在使其更加健壮，适用于灾难恢复场景。他首先概述了RBD镜像功能，然后详细讨论了如何设置、整体架构、以及在严格测试中发现的快照基础镜像功能的缺陷和解决方案。

#### 主要讨论点：
1. **RBD镜像功能概述**：
   - RBD镜像功能包括异步复制图像，由RBD镜像守护进程执行。
   - 支持两种模式：日志基础镜像和快照基础镜像。
   - 快照基础镜像模式下，在主图像上拍摄崩溃一致的镜像快照，镜像守护进程识别数据和元数据变化，并复制快照增量到非主图像。

2. **架构与配置**：
   - 支持单向和双向复制配置，便于故障切换和故障恢复协调。
   - 使用SEF orchestrator（如SEF ADM或Rook）启动RBD镜像守护进程，配置RBD池和图像进行镜像。

3. **故障切换与恢复**：
   - 计划故障切换时，先降级主图像，创建降级快照，同步到非主图像，然后提升非主图像。
   - 非计划故障切换时，强制提升非主图像，如果数据未完全同步，图像回滚到完全同步的快照。

4. **灾难恢复解决方案**：
   - 针对Kubernetes工作负载，使用RBD作为存储后端，实现跨区域的数据恢复，确保业务需求在几分钟内恢复。
   - 解决方案涉及三个Kubernetes集群，包括一个Hub集群和两个管理集群，通过ramen Hub操作符自动化管理。

5. **测试中发现的问题与修复**：
   - 发现并修复了快照对象映射不正确导致的数据损坏问题。
   - 解决了镜像快照调度器客户端被krbd客户端错误阻止的问题。
   - 改进了在高延迟环境下镜像守护进程的行为。

6. **未来工作**：
   - 支持镜像组和RBD克隆的镜像。
   - 优化强制提升时的数据同步效率。

#### 决定事项：
- RBD快照基础镜像功能已进行多项改进，提高了灾难恢复场景下的健壮性。
- 继续开发镜像组和RBD克隆的镜像支持。

#### 后续行动计划：
- 继续测试和优化RBD快照基础镜像功能。
- 完成镜像组和RBD克隆的镜像支持开发。

#### 致谢：
- 感谢Ilia和Sham作为RBD和ramen操作符的维护者。

#### 结束语：
Raman Raja感谢大家的参与和贡献，并期待未来的进一步合作和改进。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。