---
categories:
- 视频总结
date: 2019-05-24
subtitle: Ceph_Practice_And_Usage_In_China_Mobile_-_Zhang_Shaowen_China_Mobile_Suzhou_Software_Technology
tags:
- Ceph
- 分布式存储
- 云计算
- 对象存储
title: "Ceph Practice and Usage in China Mobile - Zhang Shaowen, China Mobile (Suzhou) Software Technology"
updated: 2019-05-24
---


中国移动（Suzhou）软件技术的张晓文在会议中分享了Ceph在中国移动实践与应用的情况。以下是会议的主要内容：

**一、中国移动业务介绍**

Carolyn介绍了中国移动的业务范围，强调其作为全球最大的移动通信运营商的重要性。

**二、中国Beryl云计算产品**

1. **Cloud Recorder**： 为Habana云性能管理提供支持。
2. **Big Cloud**： 为超过30家中国移动专业公司提供IT服务。

**三、中国Beryl云存储解决方案**

1. **Block Storage**： 使用Ceph块存储解决方案，总容量超过40PB，用于统一外交服务平台。
2. **Object Storage**： 使用Ceph对象存储，总容量超过1300PB。

**四、中国Beryl私有云**

1. **一级私有云**： 使用OpenStack平台，通过私有云管理平台实现资源统一管理。
2. **二级私有云**： 总容量30PB，OSD数量超过2600个。

**五、Ceph实践**

1. **CephFS**： 在CephFS基础上构建统一外交服务平台。
2. **Ceph Object Storage**： 支持Swift和S3接口。
3. **Ceph管理平台**： 用于集群部署、资源监控、自动化部署和运维升级等功能。
4. **Ceph硬件配置**： 提供多种硬件配置，满足不同用户需求。
5. **Ceph缓存**： 使用Ceph缓存技术提高数据访问效率。

**六、Ceph Object Storage应用场景**

1. 备份虚拟机镜像。
2. 存储图片、视频等大数据。
3. 支持大数据系统，如Hadoop、Spark等。
4. 托管企业网站、数据网站等。

**七、后续行动计划**

1. 持续优化Ceph管理平台。
2. 探索Ceph在更多领域的应用。
3. 加强Ceph社区贡献。

会议中提及的Ceph相关关键词包括：CephFS、Ceph Object Storage、Ceph Block Device、Ceph缓存、Ceph管理平台、Ceph硬件配置、Ceph缓存技术、Object Storage、Block Storage、Swift、S3等。