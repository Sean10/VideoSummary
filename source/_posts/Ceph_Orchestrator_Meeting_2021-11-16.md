---
title: "Ceph Orchestrator Meeting 2021-11-16"
date: 2021-11-17
updated: 2021-11-17
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
- **会议主题**: 协调器会议
- **日期**: [具体日期]
- **参会人员**: [参会人员名单]
- **主持人**: [主持人姓名]

#### 主要议题
1. **Cephalocon 的 CFP（Call for Papers）**
   - CFP 截止日期为12月10日。
   - 鼓励团队成员提交演讲提案，特别是关于安全性和NSF ADM文档的内容。
   - 讨论了是否需要为不同的开发领域（如FDM、Flu Culture系统等）设置专门的会议环节。

2. **大型集群部署计划**
   - 计划在澳大利亚珀斯的Poise超级计算中心部署大规模的SF ADM集群。
   - 讨论了如何有效组织和利用时间，避免在部署过程中浪费时间。
   - 提出了使用IRC或Matrix作为通信渠道，以确保信息的连续性和可访问性。

3. **集群测试和资源利用**
   - 讨论了如何优化集群的测试和资源利用，包括重用现有集群和有效管理NVMe设备。
   - 确认了Patrick已经对self-FFS进行了研究，并期待其他组件也能利用这一集群。

4. **技术细节和改进**
   - 讨论了从runC切换到crun以改善上游生育测试中的组错误问题。
   - 确认了Sage已经提交了相关的PR，并期待这一改变能带来更稳定的运行环境。

#### 决定事项
- 将向Cephalocon组织者提出建议，为不同的开发领域设置专门的会议环节。
- 确认使用Matrix作为通信渠道，以替代传统的IRC。
- 确认了集群部署和测试的具体计划，包括重用现有集群和优化资源利用。
- 确认了技术改进的方向，特别是从runC切换到crun。

#### 后续行动计划
- 向Cephalocon组织者提出建议，设置专门的会议环节。
- 确认并实施使用Matrix作为通信渠道。
- 继续推进大型集群的部署和测试工作，确保资源的有效利用。
- 实施从runC到crun的技术切换，并更新相关文档。

#### 下次会议
- **日期**: 下周二
- **地点**: [会议链接或地点]

#### 会议结束
- **时间**: [具体结束时间]
- **备注**: 无其他议题

---

**会议记录人**: [记录人姓名]
**审核人**: [审核人姓名]