---
title: "Ceph Performance Meeting 2021-06-10"
date: 2021-06-10
updated: 2021-06-11
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph性能对比分析及问题讨论

#### 参会人员：Mark（缺席）、其他相关人员

#### 会议时间：待定

#### 主要议题：
1. **Ceph性能对比分析**：
   - 对比了Nautilus和Pacific版本在RGW工作负载下的性能。
   - 使用了两种不同的工作负载：一种是主要针对较小对象（1KB至256KB）的cost bench，另一种是混合了小对象和大对象（最大1GB）的gauss bench。
   - 发现Pacific在处理小对象工作负载时性能优于Nautilus，但在处理混合对象工作负载时性能不如Nautilus。

2. **问题分析与讨论**：
   - **OSD内存目标设置问题**：
     - 在Pacific版本中，OSD内存目标（OSD memory target）未被任何部署方法覆盖，特别是cephadm目前无法覆盖OSD内存目标。
     - Nautilus版本中，OSD内存目标应根据主机内存自动计算，但实际上实验中使用的内存远低于预期。
   - **TC Malloc环境变量设置问题**：
     - 讨论了TC Malloc环境变量（PC Malloc Max Total Thread Cache Bytes）的设置问题，发现即使在Nautilus中，该变量也未正确设置。
     - 提出了两个相关的PR（Pull Request）来解决这个问题，一个是全局设置，另一个是通过优先级缓存管理器设置。

3. **后续行动计划**：
   - 重新进行实验以验证结果，特别是Nautilus版本的实验。
   - 确保TC Malloc环境变量正确设置，并考虑是否需要动态调整。
   - 讨论是否将相关更改回溯到Pacific版本。

#### 其他讨论：
- Mark原计划讨论RBD测试和RGW的MTP使用情况，但由于缺席，推迟到下次会议。
- 确认了TC Malloc的灵活性，并讨论了动态调整的可能性。

#### 后续会议：
- 下次会议将继续讨论RBD测试和RGW的MTP使用情况。
- 确认是否有其他议题需要讨论。

#### 会议结束：
- 会议在无其他议题讨论的情况下结束，感谢所有参与者的贡献。

---

**备注**：会议中提到的关键术语和工具包括：
- **Ceph**：分布式存储系统。
- **RGW**：Ceph的对象网关。
- **OSD**：Object Storage Daemon，Ceph的存储守护进程。
- **TC Malloc**：线程缓存malloc，一种内存分配器。
- **cephadm**：Ceph的部署和管理工具。
- **PR**：Pull Request，代码贡献的一种形式。

**行动项**：
- 重新进行Nautilus版本的实验。
- 确保TC Malloc环境变量正确设置。
- 考虑回溯相关更改到Pacific版本。
- 动态调整TC Malloc设置的可能性。