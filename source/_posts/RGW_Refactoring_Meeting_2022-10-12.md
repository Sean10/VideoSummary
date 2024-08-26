---
title: "RGW Refactoring Meeting 2022-10-12"
date: 2022-10-18
updated: 2022-10-19
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：
- 使用CBT（Ceph Benchmarking Tool）进行不同zipper后端（如DB store、Motor、Deos）的性能比较。

#### 主要讨论内容：
1. **CBT的使用和目标**：
   - 讨论了使用CBT进行不同后端的性能比较，特别是DB store和Deos。
   - 提到了Deos和Motor的开发状态，以及它们是否能够通过这些工作负载。

2. **Deos和Motor的状态**：
   - Deos和Motor都是开源项目，但可能需要特定的硬件支持。
   - Deos和Motor的后端由Seagate贡献，Intel也在其中有所参与。

3. **CBT的抽象和扩展**：
   - 讨论了如何改进CBT，使其不仅仅支持Ceph，还能支持其他存储系统如Deos。
   - 提到了可能的下一步行动，包括设置Deos并构建CBT中的客户端端点。

4. **性能测试和比较**：
   - 讨论了如何进行性能测试，包括使用IO 500和RGW。
   - 提到了Deos在Lenovo的IO-500测试中表现出色，尤其是在未启用复制模式下。

5. **后续行动计划**：
   - 计划与Seagate合作，进一步测试和集成Motor和Deos到CBT中。
   - 计划探索如何自动化安装和部署这些存储系统。
   - 计划与Seagate的Gregory Taretsky联系，以获取更多技术支持和合作。

#### 决定事项：
- 确认了与Seagate的合作意向，并将与Gregory Taretsky联系以推进合作。
- 确定了初步的行动计划，包括手动安装和测试Deos和Motor，以及后续的自动化和集成工作。

#### 后续行动：
- Mark将尝试手动安装Deos和Motor，并记录过程，以便后续自动化。
- 将与Seagate的Gregory Taretsky联系，以获取更多技术支持和合作。
- 将继续探索和改进CBT，使其支持更多类型的存储系统。

#### 会议结束：
- 会议在讨论了所有议题后结束，感谢所有参与者的贡献和讨论。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。