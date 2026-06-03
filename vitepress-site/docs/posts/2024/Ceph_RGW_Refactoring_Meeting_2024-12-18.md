---
title: "Ceph RGW Refactoring Meeting 2024-12-18"
date: 2024-12-18
updated: 2024-12-18
tags:
  - "Ceph"
  - "RGW"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要 - Ceph 开发会议

**日期**: 2023年某月某日  
**主持人**: 未提及  
**参会人员**: Jesse, Joseph, Alex, Radislav, Casey, 及其他Ceph开发人员



#### 1. **Joseph的议题：跟踪工作进展及S3接口改进**
   - **背景**: Joseph希望了解Ceph社区的活跃工作，特别是S3接口相关的开发进展，以便Bloomberg在2025年规划中提供帮助。
   - **讨论内容**: 
     - Joseph提到在过去的开发者月会上提出了S3用户和开发者的优先事项，最近注意到一些新特性（如merge y）的开发，但不确定如何跟踪这些特性的进展。
     - Casey指出，目前没有正式的特性跟踪文档，只有SEF开发者峰会上的一些非正式记录，且没有明确的优先级或截止日期。
     - Joseph建议是否可以为Ceph社区建立一个特性跟踪工具，可能通过Redmine或其他类似工具。
     - Casey提到Trello之前由Red Hat付费使用，但现已停止，建议可以考虑使用Redmine的敏捷功能或其他工具。
   - **决定事项**: 
     - 考虑为Ceph社区建立一个特性跟踪工具，可能通过Redmine或其他类似工具。
     - 每月或每两个月进行一次同步会议，更新特性进展。

#### 2. **Jesse的议题：optional yield的PR**
   - **背景**: Jesse发现Ceph中使用了`optional yield`，并考虑是否可以用C++的`std--optional`替代。
   - **讨论内容**: 
     - Jesse进行了性能测试，发现`std: -optional`与现有实现性能几乎相同，但提供了更多的成员函数和功能。
     - 讨论了是否需要这些额外功能，以及是否应该关闭相关PR。
   - **决定事项**: 
     - 如果没有人需要这些额外功能，Jesse将关闭相关PR。

#### 3. **Jesse的议题：RGW Admin工具的重构**
   - **背景**: Jesse计划对RGW Admin工具进行大量重构，希望将其代码移至单独的目录。
   - **讨论内容**: 
     - Jesse解释了将RGW Admin工具移至单独目录的原因，主要是为了更好地组织代码，避免顶级目录过于杂乱。
     - 讨论了是否有人依赖当前的文件结构，Jesse表示主要是构建系统需要调整。
   - **决定事项**: 
     - 同意将RGW Admin工具移至单独目录，Jesse将继续进行重构。

#### 4. **Alex的议题：STS（Security Token Service）的实现**
   - **背景**: Alex讨论了Ceph的STS实现，特别是如何处理OIDC和JWT的签名验证。
   - **讨论内容**: 
     - Alex提到AWS的STS实现与RFC标准不完全一致，Ceph是否应该更接近AWS的实现，还是遵循RFC标准。
     - 讨论了是否可以在Ceph中添加扩展功能，同时提供一个严格兼容AWS的模式。
   - **决定事项**: 
     - 建议安排一次专门的会议，讨论STS的实现细节，特别是如何平衡AWS兼容性和RFC标准。
     - 可能邀请Marcus Watts和Sage McTaggart参与讨论。

#### 5. **Radislav的议题：RGW的多对象RADOS事务**
   - **背景**: Radislav正在收集RGW中多对象RADOS事务的需求，特别是在开发者峰会上讨论的相关内容。
   - **讨论内容**: 
     - Radislav希望将所有涉及多对象修改的用例整理到一个文档中，以便进一步讨论。
     - 讨论了是否需要完全的多对象事务支持，还是可以通过其他方式（如单对象更新+额外操作）实现。
   - **决定事项**: 
     - Radislav将把文档移至GitHub的Gist上，方便更多人参与讨论。

#### 6. **其他议题**
   - **Barbican集成**: 讨论了Barbican与Ceph的集成问题，Marcus Watts被认为是相关领域的负责人。
   - **会议安排**: 决定取消下周的会议，因为圣诞节和新年假期临近。



**下次会议**: 2024年1月（具体时间待定）

**总结**: 本次会议主要讨论了Ceph社区的特性跟踪工具、RGW Admin工具的重构、STS实现的兼容性问题，以及RGW的多对象RADOS事务需求。会议决定将安排专门的会议讨论STS实现，并考虑为Ceph社区建立一个特性跟踪工具。