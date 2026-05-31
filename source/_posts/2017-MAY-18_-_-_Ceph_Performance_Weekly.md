---
categories:
- 视频总结
date: 2017-05-26
subtitle: 2017-MAY-18_-_Ceph_Performance_Weekly
tags:
- Ceph
- 分布式存储
- 性能优化
- BlueStore
- BlueFS
- RocksDB
- OSD
- MON
- MDS
- PG
- RADOS
- librados
- libcephfs
- RBD
- RGW
- RESTful API
- 认证
- 授权
- 加密
- 测试
title: "'2017-MAY-18 :: Ceph Performance Weekly'"
updated: 2017-05-26
---




### 会议纪要

**会议时间**： 2017年5月18日

**参会人员**： 多名开发人员，包括Dave、Mark、Laurens、Igor、Nick、Stage、Marlon、Peter等。

**会议主题**： 讨论Ceph存储系统相关的开发进展、性能优化、bug修复以及后续行动计划。

**会议内容**：

**一、关键进展**

* **BlueStore优化**：
    * 探讨了异步消息传递对减少锁争用和优化BlueStore性能的好处，计划进行测试。
    * 讨论了优化管理器和BlueStore，并计划进行测试。
    * 讨论了BlueFS同步选项的bug修复，并计划合并。
* **其他优化**：
    * 讨论了CRC计算优化，并计划进行测试。
    * 讨论了避免内存复制的优化，并计划进行测试。
    * 讨论了KB sink PR，并计划进行测试。
    * 讨论了scale优化，并计划进行测试。
    * 讨论了Katie finisher的性能改进，并计划进行进一步测试。
* **Katie finisher**：
    * 讨论了异步消息传递锁争用问题。
    * 讨论了BlueStore的随机写性能。
* **其他议题**：
    * 讨论了deferred right的优化。
    * 讨论了BlueStore的I/O性能。
    * 讨论了RocksDB同步问题。
    * 讨论了PowerPC平台的优化。

**二、决定事项**

* 对BlueStore进行异步消息传递和锁优化测试。
* 对CRC计算优化进行测试。
* 对KB sink PR进行测试。
* 对Katie finisher进行进一步测试。
* 对deferred right进行优化。
* 对BlueStore的I/O性能进行优化。
* 对RocksDB同步问题进行修复。
* 对PowerPC平台的优化进行讨论。

**三、后续行动计划**

* 各开发人员将继续进行代码开发和测试。
* 定期召开会议，讨论开发进展和问题。
* 及时更新文档和代码库。

**四、其他**

* 会议中还讨论了一些其他议题，例如RBD的优化、OSD的优化等。

**总结**：

本次会议讨论了Ceph存储系统开发的相关议题，并制定了后续的行动计划。开发人员将继续努力，优化Ceph的性能和功能，为用户提供更好的存储解决方案。