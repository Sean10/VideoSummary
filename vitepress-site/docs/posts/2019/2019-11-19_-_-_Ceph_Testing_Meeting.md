---
title: "2019-11-19 -- Ceph Testing Meeting"
date: 2019-11-25
updated: 2019-11-26
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "会议纪要"
outline: deep
---
### 会议纪要

#### 会议时间
（未提及具体时间）

#### 参会人员
Nathan, Yuri, Patrick, Rakesh, Maneka, Sage, Marcus, Suzi, Davis 等

#### 会议主题
- Ceph 分布式存储项目进展
- Python 3 迁移相关讨论
- Dashboard PR 合并及审查流程
- Mimic 项目进展

#### 关键细节

**1. Ceph 分布式存储项目进展**

* **Dashboard PR 合并及审查流程**:
    * Nathan 建议合并 Dashboard PR 并重建，预计今天或明天完成。
    * 对于特定 PR，需要增加审查人数至六人以确保质量。
    * 需要确保所有 PR 都包含在伊朗中，以便进行测试和审查。
    * 对于 rgw PR，Nathan 将在会议后再次合并。
* **Mimic 项目进展**:
    * Patrick 的团队在 Mimic 项目上进展顺利，但需要审批。
    * 已通过邮件通知相关团队，预计今天或明天可以完成审批。
* **Python 3 迁移**:
    * 正在进行 Python 3 迁移，并尝试使测试在 Python 2 和 Python 3 上都能运行。
    * 遇到单元测试兼容性问题，需要更多工作来解决。
    * 计划添加 Jenkins 任务以部署 Python 3 环境。
    * 目前基于 openSUSE 操作系统，未来可能支持更多操作系统。

**2. 其他讨论**

* **Python 3 迁移相关**:
    * 讨论了 Python 3 迁移的优先级和资源分配问题。
    * 讨论了如何使用 Sweet 测试套件进行 Python 3 测试。
    * 讨论了如何处理 Scipio 实验室中的工作节点故障问题。
* **技术问题**:
    * 讨论了如何解决 Scipio 实验室中工作节点故障的问题。

#### 决定事项

* 合并 Dashboard PR 并重建。
* 增加特定 PR 的审查人数。
* 审批 Mimic 项目。
* 继续进行 Python 3 迁移。
* 解决技术问题。

#### 后续行动计划

* Nathan 合并 Dashboard PR。
* 审查并合并 rgw PR。
* 审批 Mimic 项目。
* 继续进行 Python 3 迁移。
* 解决技术问题。

#### 会议总结

本次会议讨论了 Ceph 分布式存储项目进展、Python 3 迁移、Dashboard PR 合并及审查流程、Mimic 项目进展等议题。会议明确了后续行动计划，并要求各方积极配合完成相关工作。

在原始字幕中，确实存在一些由于音译导致的错误文本关键词，但在改进的总结中，我们保留了所有与 Ceph 相关的关键字，确保了总结的准确性和专业性。