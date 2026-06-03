---
title: "Ceph RGW Refactoring Meeting 2026-02-25"
date: 2026-05-13
updated: 2026-05-14
tags:
  - "RGW"
categories:
  - "视频总结"
outline: deep
---
## 会议概述

本次 Ceph RGW Refactoring Meeting 于 2026 年 2 月 25 日举行，主要讨论了三个议题：RGW lifecycle policy 删除 bug 的修复进展与临时规避方案、RGW 内存使用优化方向（含 TCMalloc 调优探讨），以及 OIDC thumbprint 强制校验问题与 OIDC 元数据同步的后续工作。

## 议题一：Lifecycle Policy 删除 Bug（Boris）

### 问题背景

Boris 提出了两个关联的 tracker issue，其中一个与 RGW 的 lifecycle policy 删除行为有关。内部团队在删除 lifecycle policy 后误以为策略已生效，但实际上策略并未被正确移除，导致了数据丢失。

### 修复进展

- 相关 backport 已合并至 Squid 分支，将随 **19.2.4** 版本发布。
- 当前团队正在优先推进 Tentacle 的首个 point release，之后会聚焦 19.2.4。
- 可在 Ceph upstream releases Slack 频道的 19.2.4 线程中跟踪进展。

### 临时规避方案

在等待正式修复版本期间，建议**不要直接删除 bucket lifecycle**，而是将 lifecycle policy 的status 设置为 `disabled`，以阻止规则继续执行，避免误操作导致数据问题。

## 议题二：RGW 内存使用优化（Yuval 代 Mark）

### 问题背景

在使用 multipart upload 时，RGW 会将大分片并行写入多个 RADOS object以提升吞吐量。但当底层 OSD 使用高速介质（如 SSD）时，这种并行写入带来的性能收益边际化，却会造成显著的内存峰值，尤其在高并发场景下问题更为突出。

### 优化思路讨论

**Yuval 的提案：** 将控制并行写入窗口大小的参数从全局 config option 下沉至 placement target 级别，允许运维人员针对已知高速存储池降低并行度，从而减少内存消耗。

**Casey 的反馈：** placement target 粒度不够精细，更合适的粒度是 **storage class**，因为同一个 placement target 下可能同时存在快速和慢速的 data pool。建议扩展 storage class 的描述字段，支持附加调优参数。

**更长远的方向：** 社区对类似 OSD memory target、MON memory target 的 **RGW memory target** 机制有需求，即 RGW 能够根据当前并发请求数和其他内存占用动态调整窗口大小。这一方向实现复杂度较高，需要将缓存大小等众多 config option 纳入统一的内存预算管理。

### TCMalloc 调优探讨

- 有学生在 Google Summer of Code 项目中已实现 RGW 的 TCMalloc heap profiler，参考了 OSD 侧的实现，相关 PR 已通过 mock 测试。
- 当前使用的旧版 TCMalloc 主要优化点在于：将小于 256 KB 的小内存分配放入线程本地池（thread-local cache），实现无锁分配/释放。
- 可调节的参数有限，主要是一个控制线程本地缓存大小的环境变量，缺乏对大内存分配或线程级别的精细控制。
- GSoC 项目范围可定位为"调研与评估"，约 100 小时工作量，结论本身即为交付物。

## 议题三：OIDC Thumbprint 与元数据同步（Krunal）

### OIDC Thumbprint 强制校验问题

**现状：** AWS S3 API 中，创建 OIDC provider 时 thumbprint 和 client ID 均为**可选字段**，唯一必填项是 URL。但 Ceph RGW 自该功能引入以来一直将 thumbprint 设为**必填**。

**痛点：** 证书每 6 个月轮换一次是行业惯例，thumbprint 由证书派生，证书更新后 thumbprint 随之失效，用户必须手动重新调用 create OIDC 接口更新，运维负担较重。

**结论：** 建议创建 tracker issue，将 thumbprint 改为可选字段，与 AWS 行为对齐。Casey 将协调 Preetha 跟进审查。

### OIDC Admin 命令支持

**Krunal 的需求：** Bloomberg 作为集群运维方，需要在为租户创建账时同步配置 OIDC provider，目前只能通过 AWS CLI 或 SDK（如 boto3）操作，希望增加 `radosgw-admin` 命令支持，方便集群管理员直接管理 OIDC。

**Casey 的立场：** 维护与 S3 IAM API 并行的 admin 命令集成本较高，管理员仍可使用 AWS CLI 完成操作，因此持保留态度。但若有人愿意贡献该功能，欢迎提交 PR。

### OIDC 元数据同步（Multi-site）

- Shilpa 此前有一个 OIDC metadata sync 的 PR，但长期未合并，需要 rebase 并可能存在缺失项。
- Casey 提到已完成 metadata backend 重构，Shilpa 确认其改动是在该重构合并后进行的，理论上冲突应较少。
- Casey 在 accounts 功能的测试用例中已有一个 `test_account_metadata_sync`，其中包含注释掉的 OpenID Connect provider 部分，**取消注释即可获得 OIDC metadata sync 的测试覆盖**，Krunal 可直接复用。

## 后续行动计划

| 负责人 | 行动项 |
|--------|--------|
| Boris | 关注 Ceph Slack 19.2.4 线程，临时使用 lifecycle status disabled规避问题 |
| Yuval | 在 tracker 中补充 storage class 级别内存参数的设计方案 |
| Krunal | 创建 tracker issue申请将 OIDC thumbprint 改为可选字段，并 ping Casey/Preetha |
| Krunal | 评估复用或重启 Shilpa 的 OIDC metadata sync PR |
| Krunal | 参考 Casey 的 accounts 测试用例，取消注释 OIDC 部分以补充测试覆盖 |
| Casey | 协调 Preetha 审查 thumbprint 可选化 tracker |
| GSoC 学生 | 继续推进 TCMalloc heap profiler PR的合并，并评估进一步调优空间 |
