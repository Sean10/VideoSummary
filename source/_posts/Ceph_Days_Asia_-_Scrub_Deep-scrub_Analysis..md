---
title: Ceph Days Asia- Scrub / Deep-scrub Analysis.
date: 2024-11-05
updated: 2024-11-06
tags:
- Ceph
- 分布式存储
categories: 
- "视频总结"
subtitle: Ceph_Days_Asia_-_Scrub_Deep-scrub_Analysis.
---

### 会议纪要

#### 会议主题：Ceph存储系统中的scrub和deep scrub机制及优化策略

#### 会议时间：[具体日期]

#### 会议地点：[具体地点]

#### 参会人员：Jae-min Jae-min（三星SDS）、Chaplain、Jeong Soon-Yong等

#### 会议内容总结：

1. **公司介绍**：
   - 三星SDS是三星集团内的IT服务公司，主要负责创建和运营数据系统。
   - 公司拥有两个主要平台：SCP（类似AWS）和Cello Square（现称为Diro Service）。
   - 公司在全球40个国家设有58个分支机构和18个数据中心，服务于众多国际和国内客户。

2. **scrub和deep scrub概念介绍**：
   - **scrub**：检查和比较元数据区域，确保数据的完整性和一致性。
   - **deep scrub**：在块级别进行更深入的检查，验证数据的存在和复制数量。

3. **scrub和deep scrub的重要性**：
   - 预防因磁盘故障、软件损坏、服务器故障等问题导致的数据完整性受损。
   - 通过定期执行scrub和deep scrub，可以在问题变得严重之前识别并解决。

4. **测试结果展示**：
   - 测试环境：Ceph集群包含六个主机，每个主机上部署了多个OSD、mgr和MON。
   - 测试配置：调整了OSD Max Scrubs、OSD Scrub Load Threshold等参数。
   - 测试结果：增加scrub和deep scrub的数量和大小会导致客户端IO性能下降，执行时间延长。

5. **优化策略讨论**：
   - **减少scrub运行次数**：通过调整OSD scrub lander's race和OSD scrub load tread值。
   - **降低scrub性能**：减少OSD scrub chunk max size和OSD scrub stride值。
   - **调整scrub执行频率**：通过增加OSD Scrum Max Interval和OSD Scrum Sleep值。
   - **基于集群状态和环境优化**：根据集群负载、数据故障率和操作时间进行调整。

6. **Ceph配置和代码分析**：
   - 分析了OSD Deep Scrub Randomizer Ratio和OSD Scrub Load Threshold的配置和代码实现。
   - 讨论了配置设置与实际执行之间的差异，以及如何通过代码调整来优化scrub和deep scrub的执行。

7. **后续行动计划**：
   - 继续优化scrub和deep scrub的配置，确保数据完整性和性能平衡。
   - 开发工具和脚本，以便更有效地管理和监控scrub和deep scrub的执行。
   - 分享测试结果和优化策略，帮助其他集群进行类似的优化。

#### 会议结论：
- scrub和deep scrub是确保Ceph存储系统数据完整性的关键任务，但它们对客户端性能有显著影响。
- 需要根据集群的具体状态和环境，不断优化scrub和deep scrub的设置和执行策略。
- 三星SDS将继续研究和分享相关优化策略，帮助用户更好地管理和优化其Ceph存储系统。

#### 后续行动：
- 继续监控和调整scrub和deep scrub的配置。
- 开发和分享更多的工具和脚本，以便用户更有效地管理scrub和deep scrub。
- 定期回顾和更新优化策略，确保其适应不断变化的集群环境和需求。



以上是本次会议的详细纪要，涵盖了会议的主要议题、讨论内容、决定的事项以及后续的行动计划。希望这些信息对您有所帮助。