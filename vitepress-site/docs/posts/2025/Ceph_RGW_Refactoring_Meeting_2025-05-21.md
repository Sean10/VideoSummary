---
title: "Ceph RGW Refactoring Meeting 2025-05-21"
date: 2025-05-24
updated: 2025-05-24
tags:
  - "Ceph"
  - "RGW"
  - "分布式存储"
  - "Erasure Coding"
categories:
  - "视频总结"
outline: deep
---
### 会议概述

本次 Ceph RGW (RADOS Gateway) 开发组会议主要讨论了以下技术议题：

1. **Bucket Logging 性能问题及解决方案**：讨论了在 Erasure Coding (EC) 池中使用 Bucket Logging 功能时的性能问题，并提出了使用专用 replica pool 作为临时对象池的解决方案。
2. **RGW 客户端超时处理机制**：讨论了客户端超时断开时 RGW 的处理机制，确认了当前机制的有效性。
3. **版本控制与分片方案改进**：讨论了当前分片方案对版本化对象数量有限制的问题，并提出了改进方案。
4. **Tentacle 版本发布前的功能合并状态**：讨论了 Tentacle 版本发布准备情况，包括待合并功能和测试验证。

### 主要议题与讨论

#### 1. Bucket Logging 性能问题

**问题描述**：Bucket Logging 功能在 EC 池中存在性能问题，因为 EC 池默认不支持 append 操作，修改对象需要重写整个对象。

**讨论方案**：
- 使用 replica pool 作为临时对象池，写入时先写入临时池，提交时通过更新 manifest 使对象可见。
- 使用现有的 RGW "data extra pool" 作为临时对象池。

**决议**：采用方案B，通过 manifest 指向不同池中的对象。

#### 2. RGW 客户端超时处理

**问题描述**：客户端读取大文件时超时断开，RGW 仍会继续从 OSD 获取数据。

**讨论结果**：当前机制已合理限制资源浪费，16MB 窗口大小可通过配置调整。

#### 3. 版本控制与分片方案改进

**问题背景**：当前分片方案对版本化对象数量有限制（约200,000个）。

**讨论方案**：
- 顺序分片方案（In-order sharding）。
- 版本数量限制作为可选功能提供给用户。

**决议**：优先开发 in-order sharding 方案，版本数量限制作为可选功能。

#### 4. Tentacle 版本发布状态

**待合并功能**：
- D4N (Direct-to-Daemon NFS) 视为 bug fix，可合并。
- DDUP (Data Deduplication) 尚未通过全部测试。

**发布决策**：若 DDUP 能在一周内通过全部测试，可纳入 Tentacle；否则将推迟到点发布版本。

### 后续行动计划

1. **Bucket Logging 改进**：实现基于 manifest 的跨池方案，验证性能并确保垃圾回收机制正常工作。
2. **版本控制改进**：推进 in-order sharding 方案开发，评估版本数量限制功能的实现方式。
3. **Tentacle 发布准备**：加速 DDUP 功能测试验证，跟踪 multi-site 测试中发现的数据日志问题，确定最终功能合并截止时间。
4. **客户端超时优化**：文档化当前 16MB 窗口配置选项，评估是否需要提供更细粒度的超时控制。

### 关键技术点

- **EC 池限制**：默认不支持 append 操作，修改需重写整个对象。
- **RGW 缓冲机制**：默认 16MB 传输窗口，可通过配置调整。
- **分片方案**：当前方案在大规模对象下性能下降，in-order sharding 有望改善。
- **Data extra pool**：RGW 已有用于 multipart upload 的专用临时池。