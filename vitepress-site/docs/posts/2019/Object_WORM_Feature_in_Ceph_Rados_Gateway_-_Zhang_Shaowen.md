---
title: "Object WORM Feature in Ceph Rados Gateway - Zhang Shaowen"
date: 2019-05-24
updated: 2019-05-24
tags:
  - "Ceph"
categories:
  - "存储技术"
  - "Ceph技术"
outline: deep
---
### 会议纪要

**会议时间**： 2023年11月（具体日期未提及）

**会议主题**： 介绍和讨论Ceph Rados Gateway中对象WORM（Write Once, Read Many，只写一次，多次读取）功能

**参会人员**： John Shaw（中国移动软件部门），其他与会人员

**会议内容**：

**1. 对象WORM功能概述**

* John Shaw介绍了对象WORM功能，即不可变存储，数据一旦写入，就不能被修改或删除。
* 对象WORM功能在医疗、金融等领域对数据的安全性和可靠性至关重要。

**2. S3对象锁定与Ceph实现**

* S3对象锁定功能通过Ejector Locker实现，防止对象被删除或覆盖。
* Ceph Rados Gateway实现了S3对象锁定功能，并添加了六个新的API，用于设置默认保留期限、对象锁定和法务持有者。
* Ceph提供了对象锁定配置和法务持有者配置。

**3. 后续行动计划**

* 添加测试用例，确保对象WORM功能正常工作。
* 改进支持对象锁定的策略，包括添加更多测试和优化策略。

**4. 总结**

* 对象WORM功能是Ceph分布式存储系统的一项重要功能，可以提高数据的安全性和可靠性。
* Ceph Rados Gateway的对象WORM实现已经取得进展，但仍需进一步完善。

**关键词**： Ceph, Rados Gateway, 对象WORM功能, 不可变存储, S3对象锁定, 保留期限, 法务持有者