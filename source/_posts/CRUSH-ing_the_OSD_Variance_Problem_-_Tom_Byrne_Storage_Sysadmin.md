---
categories:
- 视频总结
date: 2019-05-24
subtitle: CRUSH-ing_the_OSD_Variance_Problem_-_Tom_Byrne_Storage_Sysadmin
tags:
- Ceph
- 分布式存储
- CRUSH算法
- 高可用性
- 可扩展性
title: "CRUSH-ing the OSD Variance Problem - Tom Byrne, Storage Sysadmin"
updated: 2019-05-24
---




Tom Byrne，Rutherford 下午实验室的系统管理员，在会议中讨论了Ceph分布式存储系统中OSD利用率管理的问题。以下是会议的关键点：

**会议背景**：

* Tom在Rutherford下午实验室负责与研究人员合作存储数据，自2015年开始关注Ceph，主要关注高性能物理实验的对象存储。
* Echo是他们运行的最大的高性能计算集群，已投入生产两年，目前容量超过40PB，主要服务于大型实验设施。

**OSD利用率管理**：

* Echo集群中OSD利用率存在较大差异，导致空间浪费和数据分布不均。
* 初始方案使用reweight by utilization尝试平衡OSD利用率，但效果不佳。
* 改进方案引入upmap balancer，通过强制移动placement groups到空置或利用率较低的OSD，有效平衡了集群利用率，并将利用率差异从40%降低到5%，增加了6PB的额外可用空间。
* upmap balancer的优势包括更高效地平衡集群利用率、更灵活地控制placement groups的分布、提高集群的可用性和可靠性。

**添加OSD**：

* 添加OSD时需要逐步增加权重，并监控集群状态。
* 添加新OSD时，可能存在placement groups在现有OSD之间移动的情况，导致数据分布不均。
* 解决方案包括使用upmap map将placement groups移动到新OSD，使用工具监控placement groups的移动情况，确保数据分布均匀。

**结论**：

* Tom强调了upmap balancer在平衡Ceph集群利用率方面的重要性，并分享了添加OSD的经验和挑战。
* 后续行动计划包括继续使用upmap balancer平衡Echo集群的利用率，持续监控集群状态，确保数据分布均匀，评估添加更多OSD的可行性。

**改进点**：

* 原始总结中未提及Echo集群的规模和重要性，以及upmap balancer的具体作用。
* 改进后的总结更详细地描述了OSD利用率管理和添加OSD的过程，并强调了upmap balancer的优势。
* 保留了计算机科学/ceph相关领域的英文原文关键词。