---
title: "Ceph Notification at Scale- Notification V2, an Enterprise-Level Feature - Krunal Chheda, Bloomberg"
date: 2025-01-23
updated: 2025-01-24
tags:
  - "Ceph"
  - "分布式存储"
  - "可扩展性"
categories:
  - "视频总结"
outline: deep
---
### 改进后的中文总结

Ceph Notification at Scale: Notification V2, an Enterprise-Level Feature - Krunal Chheda, Bloomberg

该视频由Krunal Chheda，Bloomberg基础设施工程师主讲，介绍了Ceph RGW通知功能V2的增强与企业级特性。

#### 会议背景与目标
Krunal Chheda在Bloomberg负责存储基础设施，主要提供对象存储服务，底层基于Ceph。本次会议的目标是介绍Ceph RGW通知功能V2的增强，使其成为企业级特性，涵盖多区域同步、权限管理、遥测、性能优化等。

#### Bloomberg的Ceph使用情况
Bloomberg拥有10个Ceph集群，分布在4个数据中心，最大集群包含4500个OSD，支持超过45万个桶，每日处理20亿次请求。主要用于对象存储和块存储，支持Hadoop系统等大规模数据处理应用。

#### 现有通知功能概述
Ceph RGW的通知功能允许用户通过事件驱动的方式自动化工作流，支持同步和异步通知，并支持多种Broker，如Kafka、AMQ和HTTP Broker。支持的事件类型包括对象创建、删除、生命周期管理、复制事件等。

#### V2增强功能
- **所有权与权限模型**：每个Topic有明确的拥有者，支持细粒度的权限管理。
- **多区域同步**：支持多区域同步，用户只需在一个区域配置Topic和通知，系统会自动同步到其他区域。
- **遥测与洞察**：提供详细的遥测数据，如队列的待处理事件数量和大小。
- **Topic与Bucket映射**：支持查看某个Topic关联的所有Bucket。
- **新的日志子系统**：新增`rgw notification`日志子系统，便于开发者和运维人员仅查看与通知相关的日志。
- **持久性控制**：新增TTL和最大重试次数配置。
- **性能优化**：异步通知的队列写入操作从S3请求中分离，提升性能。

#### 迁移与兼容性
V2支持自动迁移现有的Topic和通知配置，用户无需手动操作。多区域控制通过Zone Group特性实现。

#### 未来计划
计划将队列从当前的128MB扩展至更大的容量，支持更多的事件处理。允许不同区域的Broker配置不同，避免强制同步到同一Broker。

#### 问答环节
会议还解答了关于ACL与Bucket Policy的兼容性、通知功能对性能的影响、队列大小与性能的关系等问题。

#### 总结
V2版本的通知功能在安全性、可扩展性、遥测和性能方面进行了显著增强，使其更适合企业级应用。Bloomberg已经在生产环境中启用该功能，并鼓励其他用户尝试使用。

#### 后续行动计划
用户在升级到Ceph Squid版本后，启用V2通知功能，并根据实际使用情况提供反馈。开发团队将继续优化队列扩展和多区域Broker支持，提升功能的灵活性和性能。