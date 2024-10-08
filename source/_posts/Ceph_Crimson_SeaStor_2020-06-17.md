---
title: "Ceph Crimson/SeaStor 2020-06-17"
date: 2020-06-17
updated: 2020-06-17
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议主题：** 讨论Ceph存储系统中的Alien、Bluestar和Sea Star内存分配器的相关问题及改进方案

**参会人员：** [未列出具体人员]

**会议时间：** [未提供具体时间]

**会议地点：** [未提供具体地点]

**主要议题：**

1. **内存分配器初始化问题：**
   - 发现两个主要问题：未初始化内存分配器池和线程在初始化时的限制。
   - Sea Star内存分配器需要两阶段初始化，需要线程协助以克服32级最大限制。

2. **线程管理假设的违反：**
   - Bluestar的Troggs DB假设使用静态线程池管理线程，但实际情况并非如此。
   - 需要讨论这一违反假设的后果及其解决方案。

3. **根节点结构的改进：**
   - 正在改进根节点的结构，将其大小从16字节减少到仅包含三个物理地址。
   - 这将简化代码并避免每次滚动日志时写入额外的空页。

4. **心跳重构：**
   - 进行了心跳重构，以减少抽象并进行全面审查。

5. **I/O测试：**
   - 询问是否能够使用最新的补丁进行I/O测试。

6. **生产环境中的内存分配器问题：**
   - 讨论了在生产环境中使用Sea Star内存分配器的问题，特别是线程管理和内存回收。
   - 提出了一些解决方案，如限制线程数量和调整配置。

7. **配置管理和默认值：**
   - 讨论了是否需要为Bluestar设置不同的默认配置值。
   - 决定首先进行配置验证，以确保错误配置不会导致系统崩溃。

**决定事项：**

1. **内存分配器初始化：**
   - 需要进一步讨论和解决Sea Star内存分配器的初始化问题。

2. **线程管理：**
   - 需要重新评估Bluestar的线程管理策略，并可能调整其配置。

3. **根节点结构改进：**
   - 继续进行根节点结构的改进工作，以简化代码并提高效率。

4. **配置验证：**
   - 首先进行配置验证，确保错误配置不会导致系统崩溃，后续再考虑调整默认配置。

**后续行动计划：**

1. **内存分配器问题：**
   - 继续研究和解决Sea Star内存分配器的初始化问题。

2. **线程管理策略：**
   - 重新评估Bluestar的线程管理策略，并制定相应的调整方案。

3. **根节点结构改进：**
   - 完成根节点结构的改进，并进行代码清理和优化。

4. **配置验证和调整：**
   - 实施配置验证机制，并根据需要调整默认配置值。

**会议结束语：**
- 感谢大家的参与和讨论，期待后续的进展和成果。

**下次会议预告：**
- [未提供具体信息]

**会议记录人：**
- [未提供具体人员]

**会议结束时间：**
- [未提供具体时间]