---
title: "Ceph Performance Meeting 2022-10-13"
date: 2022-10-20
updated: 2022-10-21
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：
- 性能测试工具CBT（Ceph Benchmarking Tool）在不同存储后端（如Motor和Deos）的比较。

#### 讨论内容：
1. **CBT的使用**：
   - 计划使用CBT来比较不同的存储后端，特别是Motor和Deos。
   - 讨论了这些后端的当前状态和是否能够通过CBT的测试。

2. **Motor和Deos的状态**：
   - Motor和Deos都是开源项目，但可能需要特定的硬件支持。
   - Deos由Intel开发，而Motor由Seagate开发。

3. **CBT的抽象和扩展**：
   - 讨论了如何改进CBT，使其不仅限于Ceph，还能支持其他存储系统如Deos。
   - 提出了在CBT中增加对Deos集群的支持，并扩展客户端端点的功能。

4. **性能和功能实现**：
   - 讨论了Deos的性能，特别是在未启用复制模式下的高速表现。
   - 提到了Deos的一些功能还未完全实现，如多部分上传。

5. **合作与联系**：
   - 建议与Seagate合作，共同推进CBT的发展。
   - 确定了与Seagate团队的联系人Gregory Taretsky。

6. **后续行动计划**：
   - Mark计划首先尝试安装和运行这些存储系统，并记录部署过程。
   - 计划逐步自动化这些过程，并探索如何将这些系统集成到CBT中。

#### 决定事项：
- 确定与Seagate的合作，特别是关于Motor和Deos的集成。
- Mark将负责初步的安装和测试工作，并与Seagate团队联系。

#### 后续行动：
- Mark将联系Gregory Taretsky，获取更多关于Motor和Deos的信息。
- 继续改进CBT，使其支持更多的存储后端和性能测试。

#### 其他讨论：
- 讨论了RBD的性能改进，特别是与Seagate的合作和CBT的扩展。
- 提到了Deos的高性能表现和潜在的应用场景。

#### 会议结束：
- 会议在讨论了所有议题后结束，感谢所有参与者的贡献。

---

本次会议主要聚焦于Ceph生态系统中不同存储后端的性能测试和集成，特别是通过CBT工具来实现这一目标。通过与Seagate的合作，预计将能够更好地理解和优化这些存储系统的性能。