---
title: "Ceph Crimson/SeaStor OSD 2020-09-09"
date: 2020-09-10
updated: 2020-09-11
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **会议开始时间**: 未明确记录，但根据内容推断为近期。
- **参会人员**: 包括但不限于Sam、Kofu等。
- **会议形式**: 视频会议，部分参会者遇到网络问题。

#### 讨论的主要议题
1. **Ratio Test 进展**:
   - 讨论了Ratio Test的失败情况，分为自动响应失败和恢复阶段跟踪问题。
   - 增加了功能以在转储前符号化电池信息，以便直接获取函数名而不是地址。

2. **Subversion Submodule 更新**:
   - 更新了Subversion子模块到最新的上游版本，希望放弃自定义的分支。

3. **Map Tree Code 调试**:
   - Kofu报告了在调试Map Tree代码方面的进展。

4. **Journal Write Out Stream 元数据**:
   - Sam正在编写代码，以便在日志写入流中包含足够的元数据，用于识别逻辑地址和类型。

5. **Interruptable Future Wrapper**:
   - 正在开发一个可中断的未来包装器，目前仍在进行中。

6. **BlueJeans 应用升级问题**:
   - 讨论了从BlueJeans应用版本1升级到版本2的问题，以及在Fedora 32上的兼容性。

7. **OSD通信压缩**:
   - 提到一个实习生正在研究压缩OSD通信，并寻求帮助。

#### 决定的事项
- 将继续使用现有的tick方法来处理OSD map的订阅问题。
- 将更新PR以使用tick方法添加新的定时器。
- 将处理BlueJeans应用在Fedora 32上的兼容性问题。
- 将帮助实习生解决OSD通信压缩的问题。

#### 后续行动计划
- 完成并提交符号化电池信息的API。
- 继续调试Map Tree代码。
- 完成Journal Write Out Stream元数据的编码工作。
- 完成Interruptable Future Wrapper的开发。
- 解决BlueJeans应用的兼容性问题。
- 协助实习生解决OSD通信压缩的问题。

#### 其他备注
- 会议中存在一些背景噪音，但不影响主要讨论。
- 部分参会者遇到网络问题，建议后续会议前检查网络连接。

### 结束语
会议在讨论了各项议题和后续行动计划后结束，参会者表示将按计划推进各自的工作，并期待下次会议的进展报告。