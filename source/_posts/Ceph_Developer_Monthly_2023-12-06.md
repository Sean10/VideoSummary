---
title: "Ceph Developer Monthly 2023-12-06"
date: 2023-12-13
updated: 2023-12-14
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议主题：** Ceph Manager模块加载问题讨论

**参会人员：** Ilia, Gas, Ramina, Radic, Patrick, Travis

**会议时间：** [未提供具体时间]

**会议地点：** 视频会议

**会议内容总结：**

1. **问题描述：**
   - 当Ceph Manager启动时，所有Manager模块类会被加载，命令会被发现。命令的发现和命令注册的过程是分开的，从加载模块到启动解释器的过程是异步的。
   - 当Manager接收到一个命令时，虽然知道命令存在，但模块可能尚未加载完成，导致错误。

2. **讨论议题：**
   - **错误处理：** 讨论了客户端在Manager模块未完全加载时接收到的错误信息，以及如何处理这些错误。
   - **模块加载同步性：** 讨论了是否应该让模块加载过程同步，并在模块完全加载后再执行相关命令。
   - **可用性标志（available flag）：** 讨论了Manager Map中的可用性标志的实际意义和如何改进其使用。

3. **决定事项：**
   - **模块加载策略：** 决定重新审视Mola的修复方案，考虑在Manager响应后异步加载Python模块，并延迟设置可用性标志，直到所有模块加载完成。
   - **客户端等待机制：** 决定客户端在执行命令前应检查模块是否真正可用，并在Manager Map中等待可用状态。

4. **后续行动计划：**
   - **实施细节讨论：** 需要进一步讨论具体的实施细节，包括是否修复现有的可用性标志或添加新的标志。
   - **征求反馈：** 需要将讨论结果总结并征求Patrick和Travis的反馈，特别是关于Manager Map的使用和外部用户的兼容性问题。
   - **文档更新：** 需要更新文档，明确Manager模块启用命令的异步性质，并指导用户如何正确等待模块可用。

**会议结束：** 会议在讨论完所有议题后结束，未有新的议题提出。

**备注：** 由于部分关键人员（如Patrick和n）未参会，会议决定在后续的PR评论中征求他们的意见，并确保所有相关方都了解并同意最终的实施方案。