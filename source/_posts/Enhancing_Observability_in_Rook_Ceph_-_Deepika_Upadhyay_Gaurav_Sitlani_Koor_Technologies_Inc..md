---
title: "Enhancing Observability in Rook Ceph - Deepika Upadhyay & Gaurav Sitlani, Koor Technologies Inc."
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题
本次会议主要围绕分布式存储系统Ceph的跟踪（tracing）技术展开，特别是使用OpenTelemetry和Jaeger进行跟踪的实践和未来展望。

#### 会议参与者
- 主讲人：云存储工程师，曾就职于Redos和RBD，现为Code Technologies员工，同时也是Rook项目的贡献者。
- 同事：Gaurav Sitlani

#### 讨论内容
1. **跟踪技术简介**
   - 跟踪技术在Ceph中的应用，特别是在调试复杂场景中的作用。
   - 当前Ceph中跟踪技术的现状及其对Rook的影响。

2. **调试挑战**
   - 在Ceph中，如OSD变慢或出现慢操作等问题，可能由多种原因引起，如硬件故障、软件故障、恢复操作等。
   - 传统上，通过日志进行问题定位非常困难，尤其是对于新手或非专家用户。

3. **跟踪技术的优势**
   - 跟踪技术可以在生产集群中提供持续的低性能开销的监控。
   - 支持自适应采样策略，减少跟踪数据的处理负担，同时保持系统的概览。

4. **OpenTelemetry与Jaeger的应用**
   - OpenTelemetry提供了一个厂商中立的API，用于在代码中编写跟踪 instrumentation。
   - Jaeger是一个使用gRPC和Thrift协议收集和展示跟踪数据的CNCF项目。

5. **跟踪技术的实现细节**
   - 跟踪数据以span的形式记录，每个span包含操作名称、开始和结束时间以及相关的标签和日志。
   - 通过上下文ID，span之间可以建立父子关系，形成完整的操作流程图。

6. **Rook集群中的跟踪部署**
   - 在Rook中，通过Jaeger operator和OpenTelemetry collector实现跟踪数据的收集和处理。
   - 用户可以通过Jaeger UI查询和分析跟踪数据。

7. **未来展望**
   - 探索更多的代码 instrumentation，特别是在生产集群中实时监控的关键需求。
   - 考虑在Rook中集成更多的自定义采样策略和CRD（Custom Resource Definitions）。

#### 决定事项
- 继续推进Ceph和Rook中的跟踪技术集成，特别是在即将发布的Reef版本中。
- 增强对开发者和贡献者的跟踪技术培训和文档支持。

#### 后续行动计划
- 完善Rook中的跟踪技术部署文档和教程。
- 探索更多的代码 instrumentation 和采样策略，以优化生产环境中的跟踪性能。
- 与社区合作，推广跟踪技术在Ceph和Rook中的应用。

#### 会议总结
本次会议详细讨论了跟踪技术在Ceph和Rook中的应用，特别是在调试复杂场景和优化生产环境中的作用。通过集成OpenTelemetry和Jaeger，可以显著提升问题定位的效率和系统的可观测性。未来的工作将集中在进一步优化跟踪技术的部署和应用，以及增强对开发者的支持。