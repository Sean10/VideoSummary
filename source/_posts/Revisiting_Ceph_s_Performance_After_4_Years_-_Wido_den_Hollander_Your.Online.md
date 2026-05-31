---
title: Revisiting Cephs Performance After 4 Years - Wido den Hollander, Your.Online
date: 2025-01-23
updated: 2025-01-24
tags:
- 性能
- 分布式存储
- CRUSH算法
- 高可用性
- 可扩展性
categories: 
- "视频总结"
subtitle: Revisiting_Ceph_s_Performance_After_4_Years_-_Wido_den_Hollander_Your.Online
---

### 会议纪要：Ceph性能回顾与优化讨论

**会议主题**: 回顾Ceph在过去五年中的性能表现及优化策略

**主讲人**: V. Hollander

**会议时间**: 2023年



#### 会议背景与目的
V. Hollander在2019年分享过Ceph在NVMe设备上的性能表现。本次会议旨在回顾过去五年来Ceph的性能变化，并探讨如何通过优化提升Ceph的性能，特别是在低延迟和高IOPS场景下的表现。

#### 关键讨论点

1. **Ceph性能的定义**
   - **性能指标**: 会议讨论了Ceph性能的不同维度，包括带宽、延迟和IOPS。V. Hollander强调，对于大多数应用场景，**延迟**是最重要的性能指标，尤其是在4K块大小的写入操作中。
   - **IOPS vs. Latency**: 尽管许多存储厂商宣传数百万的IOPS，但这些数据通常是在高并发和大块读取的条件下测得的。V. Hollander指出，实际应用中，低延迟的4K写入操作更为关键，尤其是在数据库和虚拟机应用中。

2. **Ceph性能的演变**
   - **2019 vs. 2023**: 通过对比2019年和2023年的性能测试结果，V. Hollander展示了Ceph在延迟和IOPS方面的显著提升。2019年，Ceph在4K块大小下的延迟为772微秒，而2023年通过使用最新的AMD EPYC处理器和优化后的Ceph版本，延迟降低至400微秒以下。
   - **硬件与软件的贡献**: V. Hollander认为，约70%的性能提升归功于AMD EPYC处理器的进步，30%则归功于Ceph OSD代码的优化。

3. **优化策略**
   - **CPU调优**: V. Hollander分享了通过将CPU的C-State设置为1（避免深度睡眠）和将CPU频率设置为性能模式，显著降低了延迟。
   - **网络优化**: 使用25Gbps的网络和BGP路由协议，V. Hollander展示了如何在Ceph集群中实现高效的网络通信。他强调，尽管网络延迟可以进一步优化，但Ceph代码本身是当前的瓶颈。
   - **日志优化**: 关闭OSD的日志记录功能可以进一步减少约15微秒的延迟。

4. **未来展望**
   - **Crimson OSD**: V. Hollander提到Crimson OSD的开发进展，尽管它有望进一步提升Ceph的性能，但目前尚未完全准备好用于生产环境。
   - **IPv6与BGP**: V. Hollander鼓励在Ceph集群中使用IPv6和BGP路由协议，认为这是未来存储网络的发展方向。

#### 决定事项与后续行动

1. **性能优化反馈**: V. Hollander建议用户在发现需要调整Ceph配置时，及时向社区反馈，避免因配置不当导致性能下降。
2. **继续关注Crimson OSD**: 社区应继续关注Crimson OSD的开发进展，并在合适的时机进行测试和部署。
3. **推广IPv6与BGP**: V. Hollander呼吁更多的Ceph用户尝试在集群中使用IPv6和BGP路由协议，以提升网络的可扩展性和性能。

#### 结论
V. Hollander总结道，Ceph的性能在过去五年中有了显著提升，尤其是在低延迟和高IOPS场景下。他强调，用户应根据实际应用需求选择合适的性能优化策略，并持续关注硬件和软件的进步。