---
title: "CDS Infernalis (Day 1) -- CephFS && OpenStack"
date: 2015-03-06
updated: 2015-03-06
tags:
  - "CephFS"
  - "OpenStack"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议主题**： CephFS 多租户特性及 OpenStack 相关议题

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： Sage、Danny、Josh、Mark 等

**会议内容**：

**一、OpenStack 相关议题**

1. **第三方测试**：
    * 目前 OpenStack 代码库中缺乏第三方测试支持，需要建立测试环境并在代码提交或审查时进行测试。
    * 建议由 Red Hat OpenStack 团队、Marantis、Canonical 等组织承担测试工作，并将 CephFS 测试集成到其测试中。

2. **CephFS for Manila**：
    * 讨论了三种将 CephFS 与 Manila 集成的方法：
        * 使用默认驱动程序，将卷映射到 Manila VM 并导出 NFS。
        * 使用 Ganesha 驱动程序，将现有共享文件系统重新导出为 NFS。
        * 开发原生驱动程序，使客户机直接映射 CephFS 文件系统。
    * 建议使用 Ganesha 驱动程序，因为它提供了网络隔离和多租户支持。
    * 需要解决 Manila 对共享文件系统功能的要求，例如快照和克隆，以及与 Swift 对象存储兼容性问题。

3. **Swift 兼容性**：
    * CephFS 与 Swift 的兼容性存在一些差距，例如命名空间处理、对象版本和过期等。
    * 建议更新 Swift 测试套件，并修复 Swift 兼容性相关的缺陷。
    * 可以考虑实现 Swift 对象版本，但优先级较低。

**二、多租户特性**

1. **安全**：
    * 需要实现以下安全特性：
        * 读取权限
        * 根权限限制
        * 基于路径的挂载限制
        * 数据路径安全
        * 命名空间隔离

2. **性能**：
    * 需要优化性能，例如减少网络跳数和优化数据路径。

**三、行动计划**

1. 搭建 OpenStack 测试环境，并集成 CephFS 测试。
2. 开发 Ganesha 驱动程序，并将其集成到 Manila 中。
3. 更新 Swift 测试套件，并修复 Swift 兼容性缺陷。
4. 实现多租户安全特性。
5. 优化 CephFS 性能。

**四、其他**

1. 需要收集用户对多租户功能的需求，以便确定优先级。
2. 需要考虑在多租户环境下共享数据的问题。


[改进后的总结中保留了以下关键词]：

- CephFS
- OpenStack
- Manila
- Multi-tenancy
- OpenStack Integration
- CephFS
- Ganesha driver
- Swift
- Security
- Performance
- Testing
- Compatibility
- Storage Cluster
- Cloud Computing