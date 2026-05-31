---
categories:
- 视频总结
date: 2020-09-30
subtitle: Ceph_Code_Walkthrough_-_Patrick_Donnelly_-_Metadata_Servers_2020-09-29
tags:
- Ceph
- CephFS
- 分布式存储
title: "'Ceph Code Walkthrough: Patrick Donnelly - Metadata Servers 2020-09-29'"
updated: 2020-10-01
---



### 会议纪要

#### 会议概述
本次会议由Patrick Donnelly主讲，深入讲解了Ceph文件系统（CephFS）的元数据服务器（MDS）代码结构和工作机制。会议主要围绕MDS的核心组件、启动流程、状态管理以及与FS Map和MDS Map的交互展开。

#### 主要议题
1. **CephFS代码结构**：
   - CephFS代码主要位于Ceph源码树中的`mds`目录。
   - 主要组件包括MDS本身、客户端目录（`client`）和OSD对象缓存器（`osdc`）。

2. **MDS启动与状态管理**：
   - MDS启动从`main`函数开始，进行信号处理、参数解析和全局初始化。
   - MDS启动后处于待机状态，等待分配到CephFS集群中的位置。
   - MDS通过监听新的MDS地图来处理状态转换。

3. **MDS Rank**：
   - MDS Rank用于管理MDS在CephFS文件系统中的状态，包括故障转移和恢复过程中的状态转换。

4. **FS Map与MDS Map**：
   - 监控器通过FS Map跟踪集群中的所有MDS。
   - MDS Map记录了MDS的状态、文件系统名称、最大MDS数量等信息。

5. **MDS Server**：
   - 处理客户端请求的主要模块，包括客户端重新连接、会话管理和请求处理。

6. **MDS Locker**：
   - 管理分布式锁，确保客户端对元数据的访问权限。

7. **MD Cache**：
   - 管理MDS的全局缓存，包括inode、目录片段和子树的管理。

#### 决定事项
- 会议详细讲解了CephFS的MDS组件及其代码结构，为参与者提供了深入理解CephFS内部工作机制的机会。

#### 后续行动计划
- 继续定期举行Ceph代码讲解会议，以帮助社区成员更好地理解和贡献Ceph项目。
- 鼓励参与者在下次会议前阅读相关代码，以便更深入地参与讨论。

#### 其他信息
- 会议中没有提出具体问题，但鼓励参与者在需要时通过聊天或BlueJeans提出问题。
- 下次Ceph代码讲解会议将在下个月举行。

#### 会议结束
感谢Patrick的精彩讲解和所有参与者的积极参与。希望大家继续关注和支持Ceph项目。