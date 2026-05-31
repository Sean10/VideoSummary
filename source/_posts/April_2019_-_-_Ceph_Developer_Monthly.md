---
title: "  April 2019 :: Ceph Developer Monthly  "
date: 2019-04-09
updated: 2019-04-09
tags:
- Ceph
- 分布式存储
- 编排
categories:
- "视频总结"
subtitle: April_2019_-_-_Ceph_Developer_Monthly
---



**会议纪要**

**会议时间**： 2019年4月（具体日期未提及）

**参会人员**： 
- Adam（负责内存目标选项）
- Shirred（负责内存目标选项）
- Val（负责监控内存目标）
- Mocha（负责蓝店内存管理）
- Steve（负责OSD缓存）
- Sebastian（负责Orchestrator）
- Patrick（负责Orchestrator）
- Dan（负责监控内存目标）
- Jason（负责RBD MBD）
- Neha（负责Octopus）
- Mike（负责RBD MBD）
- 其他相关人员

**会议主题**：

1. **监控内存目标**：
    - 讨论了为监控设置内存目标选项的需求，类似于USD中的内存目标选项。
    - 讨论了在蓝店中实现内存目标选项的方法，并考虑将其复制到监控中。
    - 讨论了使用优先级缓存接口来管理不同内存缓存的需求。
    - 决定由Shirred负责实现内存目标选项，并更新配置选项。

2. **Orchestrator**：
    - 讨论了不同Orchestrator的实现现状，包括Ansible、Baroque、Kubernetes和DeepSea。
    - 讨论了在Barcelona Ceph会议上讨论Orchestrator路线图的计划。
    - 讨论了DeepSea和SSH Orchestrator的未来方向。
    - 讨论了使用SSH Orchestrator进行初始化部署的方案。

3. **遥测**：
    - 讨论了遥测模块的功能和用途。
    - 讨论了从遥测数据中生成有用报告的需求，例如集群大小分布、安装版本分布和崩溃报告。
    - 讨论了使用Qivana和Kibana等工具进行数据分析和可视化。
    - 决定由End开发有用的报告，并考虑使用Qivana进行交互式查询。

4. **RBD MBD**：
    - 讨论了RBD MBD在Kubernetes环境中的集成和优化。
    - 讨论了使用RBD MBD CLI进行操作的需求。
    - 讨论了在单个RBD MBD守护进程中支持多个RBD连接的需求。
    - 讨论了使用网络接口动态添加和删除块设备的需求。
    - 决定由Mike负责改进RBD MBD与Kubernetes的集成。

5. **Octopus**：
    - 讨论了Octopus的待办事项列表，包括在线响应、内存优化、克隆、恢复和审计。
    - 讨论了将部分恢复和易于恢复的功能合并到Octopus的需求。
    - 讨论了优先级恢复和自适应恢复的需求。
    - 讨论了将Toshiba的RocksDB Roadmap集成到Ceph的需求。

**后续行动计划**：

- Shirred实现内存目标选项并更新配置选项。
- Sebastian和Patrick整理Orchestrator路线图，并在Barcelona Ceph会议上讨论。
- End开发有用的遥测报告。
- Mike改进RBD MBD与Kubernetes的集成。
- Neha和团队完成Octopus的待办事项列表。
- Adam和团队评估Toshiba的RocksDB Roadmap，并考虑集成。

**其他事项**：

- 讨论了Ceph社区的贡献和代码审查流程。
- 讨论了Ceph项目的长期发展方向。