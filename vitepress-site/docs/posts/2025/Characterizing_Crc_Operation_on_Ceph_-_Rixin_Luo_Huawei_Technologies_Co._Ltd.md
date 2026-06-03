---
title: "Characterizing Crc Operation on Ceph - Rixin Luo, Huawei Technologies Co., Ltd"
date: 2025-01-23
updated: 2025-01-24
tags:
  - "Ceph"
  - "性能优化"
  - "BlueStore"
categories:
  - "视频总结"
outline: deep
---
本会议纪要详细描述了关于Ceph中循环冗余校验（CRC）操作的分析与优化。以下是对会议内容的总结：

### 会议主题

Ceph 操作中的循环冗余校验（CRC）分析与优化

### 会议内容总结

#### 1. CRC 的重要性与背景
CRC用于检测数据错误，现代CPU提供指令加速CRC操作。在Ceph中，CRC操作占3%的CPU利用率，优化CRC有助于提升性能。

#### 2. CRC 操作的执行机制
CRC操作通过`m_worker`和`tpd_thread`两种策略执行。`m_worker`负责接收和发送消息，消息结构包括`Preamble`、`Payload`和`AppLog`。

#### 3. Bluestore 中的 CRC 计算
Bluestore在读写操作中计算CRC，确保数据正确性。相关配置参数影响CRC行为。

#### 4. 工作负载分析
使用`RBD`工作负载进行测试，测试了4KB和64KB读写操作，副本数为1和3。使用`BCC Trace`工具统计了`crc32c`函数调用次数。

#### 5. CRC 操作的分布分析
4KB读写操作中，小尺寸CRC操作占主导地位，约84%。64KB读写操作中，小尺寸CRC操作仍占50%左右。

#### 6. 副本操作的 CRC 分析
单副本和三副本读写操作中，小尺寸CRC操作占比较高。副本操作的回复消息占用了较多的CRC操作。

#### 7. 优化建议
- 优化编码预处理，避免小尺寸CRC操作。
- 优化数据结构，提高CRC操作效率。
- 使用内联汇编优化`Preamble`消息头，提升性能约2%。
- 优化内存分配策略，提升CPU缓存效率。

#### 决定事项与后续行动计划
- 对Bluestore中的CRC操作进行优化，特别是针对小尺寸数据块的CRC计算。
- 性能测试与验证优化后的CRC操作效率。
- 开发团队根据优化建议进行代码实现，并集成到Ceph的主分支中。

### 会议结论

通过优化CRC操作，可以有效提升Ceph的性能和数据完整性。开发团队将根据优化建议进行代码实现，并集成到Ceph的主分支中。