---
title: "2019-05-27:: Ceph Orchestration Meeting"
date: 2019-05-28
updated: 2019-05-28
tags:
  - "Ceph"
  - "编排"
  - "自动化"
  - "存储"
  - "CephFS"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2023年3月28日

**会议主题**： 讨论Ceph存储集群中的功能实现和改进方案。

**参会人员**： Travis, Eric Fox, Stefan等人。

**会议内容**：

**1. 会议取消情况**：
- 由于美国阵亡将士纪念日，美国团队成员无法参加，故Travis取消了本次会议。

**2. Ceph相关议题**：
- **Podcast评论**： Travis更新了关于Ceph的播客，讨论了评论提交的问题。
- **Trivial Completions**： 讨论了新计划，并指出忽略属性可能带来的风险，建议返回失败以防止问题发生。
- **Kiche信息持久化**： 讨论了Kiche信息的持久化问题，提出了使用持久存储字典存储主机列表的方案。
- **SSH Orchestrator**： 讨论了SSH Orchestrator的实现，指出其存储已知主机列表的方式与其他Orchestrator不同，讨论了是否需要替换持久化存储字典以提高性能。
- **Ansible Orchestrator**： 讨论了Ansible Orchestrator的性能问题，提出了将部分信息缓存到Ansible中的方案，并讨论了是否需要修改playbook以实现快速版本。

**3. 其他议题**：
- **Ansible Orchestrator支持安全Ansible**： 讨论了Ansible Orchestrator是否支持安全Ansible，指出这是当前工作的重点。
- **测试自动化**： 讨论了测试自动化的重要性，并指出应该优先考虑自动化测试。

**4. 行动计划**：
- 完成Ansible Orchestrator的修改，并确保功能正常。
- 对Ceph进行自动化测试。
- 在下周的会议上继续讨论其他议题。

**5. 会议总结**：
本次会议讨论了Ceph存储集群中的功能实现和改进方案，并制定了相应的行动计划，强调了Ansible Orchestrator的重要性和测试自动化的重要性。