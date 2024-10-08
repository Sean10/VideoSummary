---
title: "Ceph Crimson / SeaStor OSD 2020-09-02"
date: 2020-09-02
updated: 2020-09-03
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **Tesla 策略测试**: 上周在 Tesla 策略测试方面遇到了新的失败案例，已粘贴到聊天窗口供检查。
- **代码清理**: 创建了 PR 进行恢复相关代码的清理工作，并尝试让 Crimson 通过两个测试：`test_readers.py` 和 `test_stiff_circuit_output`。
- **Excitement Trim 更新**: Excitement Trim 已经更新了 force，请尽快审查并批准。
- **调试工作**: 正在对旧的 map 和 tree 代码进行调试，功能已基本完成，正在进行测试案例的调试。
- **Crimson 焦点**: 主要专注于卸载 RGW 中的 on-map 内容，但也关注 Crimson 的审查工作，特别是 `search_one's_interruptable_elevator`。
- **代码阅读和文档**: 主要在进行代码阅读、审查，并将纸质文档中的图表复制到计算机形式，完成后将分享并操作文档。
- **工具使用**: 使用 Lucidchart 进行图表绘制，已获得许可证。
- **基本空间会计**: 已完成基本空间会计工作，正在进行相关调试，接下来将进行段扫描和清理。
- **中断改进**: 上周仍在改进中断，代码已基本完成，但与 Radic 讨论后发现同时运行 erratic future 和 system future 存在问题，将在会议中讨论。
- **Hybrid Bar 修复**: 上周重现并修复了 Hybrid Bar，已集成到 Ceph 的 osd 实现中，认为这是一个里程碑，并将总结当前状态发送 PR 供审查。
- **测试失败**: 最近在 Unity 的 messenger 系统中发现了一些测试失败，已发送链接进行检查。
- **中断迭代器讨论**: 昨天晚上发布了一个示例问题，讨论了中断迭代器的实现问题，建议将 aerator 重命名为 aerator_and_interrupter，以明确其多重责任。

#### 主要议题
- **中断迭代器的实现和责任分配**: 讨论了中断迭代器的实现问题，包括是否应该将中断功能集成到 aerator 中，以及如何处理多个请求和不同类型的 future 混合使用的问题。
- **性能和代码复杂性**: 讨论了将中断功能集成到 aerator 中的性能影响和代码复杂性，以及是否应该采用更简单的方法，如使用装饰器或构建器来处理中断检查。

#### 决定事项
- **中断迭代器的实现**: 决定采用更简单的方法，如使用装饰器或构建器来处理中断检查，而不是将中断功能集成到 aerator 中。
- **性能考虑**: 尽管存在性能担忧，但决定优先考虑代码的可用性和可维护性，而不是微小的性能提升。

#### 后续行动计划
- **中断迭代器实现**: 将继续探索和实现更简单的中断迭代器方法，如使用装饰器或构建器。
- **性能测试**: 将进行性能测试，以确保新方法的性能影响在可接受范围内。
- **代码审查和批准**: 将继续进行代码审查和批准工作，确保所有更新和修复都能及时合并到主分支。

#### 其他
- **工具使用**: 确认使用 Lucidchart 进行图表绘制，并已获得许可证。
- **文档更新**: 将继续更新和分享文档，确保所有团队成员都能获取最新的信息和指导。

会议结束时，团队成员互相道别，并祝愿大家有一个愉快的一天。