---
title: "Optimizing Ceph IO for High Throughput Particle Physics Workflows"
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph存储系统在大型科学实验中的应用与优化

#### 会议时间：[具体日期]

#### 会议地点：[具体地点]

#### 主讲人：Tom

#### 参会人员：[参会人员名单]

#### 会议内容总结：

1. **主讲人介绍**：
   - Tom来自英国的科学与技术设施委员会（Science and Technologies Facilities Council, STFC），该组织运营大型科学资源，如粒子加速器、硬X射线源和脉冲激光等。
   - STFC旨在为学术界和商业用户提供免费的使用点访问，并参与UK Research and Innovation组织。

2. **公司背景**：
   - STFC的科学计算部门支持大量数据密集型科学研究。
   - 公司拥有近十万核心的OpenStack，用于构建科学分析工作流程，并在其后运行多种Ceph版本以支持这些工作流程。

3. **Ceph集群Echo介绍**：
   - Echo是STFC运行的最大的Ceph集群，已投入生产超过五年，从10PB增长到64.65PB。
   - 即将增加60PB的硬件，使其继续增长。
   - Echo主要为LHC实验提供磁盘存储，是英国对LHC的主要贡献。

4. **LHC和未来计划**：
   - LHC目前处于第三次运行阶段，正在进行探测器和磁铁升级。
   - 未来的高亮度LHC将显著增加碰撞记录和数据率。
   - 为准备这一变化，STFC正在进行各种数据挑战，以确保基础设施的各个部分都已准备就绪。

5. **Ceph集群Echo的优化**：
   - Echo使用XrootD作为数据传输框架，通过xrdCEPH和librados striper直接与Ceph集群交互。
   - 发现小读取性能问题，并通过缓存和其他优化措施进行缓解。
   - 最终通过优化xrdCEPH和librados striper，特别是移除锁定行为，显著提高了性能。

6. **后续行动计划**：
   - 继续探索和利用librados的其他高级功能，如异步操作和原子操作，以进一步优化性能。
   - 考虑在OSD级别实施校验和计算，以提高外部网关的效率。

#### 决定事项：
- 确认了Ceph集群Echo的性能优化措施，并计划进一步探索librados的高级功能。
- 决定继续监控和优化LHC实验的数据处理流程，以应对未来高亮度LHC的挑战。

#### 后续行动：
- 实施xrdCEPH和librados striper的优化版本，并监控其性能。
- 探索在OSD级别实施校验和计算的可能性。
- 继续参与LHC实验的数据挑战，确保基础设施的准备就绪。

#### 感谢人员：
- 感谢Joe Fish, Alexander, James等人在开发和实施优化措施中的关键贡献。

#### 会议结束：
- 会议在感谢和掌声中结束，准备进入下一个议程。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。