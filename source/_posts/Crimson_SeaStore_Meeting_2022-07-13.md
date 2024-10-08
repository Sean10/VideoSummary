---
title: "Crimson/SeaStore Meeting 2022-07-13"
date: 2022-07-19
updated: 2022-07-20
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议时间：[具体日期]
#### 参会人员：[列出参会人员]

#### 主要议题：
1. **Ceph多核PR的进展**
   - 发言人：[姓名]
   - 进展：第二个多核PR即将完成，预计明天发布。第三个多核PR的工作即将开始。

2. **OSD启动和ZNS设备测试**
   - 发言人：[姓名]
   - 进展：成功在ZNS设备上启动OSD，并进行了RADOS Bench测试。遇到了GC（垃圾回收）问题，GC启动后IO操作停止，需要进一步调试。

3. **对象数据块分割和冲突检测改进**
   - 发言人：[姓名]
   - 进展：完成了第一个PR的合并，后续工作包括进一步改进冲突检测和简化随机块管理器的循环日志。

4. **列表对象和枚举对象的调试**
   - 发言人：[姓名]
   - 进展：正在根据评论修改PR，并进行调试。

5. **物理B3优化和死亡引用问题**
   - 发言人：[姓名]
   - 进展：已分离出第一个PR，第二个PR即将提交。

6. **HDD支持的讨论**
   - 发言人：[姓名]
   - 讨论：关于是否在HDD上使用RBM（随机块管理器）进行了深入讨论。建议尽可能避免设备特定代码，并考虑使用段管理器来优化HDD的分配策略。

7. **SMR硬盘支持的可能性**
   - 发言人：[姓名]
   - 讨论：提出了在Ceph中支持SMR（叠瓦式磁记录）硬盘的可能性，建议创建SMR实现的段管理器。

#### 决定事项：
- 继续调试ZNS设备上的GC问题，并考虑创建相关bug报告。
- 继续改进冲突检测和简化随机块管理器的循环日志。
- 继续调试列表对象和枚举对象的问题。
- 继续优化物理B3和解决死亡引用问题。
- 对于HDD支持，建议尽可能避免设备特定代码，并考虑使用段管理器来优化HDD的分配策略。
- 考虑在Ceph中支持SMR硬盘，创建SMR实现的段管理器。

#### 后续行动计划：
- 发布第二个多核PR，并开始第三个多核PR的工作。
- 继续调试ZNS设备上的GC问题，并创建相关bug报告。
- 完成冲突检测的改进和随机块管理器的简化。
- 完成列表对象和枚举对象的调试。
- 提交物理B3优化的第二个PR。
- 讨论并实施HDD支持的优化策略。
- 研究并实施SMR硬盘的支持。

#### 备注：
- 会议中提到的技术术语包括ZNS（Zone Namespace）、RADOS Bench、GC（垃圾回收）、RBM（随机块管理器）、SMR（叠瓦式磁记录）等。

#### 会议结束时间：[具体时间]

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。