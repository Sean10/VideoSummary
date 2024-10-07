---
title: "2020-05-18 :: Ceph Orchestration Meeting"
date: 2020-05-18
updated: 2020-05-19
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议时间
- 日期：具体日期未提供
- 时间：具体时间未提供

#### 参会人员
- Travis
- John
- Lucy
- Tommy
- 其他未提及姓名的参与者

#### 主要议题
1. **Ceph Y版本发布**
   - Y版本即将发布，预计今天或本周内完成。

2. **CLI重构讨论**
   - 讨论了如何统一`apply`和`daemon ad`命令，特别是在使用Porticus和subversion 3.5或6的情况下。
   - 提出了一个文档草案，建议将讨论转移到会议中，并创建了一个小型文档来记录相关内容。
   - 讨论了如何围绕Beck（一个中心构建块）重新设计整个CLI，包括对象和操作（verb）的概念。
   - 提出了一些新的子命令，如`spec modify`，以简化修改流程。
   - 讨论了过渡期的挑战，包括旧命令的兼容性和命令的冗长性。

3. **代码重构和对象导向方法**
   - 讨论了如何通过采用更对象导向的方法来简化代码，特别是在FF Orchestrator中。
   - 提出了一些具体的重构步骤，如将特定实现从模块中移出，保持模块独立性。

4. **文档更新**
   - 讨论了关于设备文档的更新，建议将相关信息放在设备财务文档中。

5. **Drive Group解析和匹配**
   - 讨论了在Ceph中Drive Group解析和匹配的实现，特别是在Rook和Ceph Manager模块中的处理。
   - 提出了几种匹配机制，如使用主机名、标签等。

6. ** idempotence of the lv investment**
   - 讨论了lv投资幂等性的实现，提出了一个PR，并请求社区成员进行测试。

7. **本地开发和测试环境**
   - 讨论了如何在容器中本地测试和开发，提出了使用本地注册表和容器镜像的方法。
   - 提出了一些工具和脚本，如cube chicka，以帮助开发和测试。

#### 决定事项
- 继续讨论CLI重构，并在Google Docs上进行在线评论和讨论。
- 继续进行代码重构，特别是在FF Orchestrator中采用更对象导向的方法。
- 更新设备文档，并将相关信息放在设备财务文档中。
- 继续讨论Drive Group解析和匹配的实现，特别是在Rook和Ceph Manager模块中的处理。
- 继续测试和完善lv投资幂等性的实现。
- 继续讨论和完善本地开发和测试环境的方法和工具。

#### 后续行动计划
- 在Google Docs上进行CLI重构的在线评论和讨论。
- 继续进行代码重构，特别是在FF Orchestrator中采用更对象导向的方法。
- 更新设备文档，并将相关信息放在设备财务文档中。
- 继续讨论Drive Group解析和匹配的实现，特别是在Rook和Ceph Manager模块中的处理。
- 继续测试和完善lv投资幂等性的实现。
- 继续讨论和完善本地开发和测试环境的方法和工具。

#### 其他备注
- 会议中提到了一些具体的工具和脚本，如cube chicka，以帮助开发和测试。
- 会议中提到了一些具体的实现细节，如使用主机名、标签等匹配机制。
- 会议中提到了一些具体的代码重构步骤，如将特定实现从模块中移出，保持模块独立性。

#### 会议结束
- 会议在讨论完所有议题后结束，计划下周再次开会。

---

以上是本次会议的纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。