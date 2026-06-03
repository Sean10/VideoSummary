---
title: "Arming Ceph- CI Enhancement and UADK Integration - Rongqi Sun, HUAWEI TECHNOLOGIES CO., LTD."
date: 2025-01-23
updated: 2025-01-24
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要：Ceph社区关于ARM架构的CI增强与UADK集成讨论

**会议时间**：不详  
**主讲人**：Rongqi Sun，华为  
**参会人员**：Ceph社区成员



#### 会议主题：
- Ceph在ARM架构上的CI增强与UADK集成。

#### 主要议题：
1. **MCI（Make Check I/O）改进**
   - **背景**：ARM架构在移动、嵌入式市场和服务器领域日益重要。
   - **挑战**：MCI管道存在不稳定问题，包括单元测试失败、依赖项不匹配和不同Ubuntu版本导致的手动修改。
   - **解决方案**：清理遗留代码，统一操作系统版本，并在OpenEuler上进行构建。捕获构建工件并进行并行化以加速运行速度，解决超过20个相关问题。
   - **成果**：MCI现在要求在代码合并前必须通过测试。
2. **Crimson存储检测器问题**
   - **问题**：Crimson存储检测器在ARM上随机失败，难以重现。
   - **解决方案**：关闭Crimson存储检测器，等待Ceph子模块迁移到librados后重新开放。
3. **未来工作**
   - **MCI优化**：提议将部分单元测试从MCI移至其他CI工具，以缩短运行时间。
   - **ARM CI通道**：计划构建ARM CI通道，吸引更多ARM爱好者参与。
   - **回溯支持**：将MCI检查引入backport分支。
   - **更多开源操作系统支持**：增加对更多开源操作系统的支持。
4. **EDK集成**
   - **背景**：EDK是用户空间加速开发工具包，支持加密和压缩加速。
   - **进展**：在Ceph代码中添加了UDK与UKPI的对比类，并已合并到main分支。通过RGW和RBD的测试，EDK显著减少了CPU使用率。
   - **未来计划**：支持OpenCell3的provider接口，讨论ChaCha20模式的加速支持。

#### 决定事项：
- 继续优化MCI，缩短运行时间。
- 构建ARM CI通道，吸引更多ARM爱好者参与。
- 支持更多开源操作系统。
- 进一步讨论EDK与OpenCell3的集成，特别是ChaCha20模式的加速支持。

#### 后续行动计划：
- **MCI优化**：与Pat讨论将部分单元测试移至其他CI工具。
- **ARM CI通道**：构建ARM CI通道，吸引更多ARM爱好者参与。
- **EDK集成**：与Ric进一步讨论ChaCha20模式的加速支持。

#### 其他：
- 主讲人鼓励社区成员参与ARM相关的工作，提升Ceph在ARM架构上的性能。



**会议总结**：  
本次会议讨论了Ceph在ARM架构上的改进，特别是MCI的优化和EDK的集成。通过清理遗留代码、统一操作系统版本等措施，MCI的稳定性得到了显著提升。未来将继续优化MCI，缩短运行时间，并构建ARM CI通道以吸引更多ARM爱好者参与。此外，EDK的集成显著提升了加密和压缩的性能，未来将进一步讨论与OpenCell3的集成，特别是ChaCha20模式的加速支持。