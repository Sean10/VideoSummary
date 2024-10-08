---
title: "CDS Reef: Performance Meeting"
date: 2022-04-22
updated: 2022-04-23
tags:
categories:
- "视频总结"
subtitle: tech
---


会议主要讨论了Ceph存储系统的最新更新和问题修复，特别是162h版本的发布情况，以及针对特定性能问题的PR（Pull Request）的更新和审查。会议内容涵盖了以下要点：

1. **版本发布与问题跟踪**：团队正在处理来自Quincy及Pacific 162h版本的后续事宜，包括一个由Adam关闭的PR，该PR的内容被转移到其他VR和其他工作中，剩余部分不再必要或已被加入其他项目。
2. **代码审查**：Corey的PR经过广泛讨论，Casey和Igor已审查并认为其良好，但建议增加配置参数以在必要时恢复到旧的行为模式。
3. **性能优化**：讨论了一个时间基算法的更新，旨在改善ADL分配器的性能，避免重复搜索，简化逻辑，提高可理解性。
4. **文档更新**：关于重写硬件文档的PR，进行了一些关于措辞的建议和讨论，特别是关于时钟速度与核心数量的表述。
5. **关键问题解决**：Corey详细描述了他们遇到的一项严重性能问题，涉及动态分片操作失败导致集群性能急剧下降的问题，并提出了解决方案。该方案将作为默认行为，但也提供了配置选项以便在出现问题时能够关闭。
6. **内存管理与性能测试**：Radik讨论了Crimson项目中的内存管理问题，提出可能的解决方案，并计划进行进一步的测试和优化。