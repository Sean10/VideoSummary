---
title: "2020-03-31 :: Ceph Crimson Meeting"
date: 2020-04-03
updated: 2020-04-04
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 参会人员
- Jeremy（因病缺席）
- John
- Scott
- Adam
- Radek
- Josh Anderson

#### 主要议题
1. **Ceph项目进展**
   - **John**：上周主要忙于处理Ceph以外的任务，本周将重点关注Ceph相关工作，特别是关于CRUSH map的更新和同步。
   - **Scott**：上周根据John和Mark的反馈，对Ceph版本请求进行了大量修改，并解决了CNS路径调试问题。已提交PR修复CSO测试问题，并计划在本地测试通过后合并到主分支。
   - **Adam**：上周忙于处理DCM相关工作，本周回归Ceph，已提交多个PR，包括修复回归问题和改进代码结构。还讨论了增加单元测试以避免对象类问题，并建议引入新的测试标签。
   - **Radek**：正在完成状态机的工作，希望在一周内完成初步版本。还讨论了改进PR以在失败时重新读取对象状态，并考虑降低复制成本的问题。
   - **Josh Anderson**：上周调试了PG log based recovery代码，手动测试已通过，正在添加更多测试用例。

2. **项目管理与组织**
   - 讨论了将现有项目卡片迁移到Carrillo，并按不同类别和里程碑进行组织，以提高项目管理的可见性和效率。
   - 建议引入更短的里程碑，以便更好地跟踪进度。

#### 决定事项
- 将现有项目卡片迁移到Carrillo，并按类别和里程碑进行组织。
- 引入新的测试标签，以便更灵活地运行特定测试。

#### 后续行动计划
- **John**：继续处理CRUSH map的更新和同步。
- **Scott**：本地测试PR并合并到主分支。
- **Adam**：继续处理回归问题，并增加单元测试。
- **Radek**：完成状态机工作，并改进PR。
- **Josh Anderson**：提交PG log based recovery的PR。
- **项目管理**：迁移项目卡片到Carrillo，并按计划进行组织和跟踪。

#### 其他事项
- 讨论了代码复制的性能问题，并计划后续进行优化。
- 确认了会议的音频问题已解决。

#### 下次会议
- 下周同一时间进行。

### 会议结束
- 感谢大家的参与，祝大家有个愉快的一天/夜晚。