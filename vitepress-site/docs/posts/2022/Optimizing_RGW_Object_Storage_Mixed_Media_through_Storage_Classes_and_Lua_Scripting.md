---
title: "Optimizing RGW Object Storage Mixed Media through Storage Classes and Lua Scripting"
date: 2022-11-10
updated: 2022-11-11
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
原总结准确反映了会议的关键细节，包括讨论的主要议题、决定的事项和后续行动计划。以下是对总结的改进，以增强其准确性和清晰度：

### 改进后的会议纪要

#### 会议主题
通过存储类和 Lua 脚本优化 RADOS Gateway 对象存储在混合媒体上的性能

#### 主讲人
- **Kurt Bruns**：Solidime 的软件工程师，SPDK 项目的贡献者。
- **Anthony Diatri**：Index Exchange 的首席工程师，著有《Seth Learning Seth》第二版，并参与 stuff 项目的文档编写。

#### 会议内容
1. **背景介绍**
   - RADOS Gateway (RGW) 的特点：对象大小多样，读取密集型工作负载（80% 读取，20% 写入），适用于 AI 工作负载。
   - 小对象需要高 IOPS 和低延迟，大对象需要高读取吞吐量和带宽。

2. **存储挑战**
   - 传统 HDD 性能有限，SSD 成本高，如何有效使用 SSD 是关键问题。

3. **优化策略**
   - 使用存储类和 Lua 脚本优化 RGW 对象存储。
   - 通过 S3 协议的存储类功能，将对象引导到不同的存储池。

4. **技术细节**
   - Blue Store 的 Min Alloc 大小为 4K，SSD 的 Indirection Unit 为 64K，可能导致空间放大。
   - Lua 脚本在对象上传时检查存储类，并根据对象大小自动分配到合适的存储池。

5. **实施细节**
   - Quincy 版本中引入自动调整 OSD 的 Min Alloc 大小为 SSD 的最佳 I/O 大小。
   - Lua 脚本修改存储类头部，动态调整存储类。

6. **结果展示**
   - Lua 脚本简化了对象存储的路由，提高存储效率。
   - 示例展示了如何使用 Lua 脚本自动将对象存储到 TLC 和 QLC 池中。

#### 后续行动计划
- 继续优化和扩展 Lua 脚本功能，支持更多自定义存储策略。
- 监控和评估优化后的存储性能。

#### 参考资料
- 相关论文和演示文稿的链接。
- RADOS Gateway Lua 脚本文档和示例。
- 空间放大表和 TCO 计算器。

#### 联系方式
- Kurt Bruns 的电子邮件：kurt@solidime.com

#### 会议总结
本次会议讨论了如何通过存储类和 Lua 脚本优化 RADOS Gateway 对象存储，特别是在混合媒体环境下的存储效率。通过自动化的存储类分配和 Lua 脚本，成功简化了对象存储的管理，并提高了存储效率。