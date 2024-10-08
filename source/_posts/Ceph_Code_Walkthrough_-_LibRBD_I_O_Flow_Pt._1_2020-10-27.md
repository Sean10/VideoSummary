---
title: "Ceph Code Walkthrough: LibRBD I/O Flow Pt. 1 2020-10-27"
date: 2020-11-02
updated: 2020-11-03
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议主题：** Ceph 中 RADOS Block Device (RBD) 的 I/O 路径解析

**主讲人：** Jason Dillman

**会议内容总结：**

1. **介绍与目标：**
   - Jason Dillman 是 Ceph 项目中 RADOS Block Device (RBD) 部分的 Tech Lead。
   - 本次会议的目标是详细解析从 librbd API 到 OSD 的读写请求的转换过程。

2. **数据组织：**
   - RBD 将块设备视为一个从字节零开始的扁平文件。
   - 内部通过 librbd 将这些请求分解为更小、更易管理的对象，存储在 Ceph 存储集群中。
   - 每个 RBD 图像默认使用 4MB 大小的固定对象进行存储。

3. **API 接口：**
   - librbd 是一个用户空间库，提供 C 和 C++ 以及 Python 绑定。
   - 常见的集成包括 QEMU，它通过 librbd 与 RBD 交互。
   - API 提供同步和异步的读写、刷新和丢弃操作。

4. **内部实现：**
   - API 方法首先在 `librbd.cc` 文件中定义，负责维护 API 的稳定性和 ABI。
   - 内部将同步调用转换为异步调用，并通过异步完成回调处理。
   - I/O 请求首先被转换为图像范围的 I/O，然后进一步分解为对象范围的 I/O。

5. **I/O 分发层：**
   - I/O 分发层包括多个子组件，如排队层、服务质量层、独占锁层等。
   - 核心层负责将 I/O 请求发送到 Ceph OSD 集群。

6. **对象 I/O 分发：**
   - 对象 I/O 分发层处理具体的对象读写请求。
   - 包括缓存层、加密层、日志层等，最终通过核心层将请求发送到 OSD。

7. **测试与未来计划：**
   - 有大量的单元测试代码，确保每个组件的正确性。
   - 未来可能会有更多的会议来深入探讨这些细节。

**后续行动计划：**
- 安排更多会议以深入讨论 RBD 的 I/O 路径和其他相关主题。
- 参与者可以通过邮件列表等方式与 Jason Dillman 联系，提出问题或建议。

**会议结束：**
- 感谢 Jason Dillman 的详细讲解和所有参与者的积极参与。

**备注：**
- 本次会议由于时间限制，未能覆盖所有细节，未来会议将继续探讨。