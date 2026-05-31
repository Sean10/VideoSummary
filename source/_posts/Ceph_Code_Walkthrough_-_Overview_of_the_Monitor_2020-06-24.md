---
categories:
- 视频总结
date: 2020-06-25
subtitle: Ceph_Code_Walkthrough_-_Overview_of_the_Monitor_2020-06-24
tags:
- Ceph
- 分布式存储
- CRUSH算法
title: "'Ceph Code Walkthrough: Overview of the Monitor 2020-06-24'"
updated: 2020-06-25
---



Ceph Monitor代码架构与系统组件概述会议纪要：

### 会议主题：Ceph Monitor代码架构与系统组件概述

### 参会人员：Josh、Greg等

### 会议内容：

1. **Ceph Monitor架构概述**
   - Monitor代码位于`sourcetree`内部，主要文件包括`monitor.h`和`monitor.cc`。
   - Monitor是分布式系统，通过Elector和选举逻辑选举领导者，领导者负责排序更新请求，并授予PM租约。

2. **选举机制**
   - 监视器通过Elector和选举逻辑进行领导者选举。
   - 领导者负责管理更新排序和租约授予。

3. **数据存储与消息处理**
   - 使用LevelDB作为数据存储，MonitorDBStore类进行封装。
   - 基于MonitorMap的消息处理机制。

4. **启动与初始化**
   - Monitor启动流程包括解析标志、创建数据存储、设置消息传递机制等。
   - Bootstrap过程确保Monitor进入法定人数并保持最新状态。

5. **消息与请求处理**
   - Monitor处理多种消息类型，通过`handle_command`函数处理命令。
   - 命令最终分发到特定的Monitor组件进行处理。

6. **更新与提交**
   - 使用Paxos算法进行更新提议，一旦多数系统成员确认，更新即被提交。
   - 定期提议更新以保持系统进度。

### 决定事项：
- 确认了Ceph Monitor的核心架构和关键组件。
- 明确了选举机制、数据存储、消息处理和更新提交的具体流程。

### 后续行动计划：
- 继续优化和更新Monitor的收集系统。
- 深入研究特定Monitor组件的实现细节，如OSD Monitor。

### 会议结束：
感谢Greg的详细讲解，参会人员对Ceph Monitor的架构和运作有了更深入的理解。会议在提问环节结束后圆满结束。