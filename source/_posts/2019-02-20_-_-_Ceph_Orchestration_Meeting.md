---
categories:
- 视频总结
date: 2019-04-16
subtitle: 2019-02-20_-_-_Ceph_Orchestration_Meeting
tags:
- Ceph
- 编排
title: "'2019-02-20:: Ceph Orchestration Meeting'"
updated: 2019-04-17
---



本次会议主要讨论了Ceph存储系统中的SSH Orchestrator相关问题及其进展。以下是会议的关键细节和主要议题：

1. **SSH Orchestrator问题修复**： 昨日SSH Orchestrator出现运行失败的问题，现已修复，并计划在QA测试成功后进行到Orchestrator的迁移。

2. **开发环境**： 分享了基于Noah的集中式版本开发环境，该环境运行在Ubuntu上，表现良好。

3. **Orchestrator功能改进**：
   - 讨论了暂停和恢复命令处理器的执行，以优化性能。
   - 讨论了错误处理，建议在权重方法中仅用于操作进度。

4. **CLI模块**： 
   - 讨论了CLI模块的改进，包括添加`--weight=false`参数，使CLI返回立即，以及优化CLI命令的输出格式。

5. **其他议题**：
   - **Tipsy**： 修改以提供TLS双向认证，并进行删除测试。
   - **DeepSea**： 启用DeepSea Orchestrator模块，并在开发环境中配置，解决了DeepSea部署问题。

会议决定：
1. 完成SSH Orchestrator到Orchestrator的迁移。
2. 优化Orchestrator功能。
3. 优化CLI模块。
4. 完成Tipsy和DeepSea的改进。

会议中提到了SSH Orchestrator、CLI、Tipsy、DeepSea等关键术语，并讨论了涉及Orchestrator改进和CLI模块优化的多个议题。