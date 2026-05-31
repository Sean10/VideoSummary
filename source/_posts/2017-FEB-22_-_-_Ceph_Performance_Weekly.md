---
title: "  2017-FEB-22 :: Ceph Performance Weekly  "
date: 2017-02-28
updated: 2017-02-28
tags:
- Ceph
- 分布式存储
- 性能优化
- RBD
- RGW
categories:
- "视频总结"
subtitle: 2017-FEB-22_-_-_Ceph_Performance_Weekly
---



会议纪要

会议时间：2017年2月22日

参会人员：Sage（缺席）、Howai、Nick、Ju、Hae（Nokia）

会议主题：Ceph社区动态、性能测试、RBD性能优化、RGW性能测试

会议内容：

一、Ceph社区动态

1. **P Request进展**：
    * **位图分配器锁定问题**： 已有P Request关注位图分配器在高随机写负载下的锁定和解锁问题，期待后续进展。
    * **RDMA功能**： Howai在RDMA异步消息传递方面取得进展，包括添加性能计数器和零拷贝代码，并讨论了更好的RDMA缓冲区默认值。
    * **缓存优化**： Sage提交了一个基本的PR来优化缓存，以解决某些场景下性能问题。
    * **快速调度**： Sage与Greg合作进行快速调度工作，Greg已进行大量审查，Sage将进行性能测试。
    * **同步提交事务PR**： 等待Sage审查几个补丁。

2. **其他**：
    * Nick分享了RBD性能优化的工作，包括调整写回节流设置以平衡吞吐量和读延迟。

二、性能测试

1. **Blue Store测试**：
    * Nick使用CBT和getput基准测试工具进行Blue Store测试，并与File Store进行了比较。
    * 测试结果表明，对于大型对象写入，Blue Store比File Store快约两倍，并且性能更稳定。
    * 对于小对象，Blue Store的性能优于File Store，并且随着对象数量的增加，性能下降更少。

2. **NVMe测试**：
    * Nick使用NVMe驱动器进行测试，发现网络成为瓶颈，特别是在使用单个RGW服务器时。
    * 尽管性能很高，但CPU使用率也很高，这可能是由于线程模型导致的。

三、RBD性能优化

1. **写回节流设置**：
    * Nick发现默认写回节流设置偏向于吞吐量，而牺牲了读延迟。
    * 通过调整写回节流设置，可以平衡吞吐量和读延迟。

四、后续行动计划

1. Sage将审查同步提交事务PR中的补丁。
2. Nick将继续测试Blue Store和File Store的性能，并探索优化方案。
3. Sage将调查RBD中频繁读取的原因。

五、其他

1. Hae（Nokia）询问了RBD中频繁读取的问题，怀疑与RocksDB压缩和Blue Store有关。
2. Nick建议增加RocksDB数据分区的大小，以解决读取问题。