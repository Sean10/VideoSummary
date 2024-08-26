---
title: "CephFS Code Walkthrough: CephFS Mirroring Part 2"
date: 2021-04-27
updated: 2021-04-27
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Demurrer Daemon 后续讨论

#### 参会人员：Ceph 分布式存储研发团队

#### 会议时间：[具体时间]

#### 会议地点：[具体地点]

#### 会议内容总结：

1. **Demurrer Daemon 概述**：
   - Demurrer Daemon 负责在主集群和次集群之间同步快照。
   - 每个集群有一个 Demurrer Daemon，可以处理多个文件系统（multi-fs ready）。
   - 采用推送模型（push model），数据从主集群推送到次集群。

2. **技术细节**：
   - Demurrer Daemon 使用 libcephfs 客户端库与本地和远程集群通信。
   - 设计考虑了在主集群和次集群中进行挂载以使用 rsync，但最终选择了使用 libcephfs 客户端库。
   - 支持增量同步，但目前 Pacific 版本仅支持批量复制。

3. **配置和运行**：
   - 主集群需要 ceph 配置文件和密钥环。
   - 次集群支持两种添加方式：通过 pr add 接口和通过引导（bootstrapping）。
   - 目前建议每个集群只运行一个 Demurrer Daemon。

4. **代码实现**：
   - 从 main.c 开始，进行基本初始化，创建 messenger 和客户端。
   - 使用 Cluster Watcher 订阅 fs map，处理镜像启用和禁用等事件。
   - 通过定时器线程驱动异步操作，处理镜像启用、禁用、添加和移除对等体等操作。
   - 使用 fs mirror 类处理特定文件系统的镜像，支持多对等体。

5. **同步机制**：
   - 使用实例观察者和镜像观察者处理通知消息。
   - 通过引导令牌在主集群中导入次集群信息，存储在 mon config store 中。
   - 每个对等体分配多个线程进行快照同步，每个线程处理一个目录。
   - 使用 f-lock 确保多个 Demurrer Daemon 不会同时处理同一目录。

6. **增量同步**：
   - 通过比较快照 ID 和元数据来识别删除和重命名操作。
   - 使用 dirty snap id 扩展属性来确定是否可以进行增量同步。
   - 支持基于本地比较和远程比较的增量同步。

7. **后续行动计划**：
   - 继续完善 Demurrer Daemon 的增量同步功能。
   - 测试和验证多对等体支持。
   - 优化配置选项和性能。

#### 会议结论：
- Demurrer Daemon 的设计和实现已经基本完成，但仍需进一步测试和优化。
- 增量同步功能是当前的重点开发方向。

#### 后续行动：
- 继续开发和测试增量同步功能。
- 验证多对等体支持的可行性。
- 优化配置选项和性能，提升用户体验。

#### 会议记录人：[记录人姓名]

#### 会议结束时间：[具体时间]