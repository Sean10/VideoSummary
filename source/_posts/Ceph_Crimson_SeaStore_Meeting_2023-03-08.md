---
categories:
- 会议纪要
date: 2023-03-08
subtitle: Ceph_Crimson_SeaStore_Meeting_2023-03-08
tags:
- Ceph
- 分布式存储
- CRUSH 算法
- 可用性
- 可伸缩性
- 对象存储
- 块存储
- 文件系统存储
- 一致性
- 去中心化
- 性能
- Bluestore
- Bluefs
- Rocksdb
- OSD
- MON
- MDS
- PG
- RADOS
- librados
- libcephfs
- cephfs
- rbd
- radosgw
- RGW
- RESTful API
- 认证
- 授权
- 加密
- 纠错编码
- 复制
- 快照
- 克隆
- 虚拟化
- 云计算
- 存储
title: Ceph Crimson/SeaStore Meeting 2023-03-08
updated: 2023-03-09
---



### 会议纪要

**会议时间：** 2023-03-08
**参会人员：** [列出参会人员]

#### 主要议题：
1. **个人工作更新**
   - **Junction:** 正在处理 `classic scrub` 和 `Crimson scrub`，同时更新了 `grain cache` 的最终版本，并关注 `max application size` 的 bug 问题。本周将重点审查 `lba3 optimization`，并计划在未来几周内投入更多精力到 `multiple messenger` 项目中。
   - **Harsh:** 报告了在配置 Crimson 镜像集群时遇到的问题，确认问题与 reef build 相关，而非 Crimson 本身。
   - **Kevin:** 完成了垂直系统修改和 CN storm 系统的安装测试，并请求团队进行审查。
   - **Rocky:** 提到上周的 PR 主要关于 self volume 和 surveillance，Adam King 正在审查中。
   - **[其他人员]:** 汇报了各自的工作进展和计划。

2. **讨论文档：**
   - **Joyhound** 提出的文档关于在 systore 中实现热数据缓存功能，讨论了设计原则，包括利用应用程序访问模式的局部性，以及数据和元数据的访问模式差异。

#### 决定事项：
- **关于热数据缓存的讨论：** 团队深入讨论了 Joyhound 的文档，涉及缓存策略、数据局部性、以及如何与现有 tiering 系统集成。建议将缓存策略设计为可插拔的。

#### 后续行动计划：
- **实施计划：** 首先实现读取时的数据提升功能，然后独立考虑不同的驱逐策略。
- **文档更新：** Joyhound 将根据会议反馈更新文档，增加更多细节和设计考虑。

**会议结束：** 会议在讨论完所有议题后结束，团队成员被鼓励继续推进各自的工作，并期待下一次会议的更新。

**备注：** 会议中提到了一些技术细节和特定术语，如 `LBA tree`、`tiering implementation`、`eviction policy` 等，这些内容对于理解会议内容和后续行动非常重要。