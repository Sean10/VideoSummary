---
title: "Ceph Orchestrator Meeting 2022-01-18"
date: 2022-01-18
updated: 2022-01-19
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **Quincy 版本发布**: Quincy 版本即将发布，但并非迫在眉睫。团队需要确保对 Quincy 的回溯（backporting）工作得到妥善处理，特别是对于每个 bug 修复和功能更新。
- **回溯策略**: 会议讨论了回溯工作的策略，建议采用批量回溯（batch backports）以减少额外工作量和冲突。团队成员普遍支持这一策略。
- **Pacific 版本的回溯**: 针对 Pacific 版本的回溯工作仍在进行中，特别是需要将 agent 回溯到 Pacific。团队需要尽快解决剩余的两个问题，并加速完成回溯工作。
- **Surf Loop 中的竞争条件**: 讨论了 Surf Loop 中存在的竞争条件，特别是在不同线程中修改数据结构时可能引发的问题。团队成员 Mike 提出了一些初步的调查结果和可能的解决方案。
- **Agent 和数据一致性**: 讨论了如何通过 agent 和 metadata up-to-date flag 来解决数据一致性问题，特别是在处理同步操作时。
- **线程和超时问题**: 讨论了线程管理和超时问题，特别是在执行 SSH 命令时可能出现的挂起问题。提出了引入超时机制和健康警告的建议。
- **团队变动**: Sebastian 宣布他将在一月底离开 Red Hat，这将是他参与的倒数第二次会议。

#### 决定事项
- **回溯策略**: 决定采用批量回溯策略，避免单独回溯带来的额外工作量和冲突。
- **Pacific 版本的回溯**: 确认需要尽快解决剩余的两个问题，并加速完成对 Pacific 版本的回溯工作。
- **Surf Loop 中的竞争条件**: 需要进一步调查和解决 Surf Loop 中的竞争条件，特别是在不同线程中修改数据结构时可能引发的问题。
- **Agent 和数据一致性**: 确认通过 agent 和 metadata up-to-date flag 来解决数据一致性问题，特别是在处理同步操作时。
- **线程和超时问题**: 确认引入超时机制和健康警告，以解决执行 SSH 命令时可能出现的挂起问题。

#### 后续行动计划
- **Quincy 版本的回溯**: 确保对 Quincy 的回溯工作得到妥善处理，特别是对于每个 bug 修复和功能更新。
- **Pacific 版本的回溯**: 尽快解决剩余的两个问题，并加速完成对 Pacific 版本的回溯工作。
- **Surf Loop 中的竞争条件**: 进一步调查和解决 Surf Loop 中的竞争条件，特别是在不同线程中修改数据结构时可能引发的问题。
- **Agent 和数据一致性**: 实施通过 agent 和 metadata up-to-date flag 来解决数据一致性问题的方案。
- **线程和超时问题**: 引入超时机制和健康警告，以解决执行 SSH 命令时可能出现的挂起问题。
- **团队变动**: 确认 Adam 将接手 Orchestrator 每周会议的主持工作。

#### 其他事项
- **Docker 镜像缓存**: 讨论了 Docker 镜像缓存的问题，特别是关于 upstream CI 的镜像缓存和 OpenStack 团队的需求。

### 会议结束
- 会议在确认了各项议题的后续行动计划后结束，团队成员预祝大家有一个愉快的周末。