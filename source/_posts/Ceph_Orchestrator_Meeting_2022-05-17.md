---
title: "Ceph Orchestrator Meeting 2022-05-17"
date: 2022-05-25
updated: 2022-05-26
tags:
categories:
- "视频总结"
subtitle: tech
---


会议纪要：

主题：讨论关于Ceph Rook与NFS操作的问题及后续行动计划

1. 问题描述：
   - 当Rook Orchestrator模块启用时，NFS操作失败。John Mulligan的工作允许NFS CLI在没有Orchestrator模块的情况下工作，但用户如果启用了Orchestrator模块，NFS命令将失败。

2. 当前状况和回归分析：
   - 在Pacific版本中，无论是否启用Orchestrator模块，NFS均可正常工作。但在Quincy版本中，只有在Orchestrator模块未启用时才能正常工作。
   - 可能是由于Quincy版本的回退(backport)未能完全实现，导致部分逻辑或异常处理代码缺失。

3. 讨论内容：
   - 提出可能的解决方案，包括从模块中移除某些逻辑并引发合适的异常，或者尝试修复问题。
   - 确认问题可能与Rook模块相关，需要检查该模块在Pacific和Quincy两个版本中的差异。
   - 讨论OpenStack使用情况下对稳定虚拟IP的需求，以及可能的解决方案。

4. 后续行动计划：
   - 检查并确认Rook NFS的回退情况，确保没有遗漏。
   - 验证不同版本的Rook模块中是否存在差异，特别是与NFS操作相关的代码块。
   - 考虑OpenStack环境下对NFS服务器的要求，评估是否需要采取特殊措施来处理客户端IP限制的情况。
   - 确定OpenStack发布时间线，以便相应地调整项目的优先级和计划。

5. 其他事项：
   - 讨论了功能请求，涉及为Ganesha提供非HA Proxy解决方案以提供稳定的虚拟IPs。
   - 强调了对OpenStack发布时间的了解对于项目计划的重要性。

会议结论：
   - 团队需要调查和解决Rook NFS操作中存在的问题，同时考虑OpenStack环境中的特殊需求。
   - 下一步行动包括检查代码差异、验证回退情况，并与OpenStack团队合作明确时间线和需求。
   - 下一次会议将在一周后举行，届时将继续讨论这些问题和进展。