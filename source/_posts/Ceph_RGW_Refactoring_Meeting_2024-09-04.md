---
title: "Ceph RGW Refactoring Meeting 2024-09-04"
date: 2024-09-04
updated: 2024-09-05
tags:
categories:
- "视频总结"
subtitle: tech
---



**会议纪要**

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： Gabby（演示者）、Matt、Kyle、Seth等

**会议主题**： ddop（数据去重优化项目）演示及讨论

**会议内容**：

* **ddop项目概述**：
    * ddop项目旨在优化Ceph存储中的数据去重功能，提高存储效率和性能。
    * 第一阶段将支持大于4MB的对象进行去重。
    * ddop基于ref计数和manifest共享机制，通过sharding（分片）的方式并行处理数据。
    * 项目将分为两个阶段：第一阶段基于对象名进行sharding，第二阶段基于md5进行sharding。
    * ddop项目将采用多线程并行处理，以提高效率。
* **ddop项目演示**：
    * Gabby展示了ddop项目的演示过程，包括数据加载、去重操作、统计结果等。
    * 演示过程中，ddop项目能够有效地减少冗余数据，并提高存储效率。
    * 会议中讨论了ddop项目的可扩展性、性能优化等方面。
* **ddop项目讨论**：
    * 会议讨论了ddop项目的以下方面：
        * **可扩展性**： ddop项目通过sharding的方式，可以实现线性扩展，提高处理效率。
        * **性能优化**： ddop项目通过并行处理和数据本地化，提高了去重操作的效率。
        * **适用场景**： ddop项目适合于存储大量数据的场景，例如备份、归档等。
        * **未来方向**：
            * 支持更小的对象去重。
            * 支持子文件去重。
            * 将ddop项目与object packing（对象打包）技术结合。
            * 将ddop项目与erasure coding（冗余编码）技术结合。
* **行动计划**：
    * Gabby将整理ddop项目的代码，并提交PR（Pull Request）。
    * 参会人员将对ddop项目的代码进行审查，并提出改进意见。
    * 将ddop项目与Ceph存储系统集成，并进行测试。

**关键术语**：

* ddop（数据去重优化项目）
* sharding（分片）
* ref计数
* manifest共享
* md5
* object packing（对象打包）
* erasure coding（冗余编码）

**总结**：

ddop项目是一个非常有潜力的Ceph存储优化项目，能够有效地提高存储效率和性能。会议中，参会人员对ddop项目进行了详细的讨论，并提出了改进意见。期待ddop项目能够尽快落地，为Ceph存储带来更多价值。