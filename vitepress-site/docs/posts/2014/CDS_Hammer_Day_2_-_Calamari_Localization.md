---
title: "CDS Hammer (Day 2) - Calamari Localization"
date: 2014-10-30
updated: 2014-10-31
tags:
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
会议纪要

**会议主题**： Calamari 本地化工作进展及后续计划

**参会人员**： Lee, Jen, Greg, Dan, John 等

**会议内容**：

* **Calamari 本地化进展**：
    * Lee 和 Jen 已完成了 Calamari Dashboard 的本地化工作，将部分英文翻译为中文，并尝试了多语言切换功能。目前只完成了 Dashboard 的本地化，其他 Calamari 客户端应用（如 Manage）尚未开始本地化。
    * Lee 在本地化过程中遇到了技术难题，例如如何支持 AngularJS 2.0 和框架的本地化。
    * Greg 提出将翻译后的字符串移动到相应的资源文件中，并建议使用 AngularJS 1.3 来简化本地化工作。
    * Dan 解释了如何将字符串提取到资源文件中，并建议先完成 Dashboard 的本地化。
    * John 建议将 Calamari 代码库中的提交拆分为多个部分，以便更容易地跟踪和审查。

* **后续行动计划**：
    * Lee 将继续完成 Dashboard 的本地化工作，并将翻译后的字符串移动到相应的资源文件中。
    * Lee 将尝试使用 AngularJS 1.3 来简化本地化工作。
    * Greg 将与 Dan 合作，确定如何修改 Manage 应用以支持本地化。
    * Greg 将调查 AngularJS 1.3 的本地化支持情况。
    * Dan 将提供帮助，解释如何将字符串提取到资源文件中。
    * John 建议将 Calamari 代码库中的提交拆分为多个部分，以便更容易地跟踪和审查。

* **其他讨论**：
    * 如何处理来自 Calamari 服务器的字符串本地化问题。
    * 如何设置 Accept-Language 头部信息。
    * 如何处理错误消息的本地化问题。

**关键信息**：

* Calamari Dashboard 的本地化工作已初步完成，但仍需进行一些调整。
* 其他 Calamari 客户端应用尚未开始本地化。
* 需要进一步调查 AngularJS 1.3 的本地化支持情况。
* 需要确定如何处理来自 Calamari 服务器的字符串本地化问题。

**备注**：

* 会议中提到了一些计算机科学/ Ceph 相关领域英文原文的关键词，例如：Calamari, localization, AngularJS, l20n framework, message catalog, etc.