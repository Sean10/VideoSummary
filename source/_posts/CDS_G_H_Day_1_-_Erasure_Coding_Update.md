---
title: "CDS G/H (Day 1) - Erasure Coding Update"
date: 2014-06-24
updated: 2014-06-25
tags:
categories:
- "视频总结"
subtitle: tech
---



### 会议纪要

#### 会议时间：
（未提及具体时间）

#### 会议地点：
（未提及具体地点）

#### 参会人员：
- （未提及具体姓名）
- Veronica（负责Google Summer of Code项目及相关工作）
- L（负责Erasure Coding插件优化）
- Andreas（负责Isa插件原型）

#### 会议主题：

1. **Erasure Coding插件优化**
   - **初始问题**：Erasure Coding的初始代码支持方式较为奇怪，因为没有初始配置文件。
   - **改进计划**：提交了一个pending pull request，添加对通用AR配置文件的支持，以便定义针对QA、本地可修复代码或其他参数变体的作业。
   - **插件优化**：目前主要关注稳定化插件并进行了基准测试，但尚未对性能不佳的部分进行优化。
   - **ARM处理器性能**：讨论了ARM处理器上的性能问题，特别是对于冷存储应用。希望有人能够提供ARM机器进行基准测试。

2. **JF Complete维护和贡献**
   - **当前状态**：SEF中已同步最新稳定版本。
   - **待解决问题**：一个pending pull request（ticket 8071）正在测试中。

3. **本地可修复代码**
   - **基准测试**：已进行基准测试，但未分析调用图以确定4K和1MB解码之间的差异。
   - **性能问题**：存在显著的性能差异，但仍然足够好。

4. **Isa插件原型**
   - **实现**：Andreas已成功实现了一个插件，该插件在Intel CPU上比Gaser更快。
   - **包装问题**：需要确定如何打包该库，因为它可以以静态库或共享库的形式提供。

5. **可靠性模型和代码**
   - **当前状态**：Veronica正在尝试根据当前模型的假设实现Rados Erasure Code。
   - **基准测试工具**：提到了一个用于基准测试Erasure Code的CPU开销的工具。

#### 决定事项：

- 对Erasure Coding插件进行优化，并关注ARM处理器上的性能。
- 继续维护和贡献JF Complete。
- 对本地可修复代码进行基准测试和分析。
- 将Isa插件原型集成到JF中。
- Veronia将继续研究可靠性模型和代码。

#### 后续行动计划：

- L将继续优化Erasure Coding插件。
- Veronica将继续研究可靠性模型和代码。
- Andreas将解决Isa插件的包装问题，并尝试将其集成到JF中。
- 所有参与者将关注ARM处理器上的性能问题。