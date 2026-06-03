---
title: "2018-JAN-11 :: Ceph Performance Weekly"
date: 2018-01-12
updated: 2018-01-12
tags:
  - "Ceph"
  - "分布式存储"
  - "BlueStore"
  - "RocksDB"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
## 会议纪要

**会议时间**： 2023年11月X日

**参会人员**： Josh、David、Peter、Igor、Nick、Mark、Matt、Adam等

**会议主题**： Ceph分布式存储项目进展及讨论

**会议内容**：

**1. Pull Request进展**：

* Josh正在回补文件存储的随机分割阈值随机化功能。
* David完成了简化字符工作，将所有数据结构移入一个大类，并可能使用全局锁。
* Peter的CRC缓存更改已提交。
* David完成了简化工作，将数据结构移动到一个大类别中。
* Igor的容器清理工作正在测试分支中测试。
* 已撤销aproxice功能，因为它与标准列表大小调用冲突。
* eager的pull request已准备好合并到luminous，修复了amenity溢出问题。

**2. 新功能进展**：

* 第二轮qit加速已添加对Intel处理器加速压缩的支持，但需要解决一些问题。
* Nick正在讨论加密加速问题。
* Igor的容器清理工作已合并，并在测试分支中测试。

**3. 问题讨论**：

* Josh提出了关于BlueStore异步读取的优化问题。
* 讨论了共享独占锁定PG的问题，以及它对读性能的影响。
* 讨论了PG日志问题，包括日志大小、存储和性能影响。
* 讨论了使用不同的键值存储引擎来改进BlueStore的潜力。

**4. 行动计划**：

* Josh将继续优化BlueStore的异步读取功能。
* Nick将研究加密加速问题。
* Igor将解决qit加速问题。
* Adam将研究RocksDB的批处理I/O完成工作，并将其合并到主分支中。
* Nick将研究RocksDB的Fsync问题。

**5. 其他事项**：

* 讨论了SSL漏洞的影响，以及如何进行性能测试。
* 讨论了AIoT读取性能问题。

**会议总结**：

本次会议讨论了Ceph分布式存储项目的多个方面，包括Pull Request进展、新功能进展、问题讨论和行动计划。会议还讨论了一些与性能和安全相关的问题，如BlueStore异步读取优化、共享独占锁定PG、PG日志大小和存储等问题，并制定了相应的行动计划。