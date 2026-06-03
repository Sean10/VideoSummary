---
title: "An Open Source Distributed Rate-limiting Service for Ceph-object and Other HTTP APIs- Jacques Heunis"
date: 2025-11-19
updated: 2025-11-20
tags:
  - "Ceph"
  - "分布式存储"
  - "开源"
categories:
  - "视频总结"
outline: deep
---
### Ceph 分布式对象存储限速服务开源项目总结

**会议主题**：
Bloomberg 团队分享了其开发的针对 Ceph 对象存储的分布式限速系统（代号为 we QoS），该系统旨在管理用户请求速率、数据传输速率及并发请求，以提高 Ceph 存储系统的服务质量（QoS）。

**核心讨论内容**：
1. **背景与挑战**：
   - Bloomberg 的存储工程团队为内部团队提供对象存储服务，类似私有云，服务于不同业务团队，流量模式多样。
   - 需确保系统稳定性，防止单个用户占用过多资源（如 CPU、内存、OSD 负载）。
   - 早期使用硬件负载均衡器进行 IP 限速，但难以适应集群扩展和多租户需求。

2. **解决方案：we QoS 系统**：
   - **核心功能**：
     - 请求速率限制（RPS）
     - 数据传输速率限制（带宽）
     - 并发请求控制（防止资源耗尽）
   - **技术栈**：
     - HAProxy（核心代理层，通过 Lua API 注入限流逻辑）
     - 独立服务（非 Ceph 内置，易于调试和扩展）
   - **优势**：
     - 协议无关（支持 S3、管理 API 等 HTTP 服务）
     - 动态配置（JSON 文件定义限速策略，支持热更新）

3. **演进与优化**：
   - 初始版本（约 700 行代码）：仅限请求速率。
   - 新增功能：
     - 并发控制（防止用户占用过多连接/内存）
     - 差异化限速（基于 HTTP Method 和 S3 Operation）
     - 支持短时凭证（Ceph Squid 版本引入的 `Accounts` 功能）

4. **开源与社区反馈**：
   - we QoS 已在 GitHub 发布。
   - Q&A 重点：
     - 匿名请求：未认证请求共享同一限速池。
     - 批量操作：按操作类型整体限速。
     - 临时调整限速：修改 JSON 配置文件并触发动态加载。

**关键决定与行动计划**：
1. 推广使用：鼓励社区测试 we QoS，反馈需求。
2. 持续优化：
   - 增加对请求体动态评估的支持。
   - 探索与 Ceph Dashboard 集成，提供可视化限速管理。

**保留的关键术语**：
- Ceph, distributed storage, OSD, RADOS, S3, HAProxy, QoS, CRUSH algorithm, short-lived credentials, concurrency control

**后续跟进**：
- GitHub 协作：社区贡献与问题跟踪。
- 用户案例收集：验证多场景适用性。

通过这个开源项目，Bloomberg 为 Ceph 对象存储提供了一种有效的限速机制，以优化资源使用并提高系统性能。项目的开源使得其他组织也可以受益于这一解决方案。