---
title: "Maximizing the Value of Your Rados Gateway with Ingress Strategies - Michaela Lang & Daniel Parkes"
date: 2025-01-23
updated: 2025-01-24
tags:
  - "Ceph"
  - "RGW"
categories:
  - "视频总结"
outline: deep
---
在本次会议中，Ceph RGW服务的负载均衡策略成为了讨论的重点。会议涉及了多种负载均衡策略，包括传统的DNS轮询、硬件和软件负载均衡器、BGP路由负载均衡、Service Discovery结合DNS、SDN以及Ceph ADM提供的负载均衡服务。

**会议内容总结**：

1. **会议背景**：Daniel Parks介绍了Ceph RGW服务负载均衡的需求，Mika则介绍了如何利用Envoy作为Ingress策略来实现负载均衡。
2. **传统负载均衡策略**：讨论了DNS轮询、硬件负载均衡器、软件负载均衡器、BGP路由负载均衡、Service Discovery结合DNS、SDN等策略的优缺点。
3. **Ceph ADM提供的负载均衡服务**：介绍了Ceph ADM的Ingress服务，该服务基于HAProxy和Keepalived，可以自动管理IP地址和负载均衡，支持服务发现。
4. **Envoy作为负载均衡解决方案**：Mika介绍了Envoy在微服务架构中的应用，包括其丰富的功能、灵活的配置和优异的性能。
5. **未来发展方向**：讨论了将Envoy集成到Ceph ADM中、自动化证书管理以及全局速率限制等功能。

**会议决定事项**：

1. 探索Envoy与Ceph ADM的集成。
2. 开发自动证书轮换功能。
3. 开发基于Envoy的全局速率限制功能。

**后续行动计划**：

1. 在Ceph社区中进行Envoy集成的测试和验证。
2. 开发自动证书轮换功能。
3. 开发基于Envoy的全局速率限制功能。

本次会议对Ceph RGW服务的负载均衡策略进行了深入讨论，为Ceph社区的进一步发展提供了宝贵的技术参考。