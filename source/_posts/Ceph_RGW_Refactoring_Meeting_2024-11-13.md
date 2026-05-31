---
title: Ceph RGW Refactoring Meeting 2024-11-13
date: 2024-11-13
updated: 2024-11-13
tags:
- Ceph
- RGW
- 分布式存储
- 对象存储
categories: 
- "视频总结"
subtitle: Ceph_RGW_Refactoring_Meeting_2024-11-13
---

本次会议主要讨论了Ceph RGW的多个重要议题，包括RGW与Vector DB的集成、版本化桶的动态resharding、parallel resharding的进展、Keystone缓存优化以及bucket通知的Zone过滤和负过滤功能。

1. **RGW与Vector DB集成方案讨论**
   讨论了如何将RGW中的数据集成为Vector DB的一部分，以支持RAG或数据科学研究。提出了使用Knative作为服务框架，并通过RGW的bucket通知机制触发Knative函数的解决方案。技术细节包括使用Rook部署RGW以支持bucket通知，以及将embedding模型部署在Kubernetes集群内。

2. **Ceph RGW版本化桶的动态resharding问题**
   讨论了版本化桶在动态resharding时遇到的问题，并提出了使用archive zone减少max_objects_per_shard以避免omap警告的解决方案。

3. **Parallel Resharding项目更新**
   更新了parallel resharding项目的进展，指出已提交draft PR并测试通过，但依赖其他PR的合并和清理。讨论了RGW并发IO阻塞在条件变量上的问题，以及为bucket元数据读写提供异步接口的必要性。

4. **Keystone缓存问题讨论**
   讨论了Keystone缓存miss导致频繁访问Keystone的问题，并提出了使用mutex锁避免多次访问Keystone的解决方案。

5. **其他议题**
   Alex计划开始处理bucket通知的Zone过滤和负过滤功能，Marcus分享了一个用于测试Swift操作的独立程序。

会议总结：
本次会议重点讨论了RGW的多项重要特性和工作进展，各项目负责人将继续推进相关工作，并计划在后续会议中进行进一步讨论和演示。