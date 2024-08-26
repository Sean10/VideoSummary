---
title: "Ceph Docubetter Meeting 2020-10-14"
date: 2020-10-14
updated: 2020-10-15
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议时间：** 某日，时间略晚于预定开始时间  
**参会人员：** 会议主持人及其他相关人员

#### 主要议题及讨论内容：

1. **Pull Request 374-51 (FADM)**
   - 讨论了FADM（Faster and More Scalable Document）的Pull Request，这是一个未来文档变更的重要来源。目前无需立即行动，但需保持关注。

2. **GitHub行为变更**
   - 决定不再要求在doc目录内的提交必须有“Signed-off-by”标签，以避免通过GitHub Web界面进行的更改被阻止。

3. **CFDF细节PR更新**
   - 主持人正在处理一个CFDF相关的Pull Request，预计将在接下来几小时内或最迟明天完成。

4. **文档系统（FFS）的改进**
   - 针对Josh Cullen提出的关于侧边栏顶级链接无法正常工作的bug，主持人已通过将链接集合到restructuredText文档中的toctree来解决。同时，移除了之前注释掉的HTML代码，并添加了`:hidden:`选项以避免toctree在文档中显示。
   - 主持人请求Patrick检查这些更改是否影响了他们的需求。

5. **RADOS文档更新**
   - Anthony Diatri对RADOS文档进行了大量更新，主持人与其进行了深入的合作，更新已成功整合到文档中。

6. **defio与docs.ceph.com同步问题**
   - 讨论了defio与docs.ceph.com不同步的问题，提出了可能通过自动化工具来解决这一问题。

7. **旧Pull Request的处理**
   - 讨论了如何处理因“Signed-off-by”检查而阻塞的旧Pull Request，建议重新运行测试或创建新的Pull Request来清理积压。

8. **文档更新与维护**
   - 主持人计划对开发指南进行全面检查和更新，并确保在即将发布的Pacific版本中，文档集是全面、准确且易于导航的。

#### 决定事项：

- 不再要求doc目录内的提交必须有“Signed-off-by”标签。
- 将处理旧Pull Request的积压问题，通过重新运行测试或创建新PR来解决。

#### 后续行动计划：

- 完成CFDF细节PR。
- 继续更新和维护文档，特别是FFS和开发指南。
- 探索自动化工具以解决defio与docs.ceph.com的同步问题。
- 确保Pacific版本发布时，文档集是全面、准确且易于导航的。

**会议结束时间：** 20分钟后  
**下一次会议：** 待定

**备注：** 会议中提到的具体技术细节和代码更改需要进一步的技术审查和验证。