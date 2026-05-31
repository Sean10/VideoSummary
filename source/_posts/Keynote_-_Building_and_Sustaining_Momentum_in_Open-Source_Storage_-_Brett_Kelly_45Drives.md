---
title: Keynote- Building and Sustaining Momentum in Open-Source Storage - Brett Kelly, 45Drives
date: 2025-11-19
updated: 2025-11-19
tags:
- Ceph
- 分布式存储
categories: 
- "视频总结"
subtitle: Keynote_-_Building_and_Sustaining_Momentum_in_Open-Source_Storage_-_Brett_Kelly_45Drives
---

### Ceph 会议纪要：45 Drives 主题演讲《Sustaining Momentum in Open Source Storage》



#### **1. 会议概览**
- **会议名称**: Ceph Conference (CephCon)
- **地点**: 加拿大温哥华
- **演讲嘉宾**: Brett Kelly（45 Drives 技术总监）
- **核心主题**: 
  - 45 Drives 对 Ceph 生态的贡献与角色  
  - Ceph 在实际部署中的挑战与用户反馈  
  - 未来技术方向与社区协作建议  



#### **2. 关键讨论内容**
**(1) 45 Drives 公司介绍**  
- **业务定位**: 硬件制造商和 Ceph 解决方案供应商，提供定制化存储服务器和高密度 JBOD/SAN 设备。  
- **Ceph 参与**: 深度参与 Ceph 项目 8-9 年，支持 Rocky Linux 等开源生态，通过赞助、社区教育、用户支持等方式推动 Ceph 普及。  

**(2) Ceph 的市场定位与成功经验**  
- **“Ceph for Everyone” 策略**: 强调 Ceph 不仅适用于大规模集群，也适用于中小规模场景，通过硬件与软件协同设计降低用户门槛。  
- **用户痛点反馈**: 性能瓶颈、高密度存储挑战、开源采纳风险。  

**(3) 竞争与未来方向**  
- **技术优先级**: 提升 IOPS/美元性价比，优化 NVMe 性能，推动硬件厂商与 Ceph 社区合作。  
- **社区协作**: 提倡“开源共赢”，鼓励更多厂商加入 Ceph 基金会。  



#### **3. 行动计划**
- **短期**: 展示定制化 Ceph 硬件，与厂商合作验证新一代硬盘/NVMe 在 Ceph 集群中的表现。
- **长期**: 推动 Crimson OSD 落地，优化高性能场景下的资源利用率，参与 Ceph 文档改进项目。



#### **4. 保留的关键术语（中英对照）**
- **架构组件**: OSD/MON/MDS, PG, RADOS, CRUSH algorithm  
- **存储类型**: Object/Block/File System Storage (RBD/RGW/CephFS)  
- **技术概念**: Erasure Coding, Thin Provisioning, Tiering, Failure Domain  
- **生态工具**: librados, cephadm, Dashboard  



#### **5. 总结**
45 Drives 从硬件厂商视角提出：Ceph 需平衡**高性能**、**易用性**和**高密度存储支持**，同时加强社区与硬件厂商的协作。此次演讲为后续版本演进提供了明确的用户需求输入。  

（注：具体技术讨论可参考 Brett Kelly 提到的 [45 Drives YouTube 频道](https: //www.youtube.com/45drives) 及 Ceph 基金会文档。）