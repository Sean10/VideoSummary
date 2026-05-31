---
categories:
- 视频总结
date: 2018-04-12
subtitle: Ceph 性能周报 - 2018年4月12日
tags:
- Ceph
- 性能优化
- 分布式存储
- RocksDB
title: "'2018-Apr-12:: Ceph Performance Weekly'"
updated: 2018-04-13
---




本次会议主要讨论了 Ceph 存储系统在性能优化、功能开发以及相关技术问题。以下是会议的关键细节和决定的事项：

**关键细节**：

* **Pull Requests**： 讨论了 etherpad 加载问题，并建议开始处理 Pull Requests。
* **RocksDB2**： 更新了 RocksDB2 的当前上游版本，并讨论了相关 bug 和性能测试。
* **Beast**： 讨论了将 CivetWeb 替换为 Beast 的方案，以优化性能和资源消耗。
* **性能测试**： 讨论了性能测试的重要性，并分享了相关测试结果。
* **Buffer List**： 讨论了 Buffer List 的优化方案，包括使用 Small Vector 和改进内存管理。
* **CRC 优化**： 讨论了 CRC 优化方案，并建议移除 Buffer List 中的 CRC 相关功能。
* **C-Store**： 讨论了 C-Store 的规划，包括对象存储接口和事务协议。
* **Seastar**： 讨论了 Seastar 的性能优化和功能开发。

**讨论的主要议题**：

* **性能优化**： 讨论了 Ceph 存储系统中各个组件的性能优化方案，包括 RocksDB、Buffer List、网络协议等。
* **功能开发**： 讨论了 Ceph 存储系统中新功能的开发，例如 C-Store、对象存储接口等。
* **技术问题**： 讨论了 Ceph 存储系统中遇到的技术问题，例如 Buffer List 的内存管理、CRC 优化等。

**决定的事项**：

* 开始处理 Pull Requests。
* 更新 RocksDB2 的当前上游版本，并进行相关测试。
* 将 CivetWeb 替换为 Beast，优化性能和资源消耗。
* 对 Buffer List 进行优化，包括使用 Small Vector 和改进内存管理。
* 移除 Buffer List 中的 CRC 相关功能。
* 制定 C-Store 的规划，包括对象存储接口和事务协议。
* 继续优化 Seastar 的性能和功能。

**后续行动计划**：

* 各参会人员根据会议讨论内容，继续进行相关开发工作。
* 定期召开会议，跟踪项目进展情况。

**其他事项**：

* 讨论了 Ceph 存储系统中各个组件的优化方向和目标。
* 讨论了 Ceph 存储系统中遇到的技术难题和解决方案。
* 讨论了 Ceph 存储系统的未来发展方向。