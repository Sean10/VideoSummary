---
title: "Ceph Code Walkthrough: RGW Bucket Notifications with AMQA/Kafka"
date: 2021-04-28
updated: 2021-04-28
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议由Mike Perez主持，Yuval主讲，主题为Reno的Gateway Bucket Notifications，特别是与AMQP和Kafka相关的实现细节。会议主要通过代码走查的方式，详细介绍了如何配置和发送通知。

#### 主要议题
1. **Bucket Notifications概述**
   - 功能简介：当对象创建或删除时，发送通知到预配置的端点。
   - 两种模式：
     - **Push模式**：事件发生时立即发送通知。
     - **Pull模式**：所有通知存储在特殊的pub sub zone中，计划未来弃用。

2. **配置流程**
   - 主要涉及的文件：`rgw_rest_pubsub`和`rgw_rest_pubsub_common`。
   - 配置API：创建、删除、列出主题和通知。
   - 系统对象存储：所有配置信息作为系统对象存储。

3. **数据结构**
   - 定义在`rgw_pubsub.h`中，包括主题、通知、过滤器等。
   - 过滤器类型：前缀、后缀、正则表达式、标签和元数据。

4. **通知发送流程**
   - 从`rgw_ops`开始，涉及`publish_reserve`和`publish_commit`函数。
   - 同步和异步通知处理：
     - 同步：直接发送通知。
     - 异步（持久化）：先存储通知，后续再发送。

5. **端点实现**
   - 涉及Kafka和AMQP的实现细节。
   - 端点管理：初始化、关闭、发送确认等。

#### 决定事项
- 确认了Bucket Notifications的基本功能和配置流程。
- 明确了同步和异步通知的处理方式。
- 确认了端点（如Kafka和AMQP）的实现细节。

#### 后续行动计划
- 继续优化和完善Bucket Notifications的功能。
- 考虑未来可能的新端点类型集成。
- 如果有进一步的问题或需要详细解释，可以通过邮件联系Yuval。

#### 其他备注
- 会议中提到的某些API和模式（如非AWS合规API和Pull模式）计划弃用，不建议在新开发中使用。
- 推荐使用AWS CLI或o3border3工具进行配置，手动编写REST消息较为复杂且不推荐。

#### 会议结束
感谢Yuval的详细讲解和所有参与者的积极参与。希望大家有一个愉快的剩余时间。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。