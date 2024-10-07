---
title: "Ceph Code Walkthroughs: Paddles"
date: 2021-10-07
updated: 2021-10-08
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
本次会议是一个代码走查，主要介绍Paddles，这是我们集成测试框架的关键组件。Paddles是一个数据库包装器，用于存储和处理测试节点信息、任务状态更新等。

#### 讨论的主要议题
1. **Paddles简介**：
   - Paddles是一个数据库包装器，用于存储Toothology运行和任务信息，以及所有测试节点信息。
   - 使用PostgreSQL作为数据库。

2. **Toothology任务调度流程**：
   - Toothology调度器将任务添加到Beanstalk队列，并返回一个唯一的任务ID。
   - 任务ID和任务配置参数存储在PostgreSQL中。
   - 任务状态更新也通过Paddles进行。

3. **Paddles的模块结构**：
   - 使用轻量级Web框架Pecan，遵循MVC模式。
   - 主要关注模型和控制器部分。
   - 模型定义数据库操作函数，如启动事务、提交和回滚。
   - 控制器使用对象分派路由策略，将HTTP请求映射到控制器和方法。

4. **Paddles的配置和启动**：
   - 配置文件包含服务器特定配置，如主机、端口、Pecan应用配置等。
   - 使用Pecan的transaction hook处理数据库事务。

5. **模型和控制器详细介绍**：
   - 模型部分定义了节点、任务和运行的表结构和操作。
   - 控制器部分处理HTTP请求，如获取节点信息、锁定和解锁节点、创建和更新任务等。

6. **Alembic数据迁移框架**：
   - 用于在不停止运行的情况下修改数据库模式。
   - 通过创建修订号来管理数据库模式的版本。

7. **测试和部署**：
   - 使用Green Unicorn作为生产环境的服务器，启动多个进程处理请求。
   - 编写了多个测试用例，包括模型测试和控制器测试，以及复杂的并发更新测试。

8. **Paddles的持续改进**：
   - 正在添加排队机制，以消除对Beanstalk的依赖。
   - 新的排队机制允许在任务排队后更新任务优先级等特性。

#### 决定的事项
- 确认Paddles的关键功能和结构，以及其在Toothology集成测试框架中的作用。
- 确认使用Alembic进行数据库模式迁移的方法。
- 确认使用Green Unicorn进行生产环境部署的方法。

#### 后续行动计划
- 继续开发和完善Paddles的排队机制。
- 持续进行代码测试和优化，确保系统的稳定性和性能。
- 定期进行代码走查和知识分享，以提高团队的技术水平和协作效率。

#### 其他
- 鼓励团队成员在会议录像中留下问题或评论，以便进一步讨论和澄清。
- 计划在下个月进行另一个代码走查，具体主题待定。

---

本次会议详细介绍了Paddles的架构和功能，以及其在Toothology集成测试框架中的应用。通过本次会议，团队成员对Paddles有了更深入的了解，并为后续的开发和优化工作奠定了基础。