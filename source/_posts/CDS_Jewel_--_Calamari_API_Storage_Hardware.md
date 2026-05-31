---
categories:
- 视频总结
date: 2015-08-03
subtitle: CDS_Jewel_--_Calamari_API_Storage_Hardware
tags:
- Ceph
- 分布式存储
title: "CDS Jewel -- Calamari/API/Storage/Hardware"
updated: 2015-08-04
---




### 会议纪要

#### 一、硬件API规划与实现

**会议主题**： 讨论并规划Calamari硬件API的规划和实现。

**主要议题**：

* 通过提供硬件API，使Calamari能够了解其背后的存储，以便在硬件出现问题时，能够分析影响并帮助管理员识别合适的硬件进行更换。
* API设计，包括设备ID、驱动器信息、制造商、版本、序列号等。
* 使用全球ID作为持久标识符，并确保其在不同场景下的一致性。
* 处理智能数据（Smart Data），包括存储位置、频率和缓存策略。
* 与现有工具（如libblockid）集成。

**决定事项**：

* 将智能数据存储在Calamari中，并定期查询设备以获取数据。
* 使用libblockid等现有工具进行智能数据查询。
* 考虑使用缓存机制以避免频繁查询设备。

**后续行动计划**：

* 完成API的设计和实现。
* 在Calamari中集成智能数据。
* 测试API的功能。

#### 二、Calamari包发布

**会议主题**： 讨论Calamari包的发布和计划。

**主要议题**：

* Calamari的最新稳定版本已发布，并可在download.com/calamari下载。
* 提供Calamari的安装指南，并链接到aether pad和GitHub的readme文件。
* 目前支持SUSE、Ubuntu和CentOS。
* 探索其他发行版的支持。

**决定事项**：

* 发布Calamari包。
* 提供安装指南。
* 探索其他发行版的支持。

**后续行动计划**：

* 发布Fedora 21+的包。
* 探索其他发行版的支持。

#### 三、Calamari故障排除

**会议主题**： 讨论如何改进Calamari的故障排除。

**主要议题**：

* Calamari使用salt进行自动化，但salt的最新版本可能会与Calamari冲突。
* 需要改进故障排除文档，使其更易于使用。
* 简化Calamari的依赖关系，使其更易于安装和使用。

**决定事项**：

* 改进故障排除文档。
* 简化Calamari的依赖关系。

**后续行动计划**：

* 改进故障排除文档。
* 简化Calamari的依赖关系。

#### 四、其他讨论

* 讨论了Calamari测试框架的设置和运行。
* 讨论了Calamari的未来发展方向，包括集成其他工具和功能。

**总结**：

本次会议讨论了Calamari硬件API的规划和实现、Calamari包的发布、Calamari的故障排除以及Calamari的未来发展方向。会议确定了后续行动计划，并讨论了相关技术问题。