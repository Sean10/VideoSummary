---
categories:
- 视频总结
date: 2017-05-26
subtitle: 2017-MAY-25_--_Ceph_Tech_Talk_-_Ceph_on_ARM
tags:
- Ceph
- 分布式存储
- 开源
- 性能优化
title: "'2017-MAY-25 -- Ceph Tech Talk: Ceph on ARM'"
updated: 2017-05-26
---



### 会议纪要

**会议主题**： Ceph on ARM 工作进展及未来计划

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**：

* Sage Weil（Red Hat）
* Steve Capper（dom）
* Pankaj Brijwasi（Cavium）
* Vikram（Cavium）
* Davey (SUSE)
* Danny (Deutsche Telekom)
* Jeff Chu（ARM）

**会议内容**：

**1. 上游构建和基础设施现状**

* Sage 介绍了 Ceph on ARM 的历史和现状，包括 ARM 32 位和 ARM 64 位支持。
* 目前，Ceph on ARM 的上游构建和测试主要依赖于社区贡献的硬件和 Jenkins 服务器。
* 由于缺乏足够的硬件和 Jenkins 服务器资源，目前还没有进行大规模的 ARM 构建和测试。

**2. 社区工作进展**

* Steve Capper 介绍了 dom 公司在 Ceph on ARM 领域的工作，包括 OpenStack Swift 与 Radars 网关集成、内核参数和设置参数优化等。
* Pankaj Brijwasi 介绍了 Cavium 公司在 Ceph on ARM 领域的工作，包括基于 ARM 平台的数据中心处理器、Cavium ARM 服务器等。
* Davey 介绍了 SUSE 公司在 Ceph on ARM 领域的工作，包括提供 ARM 64 位平台上的 Ceph 企业存储产品。
* Danny 介绍了 Deutsche Telekom 公司在 Ceph on ARM 领域的工作，包括性能测试、构建 Luminous 平台、安全性等。

**3. 下一步行动计划**

* Sage 提出了以下行动计划：
    * 完善上游 Ceph on ARM 构建，使其成为每个发布版本的一部分。
    * 在 Jenkins 上设置 CI/CD 流程，以测试每个 pull request 和 master 分支。
    * 提供可用的 ARM 二进制文件。
    * 探索使用 OpenStack 作为构建和测试平台的可能性。
* Jeff Chu 提出了以下行动计划：
    * 建立一个协调机制，以了解社区中正在进行的工作。
    * 鼓励社区成员参与 ARM 构建和测试工作。
    * 探索在 ARM 平台上实现架构特定优化的机会。

**4. 其他讨论**

* 会议讨论了以下问题：
    * 是否应该继续支持 ARM 32 位构建？
    * 如何提高 ARM 构建和测试的效率？
    * 如何鼓励更多社区成员参与 Ceph on ARM 的工作？

**5. 会议总结**

本次会议讨论了 Ceph on ARM 的工作进展和未来计划，并确定了下一步行动计划。社区成员对 Ceph on ARM 的兴趣和投入令人鼓舞，相信在大家的共同努力下，Ceph on ARM 将会取得更大的进步。