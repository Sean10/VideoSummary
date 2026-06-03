---
title: "2019-07-15 :: Ceph Orchestration Meeting"
date: 2019-07-22
updated: 2019-07-22
tags:
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
在2019年7月15日的Ceph Orchestration Meeting中，参会人员讨论了多个关键议题，包括Ceph驱动器组、Rook项目进展和社区发布计划。

**会议内容**：

1. **驱动器组讨论**：
   - 讨论了驱动器组的全局信息处理方式，以及如何在本地和全局层面进行处理。
   - 讨论结果包括在Sapphire层或Orchestrator层以上完成驱动器组元描述，由Orchestrator负责处理驱动器组，并确保其一致性和可靠性。

2. **Rook项目进展**：
   - 讨论了Rook 1.1版本发布计划，目标是在8月中旬完成特性开发，8月底发布1.1版本。
   - 确定了最低SEF版本为Mimic 13.4，以支持新的功能。
   - 讨论了Rook与Ceph集成，包括对RGW的关键修复和Dashboard中Orchestrator性能的优化。

3. **后续行动计划**：
   - Sebastia和Joshua将继续讨论驱动器组的问题，并完善相关文档。
   - Kieffer将优化Orchestrator的性能，并实现Orchestrator API的introspection功能。
   - Blaine将负责Rook 1.1版本的发布计划。
   - 所有参与者将根据讨论结果，继续推进Ceph和Rook项目的开发。

会议总结了Ceph驱动器组和Rook项目的进展，并制定了后续行动计划，为项目的进一步发展奠定了基础。