---
title: "Ceph Performance Meeting 2021-07-15"
date: 2021-08-23
updated: 2021-08-24
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
- **日期**: 会议日期未明确提及，但根据内容推测为近期。
- **参与者**: Orlando, Mark, 以及其他未明确提及的开发人员。
- **主要议题**: 讨论了Ceph项目的多个技术问题，包括持久性RBD缓存、CephFS性能优化、IBM研究人员的贡献、以及Crimson存储引擎的性能问题。

#### 讨论的主要议题
1. **持久性RBD缓存**:
   - Orlando的同事在测试持久性RBD缓存时遇到了性能问题。
   - 使用GDB和pmp工具进行调试，发现与工作线程池的繁忙状态有关。
   - 测试包括fio、rbd bench和自定义Python程序，结果显示性能不如预期。

2. **CephFS性能优化**:
   - Orlando正在与Dennis Nujab合作，优化CephFS的整体性能。
   - 探讨了Octane SSD和持久内存的使用，以及IO 500测试的结果。

3. **IBM研究人员的贡献**:
   - 一位IBM研究人员提交了多个关于内存分配优化和避免内存复制的PR。
   - 这些PR主要集中在librbd，但也涉及其他部分。

4. **Crimson存储引擎**:
   - 讨论了Crimson的性能问题，特别是与Blue Store的比较。
   - 发现Crimson在某些情况下性能不如预期，主要瓶颈在于reactor线程。

#### 决定的事项
- 需要进一步分析和优化持久性RBD缓存的性能问题。
- 继续进行CephFS的性能优化工作，特别是与Octane SSD和持久内存的结合使用。
- 审查并可能合并IBM研究人员的PR，以提升Ceph的整体性能。
- 对于Crimson存储引擎，需要进一步的工作来解决reactor线程的瓶颈问题。

#### 后续行动计划
- 继续进行性能测试和调试，以解决持久性RBD缓存的问题。
- 完成CephFS的性能优化工作，并考虑在实际环境中进行更多测试。
- 审查IBM研究人员的PR，并与他们合作以确保代码的质量和性能。
- 对于Crimson存储引擎，需要进一步的研究和开发，特别是关于多reactor的支持和优化。

#### 其他备注
- 会议中还提到了一些具体的PR和代码变更，但这些细节主要涉及技术实现，未在此纪要中详细列出。

### 结束语
会议在讨论了各项议题后结束，参与者计划继续各自的工作，并在未来的会议中更新进展。会议结束时，大家互相道别，并期待下周的再次会面。