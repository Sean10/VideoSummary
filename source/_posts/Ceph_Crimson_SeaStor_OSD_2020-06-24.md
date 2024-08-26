---
title: "Ceph Crimson/SeaStor OSD 2020-06-24"
date: 2020-06-24
updated: 2020-06-25
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 参会人员
- Tommy
- 其他相关人员

#### 会议时间
- 日期：具体日期未提供
- 时间：具体时间未提供

#### 会议议题
1. **Ceph存储系统的开发进展**
2. **技术问题讨论与解决方案**
3. **后续行动计划**

#### 会议内容

1. **Ceph存储系统开发进展**
   - Tommy上周仍在处理异步another tree，并审查了一些由Ritek编写的优秀blue storylines。
   - 本周计划完成heartbeat的审查，并处理由工程师Stem提交的replicas by place。

2. **技术问题讨论**
   - **缓存依赖追踪**：Tommy正在为缓存添加支持，以跟踪依赖关系并确保所有父级extent被固定。这意味着任何逻辑extent（如extent tree或oh no tree extent）在内存中时，其所有映射页在lba tree中也将保持在内存中。
   - **零拷贝数据序列化**：Tommy正在调查零拷贝数据序列化方法，如flat buffers，以解决当前编码和解码方法消耗过多CPU的问题。
   - **Crimson测试与优化**：Tommy强调在Crimson运行自动化测试之前，不考虑进行性能优化，以避免引入新的bug。

3. **后续行动计划**
   - **Crimson自动化测试**：Tommy计划首先确保Crimson的自动化测试工作，以便后续可以自信地进行性能优化。
   - **Topology工作**：Tommy提到关于topology的工作接近完成，并寻求志愿者来处理pathology代码。
   - **技术支持与访问**：讨论了获取实验室访问权限的流程，以便能够运行pathology作业。

#### 决定事项
- 确保Crimson的自动化测试工作是当前的首要任务。
- 需要获取实验室访问权限以进行进一步的开发和测试。

#### 后续行动
- Tommy将发送相关链接并在30分钟后再次联系。
- 评估使用现有dot pi安装Crimson OSD的工作量，并选择更简便的方法。

#### 会议结束
- 会议在感谢和告别中结束。

---

**备注**：会议中提到的技术术语和项目名称如“async another tree”、“heartbeat”、“replicas by place”、“flat buffers”等，保留了英文原文以确保准确性。