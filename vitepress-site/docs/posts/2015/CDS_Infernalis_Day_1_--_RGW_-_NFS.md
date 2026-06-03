---
title: "CDS Infernalis (Day 1) -- RGW: NFS"
date: 2015-03-06
updated: 2015-03-06
tags:
  - "Ceph"
  - "NFS"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
**会议纪要**

**会议时间**： 2023年[具体日期]
**会议地点**： [具体地点或线上会议平台]
**参会人员**： [参会人员名单]
**主持人**： [主持人姓名]
**会议主题**： Rados Gateway (RGW) 新功能：通过NFS导出数据

**会议内容**：

1. **议题背景**： 
   - 讨论了RGW的新功能，即通过NFS导出数据。
   - 目前RGW无法直接进行NFS导出，需要通过抽象层或第三方工具实现。

2. **讨论方案**：
   - **方案一**： 创建librgw库，提供数据访问接口，连接Ganisha。
     - 优点：利用现有框架，降低开发难度。
     - 缺点：需要处理用户权限和上下文，可能需要修改Ganisha代码。
   - **方案二**： 创建更高层次的RGW库，在请求处理层面进行操作。
     - 优点：实现简单，易于实现。
     - 缺点：效率可能低于方案一。

3. **方案选择**：
   - 与会人员倾向于选择方案二，即创建更高层次的RGW库。
   - 需要进一步研究其他系统（如Swift、FS Gateway）的NFS导出实现方式，以获取参考。

4. **行动计划**：
   - 收集其他系统的NFS导出实现方式，了解用户需求和期望。
   - 设计并实现更高层次的RGW库。
   - 与Ganisha团队沟通，探讨可能的合作方式。

**关键词**： Rados Gateway, NFS, librgw, Ganisha, S3FS, 用户权限, 请求处理, Rados Gateway, Ceph, Distributed Storage, RGW, Object Storage, File System Storage, Decentralization

**备注**： 会议中提到S3FS和Ganisha的兼容性问题，需要进一步研究解决方案。