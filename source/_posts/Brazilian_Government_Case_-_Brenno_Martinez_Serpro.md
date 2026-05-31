---
categories:
- 视频总结
date: 2019-05-24
subtitle: Brazilian_Government_Case_-_Brenno_Martinez_Serpro
tags:
- Ceph
- 分布式存储
- OpenStack
- Kubernetes
title: "Brazilian Government Case - Brenno Martinez, Serpro"
updated: 2019-05-24
---



会议纪要

会议时间：[请填写具体日期和时间]
会议地点：[请填写会议地点]
参会人员：Brenda Martinez（自力更生工场代表）

会议主题：自力更生工场在巴西政府项目中的Ceph使用经验分享

会议内容：

一、背景介绍
自力更生工场是巴西政府下属的IT公司，提供公共机构和巴西公民的解决方案。公司拥有自己的数据中心，并开发了基于OpenStack、Kubernetes等技术的云解决方案“estelí”。

二、Ceph使用历程
1. 自2017年初，自力更生工场使用Ceph对象存储存储巴西驾驶执照数据，已有超过6000万份驾驶执照。
2. 首次使用Ceph时，由于预算限制，没有购买新的硬件。
3. 在测试阶段，Ceph集群出现性能问题，包括操作缓慢、OSD频繁上下线和Keystone服务不稳定。

三、问题分析与解决方案
1. 发现性能问题的原因是个别桶中存储了过多的对象（数千万）。
2. 解决方案包括：限制每个桶的对象数量、增加Keystone服务器数量、优化代码以复用令牌、升级硬件和软件版本。

四、Ceph应用现状
1. Ceph为巴西驾驶执照提供对象存储服务，确保数据安全。
2. Ceph为云解决方案中的容器提供块和文件系统存储服务。
3. Ceph将很快为Hadoop集群提供存储服务。
4. 正在实施多站点环境。

五、总结
自力更生工场在Ceph的使用过程中遇到挑战，但通过优化和升级硬件，成功解决了性能问题。Ceph已成为其存储解决方案的重要组成部分。

后续行动计划：
1. 持续优化Ceph集群性能，确保稳定运行。
2. 推广Ceph在更多领域的应用，如大数据、人工智能等。
3. 与Ceph社区保持紧密合作，共同推动Ceph技术的发展。