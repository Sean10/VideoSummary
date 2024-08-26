---
title: "Ceph Performance Meeting 2021-07-22"
date: 2021-08-23
updated: 2021-08-24
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
会议讨论了本周Ceph项目中的多个Pull Requests (PRs)，包括新提交的和更新的PRs，以及一些关闭的PRs。会议还涉及了Ceph的性能改进、内存分配优化、以及对Ceph存储系统的未来发展方向的讨论。

#### 主要议题
1. **新PR和更新PRs**
   - 一个新的PR改变了vlog的工作方式，Kifu已批准并要求Sam进行审查。
   - Radic提交了一个有趣的PR，允许在Crimson中使用外来的存储（alien store），这可以用来测试mem store和file store。
   - 一个新的PR用于RGW跟踪，Matt已进行审查。
   - 针对c字符串转换的buffer list优化。
   - 一个PR改进了finisher线程的CPU占用，虽然有些争议，但Kifu和Kcr正在审查。

2. **关闭的PRs**
   - Ori从IBM提交的PRs中，一些已被合并，一些因问题未解决而关闭。
   - Adam关于改变Blue Store缓存行为的旧PR被stale bot关闭。

3. **性能和优化**
   - 讨论了在Crimson中实现multi-reactor的可能性，Greg Farnham将负责此项工作。
   - 讨论了Randy和Radic在mem store和buffer list优化方面的工作。

4. **RBD和客户端性能**
   - 讨论了RBD在kernel和user land客户端的性能问题，特别是与pnfs相关的讨论。
   - 探讨了改进用户空间客户端性能的可能性，包括改进FUSE代码或探索其他技术如Zuf。

#### 决定事项
- 继续推进multi-reactor的实现，以提高Ceph的性能。
- 继续审查和优化现有的PRs，特别是那些涉及性能和存储优化的PRs。
- 继续讨论和探索RBD客户端性能的改进方案。

#### 后续行动计划
- Greg Farnham将开始着手multi-reactor的实现工作。
- 继续审查和优化现有的PRs，确保它们符合项目的需求和标准。
- 继续讨论RBD客户端性能的改进方案，并寻求社区的反馈和建议。

#### 其他事项
- 会议还讨论了一些正在进行中的测试和未来的工作计划，包括对bidding code和blue fs的改进。

#### 会议结束
会议在讨论了所有议题后结束，与会者被鼓励继续工作并享受即将到来的周末。