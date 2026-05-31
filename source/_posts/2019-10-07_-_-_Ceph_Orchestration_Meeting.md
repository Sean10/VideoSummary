---
categories:
- 视频总结
date: 2019-10-21
subtitle: 2019-10-07_-_-_Ceph_Orchestration_Meeting
tags:
- Ceph
- 分布式存储
- Rook
title: "'2019-10-07 :: Ceph Orchestration Meeting'"
updated: 2019-10-21
---




### 会议纪要

**会议时间**： 2019年10月7日

**参会人员**： [请列出参会人员名单]

**会议主题**： 分布式存储Ceph项目讨论

**会议内容**：

**一、Ceph CI更新**

*   Adam升级了Jenkins版本，并更新了插件，解决了之前CPU使用率过高的问题。
*   系统进行了一些磁盘空间清理，将不再保存所有构建，以减少存储压力。
*   期待升级后构建更加可靠。

**二、外部集群**

*   外部集群的PR即将完成，目前处于最终审查阶段。
*   即使Arches作为要求可能即将被移除，外部集群功能仍对OCS有益。

**三、Ceph Manager模块异步配置**

*   讨论了Ceph Manager模块异步配置的PR，主要关注使用互斥锁（mutex）还是通道（channels）。
*   决定使用互斥锁，因为它在此场景中更简单。
*   建议使用同步组（sync group）来控制并发，以确保在所有模块配置完成后才切换到OSD代码。

**四、卷内信息提取**

*   讨论了从配置映射中提取卷内信息的PR。
*   目前PR已提交，Sebastian开始进行审查。
*   目前CI构建出现问题，无法查看构建日志，需要进一步调查。

**五、布宜诺斯艾利斯会议**

*   Charlotte将在布宜诺斯艾利斯参加一个关于如何为TrueIT项目贡献的演讲。
*   演讲将用西班牙语进行。

**六、其他**

*   会议期间，讨论了一些与编排相关的邮件，但没有紧急事项。
*   会议期间，CI构建出现问题，需要进一步调查。

**后续行动计划**：

*   Adam将继续调查CI构建问题。
*   Charlotte将继续审查卷内信息提取的PR。
*   Sebastian将继续审查外部集群的PR。
*   Charlotte将准备布宜诺斯艾利斯的演讲。

**备注**：

*   会议中提到的英文关键词包括：CI、Rook、Cassandra、Jenkins、mutex、channels、sync group、OCS、Arches、TrueIT。