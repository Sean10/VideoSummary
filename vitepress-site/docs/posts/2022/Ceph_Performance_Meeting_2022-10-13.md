---
title: "Ceph Performance Meeting 2022-10-13"
date: 2022-10-13
updated: 2022-10-21
tags:
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
Ceph性能会议2022年10月13日的纪要如下：

### 会议主题

本次会议主要讨论了使用CBT（Ceph Benchmarking Tool）进行不同存储后端（如Motor和Deos）的性能测试。

### 讨论内容

1. **CBT的使用**： 讨论了使用CBT进行性能测试的必要性，并计划将其应用于Motor和Deos等不同存储后端。
2. **Motor和Deos的状态**： 分析了Motor和Deos的开源项目和硬件需求，Motor由Seagate开发，Deos由Intel开发。
3. **CBT的扩展**： 讨论了如何扩展CBT，使其能够支持更多存储后端，如Deos，并增加客户端端点的功能。
4. **性能和功能实现**： 讨论了Deos的性能，特别是在未启用复制模式下的高速表现，以及其他功能如多部分上传的实现情况。
5. **合作与联系**： 建议与Seagate合作，共同推进CBT的发展，并确定了与Seagate团队的联系人Gregory Taretsky。
6. **后续行动计划**： Mark计划首先尝试安装和运行这些存储系统，并记录部署过程，然后逐步自动化这些过程，并探索如何将这些系统集成到CBT中。

### 决定事项

- 确定与Seagate的合作，特别是关于Motor和Deos的集成。
- Mark将负责初步的安装和测试工作，并与Seagate团队联系。

### 后续行动

- Mark将联系Gregory Taretsky，获取更多关于Motor和Deos的信息。
- 继续改进CBT，使其支持更多的存储后端和性能测试。
- 讨论RBD的性能改进，特别是与Seagate的合作和CBT的扩展。

### 其他讨论

- 讨论了Deos的高性能表现和潜在的应用场景。

### 会议结束

会议在讨论了所有议题后结束，感谢所有参与者的贡献。

本次会议旨在通过CBT工具比较和测试Ceph生态系统中不同存储后端的性能，并与Seagate合作以优化这些存储系统的性能。