---
title: "Ceph DocuBetter Meeting 2019-01-18"
date: 2019-01-18
updated: 2019-02-03
tags:
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2019-01-18

**参会人员**： Ceph 文档团队成员、SEO 专家、项目实习生等

**会议主题**： Ceph 文档优化与 SEO 改进

**会议内容**：

**1. 文档结构优化**：

*   **问题**： Ceph 文档覆盖多个版本，可能导致用户误入旧版本文档。
*   **解决方案**：
    *   使用 `rel canonical` 标签指向主版本作为标准版本。
    *   使用别名（如 `/current`）指向最新稳定版本。
    *   自动化文档生成过程，包括生成 `rel canonical` 标签和 `robots.txt` 文件。

**2. SEO 改进**：

*   **问题**： 搜索引擎索引了过时的文档版本，导致用户体验不佳。
*   **解决方案**：
    *   在 `robots.txt` 文件中排除旧版本文档。
    *   考虑使用白名单而非黑名单，以便搜索引擎仍能索引最新版本。

**3. 文档生成自动化**：

*   **问题**： 文档生成过程依赖人工干预，效率低下。
*   **解决方案**：
    *   将文档生成过程集成到 Jenkins 作业中，实现自动化。
    *   利用可读性文件自动创建链接和 `rel canonical` 标签。

**4. 项目实习生**：

*   **问题**： 需要额外的资源来优化文档和 SEO。
*   **解决方案**：
    *   招聘实习生，负责文档编写和生成工作。
    *   实习生参与每周会议，了解项目进展。

**5. 其他**：

*   **JavaScript backboards**： 已合并 luminous 和 mimic 版本的 backboards，jewel 版本的 backboards 尚未完成。

**行动计划**：

*   Ceph 文档团队与 SEO 专家合作，制定详细的文档优化和 SEO 改进计划。
*   评估 Jenkins 作业，实现文档生成自动化。
*   与 David Galloway 合作，优化 `robots.txt` 文件。
*   招聘实习生，负责文档编写和生成工作。

**备注**：

*   会议中提到的部分关键词：SEO、rel canonical、robots.txt、Jenkins、Sphinx、白名单、黑名单、实习生、Ceph 文档团队。