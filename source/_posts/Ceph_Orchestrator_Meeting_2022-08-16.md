---
categories:
- 视频总结
date: 2022-08-17
subtitle: Ceph_Orchestrator_Meeting_2022-08-16
tags:
- Ceph
- Distributed Storage
- RGW Multi
- Site
- Configuration Automation
- Cephadm
title: "Ceph Orchestrator Meeting 2022-08-16"
updated: 2022-08-17
---




在2022年8月16日的Ceph Orchestrator会议上，与会者就几个关键议题进行了深入讨论：

1. **RGW Multi-Site 配置支持**：与会者讨论了简化RGW（RADOS Gateway）多站点配置的必要性，当前需要手动执行多个步骤，使用RGW管理二进制文件，过程繁琐。Sebastian提出了在Safe ADM中引入新的层级结构，通过关键字`kind`区分不同类型的规范，以简化配置过程。

2. **技术细节讨论**：讨论了当前实现和相关提案，包括在Python通用部署中，不同的类支持各种规范，如`host_spec`和`service_spec`。Sebastian建议添加一个通用的`spec`类，如`rgw_spec`或`generic_spec`，作为所有不同规范的基类。

3. **实施策略**：确保配置过程的原子性，成功则全部成功，失败则回滚。同时，确保创建顺序正确，如先创建realm，再创建zone group，最后创建zone。还要保证向后兼容性，确保新实现不会破坏现有功能。

4. **前端与后端讨论**：讨论了如何更好地呈现配置信息，是否需要引入类似Kubernetes的`kind`和`version`概念。后端讨论了如何实现具体的创建命令，是否可以直接使用现有的RGW管理模块。

会议决定：
- 初步决定采用Sebastian的提案，引入`kind`关键字，并确保向后兼容性。
- 后续行动包括进一步研究RGW管理模块的功能，开发后端逻辑，实现基本的创建命令，暂缓前端讨论，待后端实现后再确定最佳呈现方式。

其他议题：
- 讨论了Podman版本兼容性问题，提出了一些临时解决方案和未来可能的改进方向。

会议对RGW Multi-Site配置支持的实现进行了深入讨论，确定了初步的实施方向和后续行动计划。同时，对Podman版本兼容性问题进行了讨论，提出了一些临时解决方案。