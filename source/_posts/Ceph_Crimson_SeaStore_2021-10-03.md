---
title: "Ceph Crimson/SeaStore 2021-10-03"
date: 2021-11-04
updated: 2021-11-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 与会人员
- 主持人：未明确提及
- 参与者：未明确提及

#### 会议日期
- 2023年某月某日

#### 主要议题
1. **Ceph相关工作进展**
   - **Journal Badging PR for Young Gem**：已完成评审。
   - **C-Star Metadata PR for May**：正在进行中。
   - **Cache LRU**：工作被其他事务打断。
   - **Build问题**：测试受阻，需要进一步调查。
   - **性能测试结果差异**：不同构建选项对性能测试结果有影响，需要进一步验证。
   - **Make FS问题**：Ceph启动和停止正常，但使用特定命令启动OSD时出现问题。
   - **FSID问题**：讨论了FSID的设置和随机化问题。
   - **Spread LFS Strategy Work**：计划将工作合并到主分支，但上周因其他工作未能推进。
   - **Journal Committer Management**：修复了相关问题，并进行了性能测试。

#### 决定事项
- **Build问题**：需要进一步调查和解决。
- **性能测试结果差异**：需要验证不同构建选项对性能的影响。
- **Make FS问题**：需要进一步调查特定命令启动OSD的问题。
- **FSID问题**：决定在Ceph存储初始化时随机化FSID，避免写入零值。
- **Journal Committer Management**：决定合并相关PR，尽管在特定环境中存在性能问题。

#### 后续行动计划
- **Build问题**：继续调查并解决。
- **性能测试结果差异**：验证并分析不同构建选项的影响。
- **Make FS问题**：调查特定命令启动OSD的问题。
- **FSID问题**：在Ceph存储初始化时随机化FSID。
- **Spread LFS Strategy Work**：继续推进并将工作合并到主分支。
- **Journal Committer Management**：合并相关PR，并后续解决性能问题。

#### 其他
- 会议中提到了一些技术细节和具体代码问题，需要相关人员进一步跟进和处理。

#### 会议结束
- 会议在讨论完所有议题后结束，祝大家一周愉快。