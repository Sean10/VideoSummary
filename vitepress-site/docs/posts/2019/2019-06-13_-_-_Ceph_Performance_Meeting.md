---
title: "2019-06-13 :: Ceph Performance Meeting"
date: 2019-06-13
updated: 2019-06-14
tags:
  - "Ceph"
  - "分布式存储"
  - "CRUSH算法"
  - "高可用性"
  - "可扩展性"
  - "对象存储"
  - "块存储"
  - "文件系统存储"
  - "性能"
  - "BlueStore"
  - "BlueFS"
  - "RocksDB"
  - "OSD"
  - "MON"
  - "MDS"
  - "PG"
  - "RADOS"
  - "librados"
  - "libcephfs"
  - "RBD"
  - "RGW"
  - "RESTful API"
  - "认证"
  - "授权"
  - "加密"
  - "测试"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： Neha, Sage, Radek, Adams, Jason, Eric, Orlando, Roman, Mark Cogan, Tiago, Igor, Josh 等

**会议内容**：

**一、Ceph 项目进展**

* **Neha**： 完成对 CBT 或病理学任务中新的客户端端点的支持，正在进行最终测试。
* **Sage**： 审查了 PG 映射缓存 PR，该 PR 提供了显著的性能提升。
* **Radek**： 优化输入缓冲区工厂，以改善 Crimson 的性能。
* **Adams**： 开发新的 shirt and blue 存储迭代，需要审查。
* **Jason**： 提交了异步消息 PR，降低了调用次数，并提高了性能。
* **Eric**： 进行多点同步公平性工作，已进入测试阶段。
* **Roman**： 进行 IO 环境引擎工作，需要重新审查。
* **Mark Cogan**： 进行分布式数据缓存 PR，已审查。
* **Igor**： 审查了 mall P PR，该 PR 提高了 Auto Tuning 的启动效率。
* **Tiago**： 进行分布式数据缓存 PR，已审查。

**二、Ceph 测试平台（CBT）**

* **Neha**： CBT 支持客户端端点，可以用于 Crimson 测试和夜间测试。
* **讨论**： 讨论了 CBT 的未来发展方向，包括：
    * 支持更多安装方法，例如 Ansible 后端。
    * 自动发现集群信息。
    * 支持容器化测试。
    * UI 和结果解析工作。

**三、RocksDB**

* **Orlando**： 开发 CBT 图形和结果解析功能。
* **Adams**： RocksDB 的数据布局需要仔细考虑，以避免重复和性能问题。

**四、其他**

* **讨论**： 讨论了其他一些 PR 和议题，例如用户空间 IO 事件、MDS 缓存内存限制自动调整等。

**五、行动计划**

* 完成客户端端点支持测试。
* 完成 PG 映射缓存 PR 的审查。
* 完成输入缓冲区工厂优化。
* 完成 shirt and blue 存储迭代 PR 的审查。
* 继续优化异步消息。
* 完成多点同步公平性测试。
* 重新审查 IO 环境引擎 PR。
* 继续进行分布式数据缓存开发。
* 开发 CBT 图形和结果解析功能。
* 优化 RocksDB 数据布局。
* 其他成员：继续关注和参与 Ceph 项目开发。