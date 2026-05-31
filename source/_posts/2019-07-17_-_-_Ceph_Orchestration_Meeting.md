---
categories:
- 视频总结
date: 2019-07-22
subtitle: 2019-07-17_-_-_Ceph_Orchestration_Meeting
tags:
- Ceph
- 分布式存储
- 编排
- 性能优化
title: "'2019-07-17 :: Ceph Orchestration Meeting'"
updated: 2019-07-22
---



### 会议纪要

**会议时间**： 2019年7月17日

**参会人员**： [所有参会人员姓名]

**会议主题**： Ceph分布式存储项目进展及问题讨论

**会议内容**：

**一、Ceph Orchestrator性能优化**

1. **问题**： Ceph Orchestrator，尤其是Dashboard和Kiva的使用，性能较慢。
2. **解决方案**： 
    - 探索使用Costner改进的Rook模块，以提高性能。
    - 讨论将Rook模块优化纳入Ceph Orchestrator的拉取请求中。

**二、Ceph Dashboard集成**

1. **问题**： Ceph Dashboard集成存在问题，如服务显示不正常、软盘和磁盘代码位置不合理等。
2. **解决方案**：
    - 确认软盘和磁盘代码功能在Ceph中已有实现，但位置不太合理。
    - 讨论优化软盘和磁盘代码功能，使其更易于使用。

**三、Ceph Rook模块**

1. **问题**： Ceph Rook模块需要更多关注和维护。
2. **解决方案**：
    - 鼓励Young更多参与Ceph Rook模块的上游维护。

**四、Ceph测试Orchestrator**

1. **问题**： Ceph测试Orchestrator的功能需要增强，以更好地支持集成测试。
2. **解决方案**：
    - 鼓励开发人员增强测试Orchestrator的功能，以便返回更多数据。

**五、其他**

1. 讨论了Ceph Inventory命令的改进，以便更好地支持磁盘识别。
2. 讨论了Ceph Dashboard的命名一致性问题和SSH Orchestrator的简单设置。

**后续行动计划**：

1. Costner将修改Rook模块，以提高Ceph Orchestrator性能。
2. 开发人员将优化Ceph Dashboard和Rook模块。
3. Young将更多参与Ceph Rook模块的上游维护。
4. 开发人员将增强测试Orchestrator的功能。