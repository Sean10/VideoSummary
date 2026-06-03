---
title: "2019-05-02 :: Ceph Performance meeting"
date: 2019-05-28
updated: 2019-05-28
tags:
  - "Ceph"
  - "性能优化"
  - "分布式存储"
  - "CRUSH算法"
  - "高可用性"
categories:
  - "视频总结"
outline: deep
---
会议纪要：

**会议时间**： 2023年11月某日（具体日期未提及）

**参会人员**： Josh, Mark, Keef, Jason, Sage, Adam, Radek, Mohamed等

**会议主题**： Ceph项目性能讨论

**主要议题**：

1. **PR讨论**：
   - Keef提交的PR旨在利用用户空间IOKit事件优化性能，受到C star和FIO代码的启发，目前尚未测试，但预计效果显著。
   - Jason为LebaDB添加了zero copyrights支持，性能提升4%，主要表现为CPU使用率下降，PR已审查，预计不久后合并。
   - Sage提交了多个Crimson相关PR，通过批处理和多线程化提高性能，目前效果有限，但某些步骤的改进可能显著。
   - Adam完成了EC stripe cache的代码开发，并正在进行测试，欢迎代码审查。
   - Sage提交了Booster分配器的老化测试PR，希望将其转换为单元测试。

2. **日志记录优化**：
   - Sage提到，已在master分支中将日志记录的默认方式从D out更改为LTTE ng，以减少字符串开销。
   - Mark分享了一个关于LTTE ng性能提升的PR，在NVMe环境中对大型I/O操作性能提升显著。
   - 会议讨论了使用二进制日志格式，以及保留文本日志的必要性。

3. **其他事项**：
   - Sage计划加入对prefetch for rocks DB和masterful的讨论。
   - Adam正在尝试将Booster分配器的老化测试转换为单元测试。

**行动计划**：

- Keef将继续修复其PR，并测试其性能。
- Jason的PR预计很快会合并。
- Sage将继续关注Crimson相关PR，并与其他开发人员合作优化性能。
- Adam将继续进行EC stripe cache的测试，并欢迎任何人对代码进行审查。
- Sage将继续推动prefetch for rocks DB和masterful的讨论。
- 参会人员将继续讨论日志记录优化方案。

**后续会议**：

- 下周将再次召开核心会议，继续讨论Ceph项目的进展。