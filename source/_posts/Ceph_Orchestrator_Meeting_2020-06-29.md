---
title: "Ceph Orchestrator Meeting 2020-06-29"
date: 2020-06-29
updated: 2020-06-30
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
- **日期与时间**: [具体日期]
- **参会人员**: [参会人员名单]
- **主持人**: [主持人姓名]

#### 主要议题与讨论内容
1. **CI系统恢复**
   - CI系统已恢复正常运行，这是一个积极的进展。

2. **Alice的替换问题**
   - 讨论了在行业中测试的Alice替换问题，涉及使用hominids属性创建OSD时的问题。
   - 决定明确要求用户将unmanned instructor参数设置为true，以防止集群中的STI重读。
   - 需要进一步的信息来确定问题的具体情况，计划创建一个影响报告。

3. **Rook的拖拽组（drag groups）**
   - 讨论了Rook的节点亲和性和节点选择问题，决定采用社区的placement方法。
   - 创建了一个相关的pull request（编号3552442），并计划与Blaine同步以获取更多关于高级Cuban a displacement规范的信息。

4. **集成测试问题**
   - 讨论了集成测试中偶尔失败的问题，决定增加更多的日志信息以帮助诊断问题。

5. **Rook客户端发现问题**
   - Jeff Leighton创建了一个pull request，以从NSF组织切换到工作中的存储库，但由于不再支持在目录上部署OSD而导致失败。
   - 需要移除对目录的支持，并更新Rook管理模块的schema检查。

6. **升级测试**
   - Yuri正在进行从Octopus到Pacific的升级测试，并已有一个pull request（编号35808）成功运行。
   - 目前没有针对Pacific的升级测试，计划在未来进行。

#### 决定事项
- 明确要求用户将unmanned instructor参数设置为true。
- 增加集成测试的日志信息以帮助诊断问题。
- 移除对目录的支持并更新Rook管理模块的schema检查。

#### 后续行动计划
- 创建一个影响报告，收集更多关于Alice替换问题的信息。
- 与Blaine同步以获取更多关于高级Cuban a displacement规范的信息。
- 继续进行从Octopus到Pacific的升级测试，并计划未来进行Pacific的升级测试。

#### 其他事项
- 本周工作进展较为缓慢，没有重大进展。
- 会议结束时，主持人提醒大家在下周继续同步工作进展。

#### 会议结束
- 会议在简短的讨论后结束，主持人祝愿大家周末愉快，并期待下周的同步。