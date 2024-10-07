---
title: "Ceph Performance Meeting 2021-11-11"
date: 2021-11-11
updated: 2021-11-12
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **新拉取请求（Pull Request）**: Radic提交了一个引入基于Huge Page的读缓冲区的新拉取请求，这看起来很有趣，但尚不确定在何种情况下会带来帮助。
- **更新拉取请求**: Adam的BlueFS细粒度锁定重试通过了本周的QA测试，之前失败的案例现在通过了。
- **优化请求超时**: 对Beast库的优化拉取请求包含大量基准测试数据和讨论，Casey进行了审查，发现自定义分配器部分并不真正有帮助，因此被移除。
- **性能问题**: 一个关于RGB性能的拉取请求被提及，但未详细讨论。
- **其他拉取请求**: 包括设置最小ALEX大小、减少blob fsck的RAM使用、优化PG移除等，这些都在积极讨论和测试中。

#### 讨论的主要议题
- **构建时间优化**: 讨论了如何优化包构建时间，特别是单线程部分，提出了并行化构建和优化DWZ工具的可能性。
- **快速关闭（Fast Shutdown）**: 讨论了快速关闭的必要性和实际效果，提出了可能的改进措施，如限制关闭时间。
- **客户端请求大小**: 讨论了客户端请求大小的优化，提出了限制最大请求大小和优化内存使用的建议。

#### 决定的事项
- **继续测试和优化**: 对于所有提到的拉取请求，决定继续进行测试和优化，以确保性能和稳定性。
- **关注构建时间**: 决定进一步研究和优化包构建时间，特别是单线程部分。
- **考虑快速关闭的改进**: 考虑对快速关闭功能进行改进，以减少关闭时间和提高一致性。

#### 后续行动计划
- **继续测试和审查拉取请求**: 对所有拉取请求进行进一步的测试和审查，确保它们符合性能和稳定性的要求。
- **优化构建时间**: 研究和实施构建时间的优化措施，特别是并行化和单线程部分的优化。
- **改进快速关闭功能**: 考虑实施改进措施，以优化快速关闭功能，减少关闭时间并提高系统一致性。
- **客户端请求大小优化**: 研究和实施客户端请求大小的优化，以减少内存使用并提高系统性能。

本次会议涵盖了多个技术议题，涉及性能优化、构建时间优化和系统关闭策略等多个方面，后续行动计划旨在确保Ceph系统的性能和稳定性得到持续改进。