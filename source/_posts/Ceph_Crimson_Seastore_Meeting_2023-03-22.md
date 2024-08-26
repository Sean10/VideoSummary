---
title: "Ceph Crimson/Seastore Meeting 2023-03-22"
date: 2023-03-22
updated: 2023-03-23
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议时间：** [具体日期]  
**参会人员：** [参会人员名单]  

**主要议题：**

1. **代码审查与开发进展**
   - **scrub 和 aerator 代码迁移**：会议开始时，提到了正在进行的工作，包括对 scrub 和 aerator 代码的审查，以及将 interruptable future 代码迁移到标准协程（co-routine）的工作。讨论了这种迁移可能带来的便利性和效率提升。
   - **协程与 Future 的使用**：讨论了将现有代码中的 Future 实现转换为协程的可能性。强调了这种转换是可选的，主要为了减少内存分配，提高性能。同时，现有代码不需要强制转换，可以自由混合使用两种风格。

2. **Shaded 存储接口定义**：讨论了定义 Shaded future store 接口和 Shaded c-store 设备接口的工作。请求对新的 future store 接口从 OSD 角度进行审查。

3. **Marco 系统 PR 修改**：根据 AC 的评论，对 Marco 系统的 PR 进行了修改，包括未来写入扭曲和过滤包装短安装的耦合接口定义。讨论了设备接口定义，并计划将其修改为设备类和共享设备类。

4. **LBA point rpr 代码修改**：报告了 LBA point rpr 代码修改的调试进展，预计本周可以替换现有代码。同时，审查了由某人提交的正在进行中的缓存 PR。

5. **systore Clone 方法论讨论**：与 Ian 讨论了 systore Clone 的方法论，并开始着手开发原型。

**决定事项：**

- 对 Shaded future store 接口进行进一步审查。
- 继续进行 LBA point rpr 代码的调试和替换工作。
- 开始 systore Clone 的原型开发。

**后续行动计划：**

- 完成 Shaded future store 接口的审查并根据反馈进行调整。
- 完成 LBA point rpr 代码的调试，并替换现有代码。
- 继续开发 systore Clone 的原型，并根据需要进行调整。

**会议结束：** 会议简短，大家表示有好的周末。

**备注：** 保留了部分计算机科学/ceph相关领域英文原文的关键词，如 "scrub", "aerator", "co-routine", "Future", "OSD", "PR", "LBA point rpr", "systore Clone" 等。