---
title: "Ceph Performance Meeting 2020-08-06"
date: 2020-08-06
updated: 2020-08-07
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **PR提交情况**: 本周收到了两份新的PR，均来自Majiang Peng。他还提交了其他非性能相关的PR，显示出活跃的贡献。
- **性能优化**:
  - 一个PR旨在避免在BlueStore环境中一次性刷太多数据，以减少延迟峰值。
  - 另一个PR旨在减少BlueFS中的缓冲列表重建，复杂度较高，需要进一步审查。
- **RGW更新**: 两个更新的PR涉及rgw的d3n缓存更改，Matt和Mark Hogan正在审查。
- **未解决的PR**: 仍有一些PR需要审查，特别是来自ajianpang的PR，目前无人深入研究。
- **内存优化**: 需要进一步研究Igor的内存减少PR和会议主持人的双缓存优化。

#### 讨论的主要议题
- **性能优化**: 讨论了如何通过改进缓存管理和数据刷新策略来优化性能，特别是在BlueStore环境中。
- **缓存策略**: 讨论了缓存命中和未命中的影响，以及如何通过调整缓存大小和刷新策略来优化性能。
- **压缩测试**: Adam分享了关于压缩测试的进展，强调了均匀分布在测试中的不适用性，建议使用更接近实际工作负载的分布。

#### 决定的事项
- **PR审查**: 确认了需要进一步审查的PR，包括性能优化和缓存策略相关的PR。
- **缓存策略**: 讨论了双缓存策略的潜在益处和挑战，决定需要进一步的实现和测试。

#### 后续的行动计划
- **PR审查**: 继续审查和讨论未决的PR，特别是性能和缓存相关的PR。
- **缓存策略**: 进一步研究和实现双缓存策略，特别是在BlueStore环境中。
- **压缩测试**: 继续进行压缩测试，特别是使用更接近实际工作负载的数据分布。
- **性能监控**: 考虑在CBT测试中加入性能监控，特别是在测试开始和结束时收集性能计数器。

#### 其他讨论点
- **缓存命中和未命中的影响**: 讨论了缓存命中和未命中对性能的影响，以及如何通过调整缓存策略来优化性能。
- **实际工作负载的模拟**: 讨论了如何更准确地模拟实际工作负载，特别是在压缩测试中。

#### 结论
会议涵盖了多个关键议题，包括性能优化、缓存策略和压缩测试。决定继续审查和讨论未决的PR，并进一步研究和实现双缓存策略。同时，考虑在CBT测试中加入性能监控，以更好地理解性能影响因素。