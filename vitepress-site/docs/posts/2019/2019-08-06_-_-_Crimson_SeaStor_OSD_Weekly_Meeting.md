---
title: "2019-08-06 :: Crimson SeaStor OSD Weekly Meeting"
date: 2019-08-06
updated: 2019-08-12
tags:
  - "Ceph"
  - "分布式存储"
  - "Crimson"
  - "OSD"
  - "测试"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2023年11月某日

**会议地点**： 圣克拉拉

**参会人员**： Marya, Peter, Suri, Rida, Milan, Comment, Justin

**会议内容**：

**1. 复制副本测试**：

* Marya汇报了其使用Crimson II进行复制副本测试的进展，未发现性能退步。
* 讨论了将测试合并到Merger的可行性，但需要Crimson Messenger的支持。
* Marya将继续进行测试，并尝试将其合并到Merger。

**2. 性能测试集成**：

* 讨论了将性能测试集成到Jenkins和Ritter的TD Site中。
* 需要比较不同测试用例的性能，包括Crimson II和Crimson Messenger。
* 计划编写SMO测试，比较基线性能。
* 将确保测试用例反映实际使用场景。

**3. 对象存储设计**：

* 讨论了对象存储的设计，包括命名空间和硬件支持。
* 认识到需要支持不同的硬件，包括HDD和SSD。
* 讨论了Sister和Blue Store的差异和适用场景。

**4. 其他议题**：

* Suri汇报了其在Crimson中实现安全类和对象类的进展。
* Rida讨论了Sitar输入缓冲区的实现，并计划与Avi面对面讨论。
* Comment讨论了使用Python或批处理代码驱动测试的想法。
* Milan讨论了将UNIX域套接字支持合并回系统的计划。

**行动计划**：

* Marya将继续进行复制副本测试，并尝试将其合并到Merger。
* 讨论性能测试用例的设计和实现。
* 继续进行对象存储的设计和开发。
* Suri将完成Crimson中安全类和对象类的实现。
* Rida将讨论Sitar输入缓冲区的实现。
* Comment将研究使用Python或批处理代码驱动测试。
* Milan将合并UNIX域套接字支持。

**备注**：

* 会议中提到了Crimson II、Crimson Messenger、Sister、Blue Store、Innings、Merger、TD Site、SMO、Sitar、输入缓冲区等关键术语。