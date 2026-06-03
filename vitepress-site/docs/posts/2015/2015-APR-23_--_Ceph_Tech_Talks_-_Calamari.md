---
title: "2015-APR-23 -- Ceph Tech Talks: Calamari"
date: 2015-05-04
updated: 2015-05-04
tags:
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
## 改进后的中文总结内容

本次Ceph技术讲座主要围绕Calamari和Romana两个项目展开，这两个项目分别是Ceph的管理API和图形用户界面（GUI）。

**主要内容**：

1. **Calamari和Romana简介**：
   - Calamari作为API，提供所有信息，支持用户界面操作。
   - Romana作为管理监控仪表板，提供Ceph集群的概览，包括集群状态、OSD状态、集群管理功能等。

2. **Calamari后端架构**：
   - 架构包括仪表板、Django REST框架应用、Thulu服务（缓存层）、数据库和Graphite数据存储。
   - 使用Salt和ZeroMQ消息总线与Ceph集群上的代理进行通信，收集集群状态信息。

3. **Calamari未来发展**：
   - 计划增加对硬件状态的监控，如硬盘健康状态、热插拔支持等。
   - 考虑增加更多管理功能，如集群部署、OSD管理等。
   - 欢迎社区反馈和合作。

4. **后续行动计划**：
   - 开发并测试硬件监控模块。
   - 根据社区反馈，确定API扩展的具体功能和优先级。
   - 加强与社区的沟通，鼓励社区成员参与Calamari的开发和测试。

5. **其他讨论**：
   - 讨论了Calamari的包装和部署问题，欢迎社区帮助改进。
   - 提到了一些需要上游贡献的组件，如Diamond，希望社区能参与讨论和贡献。

本次讲座详细介绍了Calamari和Romana的架构、功能以及未来的发展方向，为Ceph的用户和开发者提供了宝贵的参考信息。