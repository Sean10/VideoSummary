---
categories:
- 视频总结
date: 2023-07-03
subtitle: Ceph_Performance_Meeting_2023-07-03
tags:
- Ceph
- RocksDB
- Snappy库
- RBD性能
- Elastic Shared Blobs
title: Ceph Performance Meeting 2023-07-03
updated: 2023-07-04
---



### 会议纪要

#### 会议时间
- 日期：2023年7月3日
- 参与者：Igor, Casey, Adam, Corey Snyder, Paul等

#### 主要议题
1. **GCC 13修复与RocksDB更新**
   - 讨论了GCC 13的修复问题，特别是针对RocksDB的FTBFS问题。
   - 决定将修复合并到Reef分支，并确保未来更新Main分支时能同步这些更改。
   - 讨论了RocksDB的版本管理和更新策略，建议定期跟进RocksDB的主要版本更新。

2. **Snappy库的问题与替代方案**
   - 讨论了Snappy库在新的操作系统发行版中导致的编译问题，特别是与RTTI支持的缺失有关。
   - 提出了几种解决方案，包括使用自定义的Snappy分支、禁用系统Snappy库等。
   - 讨论了Snappy的性能和替代方案，建议考虑弃用Snappy，特别是在RGW中的使用。

3. **Elastic Shared Blobs PR的讨论**
   - 讨论了关于Elastic Shared Blobs的PR，特别是关于如何处理部分代码的ifdefs问题。
   - 决定暂不合并PR，而是先进行必要的修改以适应新的运行时条件。

4. **RBD性能测试结果分析**
   - 讨论了RBD在Reef和Quincy版本中的性能测试结果，特别是关于CPU使用率和I/O效率的问题。
   - 提出了一些假设和测试方向，包括调整内存目标大小、不同I/O大小的测试等。

#### 决定事项
- 确认了RocksDB的更新策略，建议定期跟进主要版本更新。
- 对于Snappy库的问题，决定先观察其他发行版的处理方式，再决定具体实施方案。
- Elastic Shared Blobs PR将进行必要的修改后再考虑合并。

#### 后续行动计划
- 继续监控和分析RBD性能测试结果，特别是关于RocksDB和I/O效率的问题。
- 跟进Snappy库的问题，特别是与其他发行版的协调和处理方式。
- 修改并重新审查Elastic Shared Blobs PR，确保其符合新的运行时条件后进行合并。

#### 其他讨论
- 讨论了Debian和Fedora对于Snappy库的处理方式，建议在主问题跟踪器中记录相关问题。
- 讨论了RBD性能测试中的具体细节和可能的优化方向。

#### 会议结束
- 会议在讨论完所有议题后结束，感谢所有参与者的贡献，并祝愿大家有一个愉快的一周。