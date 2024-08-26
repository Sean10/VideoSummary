---
title: "2019-11-27 :: Ceph Orchestration Meeting"
date: 2019-11-27
updated: 2019-11-28
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**日期：** [未提供具体日期]

**参会人员：** Sebastian, Keifa, 以及其他相关人员

**会议目的：** 讨论Ceph Orchestrator的性能问题及后续行动计划。

**主要议题及讨论内容：**

1. **会议时间调整：**
   - Sebastian提出由于Paul无法参加晚间会议，建议调整会议时间或取消。
   - 决定取消当前会议，后续会议将在Sebastian休假回来后重新安排。

2. **Ceph Orchestrator性能问题：**
   - 当前Orchestrator使用单线程池（kernel threads）处理后台操作，导致性能受限。
   - 讨论了三个主要的使用案例：部署OSD、设备列表刷新（device ls refresh）和服务列表刷新（service ls refresh）。
   - 提出增加线程池数量至10以提升性能，但仍存在局限性。
   - 探讨了使用parallel SSH或pssh工具来并行处理多个主机上的操作，以提高效率。

3. **GitHub浏览技巧：**
   - 分享了在GitHub上快速查找文件的技巧，通过输入“T”并搜索文件名。

4. **Dashboard更新：**
   - OSD创建的相关Pia已获批准，等待QA测试。
   - 讨论了预览功能的进展。

**决定事项：**

- 取消当前会议，直至Sebastian休假回来。
- 研究使用parallel SSH或pssh工具来解决Orchestrator的性能问题。
- 继续推进Dashboard的更新和预览功能。

**后续行动计划：**

- Sebastian休假期间，团队将通过Dashboard stand-up进行同步。
- 研究并评估parallel SSH或pssh工具的可行性，并考虑维护或采用现有项目。

**其他事项：**

- Sebastian休假期间，团队成员需自行处理升级等相关事宜。
- 会议结束时，Sebastian祝愿大家假期愉快，并感谢大家的努力。

**会议结束：**

- 会议在Sebastian的祝福中结束，Keifa和其他成员也表达了良好的祝愿。

**备注：**

- 会议中提到的技术术语和工具如“kernel threads”、“parallel SSH”、“pssh”等，是计算机科学和Ceph分布式存储领域的关键技术点。