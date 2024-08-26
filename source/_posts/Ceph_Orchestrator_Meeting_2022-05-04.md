---
title: "Ceph Orchestrator Meeting 2022-05-04"
date: 2022-05-04
updated: 2022-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


- **当前问题**：如果限制NFS导出到特定IP，尝试从这些特定IP挂载时会遭到拒绝。
- **原因**：后端NFS服务器仅看到HAProxy代理的IP，而非客户端ID。
- **可能的解决方案**：设置HAProxy以透明模式运行，使后端服务器能看到客户端IP，而非H8代理IP。
- **实施难点**：需要后端服务器支持代理协议，但当前的Ganesha服务器不支持，因此需要寻找其他方法。
- **进一步研究**：探索是否有其他方式可以设置HAProxy在透明模式下工作，或者为Ganesha服务提供稳定的IP地址解决方案。