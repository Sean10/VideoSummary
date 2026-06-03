---
title: "Ceph EC Performance Journey- Classic vs. Fast EC"
date: 2026-04-20
updated: 2026-04-21
tags:
  - "Erasure Coding"
  - "性能优化"
  - "OSD"
categories:
  - "视频总结"
outline: deep
---
## 演讲背景

本次演讲由 IBM 高级工程经理主持，实际性能测试工作由其印度团队的工程师 Tejas 完成。演讲聚焦于 Classic EC（经典纠删码）与 Fast EC 在实际硬件环境下的性能对比，以及在测试过程中发现并修复的一个关键内存泄漏问题。

## 测试环境

**硬件配置：**
- 存储节点：Dell R760，X5D 节点，共 12 个节点
- 测试规模：分别测试 4、8、12 节点三种规模
- 每节点配备 24 块磁盘
- OSD 扩展测试：8、16、24 个 OSD
- 客户端：Dell R630，作为文件数据路由器，128 GB RAM
- BIOS 配置为 Performance模式

**软件配置：**
- Ceph 版本：Squid 19.2.1（Classic EC 基准）
- Ceph 版本：Tentacle 30.1.0（Fast EC 测试版本）
- 测试期间禁用 auto scaler、balancer 和 scrubing，确保不同测试轮次之间的公平对比

**测试参数：**
- 客户端数量：6 个，每个客户端运行 5 个镜像，共约 30 个镜像
- IO depth：1 到 256
- Pool 类型：replica 3 及 EC profile（2+2、4+2、6+2）
- 工作负载：100% 读、100% 写、70/30 读写混合
- Block size：4 KB、16 KB、32 KB、64 KB、4 MB
- OSD 数量：6 节点 144 个 OSD；12 节点 288 个 OSD

## EC Plugin 变更

本次测试同步更换了 EC 编码插件，从 Jerasure 切换至新的高性能插件（Tentacle 版本）。原因是 Jerasure 维护活跃度不足，新插件能够提供更好的 EC 优化性能。

## 初步测试结果：发现回归问题

**16K block size 测试（4+2 EC profile）：**
- Fast EC（Tentacle）相比 Classic EC（Squid）延迟约 2ms，性能提升约 60%，表现优异。

**64K block size 测试：**
- 出现意外回归：Squid Classic EC 的性能反而优于 Tentacle Fast EC。
- 这一结果不符合预期，触发了深入调查。

## 根因分析：内存泄漏

团队借助 Prometheus、Ceph exporter 等监控工具导出了大量客户端和存储服务器的数据集，并联合 Fast EC 开发团队（Alex、Lee、Bill）共同排查。

**发现问题：**
- OSD memory target 设置为 16 GB，但实际 OSD RSS 内存消耗仅约 1 GB，远低于预期。
- 这表明存在内存泄漏，存未被正确释放。

**内存泄漏根因：**
- 在 Fast EC 的实现中，每次写操作包含两个阶段：apply（应用）和 commit（提交）。
- 在 commit 阶段，会创建 EC dummy ops，用于将写操作刷入 PG log。
- 当 PG 进入 idle 状态时，约 1K 大小的对象残留未被释放，随着时间推移逐渐累积，导致内存持续增长。
- PG log 在Ceph 内部用于区分 backfill 和 recovery 操作。

## 修复方案与验证

**临时 Workaround：**
- 强制将 PG 状态从 idle 切换，触发内存刷新，使残留对象得以释放。
- 此方案用于测试验证，确认修复方向正确。

**正式 Patch：**
- 开发团队在 workaround 验证后编写了正式补丁，并以 hot patch 形式应用于测试环境。

**修复后效果：**
- OSD 内存消耗恢复至 16 GB 目标值附近，行为正常。
- CPU 使用率从约 780% 下降至约 600%。
- 16K block size 下，IOPS 从约 1.2M 提升至约 1.6M，提升约 400K。
- 64K block size 的回归问题消失，Fast EC 性能重新超越 Classic EC。

## 扩展性验证：12 节点集群

将集群从 6 节点（144 OSD）扩展至 12 节点（288 OSD）后：
- 整体吞吐量翻倍，验证了 Ceph scale-out 存储的线性扩展能力。
- Fast EC 与 Classic EC 之间的性能差距也随规模扩大而成比例增大，进一步证明 Fast EC 在大规模集群中的优势更为显著。

## Fast EC 与Replica 3 对比

修复后，Fast EC（4+2）与 replica 3 的性能对比：
- Fast EC 读性能尚未达到 replica 3 水平，但差距在缩小。
- Ceph 8.1 replica 3 与 9.2 replica 3 之间本身也存在性能提升。
- 团队预计后续版本（Tentacle 及后续 umbrella release）将在读性能和写性能上持续改进，逐步接近 replica 3。

## 后续计划

- 当前 12 节点 288 OSD 的完整规模测试仍在进行中。
- 针对写性能的优化工作正在推进，预计在下一个 umbrella release 中落地。
- 持续关注 Fast EC 在大 block size（64K、4MB）场景下的性能改善。

## 总结

本次性能测试历程揭示了 Fast EC 在实际部署中的一个关键内存泄漏缺陷，并通过系统化的监控数据分析和开发团队协作完成了定位与修复。修复后，Fast EC 在小 block size 场景下相比 Classic EC 有显著性能优势，在大规模集群中优势更为突出，整体上朝着接近 replica 3 读性能的目标稳步推进。
