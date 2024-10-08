---
title: "Ceph Science Working Group 2021-09-22"
date: 2021-10-07
updated: 2021-10-07
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议基本信息
- **时间**: 会议开始于整点后几分钟
- **主持人**: 未明确提及
- **参与者**: 一群管理Ceph集群的人员，主要在科学或研究计算环境中工作

#### 会议内容概述
- **会议目的**: 开放讨论，分享Ceph集群管理经验，讨论近期影响Ceph集群的问题和挑战。
- **会议记录**: 会议被录制并上传到YouTube频道。

#### 主要讨论议题
1. **新成员介绍**:
   - 新成员Joel来自国家太阳能天文台，正在开始Ceph之旅，目前有6PB的存储在Octopus中，主要用于S3服务。

2. **Ceph集群配置和经验分享**:
   - Joel询问关于Ceph集群的经验和建议，特别是关于S3服务的性能优化。
   - 讨论了NVMe SSD的使用，特别是在处理大量小对象时的性能问题。
   - 分享了关于Ceph集群在网络故障后的恢复经验，强调了耐心和系统自我恢复的重要性。

3. **Ceph版本升级和硬件问题**:
   - 讨论了从Nautilus到Octopus的升级经验。
   - 提到了硬件问题，特别是硬盘和NVMe的固件更新问题，以及这些更新对集群稳定性的影响。

4. **Ceph集群的可用性和恢复**:
   - 分享了在网络故障和电源故障后的集群恢复经验，强调了集群的自我恢复能力和数据完整性的重要性。

5. **Ceph的未来发展**:
   - 讨论了Ceph的容器化部署和Rocky Linux的使用，以及这些新技术对现有集群管理的影响。

#### 决定事项
- 继续关注Ceph的最新版本和硬件更新，确保集群的稳定性和性能。
- 计划进行Ceph版本的升级，特别是从Nautilus到Octopus或Pacific。

#### 后续行动计划
- 定期举行会议，每两个月一次，下一次会议计划在11月24日。
- 继续分享和讨论Ceph集群管理的经验和挑战，特别是在处理大规模数据和复杂环境下的性能优化。

#### 其他备注
- 会议记录和讨论内容将被上传到YouTube频道供后续参考。
- 鼓励新成员加入并分享他们的经验，以促进知识共享和技术交流。

---

本次会议为Ceph集群管理人员提供了一个宝贵的交流平台，通过分享经验和讨论问题，有助于提升集群管理的效率和可靠性。