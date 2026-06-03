---
title: "How we operate Ceph at scale"
date: 2022-11-10
updated: 2022-11-11
tags:
  - "Ceph"
  - "分布式存储"
  - "自动化"
  - "容器化"
  - "云计算"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

#### 会议主题：DigitalOcean的Ceph存储系统运营实践

#### 主讲人：Matt（DigitalOcean存储系统团队）

#### 会议内容总结：

1. **公司简介**：
   DigitalOcean成立于2012年，是一家提供云服务的公司，以简单性为核心理念。公司提供的产品包括SSD支持的虚拟机（Droplet）、可拆卸的Droplet存储（Volumes）和S3兼容的对象存储（Spaces）等。截至2021年，DigitalOcean在全球拥有八个数据中心。

2. **团队介绍**：
   DigitalOcean的存储系统团队由六名工程师组成，致力于实现团队规模与部署规模解耦，并通过自动化减少对SSH的需求。

3. **Ceph在DigitalOcean的应用**：
   Ceph在DigitalOcean用于块存储和对象存储，支持Volumes和Spaces产品。DigitalOcean运营着46个Ceph集群，其中38个为生产集群，总存储容量超过140PB。

4. **自动化与运营**：
   DigitalOcean使用Chef、Ansible和AWX等工具进行配置管理和集群部署。自动化流程覆盖硬件采购、集群部署和维护的全过程。

5. **挑战与解决方案**：
   DigitalOcean通过自动化和优化配置来应对大规模集群的运营挑战。针对性能问题，如PG peering延迟和RGW索引层性能，团队通过调整参数和优化流程来改善性能。

6. **未来展望与招聘**：
   团队将继续优化自动化流程，探索新的技术解决方案，如Rook，并招聘新的工程师。

#### 决定事项：
- 继续推进自动化和优化Ceph集群的运营流程。
- 探索和评估新的技术解决方案，如Rook，以提高效率和性能。

#### 后续行动计划：
- 持续监控和优化Ceph集群的性能。
- 加强团队建设，吸引和培养新的技术人才。
- 定期回顾和更新自动化流程，确保其适应不断变化的技术和业务需求。

#### 会议结束语：
- 感谢Matt的精彩分享和团队的辛勤工作。
- 期待DigitalOcean在存储领域的进一步发展和创新。