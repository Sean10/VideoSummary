---
title: MSR(Mutli-Step Retry)- An Generalization of CRUSH Allowing Multiple OSDs Per Failure Domain- S. Just
date: 2025-11-19
updated: 2025-11-20
tags:
- Ceph
- CRUSH算法
- 分布式存储
categories: 
- "视频总结"
subtitle: MSR_Mutli-Step_Retry_-_An_Generalization_of_CRUSH_Allowing_Multiple_OSDs_Per_Failure_Domain-_S._Just
---


### **Ceph MSR规则讨论会议纪要**  

#### **会议概述**  
本次会议主要讨论了Ceph分布式存储系统中CRUSH算法的改进版本——MSR（Multi-Step Retry）规则。该规则旨在解决传统CRUSH在处理密集EC（Erasure Coding）集群时的局限性，并提高了Ceph在密集EC场景下的性能和稳定性。

#### **关键议题与讨论内容**  

##### **1. CRUSH算法回顾**  
- **核心功能**：CRUSH是Ceph用于数据分布的确定性算法，通过哈希对象名生成PG（Placement Group）ID，再结合OSD Map映射到具体的OSD。
- **关键特性**：稳定性、容灾与权重感知、层级选择。

##### **2. 传统CRUSH的局限性**  
- **密集EC集群问题**：在小型集群中，难以均匀分布EC分片，导致容灾能力下降。
- **Chooseleaf的不足**：在多步骤选择时，若中间步骤故障，可能被迫在同一Host内重试。

##### **3. MSR规则的设计与优势**  
- **核心改进**：深度优先+多向量管理、动态重试逻辑。
- **用例适配**：适用于小规模EC集群，如跨少量Host分布宽条带编码。

##### **4. 实现细节与调优**  
- **参数调优**：`retry_collision`、`max_retries`。
- **稳定性保障**：严格测试映射一致性。

##### **5. 决策与行动计划**  
- **推广MSR规则**：在EC池配置中优先使用`osd_per_failure_domain`参数，自动化生成MSR规则。
- **兼容性维护**：确保MSR与传统CRUSH规则共存。
- **性能监控**：收集用户反馈，验证MSR在小集群中的实际效果。

##### **6. 遗留问题与后续跟进**  
- **用户适配**：评估迁移至MSR的必要性。
- **高级调优**：补充用例指南，针对极端场景调整参数。

#### **会议记录人**：Ceph社区研发团队  
#### **日期**：2023年X月X日  
