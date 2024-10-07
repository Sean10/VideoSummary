---
title: "Chasing Bad Checksums: A Journey Through Ceph, TCMalloc, and the Linux Kernel - Dan Hill, Canonical"
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议主题：** Ceph性能问题及解决方案探讨

**主讲人：** Dan Hill, Canonical 公司持续工程部门

**会议日期：** [具体日期未提供]

**会议地点：** [具体地点未提供]

**参会人员：** Ceph社区成员、Canonical公司代表、技术支持团队等

### 会议内容总结

**背景介绍：**
- Dan Hill介绍了Canonical公司的持续工程部门职责，包括作为技术支持团队的升级点，处理复杂问题，测试和验证解决方案，确保满足客户需求。
- 提到了Ubuntu Pro的自支持服务，感兴趣的可以通过ubuntu.com/self了解更多。
- 感谢Mauricio Oliviera的贡献，他虽未能参会，但对本次演讲的幻灯片和问题根源识别及补丁提交有重要贡献。

**问题描述：**
- 客户报告了一个Ceph集群的性能问题，集群规模庞大，包含数十个节点，数百个OSDs，存储容量约10PB，运行在Ubuntu Bionic LTS上，使用Ceph的Octopus版本。
- 集群被用作大型环形缓冲区，持续进行数据摄取和探索，读取活动较少且随时间变化。
- 初始问题是多个OSDs随机崩溃，原因是校验和错误（checksum errors）。

**问题分析与解决过程：**
- 初步怀疑是硬件问题，但系统日志、固件级别和SMART数据均未发现异常。
- 发现校验和错误在集群中广泛分布，且仅在内存压力高时发生。
- 通过详细分析校验和错误，发现校验和计算指向了一个零填充的缓冲区。
- 在Blue Store中存在一个已知的缓解措施，即遇到校验和错误时会重试，但在RocksDB中没有这种机制，导致RocksDB在遇到校验和错误时直接崩溃。

**实验与验证：**
- 在实验室环境中模拟了类似的读写负载和高内存压力，成功复现了问题。
- 通过增加删除操作，复现了元数据密集型工作负载，将问题复现时间从几天缩短到几小时。
- 测试了不同内核版本和其他代码级别，发现问题在较新的内核上仍然存在，但在Ubuntu Focal上无法复现。

**根本原因分析：**
- 发现问题与TC malloc库中的madvise free系统调用有关，该调用允许延迟释放内存，可能导致页面在未被标记为脏之前被释放，返回零填充页面。
- 确认问题为内核问题，涉及CPU调度、虚拟内存管理、内存回收和块I/O子系统。

**解决方案：**
- 在RocksDB路径中添加重试机制，以避免崩溃。
- 在Gperftools中修改madvise free为madvise don't need，确保内存立即释放，避免校验和错误。
- 提交了内核补丁，增加了对页面引用计数的检查，确保在内存回收时不会错误地释放页面。

**后续行动计划：**
- 继续跟踪内核补丁的上游合并进度，确保问题在稳定内核版本中得到修复。
- 提供Ubuntu内核的修复版本列表，供用户升级。
- 提醒开发者在项目中使用madvise free时需考虑其潜在影响，特别是在容器环境中。

**其他信息：**
- 提到了madvise free在其他开源项目中的问题，建议开发者在使用时进行充分考虑。
- 会议结束时，Dan Hill回答了观众的问题，并感谢大家的参与。

### 结论

本次会议详细讨论了一个Ceph集群性能问题的分析与解决过程，涉及内存管理、内核调度等多个技术层面。通过实验验证和根本原因分析，最终确定了问题所在并提出了有效的解决方案。会议强调了持续工程部门在技术支持中的重要作用，并鼓励社区成员在遇到类似问题时参考本次讨论的经验。