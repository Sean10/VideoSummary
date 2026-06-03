---
title: "Optimizing Ceph IO for High Throughput Particle Physics Workflows"
date: 2023-05-05
updated: 2023-05-05
tags:
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
会议纪要

### 会议主题：Ceph存储系统在大型科学实验中的应用与优化

#### 会议时间：[具体日期]

#### 会议地点：[具体地点]

#### 主讲人：Tom

#### 参会人员：[参会人员名单]

#### 会议内容总结：

1. **主讲人介绍**：
   - Tom来自英国的科学与技术设施委员会（STFC），负责设计和构建存储解决方案，支持设施用户和外部用户。

2. **STFC背景**：
   - STFC运营大型科学资源，支持大量数据密集型科学研究，并参与UK Research and Innovation组织。

3. **Ceph集群Echo介绍**：
   - Echo是STFC运行的最大的Ceph集群，已投入生产超过五年，从10PB增长到64.65PB，主要用于LHC实验的磁盘存储。
   - Echo使用XrootD作为数据传输框架，通过xrdCEPH和librados striper与Ceph集群交互。

4. **Ceph集群Echo的优化**：
   - 发现小读取性能问题，并通过缓存和其他优化措施进行缓解。
   - 通过优化xrdCEPH和librados striper，特别是移除锁定行为，显著提高了性能。

5. **后续行动计划**：
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