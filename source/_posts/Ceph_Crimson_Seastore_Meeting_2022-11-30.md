---
title: "Ceph Crimson/Seastore Meeting 2022-11-30"
date: 2022-12-02
updated: 2022-12-03
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议主要讨论了Ceph存储系统的开发进展和相关技术问题，包括性能优化、代码审查、功能实现等方面。

#### 主要议题
1. **代码审查和功能迁移**
   - 上周主要进行了代码审查工作。
   - 计划迁移Oh Map功能，并推进Split Protocol V2 Messenger和Handshake的开发。

2. **性能回归问题**
   - 发现共享存储支持下的性能有所下降，目前正在解决这一问题。
   - 通过添加Mall客户端进行测试，以验证性能改进。

3. **代码调试和单元测试**
   - 正在调试Picture Remove代码，已接近完成，计划添加单元测试并准备PR（Pull Request）进行审查。

4. **缓存数据提升功能**
   - 讨论了实现缓存数据提升功能的必要性和可行性。
   - 该功能旨在将频繁访问的数据从冷存储提升到热存储，以优化内存使用效率。
   - 讨论了该功能对最终性能的贡献和引入的复杂性。

#### 决定事项
- 继续推进Split Protocol V2 Messenger和Handshake的开发。
- 解决共享存储支持下的性能回归问题。
- 完成Picture Remove代码的调试和单元测试，并提交PR进行审查。
- 探讨并实现缓存数据提升功能，评估其对性能的影响和重要性。

#### 后续行动计划
- 完成Oh Map功能的迁移工作。
- 继续解决性能回归问题，并进行相关测试。
- 完成Picture Remove代码的单元测试，并提交PR。
- 进一步讨论和实现缓存数据提升功能，评估其对性能的影响，并考虑架构上的调整。

#### 其他事项
- 会议结束时，与会者互相祝愿一周愉快。

### 关键词
- Ceph
- Split Protocol V2
- Oh Map
- Performance Regression
- Blue Store
- Object Store Interface
- Cache Data Promote
- Memory Constrained Devices

### 结束语
会议顺利结束，各项议题和后续行动计划已明确，期待各团队成员的进一步进展和合作。