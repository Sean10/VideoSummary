---
title: "Beyond Balancing- How Upmaps Were Used To Avoid Disaster! - Bryan Stillwell, Akamai Technologies"
date: 2025-11-19
updated: 2025-11-20
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### Ceph 技术会议纪要

#### 会议基本信息
- 主讲人：Bryan Stillwell（原 Okami 工程师，现 Clyo Communications 高级 SE 工程师）
- 主题：利用 upmap 解决硬件故障导致的数据分布问题
- 背景：Ceph 集群中因 NVMe retimer 卡硬件缺陷引发的 OSD 异常问题

#### 会议关键内容总结

#### 1. 问题背景：硬件“定时炸弹”
- 现象：内核升级后，多台服务器的 NVMe OSD 在重启时批量消失，集中在特定插槽（如 slot 4-7）。
- 硬件调查：部分 NVMe 盘通过 retimer 卡连接主板，设计缺陷导致启动时电压过高烧毁，影响 PCIe 16x 插槽的 OSD。
- 风险：数据中心断电可能导致大量 retimer 卡损坏，PG 因副本不足进入阻塞状态。

#### 2. 解决方案：Ceph upmap 技术
- upmap 简介：在 CRUSH 算法计算后手动调整 PG 的 OSD 分布，用于平衡数据分布、修复异常 PG。
- 应用场景：规避 retimer 卡风险，通过 `ceph osd pg-upmap-items` 命令替换高危 OSD。
- 工具开发：编写 `retimer_upmap` 脚本自动化处理，动态调整 PG 分布。
- 验证方法：使用 `ceph osd ok-to-stop` 命令验证 retimer OSD 停机是否安全。

#### 3. upmap 的其他应用场景
1. 集群扩容：禁用 balancer → 添加新 OSD → 手动 upmap 迁移数据 → 重新启用 balancer。
2. 快速恢复：将故障 OSD 的 PG 分散到全集群，利用多盘并行恢复加速。
3. 存储后端迁移：如 filestore → bluestore 或未来 bluestore → seastore 的转换。
4. 热点缓解：将高负载 OSD 的 Primary PG 分散到其他 OSD。
5. 故障域迁移：从 host-based 切换至 rack-based 故障域时预分配 PG 位置。

#### 4. 讨论与问答
- Q：OSD 编号是否全局有序？
  - A：实际无序，通过 Ansible 脚本动态生成 retimer OSD 列表并存储为 JSON。
- 其他用例：开发者提到可用 upmap 对集群进行压力测试。

#### 行动计划
1. 短期：在受影响集群中部署 `retimer_upmap` 工具，优先处理含多个 retimer OSD 的 PG。
2. 长期：逐步更换所有有缺陷的 retimer 卡，同步监控硬件厂商的固件更新。
3. 最佳实践：定期备份 upmap 配置（OSD 重启可能导致映射丢失）。