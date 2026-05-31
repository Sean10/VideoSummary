---
categories:
- 视频总结
date: 2019-04-16
subtitle: 2019-02-27_-_-_Ceph_Testing_meeting
tags:
- Ceph
- 分布式存储
- 测试
title: 2019-02-27 -- Ceph Testing meeting
updated: 2019-04-17
---


**会议纪要**

**会议时间**： [请填写会议时间]

**参会人员**： [请填写参会人员名单]

**会议主题**：

本次会议重点讨论了Ceph项目中的两个关键议题：依赖库Coverity的测试以及Python 2.7到Python 3的迁移计划。

**关键细节及讨论议题**：

1. **Coverity依赖库测试**：
   - 提出了一个针对Python库Coverity dependency的pull request，其中charcoal已批准，但需要进一步的测试。
   - 讨论了由于依赖库的更改，现有测试可能无法覆盖所有情况，需要新的测试用例。
   - 讨论了如何进行测试，以及如何确保测试的全面性。

2. **Python 2.7到Python 3的迁移**：
   - 由于Python 2.7将不再支持，需要制定迁移计划。
   - 讨论了现有的迁移方案，包括使用Alfredo的补丁来使代码仅在Python 3上运行。
   - 讨论了如何测试迁移后的代码，以确保兼容性和稳定性。
   - 讨论了是否需要将代码拆分为两个部分，以便在迁移过程中逐步进行。

**决定事项**：

1. 将Coverity依赖库的测试用例添加到pull request中，并确保测试覆盖全面。
2. 对于Python 2.7到Python 3的迁移，将使用Alfredo的补丁，并在Nautilus版本发布后进行合并。
3. 制定详细的测试计划，以确保迁移后的代码兼容性和稳定性。

**后续行动计划**：

1. [请填写负责人] 将Coverity依赖库的测试用例添加到pull request中。
2. [请填写负责人] 跟进Python 2.7到Python 3的迁移进度，并确保测试计划。
3. [请填写负责人] 与QA团队合作，确保测试覆盖全面。

**其他事项**：

- 讨论了Custer部署SAP的进展，以及Red Hat会议对项目的影响。
- 讨论了Python 3兼容性问题，以及如何解决不同库之间的兼容性问题。

**备注**：

- 会议中提到的关键术语和英文原文如下：
  - Coverity dependency
  - Tour de suite
  - D code
  - QA Suites
  - T dollars
  - Dettol diamo
  - Custer
  - Python 2.7
  - Python 3