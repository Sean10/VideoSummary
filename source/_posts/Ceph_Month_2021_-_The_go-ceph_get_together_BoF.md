---
title: "Ceph Month 2021: The go-ceph get together BoF"
date: 2021-06-10
updated: 2021-06-11
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议基本信息
- **主持人**: John Mulligan
- **主题**: GoCeph项目公开讨论
- **时间**: 具体时间未提及

#### 会议内容总结

1. **项目历史回顾**
   - GoCeph项目始于2014年，由Noah Watkins发起。
   - John Mulligan和其他维护者于2019年10月加入项目并开始活跃。
   - 2020年2月发布了第一个官方版本0.2，此后每两个月发布一次新版本。

2. **项目现状**
   - 主要模块包括FFS、RADOS和RBD，这些模块是对C API的封装。
   - 主要目标是提供与Go函数类似的Ceph API，避免暴露C语言的复杂性。
   - RBD API是重点开发领域，CSI项目是其主要用户。
   - 近期重要更新包括RBD镜像、快照以及厚/薄图像配置。

3. **未来计划**
   - 短期计划包括完成RBD镜像功能和探索CephFS镜像功能。
   - 项目仍有许多未封装的Ceph API，需要评估哪些功能需要优先实现。

4. **技术发展**
   - 最近开发了多个管理包，如CephAdmin、RBDAdmin和RGWAdmin，使用JSON API进行管理操作。
   - Sven Anderson正在研究Go和C之间共享缓冲区的性能增强。

5. **社区和文档**
   - 需要提高PR处理速度和改进文档。
   - 正在考虑从v0升级到v1，但需要确保API的兼容性。

6. **用户和项目反馈**
   - 讨论了如何更好地了解用户需求和优先级。
   - 提到了一些使用GoCeph的项目，如CSI驱动和Rook。

7. **技术细节讨论**
   - 讨论了Admin Socket的实现和GoCeph在Mac上的兼容性。
   - 提到了改进PR处理速度和自动化测试的可能性。

#### 后续行动计划
- 继续开发RBD镜像和CephFS镜像功能。
- 评估并决定哪些Ceph API需要优先封装。
- 改进文档和错误处理，准备从v0升级到v1。
- 探索提高PR处理速度的方法，如减少审查要求或增加自动化测试。

#### 会议结束
- 会议在讨论了未来可能的改进和用户反馈后结束。
- 会议记录将被上传到Ceph YouTube频道。

**备注**: 会议中提到的具体技术细节和项目名称（如CSI、Rook、Admin Socket等）是Ceph和GoCeph项目中的关键术语，保留原文有助于理解相关领域的专业内容。