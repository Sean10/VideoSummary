---
title: Ceph on ARM- The Next Tentacle
date: 2025-06-24
updated: 2025-06-24
tags:
- Ceph
- 分布式存储
- 性能优化
- 云计算
categories: 
- "视频总结"
subtitle: Ceph_on_ARM_-_The_Next_Tentacle
---

Ceph on ARM- The Next Tentacle会议纪要主要讨论了Ceph在ARM 64架构上的支持计划以及性能测试结果。

#### 会议要点：

1. **ARM架构支持计划**：
   - 自2024年6月25日起，Ceph将正式支持ARM 64架构，首次在SAF客户端中实现。
   - 该计划不仅关注技术优化，还旨在推动商业化落地，如企业级收益。
   - ARM客户端GA将在本月（6月）内发布。

2. **关键时间节点**：
   - ARM客户端GA：本月（6月）内。
   - 社区实验室重启：从Red Hat北卡罗来纳设施迁移至IBM亚利桑那设施，重新开放后可使用Ampere捐赠的ARM硬件。
   - ARM集群支持目标：2024年底前完成。
   - 支持范围扩展至IBM SEF、Red Hat SEF、OpenShift Data Foundation (ODF) 及 Red Hat Enterprise Linux (RHEL)。

3. **待完成事项**：
   - 社区层面：重启社区实验室，确保ARM硬件可用；完善CI/CD测试（支持ARM而非仅x86）；性能调优；制定ARM集群的参考架构设计。
   - 流程层面：指定社区联络人（PTL）、定期会议机制。
   - 呼吁贡献：欢迎开发者提交补丁或参与协作。

4. **ARM性能测试分享**：
   - 测试环境：临时搭建的集群（非生产级架构），含3节点、24 OSD、4 pools（Bluestore后端）。
   - 对比平台：Ampere One（自研核心） vs. Ampere Ultra（Neoverse核心）。
   - 性能结果：Ampere One在4KB随机写入中达到400K IOPS，读取性能成功饱和磁盘带宽，核心利用率更优，能效比显著优于Ultra。
   - 未来方向：进一步测试更大规模磁盘组；核心差异：Ampere One采用高密度自研核心，效率优于Neoverse。

5. **限制与注意事项**：
   - 推荐个人实验环境使用Ubuntu/Debian/Fedora或Arbian，但明确排除Raspberry Pi的企业支持。

6. **后续行动项**：
   - 短期：完成ARM客户端GA发布；推进社区实验室硬件迁移与重启。
   - 中期：完善ARM集群的自动化测试与性能调优；制定参考架构文档。
   - 长期：2024年底前实现完整ARM集群支持；探索ARM加速扩展（如加密/压缩卸载）。

7. **Q&A重点**：
   - Ampere One自研核心与Ultra的Neoverse相比，前者更高效。
   - Ampere One在更高IOPS下仍保持更好能效比。

会议强调了Ceph在ARM架构上的重要升级，以及性能测试中展现出的积极成果。未来，Ceph社区将致力于优化ARM架构的支持，并推动其在企业级应用中的落地。