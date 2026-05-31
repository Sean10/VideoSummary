---
title: " 2019-09-12 :: Ceph Performance Meeting "
date: 2019-09-20
updated: 2019-09-21
tags:
- Ceph
- 分布式存储
categories:
- "视频总结"
subtitle: 2019-09-12_-_-_Ceph_Performance_Meeting
---

### 会议纪要

**会议时间**： 2019年9月12日
**会议地点**： 线上会议
**参会人员**： Mark, Garrett, Eric, Casey, Sage, Neha, Igor, OSHA, Ping, Adam, Josh, 等
**会议主题**： Ceph分布式存储项目进展讨论

**主要讨论议题**：

* **SATA SSD利用率**： 讨论了SATA SSD的利用率，指出其接近最大吞吐量，具体取决于设备性能和IO负载类型。
* **Luminous代码改进**： 讨论了Luminous代码的改进，包括性能提升和功能增强。
* **CLS代码中的过滤功能**： 讨论了在OSD中的CLS代码中实现过滤功能的改进，包括对性能提升和减少网络使用量的影响。
* **bucket reshaping性能**： 讨论了bucket reshaping的性能，包括在resharding过程中允许客户端写入和优化锁定机制。
* **4K金属块大小**： 讨论了在OMAP中使用4K金属块大小对性能和空间利用率的影响。
* **小对象在OMAP中的存储**： 讨论了在OMAP中使用小对象（小于4K）存储的改进，包括对性能和空间利用率的影响。

**决定事项**：

* 推进Luminous代码的改进，并迁移到Nautilus代码库进行对比测试。
* 评估CLS代码中过滤功能的性能提升和网络使用量减少。
* 研究bucket resharding的性能和优化锁定机制。
* 在OMAP中使用4K金属块大小进行测试，并评估其对性能和空间利用率的影响。
* 对小对象在OMAP中的存储进行改进，并评估其对性能和空间利用率的影响。

**后续行动计划**：

* Mark将继续推进Luminous代码的改进。
* Eric将评估CLS代码中过滤功能的性能提升和网络使用量减少。
* Casey将研究bucket resharding的性能和优化锁定机制。
* Josh将测试4K金属块大小在OMAP中的性能和空间利用率。
* OSHA和Ping将评估小对象在OMAP中的存储改进。

**其他事项**：

* 会议中提到了许多其他PR和改进，包括自动更新、测试、性能优化等。
* 会议讨论了如何进行基准测试和验证回归。
* 会议讨论了如何优化小对象存储。

**关键词**：

* Ceph
* Luminous
* Nautilus
* SATA SSD
* CLS
* bucket resharding
* 4K金属块大小
* OMAP
* 小对象
* 性能优化
* 测试
* 回归

