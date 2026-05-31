---
categories:
- 视频总结
date: 2018-11-02
subtitle: Ceph_Performance_Meeting_2018-11-01
tags:
- Ceph
- 分布式存储
- 性能优化
- BlueStore
title: "Ceph Performance Meeting 2018-11-01"
updated: 2018-11-03
---



会议纪要

会议时间：2018年11月1日（万圣节之后的一天）
参会人员：Mark、Nick、Josh、Sage、Igor、Radek、Adam（远程）
会议主题：Ceph分布式存储项目进展与讨论

一、会议关键细节

1. 由于假期原因，参会人员较少，但讨论内容丰富。
2. 会议主要围绕Ceph项目的Pull Requests（PRs）进展、代码优化、性能提升等方面展开。

二、讨论的主要议题

1. **PR进展**：
   - Radek本周提交了3个新的PRs，包括一个关于超合并缓冲列表的PR，引起了广泛关注。
   - Sage正在审查一个关于BlueFest的PR，目前处于初步审查阶段。
   - Erik正在研究IO节流器，得到大家的支持。
   - Josh提到了CS Career项目中存在的问题，需要进一步解决。

2. **代码优化与性能提升**：
   - Mark提到Radek的合并缓冲列表PR可能对代码性能产生积极影响。
   - Sage提出关于原子对象PR的命名问题，尚未确定。
   - 大家讨论了C++接口的稳定性问题，考虑放弃对C++ API的稳定性保证，以便更好地进行代码维护和优化。
   - Matt提到Adam的一个旧PR最近得到了更新，值得关注。

3. **BlueStore性能优化**：
   - Nick和Josh讨论了BlueStore的分区大小问题，认为需要调整层级结构以更好地利用SSD。
   - Sage提出了一种自动调整层级大小和乘数的方法，以优化使用SSD的性能。
   - 大家探讨了将部分层级存储在SSD上的可能性，但目前尚无明确解决方案。

三、决定的事项

1. 继续关注Radek的合并缓冲列表PR，并尝试将其应用于其他代码优化。
2. 对C++接口的稳定性问题进行讨论，考虑放弃对C++ API的稳定性保证。
3. 关注Adam的更新PR，并评估其价值。
4. 进一步研究BlueStore的性能优化问题，寻找改进方案。

四、后续行动计划

1. Mark将继续跟进Radek的合并缓冲列表PR。
2. Sage将继续审查BlueFest的PR。
3. 大家将共同讨论C++接口的稳定性问题。
4. Nick和Josh将研究BlueStore的性能优化方案。
5. 会议结束后，参会人员将就讨论内容进行进一步沟通和协作。