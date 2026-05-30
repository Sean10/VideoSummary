---
categories:
- 视频总结
date: 2020-06-10
subtitle: Ceph_Crimson_Seastor_OSD_Weekly_2020-06-10
tags:
- Ceph
- Distributed Storage
- Performance Optimization
- Memory Allocator
- System Failures
- CephFS
title: "Ceph Crimson/Seastor OSD Weekly 2020-06-10"
updated: 2020-06-10
---



## 改进后的中文总结内容

### 会议纪要

#### 关键细节
- **异步版本开发**：计划开发异步版本，重点关注处理repellents of the leaf notice。
- **性能测试**：进行了两个分支的性能测试，包括graceful shutdown PR，发现其对性能有3.5%的惩罚。从istil到Lipsy的内存分配器转换对性能有50%的影响。
- **内存分配器问题**：讨论了sister's memory allocator和alien stars的问题，发现多线程环境下的内存分配存在重要误解和实际问题。
- **系统崩溃分析**：分析了系统崩溃的原因，与sister memory allocator的内存分配问题有关，特别是在处理大量线程时。
- **后续行动计划**：计划进一步调查和优化sister memory allocator，特别是多线程环境下的表现，并调整系统的内存分配策略。

#### 讨论的主要议题
- **异步版本开发**：讨论异步版本的开发计划和进展。
- **性能测试结果**：分享性能测试结果，特别是graceful shutdown PR和内存分配器转换的影响。
- **内存分配器问题**：深入讨论sister's memory allocator和alien stars的问题，包括其在多线程环境下的表现和存在的问题。
- **系统崩溃原因**：分析系统崩溃的原因，特别是在处理大量线程时的内存分配问题。

#### 决定的事项
- **异步版本开发**：决定在下一周尝试开发异步版本，特别是在处理repellents of the leaf notice方面。
- **性能测试**：确认性能测试的结果，并决定进一步调查和优化内存分配器。
- **内存分配器问题**：决定进一步调查和优化sister's memory allocator，特别是在多线程环境下的表现。

#### 后续行动计划
- **异步版本开发**：继续开发异步版本，并关注其在实际应用中的表现。
- **性能测试**：继续进行性能测试，并根据测试结果调整和优化内存分配策略。
- **内存分配器问题**：进一步调查和优化sister's memory allocator，特别是在多线程环境下的表现。
- **系统崩溃原因**：继续分析系统崩溃的原因，并寻找解决方案。

### 结论
本次会议主要讨论了异步版本的开发、性能测试结果、内存分配器问题以及系统崩溃的原因。决定继续开发异步版本，并进一步调查和优化内存分配器。同时，需要继续分析系统崩溃的原因，并寻找解决方案。