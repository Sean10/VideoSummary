---
categories:
- 视频总结
date: 2019-07-03
subtitle: 2019-07-01_-_-_Ceph_Orchestration_Meeting
tags:
- Ceph
- 编排
title: "'2019-07-01 :: Ceph Orchestration Meeting'"
updated: 2019-07-04
---




会议纪要：

**会议时间**： 2019年7月（具体日期未提及）

**参会人员**： Joan Miguel, Takata, Billy, Nick Payne, Patrick Connelly, Frida, Taste, Element等

**会议主题**： Ceph社区讨论，包括Python代码统一、API生成、Orchestrator功能、SD移除、Rook与Ceph的集成、Drive Groups等。

**会议关键细节**：

* **Python代码统一**： 讨论了将Ceph中分散的Python代码统一到一个地方的提案，以减少代码重复并提高代码质量。提议得到积极响应，但需要更多人反馈。
* **API生成**： 讨论了API生成的问题，包括何时触发API生成、API生成后的测试等。决定在API发生变化时触发生成，并要求API变更者负责重建文件和提交新生成的API方法。
* **Orchestrator功能**： 讨论了Orchestrator的功能，包括SD移除、替换OSD等。认为目前SD移除的代码不够清晰，可能存在性能问题。
* **Rook与Ceph的集成**： 讨论了Rook与Ceph的集成，包括如何处理SD移除、替换OSD等。认为Rook需要更好的支持Ceph的驱动组功能。
* **Drive Groups**： 讨论了Drive Groups的功能和实现方式，认为将其集成到Ceph Volume中可以简化操作并提高效率。

**决定的事项**：

* 推进Python代码统一的提案，并邀请更多社区成员参与反馈。
* 完善API生成机制，确保API生成的正确性和可靠性。
* 优化Orchestrator的功能，提高代码质量和性能。
* 加强Rook与Ceph的集成，提高Rook对Ceph功能的支持。
* 探索将Drive Groups集成到Ceph Volume中的可能性。

**后续行动计划**：

* 继续讨论并完善Python代码统一的提案。
* 开发API生成工具，并编写相应的测试用例。
* 优化Orchestrator的功能，并修复相关bug。
* 与Rook社区合作，改进Rook对Ceph功能的支持。
* 探索将Drive Groups集成到Ceph Volume中的可能性。

**其他**：

* 提到了Ceph社区每周会议和每月上游会议，鼓励大家积极参与。

**关键词**： Python代码统一、API生成、Orchestrator、SD移除、Rook、Drive Groups、Ceph Volume