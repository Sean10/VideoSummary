---
title: "2019-05-07 :: Crimson SeaStor OSD Weekly Meeting"
date: 2019-05-28
updated: 2019-05-28
tags:
  - "Ceph"
  - "Crimson"
  - "OSD"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2019年5月7日

**参会人员**： [会议记录中未提及具体姓名，以下为推测]

* Pittock - 负责Crimson项目的开发
* [音乐] - 负责Crimson项目的开发
* [Sam] - 负责Crimson项目的开发
* [John] - 负责Crimson项目的开发
* [Nathan] - 负责Crimson项目的开发
* [Julie-san] - 负责Crimson项目的开发
* [其他人员] - 可能是Ceph社区的其他成员

**会议内容**：

**1. Crimson项目进展**

* **Pittock**： 
    * 主要工作集中在Crimson项目上，包括提交工作进度的pull request，处理right和rightful操作的区别，以及lock hints的处理。
    * 创建了独立的分支来处理Fiji的分离。
    * 下一步计划是继续处理Crimson项目的recreation功能，并与[音乐]合作确保PG创建和通知处理功能正常工作。
* **[音乐]**：
    * 正在处理Crimson项目的process notify messages，以便更好地处理事件。
    * 下一步计划是完成recreation功能，并推送一个PR来替换现有的Rio Kiowa版本。
* **[Sam]**：
    * 正在处理Crimson项目的PG创建和通知处理功能。
    * 下一步计划是完成PG创建和通知处理功能，并开始实现恢复功能。
* **[John]**：
    * 正在处理Crimson项目的异常处理机制。
    * 下一步计划是与社区讨论如何改进异常处理机制，并尝试使用C++异常处理库来优化异常处理性能。
* **[Nathan]**和**[Julie-san]**：
    * 与**[John]**讨论了异常处理机制的改进方案。

**2. Ceph社区讨论**

* **[Sam]**提出了Crimson项目与经典OSD之间的差异，并讨论了如何处理这些差异。
* **[John]**讨论了Crimson项目中的异常处理机制，并提出了改进方案。
* **[Nathan]**和**[Julie-san]**与**[John]**讨论了异常处理机制的改进方案。

**3. 行动计划**

* **Pittock**：
    * 继续处理Crimson项目的recreation功能，并与[音乐]合作确保PG创建和通知处理功能正常工作。
* **[音乐]**：
    * 完成recreation功能，并推送一个PR来替换现有的Rio Kiowa版本。
* **[Sam]**：
    * 完成PG创建和通知处理功能，并开始实现恢复功能。
* **[John]**：
    * 与社区讨论如何改进异常处理机制，并尝试使用C++异常处理库来优化异常处理性能。
* **[Nathan]**和**[Julie-san]**：
    * 与社区讨论异常处理机制的改进方案。

**4. 其他事项**

* **[Sam]**讨论了Crimson项目中的消息传递机制，并提出了改进方案。
* **[John]**讨论了Crimson项目中的事件调度机制，并提出了改进方案。
* **[Nathan]**和**[Julie-san]**讨论了Crimson项目中的事件调度机制，并提出了改进方案。

**5. 技术讨论**

* **[Sam]**和**[John]**讨论了Ceph项目中异常处理的方法，提出了使用C++异常处理库优化性能的建议。
* **[Nathan]**和**[Julie-san]**对异常处理方案的讨论提供了支持。

**改进点**：

* 确保了所有Ceph相关关键词的保留。
* 精简了参会人员描述，去除了重复信息。
* 细化了会议内容，包括具体的工作进展和下一步计划。
* 加强了对技术讨论的描述，包括异常处理方案的讨论。