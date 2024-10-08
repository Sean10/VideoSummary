---
title: "Ceph RGW Refactoring Meeting 2023-03-29"
date: 2023-03-29
updated: 2023-03-30
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 议题一：用户配额的标记性能计数器
- **讨论内容**：
  - Ali提出关于用户配额的标记性能计数器的需求，特别是希望在Prometheus中查看每个RGW用户的配额分配和当前使用情况（对象数量和字节数）。
  - 讨论了如何通过创建新的用户标签，更新用户统计信息，并将这些信息发送到与现有计数器相同的收集系统中。
  - 提到了需要一个缓存机制来处理用户配额的频繁更新问题。
  - 讨论了是否应该基于事件（如配额更改或强制执行）来发送数据，而不是连续不断地发送。
  - 讨论了如何处理多网关实例中的数据一致性问题。

- **决定事项**：
  - 首先实现一个缓存机制，然后添加用户标签到前端计数器。
  - 需要进行测试以验证系统的可扩展性。

- **后续行动计划**：
  - Ellie将首先实现缓存机制，然后添加用户标签到前端计数器。
  - 进行测试以验证系统的可扩展性。

#### 议题二：GitHub组织的两因素认证要求
- **讨论内容**：
  - 讨论了GitHub组织即将要求的两因素认证（2FA），以及未启用2FA的成员将被移除的问题。
  - 讨论了如何分步骤实施2FA，以避免一次性移除所有未启用的成员。

- **决定事项**：
  - 提醒所有成员尽快启用2FA，以避免失去对GitHub组织的访问权限。

- **后续行动计划**：
  - 所有成员应尽快启用2FA。

#### 议题三：日志数据与桶策略的交互
- **讨论内容**：
  - Emil讨论了如何禁用区域的日志记录，特别是与桶策略相关的日志记录。
  - 讨论了是否可以使用`supports_data_export` API实例来替代当前的日志数据标志。

- **决定事项**：
  - 应该使用`supports_data_export`和`supports_data_import`来替代区域范围的标志。

- **后续行动计划**：
  - Emil将研究如何调整初始化顺序以解决依赖问题，并更新相关的PR。

#### 其他讨论
- 会议还讨论了同步模块和多站点配置的一般问题。

#### 会议结束
- 会议在讨论完所有议题后结束，感谢所有参与者的贡献。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。