---
categories:
- 视频总结
date: 2023-05-17
subtitle: Ceph_Days_NYC_2023_-_NVMe-over-Fabrics_support_for_Ceph
tags:
- Ceph
- 分布式存储
- CephFS
title: "'Ceph Days NYC 2023: NVMe-over-Fabrics support for Ceph'"
updated: 2023-05-18
---




Ceph Days NYC 2023 会议讨论了 Ceph 对 NVMe over Fabrics 支持的最新进展。以下是对会议内容的总结：

1. **背景与动机**：该项目始于三年前，旨在探索在 DPU 硬件上支持 Ceph 的可能性。由于 DPU 硬件性能限制，团队决定引入 NVMe over Fabrics 以提升性能和集成度。

2. **技术实现**：
   - Ceph 集群通过 NVMe over Fabrics Gateway 与客户端通信，支持 TCP、RDMA 和 Fiber Channel。
   - 控制路径使用 Python 进程通过 gRPC 服务进行配置管理，数据路径采用 SPDK 进行高效数据传输。
   - 引入 Gateway 组概念，通过 Ceph 的 watch-notify 机制和轮询机制保持配置同步，支持多路径优化和负载均衡。

3. **性能测试**：在实验室环境中，通过优化和增加并发客户端实例，性能已接近原生性能的 92%。

4. **未来计划**：
   - 引入 Discovery Service 和集中式发现功能。
   - 考虑增加身份验证和加密支持，采用插件架构以灵活支持不同的安全方法。
   - 与 Intel 合作，探索 ADNN 技术，优化数据路径选择。

5. **可用性与支持**：当前版本已可下载试用，但仍在进行更多测试和优化。计划在 Reef 版本中发布初始版本。

6. **决定事项**：确认了 NVMe over Fabrics 在 Ceph 中的实现方案和性能优化方向，并确定了未来版本的功能增强和优化计划。

7. **后续行动计划**：继续进行性能测试和优化，开发 Discovery Service、身份验证和加密功能，与社区合作收集反馈并改进产品。

会议强调了 Ceph 对 NVMe over Fabrics 的支持将提高性能和可用性，并探讨了对未来存储解决方案的影响。