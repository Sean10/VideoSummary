---
title: "Ceph Performance Meeting 2021-07-29"
date: 2021-07-29
updated: 2021-08-24
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
categories:
  - "会议纪要"
  - "存储技术"
outline: deep
---
## 改进后的中文总结内容

### 会议纪要

#### 主要议题与讨论内容

1. **PRs本周更新**
   - 会议主持人提出对`memstor`的重新架构，引入了`vector object`，并发现`buffer list`性能与`vector object`相当，甚至略优。
   - `braddock`提出智能变更，允许`alien store`使用任何经典对象存储，包括`blue store`。
   - 合并了关于设置`osd client message cap`的PR，预计能解决生产环境中与心跳超时相关的问题。
   - `AVX 512 erasure coding`的实现因作者无法继续测试而被关闭。

2. **其他技术讨论**
   - 讨论了`pg log`的更新，特别是关于`acceptable rollback info`的变更。
   - `rgw tracing`优化和`bufferless c-string`处理优化正在讨论中。
   - 进行了关于`finisher`的CPU自动释放优化的详细讨论。

3. **SMR存储技术**
   - 讨论了`SMR`（Shingled Magnetic Recording）存储技术在`blue store`中的实现状态和未来发展方向。
   - 目前`SMR`实现处于初级阶段，需要进一步的工作来完善功能和性能。
   - 讨论了如何更好地支持`SMR`硬件，包括可能的硬件测试环境和模拟测试方法。

#### 决定事项

- 进一步研究和优化`memstor`在写路径上的效率问题。
- 对`SMR`存储技术的实现进行更深入的代码审查和功能测试。

#### 后续行动计划

- 会议主持人将重新审视`memstor`的性能问题，并尝试找出其效率低下的原因。
- 安排一次代码审查会议，以确定`SMR`存储技术的下一步开发方向和具体实施计划。
- 探索在现有测试环境中引入`SMR`硬件的可能性，以便进行更真实的性能测试。

#### 其他信息

- 讨论了关于`crimson`性能和效率的比较研究，特别是在小数据集和大数据集上的表现差异，以及`memstor`和`blue store`在不同场景下的效率对比。

### 结论

本次会议主要围绕Ceph存储系统的性能优化和`SMR`存储技术的实现进行了深入讨论，确定了后续的研究和开发方向。会议强调了代码审查和性能测试的重要性，并计划通过实际硬件测试来验证和优化系统性能。