---
categories:
- 视频总结
date: 2021-05-26
subtitle: Ceph_Crimson_SeaStore_2021-05-26
tags:
- Ceph
- CRUSH algorithm
- distributed storage
- performance tuning
- scalability
title: "Ceph Crimson/SeaStore 2021-05-26"
updated: 2021-05-27
---




### 会议纪要

#### 关键细节
1. **代码链接问题**：
   - 发现三段代码注释后可解决链接问题，Kifu正在调查原因，并已发送回滚更改的提交。
2. **mclock移植**：
   - 讨论将mclock移植到Ceph组件，特别是PG和OSD（crimson和systole）。
   - 讨论mclock与线程模型的解耦，以及pthread锁的处理。
3. **性能计数器与指标**：
   - 讨论在crimson OSD中使用性能计数器和指标，决定使用seastar metrics。
4. **其他更新**：
   - 讨论extent placement manager的工作进展，ono tree API的合并和测试。
   - 讨论tc malloc属性的复制问题，以及如何区分OSD变体。

#### 决定事项
1. 代码链接问题：暂时注释掉三段代码，Kifu继续调查。
2. mclock移植：初步决定移植mclock，但需进一步讨论。
3. 性能计数器与指标：在crimson中使用seastar metrics。
4. 其他更新：继续推进extent placement manager和ono tree的工作。

#### 后续行动计划
1. 代码链接问题：Kifu继续调查原因。
2. mclock移植：开始讨论和实施移植工作。
3. 性能计数器与指标：在crimson中实现seastar metrics。
4. 其他更新：继续推进相关工作。
5. tc malloc属性的复制：讨论并实施区分OSD变体的解决方案。