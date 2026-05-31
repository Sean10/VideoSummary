---
categories:
- 视频总结
date: 2023-04-12
subtitle: Ceph_Crimson_SeaStar-OSD_2023-04-12_Meeting
tags:
- Ceph
title: Ceph Crimson/SeaStar-OSD 2023-04-12 Meeting
updated: 2023-04-12
---



### 会议纪要

#### 参会人员
- Ceph开发和质量保证（QE）团队成员。

#### 主要议题
1. **Crimson项目进展**
   - 讨论了将Classic Q Quality Service工作移植到Crimson的计划。
   - 探讨了LBA优化和parent-child link优化，提出后续改进的可能性。

2. **RBD测试结果**
   - QE团队在RBD测试中发现了五个失败案例，其中两个确认为误报。
   - 计划进一步调查其余失败案例，并可能提出新的bug报告。

3. **系统调试与更新**
   - 更新了医疗系统，并在垂直OST上进行调试，特别是单个和多个OSD的调试。

4. **会议安排**
   - 下一周的会议将照常进行，之后可能会切换到新的会议软件。

#### 决定事项
- 确认将Classic Q Quality Service工作移植到Crimson。
- 对RBD测试中的失败案例进行初步分析，并计划进一步讨论和调查。
- 确认下一周的会议将继续使用当前的会议软件。

#### 后续行动计划
- 继续进行LBA优化和parent-child link优化的工作。
- QE团队将调查RBD测试中的失败案例，并根据讨论结果决定是否提出新的bug报告。
- 调试和更新医疗系统，确保其稳定运行。
- 准备切换到新的会议软件，并提前通知参会人员。

#### 备注
- 会议中提到了技术细节，如LBA优化、parent-child link优化等，这些是Ceph存储系统中的关键技术点。
- 会议还涉及了RBD（RADOS Block Device）的测试，这是Ceph提供的一种块存储服务。

#### 会议结束
- 会议在确认了后续行动计划和会议安排后结束。