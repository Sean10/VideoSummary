---
categories:
- 视频总结
date: 2021-06-15
subtitle: Ceph_Month_2021_-_Dashboard_Update
tags:
- Ceph
- Dashboard
- Pacific 版本
- Quincy 版本
- Orchestration
title: "'Ceph Month 2021: Dashboard Update'"
updated: 2021-06-16
---



Ceph Dashboard 组件负责人 Ernesto Puerta 在 Ceph Month 2021 会议中介绍了 Dashboard 的最新更新和未来规划。以下是会议的关键点：

1. **Pacific 版本亮点**：
   - **Cepheum 集成**：与 Orchestrator 的整合，主要集中在 Cepheum 上，Rook 的支持预计将在 Quincy 版本中完成。
   - **RGW 增强**：支持高级工作流程，如多站点监控和多站点同步监控。
   - **RESTful API**：Dashboard 的 API 正式化，并承诺保持 API 的稳定性。
   - **安全性改进**：包括账户锁定、使用安全 cookies 存储敏感信息等。

2. **Quincy 版本规划**：
   - **用户工作流程**：提供更多高级用户工作流程，如集群安装向导。
   - **多站点与多集群支持**：增强对多站点和多集群的支持，包括 RGW 镜像和 CephFS 镜像。
   - **RGW 高级工作流程**：增加桶策略、生命周期管理、服务器端加密等功能。
   - **可观测性增强**：考虑增加日志聚合功能，以改善日志管理。

3. **性能与用户体验改进**：
   - **性能优化**：讨论了关于 RBD 图像列表等性能问题，计划进行内部清理和重构以提高性能。
   - **用户体验**：计划改进 Dashboard 的登录页面，使其对所有用户更加友好。

4. **后续行动计划**：
   - **社区参与**：鼓励社区成员通过 IRC 频道和 GitHub 参与到 Dashboard 的开发中。
   - **技术分享**：计划举办技术讲座，分享 Dashboard 的开发经验和代码走查。

会议确认了 Pacific 版本的主要更新和 Quincy 版本的发展方向，并确定了性能优化和用户体验改进的具体计划。