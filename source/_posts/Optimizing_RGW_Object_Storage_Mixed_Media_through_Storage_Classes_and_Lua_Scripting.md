---
title: "Optimizing RGW Object Storage Mixed Media through Storage Classes and Lua Scripting"
date: 2022-11-10
updated: 2022-11-11
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题
优化 RADOS Gateway 对象存储在混合媒体上的存储类和 Lua 脚本

#### 主讲人
- **Kurt Bruns**：Solidime 的软件工程师，同时也是 SPDK 项目的贡献者。
- **Anthony diatri**：Index Exchange 的首席工程师，著有《Seth Learning Seth》第二版，并对 stuff 项目和文档部分有所贡献。

#### 会议内容
1. **背景介绍**
   - RADOS Gateway (RGW) 部署的特点：对象大小多样，读取密集型工作负载（80% 读取，20% 写入），特别是在 AI 工作负载中，读取比例更高。
   - 小对象操作需要高 IOPS 和低延迟，而大对象操作需要高读取吞吐量和带宽。

2. **存储挑战**
   - 传统硬盘（HDD）虽然成本效益高，但 IOPS 和带宽有限，导致集群瓶颈。
   - SSD 成本较高，但性能优越，如何有效使用 SSD 是一个关键问题。

3. **优化策略**
   - 使用存储类和 Lua 脚本在 RADOS Gateway 中实现对象存储的优化。
   - 通过 S3 协议的存储类功能，将不同类型的对象引导到不同的存储池（例如，大对象到 HDD 或高容量 SSD 池，小对象到 SSD 池）。

4. **技术细节**
   - Blue Store 的 Min Alloc 大小为 4K，即使写入 1 字节也会分配 4K。
   - QLC SSD 的 Indirection Unit 为 64K，可能导致空间放大问题，特别是对于小对象。
   - 通过 Lua 脚本在对象上传时检查存储类，并根据对象大小自动分配到合适的存储池。

5. **实施细节**
   - 在 Quincy 版本中，引入了自动调整 OSD 的 Min Alloc 大小为 SSD 的最佳 I/O 大小。
   - RADOS Gateway 的 Lua 脚本修改了存储类头部的可写性，以便在对象上传时动态调整存储类。

6. **结果展示**
   - 通过 Lua 脚本，成功简化了对象存储到正确池的路由，避免了用户手动选择存储类可能带来的问题。
   - 示例展示了如何通过 Lua 脚本自动将 4K 对象和 64K 对象分别存储到 TLC 和 QLC 池中，从而优化存储效率。

#### 后续行动计划
- 继续优化和扩展 Lua 脚本功能，以支持更多自定义的存储策略。
- 监控和评估优化后的存储性能，确保满足不同工作负载的需求。

#### 参考资料
- 相关论文和演示文稿的链接。
- RADOS Gateway Lua 脚本的相关文档和示例。
- 空间放大表和 TCO 计算器。

#### 联系方式
- Kurt Bruns 的电子邮件：kurt@solidime.com

#### 会议总结
本次会议详细讨论了如何通过存储类和 Lua 脚本优化 RADOS Gateway 对象存储，特别是在混合媒体环境下的存储效率。通过自动化的存储类分配和 Lua 脚本，成功简化了对象存储的管理，并提高了存储效率。