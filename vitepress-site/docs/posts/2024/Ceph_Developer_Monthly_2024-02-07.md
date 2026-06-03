---
title: "Ceph Developer Monthly 2024-02-07"
date: 2024-02-07
updated: 2024-02-14
tags:
  - "Ceph"
  - "分布式存储"
  - "NVMe"
  - "高可用性"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

#### 会议主题：S Dev 月度会议

#### 日期：2024年2月7日

#### 参会人员：Pon、Yal等Ceph开发者

#### 会议议程：

1. **PR审查请求** - Pon的PR，关于monit monitor manager不输出Network ping stats。
2. **NVMe TCP Gateway** - 介绍NVMe-oF的基本概念和其在Ceph中的应用，以及高可用性解决方案。
3. **PR审查请求** - Pon的PR，关于monit monitor manager不输出Network ping stats的后续讨论。
4. **端到端追踪** - Yal的PR，关于端到端追踪功能的实现和测试。

#### 讨论内容：

1. **PR审查请求 - monit monitor manager不输出Network ping stats**
   - Pon提出了一个PR，请求审查关于monit monitor manager不输出Network ping stats的改动。
   - 讨论了该PR的动机和潜在影响，特别是对现有脚本和API的兼容性问题。
   - 决定在下一个主要版本中进行此改动，并更新发布说明。

2. **NVMe TCP Gateway**
   - 介绍了NVMe-oF的基本概念和其在Ceph中的应用。
   - 讨论了NVMe-oF的高可用性解决方案，包括Gateway Group和自动故障转移机制。
   - 展示了如何在Ceph中实现NVMe-oF的高可用性，并讨论了未来的发展方向。

3. **PR审查请求 - monit monitor manager不输出Network ping stats（后续讨论）**
   - 进一步讨论了该PR的影响和是否需要添加配置选项以保留网络ping统计信息。
   - 决定先解决主要问题，后续再考虑添加配置选项。

4. **端到端追踪**
   - Yal介绍了端到端追踪功能的PR，并请求帮助审查测试结果。
   - 讨论了该功能的测试情况和未来的推广计划。
   - 决定将此功能作为Squid版本的阻塞项，并确保测试结果的审查。

#### 决定事项：

- 批准Pon的PR，关于monit monitor manager不输出Network ping stats的改动，并更新发布说明。
- 确认NVMe-oF的高可用性解决方案，并计划在未来版本中实现生产就绪。
- 将端到端追踪功能作为Squid版本的阻塞项，并确保测试结果的审查。

#### 后续行动计划：

- Pon将发送邮件通知社区关于monit monitor manager改动的情况。
- Yal将更新PR，添加性能测试结果的链接，并确保测试结果的审查。
- 继续推进NVMe-oF的高可用性解决方案的开发和测试。

#### 会议总结：

本次会议讨论了多个关键的技术议题，包括NVMe-oF的高可用性解决方案和端到端追踪功能的实现。通过详细的讨论和审查，确定了各个议题的后续行动计划，并确保了技术决策的透明性和社区的参与度。