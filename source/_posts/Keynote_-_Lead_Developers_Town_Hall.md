---
title: "Keynote: Lead Developers Town Hall"
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


# Ceph社区会议纪要

## 参会人员介绍
- **Radakaim**: Raiders car techlete
- **Yarit**: Telemetry techlete
- **Matt Benjamin**: Senior Engineering Manager for Rails Gateway and NFL Schedule
- **Sam**: Lead for Crimson
- **Zach Dover**: Docs guy
- **Josh Duggan**: Member of the application here Council and long-time staff developer

## 主要议题及讨论内容

### 升级问题
- **问题**: 是否可以从Octopus直接升级到Reef，跳过Quincy？
- **答案**: 不可以，Ceph支持一次升级两个版本。可以从Octopus直接升级到Pacific或Quincy，但不能直接升级到Reef。

### 认证问题
- **问题**: 如何在不停机的情况下添加认证？
- **答案**: 可以通过文档添加认证，已有相关页面介绍如何启用认证，但可能缺少不停机的具体步骤。建议联系Zach获取更多细节。

### PG资源消耗
- **问题**: 如何获取PG的CPU或内存消耗？
- **答案**: 目前没有直接的方法，但可以考虑通过收集和聚合相关指标来推断PG的资源消耗。

### 冻结数据迁移
- **问题**: 是否有计划将冻结数据迁移到磁带存储？
- **答案**: 目前正在开发两个对象存储系统，Crimson项目可能是未来的解决方案。

### 性能改进
- **问题**: 新均衡器对读取IOPS和吞吐量的性能改进如何？
- **答案**: 正在进行测试，具体数据尚未公布。

### 大桶删除
- **问题**: 如何快速删除包含数百万文件的大桶，同时不 overload 集群？
- **答案**: 可以通过增加垃圾回收队列和调整相关设置来实现，但可能会影响其他流量。

### SSD性能优化
- **问题**: 如何配置OSD以最大化NVMe设备的性能？
- **答案**: 需要根据具体工作负载进行调整，可以参考Ceph官方博客中的性能优化文章。

### 文档改进
- **问题**: 如何帮助清理和改进Ceph文档？
- **答案**: 可以通过访问docs.ceph.com并点击顶部的大黄框链接，按照开发者指南的基本工作流程进行贡献。

## 决定事项
- **认证添加**: 确认可以通过文档添加认证，建议联系Zach获取更多细节。
- **文档改进**: 社区将致力于改进文档，特别是编写初学者指南和概述段落。

## 后续行动计划
- **认证文档**: Zach将负责更新认证相关的文档，确保包含不停机的具体步骤。
- **性能测试**: 继续进行新均衡器的性能测试，并及时公布测试结果。
- **文档贡献**: 鼓励社区成员通过docs.ceph.com参与文档的改进工作。

## 其他讨论
- **多站点配置**: 讨论了Ceph Gateway的多站点配置和重启桶的当前支持情况。
- **IPv6支持**: 强调了IPv6支持的重要性，并讨论了可能的解决方案。

## 会议结束
- 会议在感谢和掌声中结束，鼓励社区成员继续参与和贡献。