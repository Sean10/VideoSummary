---
title: "  Ceph Month 2021: Improving Cosbench for Ceph Benchmarking  "
date: 2021-06-23
updated: 2021-06-24
tags:
- Ceph
- 开源
categories:
- "视频总结"
subtitle: Ceph_Month_2021_-_Improving_Cosbench_for_Ceph_Benchmarking
---

### 会议纪要

#### 会议主题：改进Cosbench的成本基准测试

#### 会议时间：[具体时间]

#### 会议地点：[具体地点]

#### 参会人员：[参会人员名单]

#### 会议内容总结：

1. **Cosbench简介**：
   - Cosbench是一个开源项目，主要用于S3对象存储的基准测试，由Intel上海研发中心开发。
   - 该项目旨在提高可扩展性和模块化设计，支持多种对象存储系统，包括Amazon S3和Google Cloud。

2. **Cosbench的应用**：
   - Cosbench在Softline公司被用于客户特定的基准测试，帮助客户了解如何配置适合其工作负载的集群。
   - 尽管存在其他基准测试工具，如fio和hsbench，但Cosbench因其广泛采用而成为比较性能结果的标准。

3. **Cosbench的架构和功能**：
   - Cosbench采用控制器-驱动器架构，易于扩展到大集群。
   - 它支持多种工作负载，包括混合读写操作，并能自动平衡多个HTTP端点的负载。

4. **Cosbench的挑战和改进**：
   - Cosbench缺乏有效的构建系统，项目维护不足，最新版本存在问题。
   - 会议中提出了一些改进措施，包括引入Maven构建系统、打包为Debian软件包、改进工作负载生成和结果处理脚本。

5. **后续行动计划**：
   - 计划将内部改进的Cosbench分支公开，以便社区其他用户受益。
   - 探索进一步改进Cosbench的可能性，如增加数据流的随机性，以更好地测试去重功能。

#### 决定事项：
- 将内部改进的Cosbench分支公开，并提供Debian软件包。
- 继续探索和改进Cosbench的功能，特别是数据流的随机性。

#### 后续行动：
- 准备并发布改进后的Cosbench分支。
- 收集社区反馈，进一步优化和扩展Cosbench的功能。

#### 会议结束时间：[具体时间]

#### 备注：
- 鼓励社区成员参与Cosbench的改进和扩展，共同推动项目的发展。
- 会议中提到的其他工具和项目，如fio、hsbench、cbt等，也值得进一步研究和评估。