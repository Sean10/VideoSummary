---
title: Ceph Benchmarking- An Update on CBTs Vision
date: 2025-06-24
updated: 2025-06-24
tags:
- Ceph
- 存储优化
- 分布式存储
categories: 
- "视频总结"
subtitle: Ceph_Benchmarking_-_An_Update_on_CBT_s_vision
---

在Ceph社区会议中，Lee Sanders就Ceph性能测试工具CBT（Ceph Benchmarking Tool）的改进进行了讨论。以下是会议的主要内容和改进方向：

### 会议基本信息
- 演讲人：Lee Sanders（英国团队性能分析师，专注于纠删码开发）
- 主题：CBT改进——标准化Ceph性能测试与数据分析
- 目标：通过改进CBT，实现确定性、可重复、可比较的性能测试方法，并推动社区统一采用。

### 当前CBT的问题与挑战
- 测试方法不一致，导致结果难以比较。
- 后处理工具不足，影响数据分析的准确性和一致性。
- CBT更偏向开发者，需要用户自行编写编排逻辑，导致社区测试方法碎片化。

### CBT改进方向
- **核心目标**：
  - 单点击标准化测试：支持`block`、`object`、`file`存储类型的统一测试流程，生成可比较结果。
  - 结果对比工具：支持跨版本的性能对比，识别性能回退或优化效果。
  - 社区共享数据：将测试结果上传至GitHub repo，形成社区共享的基准数据集，辅助客户容量规划。
- **关键改进**：
  - 自动化报告生成：支持生成PDF/Markdown格式报告，新增中间数据格式，简化对新`IO exerciser`的支持。
  - 精细化测试控制：引入`total IO depth`参数，优化多卷测试的粒度。
  - 配置透明化：开发`cephadm configuration generator`，在报告中明确标注测试配置。

### 未来计划
- 扩展测试覆盖：聚焦`erasure coding`和`RBD`，下一步支持`NVMe gateway`和`object storage`。
- 增强报告功能：增加性能随时间变化趋势图、CPU/内存利用率监控、`min/max`直方图等。
- 社区协作：呼吁贡献者参与开发。

### 行动项
- 完善`cephadm`配置生成器。
- 社区讨论`object exerciser`工具选型。
- 集成CPU/内存监控到报告。

### 相关资源
- 示例报告：[Lee Sanders的GitHub Repo](https://github.com/leesanders/cbt)（含`erasure coding`测试数据）。

会议鼓励社区成员试用CBT并提供反馈，共同推动Ceph性能测试标准化。