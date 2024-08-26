---
title: "CDS Pacific: Performance"
date: 2020-04-03
updated: 2020-04-04
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议主要讨论了Ceph项目在即将发布的Pacific版本中的各项开发进展和计划。会议涵盖了多个关键领域，包括性能优化、代码库的小规模改进、以及持续集成和测试的增强。

#### 主要议题
1. **BlueStore性能优化**
   - **Adam's comb family sharding**: 该项目在Octopus时间框架内成为重要项目，虽然尚未合并，但正在积极开发中。预计将大幅改善写入放大和空间放大问题。
   - **Double cache fix**: 等待Adam's comb family sharding合并后，将解决缓存重复数据问题，避免缓存污染。
   - **Cache age based bidding**: 计划在上述修复后实施，通过分析缓存中数据的相对年龄来优化内存分配。
   - **Node data structure diet**: 由Igor负责，旨在减小O节点数据结构的大小，预计带来10-20%的改进。
   - **Hybrid allocator and deferring big writes**: 这些改进将有助于减少硬盘上的中间层，特别是在4K块大小的情况下。

2. **PG log和PG balancer的改进**
   - **PG scaling和PG balancer的变化**: 这些改进在Octopus中已经开始，但需要持续关注以确保不会引入不良行为。

3. **RGW优化**
   - **避免写入暂停**: 针对bucket index splitting的优化，虽然设计可行，但目前优先级较低。

4. **MDS和CephFS的动态子树分区方案**
   - **MDS性能优化**: 尝试通过改变MDS的请求服务方式来提高性能，特别是对于大型目录文件的处理。

5. **RBD和内核客户端的性能问题**
   - **25Gbps链路的瓶颈问题**: 正在诊断中，希望在Pacific版本中解决。

6. **持续集成和性能测试**
   - **性能测试框架的增强**: 计划通过Jenkins集成CBT来运行性能测试，确保不引入性能回归。
   - **长期运行的大型规模测试**: 考虑使用Toothology进行更复杂的性能测试，特别是对于大型集群和长时间运行的测试。

#### 决定事项
- **BlueStore的多个性能优化将在Pacific版本中继续推进。**
- **PG log和PG balancer的改进将持续进行，以确保稳定性和性能。**
- **RGW的优化将根据优先级进行，可能会有所延迟。**
- **MDS和CephFS的优化将尝试新的方法来提高处理大型目录的性能。**
- **RBD和内核客户端的问题将作为优先事项进行诊断和修复。**
- **性能测试框架将得到增强，包括Jenkins集成和Toothology的使用。**

#### 后续行动计划
- **继续推进BlueStore的性能优化工作，特别是Adam's comb family sharding和相关缓存优化。**
- **持续监控和改进PG log和PG balancer的性能和稳定性。**
- **评估RGW优化的优先级，并根据资源情况进行调整。**
- **探索MDS和CephFS的新优化方法，特别是在处理大型目录文件时。**
- **解决RBD和内核客户端的性能瓶颈问题，特别是在高速网络环境下。**
- **增强性能测试框架，确保能够有效检测和防止性能回归。**

#### 结论
本次会议为Ceph的Pacific版本开发提供了明确的方向和行动计划，特别是在性能优化和持续集成测试方面。所有团队成员将继续努力，确保新版本的质量和性能达到预期目标。