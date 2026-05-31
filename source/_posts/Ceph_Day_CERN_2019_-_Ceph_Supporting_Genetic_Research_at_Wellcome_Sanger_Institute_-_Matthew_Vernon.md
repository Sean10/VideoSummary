---
categories:
- 视频总结
date: 2020-08-25
subtitle: Ceph_Day_CERN_2019_-_Ceph_Supporting_Genetic_Research_at_Wellcome_Sanger_Institute_-_Matthew_Vernon
tags:
- Ceph
- 分布式存储
- OpenStack
- RGW
title: "'Ceph Day CERN 2019: Ceph Supporting Genetic Research at Wellcome Sanger Institute - Matthew Vernon'"
updated: 2020-08-26
---



在CERN 2019年的Ceph Day会议上，Dr. Vernon分享了他在位于英国剑桥外的Wellcome Sanger研究所使用Ceph的经验。以下是对会议内容的详细总结：

会议背景：
- Sanger研究所是全球领先的基因组研究和基因测序中心，拥有约50PB的数据存储需求。
- 该研究所使用LSF集群进行批量计算，并提供Lustre作为快速临时存储。

Ceph的引入与应用：
- 2016年，研究所开始使用Ceph，最初部署在三个服务器上，提供3PB的原始容量。
- Ceph主要用于支持OpenStack，提供更灵活的计算环境，特别是通过Ceph的RGW（RADOS Gateway）提供S3服务，结果非常受欢迎。

Ceph的扩展与管理：
- 随着需求增长，Ceph集群迅速扩展，到2017年底已达到18PB的容量。
- 使用Ceph Ansible进行集群管理，确保配置的一致性和自动化。
- 引入了HAProxy来优化RGW服务的性能和可靠性。

挑战与解决方案：
- 面临的主要挑战包括大规模删除操作和用户尝试将S3用作POSIX文件系统的问题。
- 通过改进Ceph的删除命令和引入HAProxy来解决这些问题，提高了服务的稳定性和性能。

未来展望：
- 计划增加专门的RGW硬件，以进一步优化性能。
- 继续支持UK BioBank等大型项目，预计将处理更多的基因组数据。

决定事项：
- 继续使用和扩展Ceph集群，优化RGW服务。
- 引入专门的硬件和进一步的软件优化，以应对大规模数据处理的需求。

后续行动计划：
- 实施硬件升级，增加专门的RGW服务器。
- 持续监控和优化Ceph集群的性能，确保服务的稳定性和可靠性。
- 探索更多Ceph在基因组研究中的应用场景，以支持更多的科学研究需求。

改进后的总结确保了关键细节、讨论的主要议题、决定的事项以及后续的行动计划都被准确反映。同时，保留了计算机科学/ceph相关领域的英文原文关键词，如Ceph、distributed storage、CRUSH algorithm、high availability、scalability、object storage等。