---
title: "2018-08-09 Ceph Performance Weekly"
date: 2020-08-26
updated: 2020-08-26
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 参会人员
- Casey
- Mark
- Sage
- Igor
- Radek
- Gregor
- Jason
- Braddock
- Shawn Peng
- Alfredo
- Ari

#### 会议时间
- 日期：具体日期未提供
- 时间：具体时间未提供

#### 主要议题
1. **旧的Pull Request复活**
   - 讨论了复活一个旧的Pull Request，该请求涉及重新启动一个复杂的实现，主要关于维护顺序的问题。

2. **Radek的加密工作**
   - Radek介绍了他在加密方面的工作，特别是关于使用低级AES实现的问题，该实现不使用硬件加速。讨论了与设置成本和实际加速之间的关系。

3. **Igor的Tiny Appends Pull Request**
   - Igor介绍了他的Tiny Appends Pull Request，该请求涉及在数据库中直接存储小对象，而不是将它们存储在磁盘上。讨论了性能结果和潜在的改进。

4. **EC Partial Stripe Reads**
   - 讨论了新的EC Partial Stripe Reads，需要进一步的审查。

5. **RGW Up Tracker优化**
   - 讨论了RGW Up Tracker的优化，包括合并的请求和未合并的优化。

6. **MVS Balancer和Blue Store Shard Completions**
   - 讨论了MVS Balancer的工作和Blue Store中的Shard Completions，特别是关于性能测试和线程配置的问题。

7. **EDP配置选项和设备模板**
   - 讨论了EDP配置选项和设备模板，特别是关于如何简化用户设置和避免配置混乱的问题。

8. **Blue Store的Tiny Writes优化**
   - Igor详细介绍了Blue Store的Tiny Writes优化，包括性能测试结果和不同方法的比较。

#### 决定事项
- 需要进一步审查和测试EC Partial Stripe Reads。
- RGW Up Tracker的优化将继续进行，包括更详细的性能数据。
- 需要对Blue Store的Tiny Writes进行更深入的性能测试，特别是在实际使用场景中。
- 对于EDP配置选项和设备模板，决定不引入新的HDD/SSD设置，而是保持现有选项，避免用户混淆。

#### 后续行动计划
- 对EC Partial Stripe Reads进行详细审查和测试。
- 继续优化RGW Up Tracker，提供更多性能数据。
- 对Blue Store的Tiny Writes进行实际使用场景的性能测试，特别是关注RocksDB的compaction负载。
- 继续讨论和优化EDP配置选项和设备模板，确保用户设置的简化和清晰。

#### 其他讨论
- 讨论了RocksDB的compaction负载和如何更好地配置RocksDB的存储空间。
- 讨论了Blue Store的存储配置和如何动态调整数据库卷的大小。

#### 会议结束
- 会议在感谢所有参与者的贡献后结束。