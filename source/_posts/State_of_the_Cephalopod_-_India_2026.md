---
title: State of the Cephalopod - India 2026
date: 2026-04-02
updated: 2026-04-03
tags:
- Ceph
- 分布式存储
categories: 
- 视频总结
subtitle: State_of_the_Cephalopod_-_India_2026
---

## 活动背景与欢迎致辞

本次活动为 Ceph Days2026 India 章节，在印度班加罗尔举办，是该地点举办的第四届 Ceph Day，也是迄今为止参与人数最多的一届。活动由 IBM 主办，主持人 Vinayak（IBM QA 测试开发工程师）和 Shukha（IBM 软件包开发工程师）共同主持。IBM 项目总监 Viri 和 SA 管理项目总监 Sina 代表 IBM 发表欢迎致辞，对社区成员克服班加罗尔交通不便前来参会表示感谢。

## 主题演讲：Ceph 项目现状（State of the Cephalopod）

主讲人为 IBM 产品项目总监、Ceph 核心开发团队负责人，同时也是 Ceph 执行委员会成员及 Ceph 基金会治理委员会成员，曾长期担任 RADOS 组件技术负责人。

### 项目规模与贡献数据

Ceph 从一个博士研究项目发展为企业级存储软件，拥有近 20 年的存储革新历史。当前项目主要指标如下：

- 贡献者数量：约 1,500 人
- 源代码行数：超过 700,000 行（不含文档和 QA 相关代码）
- 总提交次数：超过 160,000 次，且仍在持续增长

通过 Linux Foundation Insights（LFX）平台对接 GitHub仓库，可以观察到过去五年项目 Star 数量和提交活跃度的持续增长趋势，充分体现了 Ceph 在开发者社区和用户社区中的广泛影响力。

### 用户社区增长

Ceph 上游 telemetry 框架数据显示，过去五年中集群总存储容量和已用容量均呈现显著增长态势，截至 2025 年底数据尤为亮眼，印证了 Ceph 用户社区的持续壮大。

### 版本发布情况

Ceph 项目保持每年发布一个主要版本的节奏，同时维护两个 backport 版本以支持旧版本用户：

- **Tentacle**：2025 年 11 月正式 GA 发布，为当前最新稳定版本
- **Umbrella**：正在开发中，将是第 21 个 Ceph 上游版本
- **Reef（18.x）**：即将 EOL（End of Life），18.28 版本正在发布中
- **Squid**：自 2024 年起持续维护中

### 重要里程碑公告

演讲者在本次活动上首次正式宣布：**V 版本已被命名为 Vampire**。Vampire Squid（吸血鬼乌贼）是真实存在的头足类动物，与 Ceph 的命名传统完全吻合。

## 社区建设与新举措

### Ceph 用户委员会（Ceph User Council）

该委员会于 2025 年启动，持续成长和成熟。主要工作方式是向生产环境中使用 Ceph 的用户社区发送调查问卷，重点关注 performance、orchestration、usability 等日常运维关切，并将反馈转化为可落地的改进项，包括软件优化、文档改进和 bug 修复等。相关讨论在每月一次的 Ceph UserDev 会议中进行，欢迎社区成员参与。

### 社区互动渠道

- **Slack**：最主流的社区互动平台，设有用户频道、开发者频道和版本讨论频道
- **Meetup 群组**：用于发布 UserDev 会议、Ceph Developer Summit 等活动通知

### 2026 年新举措

1. **Ceph Tech Talks 重启**：2026 年 1 月由 Deepshika Singh 主讲首期，内容为如何在 Sepia Lab 外部环境运行 Teuthology（Ceph 自动化测试框架），所有录像均上传至 YouTube
2. **Ceph Release Engineering 社区会议**：由 Patrick Donnelly 主导，旨在通过引入更严格的流程来规范版本发布节奏
3. **Ceph Subreddit 恢复**：此前因故暂停，现已重新开放
4. **Google Summer of Code（GSoC）**：Ceph 再次入选 GSoC，多个项目和导师参与其中

## 技术亮点

### 基础设施迁移

Ceph 上游 Sepia Lab 的所有服务（包括开发、testing、performance 和 release 基础设施）已从 Red Hat 基础设施完成迁移至 IBM 基础设施。此次迁移历时数年，于 2025 年底启动，目前日常运营已全面恢复正常。

### RADOS 层新特性

**Fast EC（快速 Erasure Coding）** 是本次最受期待的重磅特性，为各类工作负载带来显著的 performance 和容量提升：

- 传统上 object storage 配合 erasure coding 已广受欢迎
- Fast EC 现在使 block storage 和 file system storage 工作负载也能使用 erasure coded pools
- 鼓励用户积极测试并反馈结果

### RGW（RADOS Gateway）新特性

引入 **AWS IAM Accounts** 支持，通过与 AWS 兼容的自助服务 API，为客户和租户提供对角色、身份和权限的细粒度控制。详细信息可参阅 ceph.io 上的专题博客。

### CephFS 新特性

新增 **大小写不敏感目录（Case-Insensitive Directories）** 支持，提升与 kernel cephfs、NFS 和 Samba 的互操作性。

### Dashboard 与管理界面

- IAM Account 管理和多项 RGW 功能已集成至 UI
- 新增 SMB、NVMe 相关工作流的 Day 1/Day 2 操作支持

### cephadm 改进

- 新增 **证书管理（Certificate Management）** 功能
- 持续投入 scalability 改进，提升 Ceph Manager 处理大规模 OSD 集群的能力

### Crimson 项目进展

Crimson 项目配套的新一代 object store **Seastore** 已在 Tentacle 版本中进入 **Tech Preview** 阶段，这是团队的重大里程碑。目前仍在持续优化 performance，欢迎对 performance 感兴趣的用户测试并通过专属 Slack 频道反馈结果。

## 近期与未来活动

- **Cephalocon 2025**：已成功举办
- **Ceph Day India 2026**（本次活动）：班加罗尔，2026 年开年首场
- **Frankfurt Meetup**：与本次活动同日举行
- **Ceph Day Raleigh**：由 IBM赞助，在 IBM Raleigh 办公室举办，即将于下周举行
- **Ceph Day London**：计划于 2026 年 6 月举办，将是连续第三届伦敦 Ceph Day

更多活动信息请关注 Ceph 邮件列表和 Slack 频道。

## 致谢

本次活动由赞助商 **Clyso** 和 **IBM** 提供支持，同时向幕后付出大量心血的组织委员会、评审委员会及全体工作人员致以诚挚感谢。
