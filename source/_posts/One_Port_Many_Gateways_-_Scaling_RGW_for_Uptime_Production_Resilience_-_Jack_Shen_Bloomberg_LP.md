---
title: One Port, Many Gateways- Scaling RGW for Uptime & Production Resilience - Jack Shen, Bloomberg LP
date: 2025-11-19
updated: 2025-11-20
tags:
- Ceph
- RGW
- 高可用性
- 可扩展性
- 存储优化
categories: 
- "视频总结"
subtitle: One_Port_Many_Gateways_-_Scaling_RGW_for_Uptime_Production_Resilience_-_Jack_Shen_Bloomberg_LP
---

Bloomberg的存储工程负责人Jack Shen在Ceph社区会议上分享了Bloomberg如何通过Ceph RGW实现零停机重启的方案。

**会议要点**：

* **Bloomberg业务背景**：Bloomberg是一家金融科技公司，其核心业务依赖于处理海量金融数据，并采用混合存储架构，其中Ceph作为核心存储技术，对高可用性要求极高。
* **当前RGW重启痛点**：传统的滚动重启方式在Bloomberg的生产环境中需要4小时才能完成，导致客户端遭遇500错误和延迟，操作复杂且无法满足金融监管要求的快速补丁部署。
* **解决方案**：
    * 利用Linux Kernel的SO_REUSEPORT特性，允许多个进程绑定相同端口，内核充当简易负载均衡器。
    * 修改Ceph代码，使RGW支持端口重用标志。
    * 系统架构变化，实现新旧实例同时运行，旧实例处理现有请求，新实例处理新请求。
* **实施细节**：包括配置变更、systemd调整、自动化脚本等。
* **收益验证**：错误率降低500倍，重启窗口从4小时缩短至接近零，扩展性提升。
* **最佳实践参数**：包括graceful_shutdown_timeout和systemd TimeoutStopSec的计算公式。
* **问答环节要点**：包括监控策略、异常处理等。
* **行动计划**：社区采纳、Backport建议、操作手册等。
* **专业术语保留**：RGW、SO_REUSEPORT、inflight request、rolling restart、LB、SLO、tick data、draining状态等。

**改进后的总结**：

Bloomberg通过利用Linux Kernel的SO_REUSEPORT特性和修改Ceph代码，实现了Ceph RGW的零停机重启。该方案显著降低了重启时间，提高了系统的可用性和扩展性，对于需要高可用性的存储环境具有参考价值。

**可能的错误、误解或遗漏**：

* 原始总结中未提及Bloomberg如何处理自动化过程中的异常情况。
* 原始总结中未详细说明如何实现新旧实例同时运行的具体技术细节。

**改进后的总结内容**：

Bloomberg的存储工程负责人Jack Shen在Ceph社区会议上分享了Bloomberg如何通过Ceph RGW实现零停机重启的方案。该方案利用Linux Kernel的SO_REUSEPORT特性和修改Ceph代码，实现了新旧实例同时运行，显著降低了重启时间，提高了系统的可用性和扩展性。方案包括配置变更、systemd调整、自动化脚本等实施细节，适用于需要高可用性的存储环境。