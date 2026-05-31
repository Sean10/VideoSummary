---
categories:
- 视频总结
date: 2023-04-07
subtitle: Ceph_Developer_Monthly_2023-04-05
tags:
- Ceph
- 分布式存储
- CI/CD
title: "Ceph Developer Monthly 2023-04-05"
updated: 2023-04-08
---



### 会议纪要

**会议主题：** 开发者月度会议 - 友好版  
**日期：** 2023年4月5日  
**主持人：** Radic  
**出席人员：** Kevin, Laura, 以及其他开发者和社区成员

#### 主要议题

1. **引入 openEuler 至 Upstream**
   - Kevin 分享了将 openEuler 操作系统引入 Ceph Upstream 的想法。
   - openEuler 是一个中国最大的开源操作系统社区，拥有丰富的用户和商业发行版。
   - openEuler 的 SDS SIG 致力于开发和维护存储相关功能，并已提交相关页面至 Upstream。
   - 讨论了如何确保 openEuler 的 LGS 支持在 Upstream 中运行，并探讨了如何将 openEuler 的构建集成到 Upstream 的 CI 系统中。

2. **技术讨论**
   - 讨论了在 Upstream 中支持新操作系统的技术细节，包括构建规范、自动化测试、资源需求等。
   - 提到了 openEuler 的存储 SIG 已经有一些自动构建，但需要更多硬件资源来执行构建。

3. **PR 讨论**
   - 讨论了提交到 Upstream 的 PR，特别是关于 openEuler 的 spec 文件更改。
   - 确认了 spec 文件在 main 分支上已知可以工作，建议先贡献到 main 分支，然后再回溯到特定分支。

4. **反馈和后续行动**
   - 讨论了从 Upstream 和 openEuler 社区获得的反馈，以及如何继续贡献支持。
   - 确认了 openEuler 社区可以提供硬件资源来帮助 Upstream 设置自动化作业。
   - 讨论了如何确保 Centos 和 RHEL 的包仍然可以构建。

5. **其他议题**
   - 讨论了在 Reef 版本中切换某些组件从使用旧的未标记计数器到新的标记计数器的问题。
   - 讨论了 perf 计数器是否应被视为公共 API 的一部分，以及如何在社区中形成共识。

#### 决定事项

- 确认了 openEuler 的 spec 文件在 main 分支上已知可以工作，建议先贡献到 main 分支，然后再回溯到特定分支。
- 确认了 openEuler 社区可以提供硬件资源来帮助 Upstream 设置自动化作业。
- 讨论了如何在社区中形成关于 perf 计数器是否应被视为公共 API 的共识。

#### 后续行动计划

- 继续贡献支持 openEuler 在 Upstream 中的运行。
- 提供硬件资源帮助 Upstream 设置自动化作业。
- 在社区中讨论并形成关于 perf 计数器是否应被视为公共 API 的共识。
- 在 7.io 网站上提及 openEuler 的存储 SIG 仓库。

**会议结束：** 感谢所有参与者的讨论，期待下个月的会议。