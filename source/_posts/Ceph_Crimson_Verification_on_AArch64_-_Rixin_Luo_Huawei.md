---
title: "Ceph Crimson Verification on AArch64 - Rixin Luo, Huawei"
date: 2023-05-18
updated: 2023-05-19
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Crimson验证在Arc 34上的部署与优化

#### 会议时间：[具体日期]

#### 会议地点：[具体地点]

#### 主持人：Lindsay

#### 参会人员：[参会人员名单]

#### 会议内容：

1. **部署与优化**
   - **部署方法**：通过yum文件添加代码，支持在ARM版本上构建Crimson镜像，并使用Benchmark工具如rados bench和fio进行性能测试。
   - **优化进展**：PRS self-adium部分已由Adam King审核，希望有人能帮助审查并合并。

2. **内存泄漏与浪费**
   - **问题描述**：在内存存储中，大量小写操作会导致缓冲区列表包含许多无效数据，无法重用保留的内存页，可能导致内存不足。
   - **解决计划**：将问题贡献给社区，并继续优化。

3. **性能优化**
   - **瓶颈分析**：发现原子操作在内存端口模块中占用近35%的 overhead，建议禁用lse指令以减少争用。
   - **测试结果**：禁用lse后，使用2MB页面大小，对于小包和大包分别获得50%和8%的性能提升。

4. **多节点集群测试**
   - **测试环境**：使用三台ARM服务器构建测试场景，使用36个OSD和三副本。
   - **测试结果**：系统在单次测试中表现良好，但与经典BlueStore相比，性能仍有差距，正在进行优化。

5. **社区贡献与未来计划**
   - **贡献内容**：将优化代码和协议贡献给社区，包括内存池和缓冲区列表的优化。
   - **未来工作**：继续优化Ceph存储系统，特别是C-Store部分，解决读写放大问题，并进行更多测试案例和CI集成。

#### 决定事项：
- 继续优化Crimson的部署和性能，特别是内存管理和原子操作的优化。
- 将优化成果和协议贡献给Ceph社区。

#### 后续行动计划：
- 完成PRS self-adium部分的合并。
- 继续进行多节点集群的性能测试和优化。
- 解决内存泄漏和浪费问题，并贡献给社区。
- 优化C-Store的读写放大问题，并进行更多测试。

#### 会议结束：
- 会议在提问环节后圆满结束，Lindsay感谢大家的参与和贡献。

#### 备注：
- 如有进一步问题或需要更多技术细节，请联系Jason Johnson或发送邮件至[相关邮箱]。

[会议纪要结束]