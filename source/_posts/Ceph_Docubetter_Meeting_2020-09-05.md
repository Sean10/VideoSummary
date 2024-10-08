---
title: "Ceph Docubetter Meeting 2020-09-05"
date: 2020-09-10
updated: 2020-09-11
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议时间：** [具体日期]  
**参会人员：** [主持人]、[参会者]

#### 主要议题：

1. **hacking.rst 集成到开发者指南**
   - [主持人] 本周主要工作是将包含2300行代码的 `hacking.rst` 集成到开发者指南中。
   - 遇到了文档构建问题，经过与 Sebastian 的合作，发现特定提交（commit）4ea54664 可以解决构建问题。
   - 该问题已解决，`hacking.rst` 已成功集成，后续可能需要进一步调整。

2. **文档构建问题**
   - 发现了其他PR中的构建问题，特别是与 `prompt` 指令相关的问题。
   - 这些问题将在后续的非正式会议中进一步讨论和解决。

3. **入门指南与部署指南**
   - [主持人] 对入门指南和部署指南的看法有所改变，认为部署指南更为实用。
   - 尽管如此，仍计划推进入门指南的发布，特别是针对新手。

4. **网站界面更新**
   - 讨论了网站 landing page 的更新，包括添加三个按钮（tracker、dev guide、install guide）。
   - 由于 Sebastian 对按钮大小的意见，该PR目前停滞，需要进一步调整和拆分。

5. **文档贡献流程优化**
   - 与 Brad Hubbard 讨论了如何优化从远程分支拉取、修改并推送回原分支的流程。
   - 该流程有助于处理格式不规范但内容有价值的贡献。

6. **视频教程的想法**
   - [主持人] 提出了制作视频教程的想法，特别是针对入门指南的安装步骤。
   - 视频长度控制在47秒，强调简洁和实用。

#### 决定事项：

- `hacking.rst` 已成功集成到开发者指南，后续可能需要进一步调整。
- 网站 landing page 的更新需要进一步讨论和调整按钮大小。
- 入门指南和部署指南的发布将继续推进，特别是针对新手。
- 视频教程的想法将在线下进一步讨论。

#### 后续行动计划：

- [主持人] 将发送关于 `hacking.rst` 的邮件，鼓励更多人参与贡献。
- 继续解决文档构建问题，特别是与 `prompt` 指令相关的问题。
- 调整并拆分网站 landing page 的PR，以适应不同需求。
- 进一步讨论和优化视频教程的想法，确保内容简洁实用。

**会议结束时间：** [具体时间]  
**下次会议时间：** [具体日期]

**记录人：** [记录人姓名]  
**审核人：** [审核人姓名]