---
title: "2019-04-11 :: Ceph Performance meeting"
date: 2019-04-12
updated: 2019-04-13
tags:
  - "Ceph"
  - "分布式存储"
  - "BlueStore"
  - "OSD"
categories:
  - "视频总结"
outline: deep
---
会议纪要

**会议时间**： 2023年某月某日

**会议地点**： 线上会议

**参会人员**： Aaron, Jason, Sage, Kevin, Adam, 等（部分人员未出席）

**会议内容**：

**1. 本周新提交的Pull Request (PR)**:

* Aaron提交了一个PR，修改了OP Q的工作方式，旨在改善锁竞争行为并提高性能，目前还在等待性能数据。
* LaBarbera团队提交了d1 PR，Jason正在审查，需要通过QA。
* Crimson团队提交了性能改进PR，这些改进每周都会定期提交。
* Ian的Blue Store后端I/O引擎合并到内核中，这可能会消除一些阻塞行为并提高性能。
* 一些调试和性能测试工具PR被关闭。
* Space Iterator工作已合并到其他PR中，用于分片工作。
* OSD内存策略工作未通过测试，需要解决。
* Messenger I/O操作PR和对象存储PR可能很快会合并。

**2. 本周讨论的主要议题**：

* **Priority Cache Manager PR**： 本PR已经通过审查，正在等待Patrick再次审查。
* **内存目标设置**： 有用户在OSD中看到大量堆内存使用，但设置的目标内存只有4MB，而实际使用的是6GB。建议用户禁用透明大页。
* **Blue Store**： Blue Store节点在Brock TB块缓存和Blue Store中都会获得双重缓存。建议禁用存储Blue Store节点的组合族的块缓存，以避免双重缓存。
* **对象存储后端**： 目前对象存储后端使用的是自定义mm存储工作，Adam正在研究。
* **性能改进**： 一些性能改进工作正在进行中，例如Blue Store和Crimson的性能改进。

**3. 决定的事项**：

* 继续关注Aaron的PR，等待性能数据。
* 审查LaBarbera团队的d1 PR，并确保通过QA。
* 持续关注Crimson和Blue Store的性能改进工作。
* 解决OSD内存策略工作的问题。
* 研究禁用存储Blue Store节点的组合族的块缓存的方法。

**4. 后续行动计划**：

* Aaron提供Blue Store PR的性能数据。
* Jason完成LaBarbera团队的d1 PR的审查工作。
* 研究禁用存储Blue Store节点的组合族的块缓存的方法。
* Adam提供对象存储后端的研究进展。
* 继续关注其他性能改进工作。

**5. 其他事项**：

* 下周可能会更新SeaStar和Adam的图表工作。