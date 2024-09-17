---
title: "Morning Lightning Talks | Ceph Days London 2024"
date: 2024-08-23
updated: 2024-08-24
tags:
categories:
- "视频总结"
subtitle: tech
---



### 会议纪要

**会议时间**： 2023年（具体日期未提及）

**参会人员**： Dave Holland（Sanger Institute系统管理员），Jose Palas Perez（IBM SE团队），Ceph社区成员

**会议主题**： Sanger Institute的Ceph存储使用经验分享，Crimson性能测试及优化

**会议内容**：

**一、Sanger Institute的Ceph存储使用经验**

* **Sanger Institute简介**： Sanger Institute是英国人类基因组计划的贡献者，致力于基因组研究和测序。
* **Ceph存储应用**： Sanger Institute使用Ceph存储进行数据存储，包括：
    * OpenStack私有云存储
    * S3对象存储
    * 数据传输
* **Ceph存储优势**： Ceph存储具有高可靠性、可扩展性和性能优势，能够满足Sanger Institute的存储需求。
* **Ceph存储挑战**： Sanger Institute在Ceph存储使用过程中遇到了一些挑战，例如：
    * OSD崩溃
    * 性能瓶颈
    * 监控和可观测性不足

**二、Ceph存储优化方案**

* **解决OSD崩溃**： Sanger Institute通过将垃圾回收池迁移到NVMe存储来解决了OSD崩溃的问题。
* **性能优化**： Sanger Institute通过调整Ceph配置和优化工作负载来提高了Ceph存储性能。
* **监控和可观测性**： Sanger Institute正在实施新的监控系统，以更好地监控Ceph存储性能。

**三、Crimson性能测试及优化**

* **Crimson介绍**： Crimson是Ceph的新一代OSD，具有更高的性能和可扩展性。
* **Crimson性能测试**： Jose Palas Perez对Crimson进行了性能测试，主要关注CPU利用率。
* **测试结果**： 测试结果表明，Crimson能够充分利用CPU资源，并具有良好的性能。
* **Crimson优化**： Sanger Institute计划进一步优化Crimson的性能，例如：
    * 调整CPU核心分配
    * 优化Ceph配置

**四、会议总结**

* Sanger Institute的Ceph存储使用经验为Ceph社区提供了宝贵的参考。
* Crimson性能测试结果表明，Crimson具有很高的性能潜力。
* Ceph社区需要共同努力，优化Ceph存储性能和可观测性。

**后续行动计划**：

* Sanger Institute将继续优化Ceph存储性能和可观测性。
* Ceph社区将共同推进Crimson的性能优化和功能完善。
* Ceph社区将加强监控和可观测性工具的开发。