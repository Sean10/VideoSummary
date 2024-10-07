---
title: "Ceph Orchestrator Meeting 2022-06-28"
date: 2022-06-28
updated: 2022-06-29
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**日期：** 2023年6月28日

**参会人员：** [参会人员名单]

**主要议题：**
1. **Ceph编译更新（compiles fdm1）**
   - **问题描述：** e2e仪表板测试持续失败，但未发现与当前变更直接相关的联系。
   - **当前状态：** 新日志行出现在日志输出中，表明Cepheum正在被测试。
   - **行动建议：** 继续重新运行测试，观察是否为间歇性问题。

2. **NFS相关问题**
   - **问题描述：** NFS测试失败，可能与最近容器设置的变更有关。
   - **行动建议：** 关注NFS相关问题，等待容器问题解决后再次测试。

3. **API测试问题**
   - **当前状态：** API测试已重启并通过。
   - **后续行动：** 继续关注其他潜在的失败测试。

4. **OpenStack团队需求**
   - **需求描述：** OpenStack团队提出了关于NFS设置的需求。
   - **行动建议：** 评估并实施相关需求，重点关注独立部署的维护。

5. **监控和安全更新**
   - **当前状态：** 监控堆栈的安全特性已准备好，等待其他变更请求（VR）合并后进行测试。
   - **后续行动：** 替换并审查相关变更，进行进一步测试。

6. **一致性哈希与随机分布**
   - **当前状态：** 正在重新启用并测试FDM调度器的随机分布支持。
   - **后续行动：** 继续测试并评估其在实际环境中的性能。

**决定事项：**
- 继续监控和重新运行Ceph编译及相关测试，以确定问题的稳定性。
- 关注并解决NFS相关问题，确保其稳定性。
- 实施OpenStack团队的NFS设置需求。
- 完成监控堆栈的安全特性更新，并进行全面测试。
- 测试并优化FDM调度器的随机分布支持。

**后续行动计划：**
- 持续关注测试结果，及时调整和优化相关配置。
- 与OpenStack团队保持沟通，确保需求的准确实施。
- 完成所有安全特性的测试，并准备发布。
- 评估并优化一致性哈希与随机分布的实现。

**会议结束：**
- 会议于[具体时间]结束，无其他重大议题讨论。

**备注：**
- 请相关人员关注并执行上述行动计划，确保项目进度和质量。

**下次会议预告：**
- 下次会议时间：[具体日期和时间]
- 主要议题：[预定的讨论内容]

**会议记录人：** [记录人姓名]

**会议结束语：**
- 感谢大家的参与和贡献，祝大家工作顺利，再见。