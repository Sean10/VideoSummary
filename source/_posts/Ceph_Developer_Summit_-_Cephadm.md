---
title: Ceph Developer Summit - Cephadm
date: 2025-09-11
updated: 2025-09-12
tags:
- Ceph
- 分布式存储
- 自动化
- 云计算
categories: 
- "视频总结"
subtitle: Ceph_Developer_Summit_-_Cephadm
---

### Ceph 分布式存储会议纪要

#### 会议主题：
Ceph 编排（Orchestration）与存储管理讨论

#### 参会人员：
Adam、John Mulligan、Redon、Anthony Datri 等

#### 关键讨论议题：

1. **PIO3 加密库加载问题**：
   - 描述：Python 加密库 `cryptography` 在多模块加载时存在冲突，导致部分模块无法接收事件。
   - 解决方案：重构 Dashboard 和 `cephadm` 调用逻辑，避免直接导入 `cryptography`。
   - 后续行动：由 John Mulligan 牵头，调研模块加载优化方案。

2. **Python 工具链升级**：
   - 现状：当前代码库依赖较旧版本的 Python 工具，无法兼容 Python 3.13+。
   - 目标：升级至较新版本工具链，确保兼容性。
   - 行动计划：分阶段更新工具链，优先解决 `cephadm` 的兼容性问题。

3. **`ceph` 命令行工具优化**：
   - 问题：`ceph` CLI 代码结构混乱，缺乏维护团队。
   - 建议方案：将部分功能迁移至 `python-common` 库，标准化代码结构。
   - 后续行动：Adam 联系 Yuri（Manager Core 团队）讨论代码所有权问题。

4. **服务配置变更自动化**：
   - 背景：用户修改服务规格后需手动触发 `ceph orch reconfigure`。
   - 提案：自动检测 Spec 变更并触发服务重配置。
   - 技术方向：在服务类中实现字段级变更检查，支持多种响应动作。

5. **密钥与证书管理**：
   - 当前进展：支持通过 Vault 存储证书，但缺乏统一的 Secrets 管理框架。
   - 未来计划：扩展后端支持，集成 ACME 协议实现自动化证书轮换。

6. **大规模集群优化**：
   - 性能问题：主机元数据刷新和部署任务串行执行导致延迟。
   - 优化措施：并行化部署与删除操作，升级时结合 `ok-to-stop` 检查。

7. **用户需求与功能扩展**：
   - **Central Config 版本控制**：将集群配置纳入 Git 管理，实现基础设施即代码（IaC）。
   - **SMB 增强**：支持离线域加入令牌，扩展 gRPC 接口供云平台直接管理 SMB。

#### 决议事项：
1. 优先调研 K8S Events 模块的使用情况，再决定是否重构或移除。
2. 建立定期工具链更新流程，由团队分阶段执行。
3. 探索代码重构方案，明确维护责任。
4. 设计服务级别的变更响应机制。
5. 推进 ACME 协议集成，列为 Umbrella 版本目标。

#### 后续行动计划：
- 提交模块加载优化提案
- 启动 Python 工具链升级
- 联系 Manager Core 团队讨论 CLI 所有权
- 实现 Spec 变更自动化原型

#### 备注：
需关注核心团队对 Central Config 版本控制的反馈。