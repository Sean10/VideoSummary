### 会议纪要

#### 会议主题：RBD Snapshot Based Mirroring 功能的改进

#### 主讲人：Raman Raja，IBM 软件工程师

#### 会议内容概述：
Raman Raja 介绍了 RBD（RADOS Block Device）的 Snapshot Based Mirroring 功能的最新改进，旨在提高其在灾难恢复场景中的鲁棒性。他首先概述了 RBD Mirroring 功能，然后详细讨论了如何设置、整体架构、遇到的问题及其解决方案，以及未来的工作计划。

#### 主要议题：
1. **RBD Mirroring 概述**：
   - RBD Mirroring 是一种异步复制图像的功能，通过 RBD Mirror Daemon 实现。
   - 支持两种模式：Journal Based Mirroring 和 Snapshot Based Mirroring。

2. **Snapshot Based Mirroring 的设置**：
   - 使用 SEF Orchestrator（如 SEF ADM 或 Rook）启动 RBD Mirror Daemon。
   - 配置 RBD Pool 和图像以支持 Mirroring。
   - 通过 Snapshot Schedule 命令定期创建镜像快照。

3. **灾难恢复解决方案架构**：
   - 针对 Kubernetes 工作负载，使用 RBD 作为存储后端。
   - 涉及三个 Kubernetes 集群：Hub 集群和两个管理集群。
   - 使用 Ramen Hub Operator 自动化管理。

4. **Failover 和 Relocate 场景**：
   - 讨论了计划和非计划 Failover 的流程。
   - 介绍了 Failback 和 Relocate 的操作步骤。

5. **遇到的问题及解决方案**：
   - 解决了镜像快照对象映射不准确导致的数据损坏问题。
   - 修复了高负载下镜像快照创建失败的问题。
   - 改进了在高延迟环境下的镜像同步性能。

6. **未来工作**：
   - 支持镜像组的镜像功能。
   - 改进 Clone 和 Discard 操作的镜像同步。
   - 探索多 RBD Mirror Daemon 的负载均衡和更高效的强制提升方法。

#### 决定事项：
- 确认了 RBD Snapshot Based Mirroring 功能的改进方向和优先级。
- 确定了未来工作的重点，包括镜像组的支持和性能优化。

#### 后续行动计划：
- 继续开发和测试镜像组和 Clone 的镜像功能。
- 优化 RBD Mirror Daemon 的性能和可靠性。
- 完善文档和用户指南，以便用户更好地理解和使用新功能。

#### 感谢：
- 感谢 Ilia 和 Sham 作为 RBD 和 Ramen Operator 的维护者所做的贡献。

### 结束语
Raman Raja 对与会者的参与表示感谢，并期待未来在 RBD Snapshot Based Mirroring 功能上的进一步合作和改进。