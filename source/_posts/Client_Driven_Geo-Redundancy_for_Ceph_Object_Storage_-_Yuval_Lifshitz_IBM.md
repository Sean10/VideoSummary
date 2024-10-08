---
title: "Client Driven Geo-Redundancy for Ceph Object Storage - Yuval Lifshitz, IBM"
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Redis Gateway在IBM中的应用及多站点复制改进

#### 会议时间：[具体日期]

#### 参会人员：
- Yuval（IBM，Redis Gateway项目负责人）
- Liave和Omar（学生，参与项目开发）
- 其他相关技术人员

#### 会议内容：

1. **项目背景**：
   - Yuval介绍了Redis Gateway项目，该项目是由Red Hat和Reichmann University在以色列的合作项目Connect的一部分。
   - 感谢Liave和Omar两位学生在该项目中的贡献。

2. **多站点复制的挑战**：
   - 多站点（multi-site）设置在集群中是一个复杂且常有问题的系统。
   - 地理复制（Geo replication）和地理冗余（Geo redundancies）面临网络问题、性能问题、数据日志和集群间通信问题。
   - 动态重分片（dynamic resharding）和其他问题增加了系统的复杂性。

3. **用户控制的需求**：
   - 当前系统高度异步，用户难以了解数据何时安全同步。
   - 项目旨在通过增加新的桶通知（bucket notifications）来增强用户对复制系统的控制。

4. **解决方案介绍**：
   - 在Redis Gateway中增加新的桶通知类型，通知用户对象何时安全同步到一个区域（Zone）。
   - 通过Kafka或其他通知机制，用户可以订阅这些通知并据此采取行动。

5. **演示和实施细节**：
   - 演示了如何在两个站点（Zone A和Zone B）之间设置主题（topic）和通知。
   - 展示了对象上传到主站点（Zone A）后，如何在备份站点（Zone B）同步并发送通知。

6. **后续改进和行动计划**：
   - 需要改进多站点间的信息同步，特别是主题和通知的配置。
   - 计划增加更多类型的通知事件，如删除事件和版本桶创建事件。
   - 学生已经开始编写一个围绕Boto3 Python库的包装器，以简化端到端的功能。
   - 鼓励社区成员参与完善和扩展这些功能。

7. **问题与回答**：
   - 讨论了通知的具体内容和如何自定义通知数据。
   - 确认了通知机制与AWS S3的兼容性和扩展性。

#### 后续行动：
- 完善多站点间的信息同步机制。
- 增加更多类型的通知事件。
- 完成并发布Boto3 Python库的包装器。
- 社区成员参与测试和反馈，以进一步优化系统。

#### 会议结束：
- Yuval感谢大家的参与，并鼓励大家提出问题和建议。
- 会议在掌声中结束。

---

**备注**：本会议纪要基于Yuval的介绍和讨论内容整理，旨在记录会议的关键细节和后续行动计划。