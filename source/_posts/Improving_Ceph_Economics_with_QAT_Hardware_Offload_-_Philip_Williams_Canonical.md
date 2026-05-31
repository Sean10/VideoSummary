---
title: Improving Ceph Economics with QAT Hardware Offload - Philip Williams, Canonical
date: 2025-01-23
updated: 2025-01-24
tags:
- Ceph
- 存储优化
- 分布式存储
categories: 
- "视频总结"
subtitle: Improving_Ceph_Economics_with_QAT_Hardware_Offload_-_Philip_Williams_Canonical
---

### 会议纪要：Ceph与Intel QAT技术的集成与优化

**会议主题**：Ceph与Intel QAT（Quick Assist Technology）技术的集成与性能优化

**主讲人**：pH Williams，Canonical产品经理

**会议时间**：近期

#### 会议关键细节：

1. **Ceph与QAT的集成背景**：
   - Ceph作为硬件无关的分布式存储系统，通过集成Intel QAT硬件加速技术，可以提升性能和效率。
   - QAT支持加密、压缩等功能，特别适用于需要高性能存储和处理的场景。

2. **QAT的历史与硬件支持**：
   - QAT技术最初作为PCIe卡于2008-2010年推出，后来集成到CPU中，如Intel的Ice Lake、Sapphire Rapids和Emerald Rapids处理器。

3. **Ceph中的QAT应用**：
   - 在RADOS Gateway (RGW)、BlueStore和OpenSSL等组件中启用QAT加速，提高压缩和加密效率。

4. **性能测试与结果**：
   - 在4节点Ceph集群上进行的性能测试显示，启用QAT压缩后，读取吞吐量恢复至接近无压缩水平，写入吞吐量略有提升。

5. **不同数据集的压缩效果**：
   - 对于合成数据，压缩后存储节省约25%；对于真实数据集，压缩效果各异，最高可达68%。

6. **成本与收益分析**：
   - 通过QAT压缩，可以在不显著增加成本的情况下，大幅减少存储空间需求，降低每GB存储的成本。

7. **Ceph中的QAT启用步骤**：
   - 使用MicroOS快速部署Ceph集群，启用QAT引擎服务，配置RADOS Gateway和Zone Placement，启用Zstandard（Zstd）压缩算法。

8. **未来改进**：
   - Canonical正在改进snapd，以便更方便地与QAT引擎集成。

#### 讨论与决定事项：

- **QAT在Ceph中的应用前景**：QAT的压缩功能在Ceph中具有显著的商业价值。
- **性能与成本的平衡**：启用QAT会增加一定的CPU开销，但通过减少存储空间需求，可以在总体成本上获得显著收益。
- **未来工作**：Canonical将继续优化Ceph与QAT的集成。

#### 后续行动计划：

1. **进一步测试**：在更多真实场景中测试QAT压缩的效果。
2. **文档更新**：更新Ceph与QAT集成的文档。
3. **社区推广**：向Ceph社区推广QAT的应用。