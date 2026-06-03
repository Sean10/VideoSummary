---
title: "Ceph RGW Refactoring Meeting 2026-01-28"
date: 2026-01-28
updated: 2026-01-29
tags:
  - "RGW"
  - "对象存储"
  - "加密"
  - "去重"
categories:
  - "视频总结"
outline: deep
---
## 会议概述

本次 Ceph RGW Refactoring Meeting 于 2026 年 1 月 28 日举行，主要讨论了三个议题：RGW 中 object history (OH) 索引条目泄漏问题、RGW admin CLI帮助文档自动生成改进方案，以及 GCM 加密实现计划。

## 议题一：Object History 索引条目泄漏问题

### 问题描述

Bloomberg 团队在下游测试中发现，当一个对象的所有版本被删除后，OH（object history）相关的索引条目存在泄漏现象。清理代码中存在某种竞态条件（race condition），导致清理流程未能正常完成。

### 关键细节

- 该问题并非新版本引入的 regression，在 squid 和更早版本中同样存在，tentacle 版本也受影响
- tentacle 版本尚未引入基于时间戳的变更，因此可以排除时间戳相关改动导致的回归
- 清理失败时会返回 `E_CANCELLED` 错误，表明清理操作正在与其他操作产生竞争，但竞争的另一方并未完成清理工作
- 问题与 multi-site 场景相关，在 secondary 侧尝试将某个版本提升为 current 时被发现
- 已有 `bucket check --o` 和 `bucket check --unlink` 命令可用于发现和修复此类问题

### 后续行动

- 正在编写 multi-site 测试用例以复现该问题，目前测试本身存在一些行为异常需要修复
- 相关 tracker issue 和 pull request 已创建并在议程中链接
- 团队将持续跟进该问题的根本原因排查

## 议题二：RGW Admin CLI 帮助文档自动生成

### 背景与痛点

Jack 提出了改进 RGW CLI 帮助文档生成机制的想法。当前存在的核心问题是：帮助文档与实际代码行为不一致，且每次新增或修改命令时需要手动同步多处文档，包括：

- man page
- radosgw-admin 的 help 输出
- admin 操作指南文档
- docs.ceph.com 上的独立文档页面

以新增 bucket logging 命令为例，需要手动修改至少三到四处地方，极易出错或遗漏。

### 讨论方向

**目标**：将所有命令和参数的描述信息集中定义在代码中，然后自动生成各类文档输出。

**技术方案讨论**：

1. **Boost Program Options**：团队讨论了使用 boost program options 库重构 radosgw-admin 命令行解析的可行性。该库功能强大，支持子命令（git 风格的 subcommand）和层级化参数，但对子命令的支持需要一定的手动控制，使用体验不如一些新库流畅。

2. **新型 CLI 库**：提到了 Lyra 等更现代的 C++ CLI 库，但这些库在功能覆盖上可能不如 boost program options 全面。

3. **YAML 描述文件方案**：参考 Ceph 配置选项的现有做法——用 YAML 文件描述所有选项，再通过 Python 脚本生成文档和源代码。如果 boost program options 无法满足文档生成需求，可以考虑类似的元数据驱动方案。

4. **RST 引用机制**：现有的 Ceph 选项文档已实现通过 RST 指令直接引用 YAML 中的描述，避免复制粘贴，这一机制可以推广到 admin 命令文档。

**兼容性考量**：

- 团队倾向于不破坏现有脚本的兼容性，但对于有充分理由的语法变更可以接受
- 建议采用先 deprecation 再移除的流程，给用户至少一到两个版本的过渡期
- radosgw-admin 目前复用了 Ceph 通用的 arg parse 机制，任何改动需要考虑与 `ceph_argparse` 的兼容性

**范围与决策**：

- 本次讨论聚焦于 RGW 组件内的改进，RGW 团队有权自主决策
- 若要推动 Ceph 全局 CLI 统一改造，应在 Ceph Developer Monthly 会议上提出（下周三有一场）
- 建议先在 radosgw-admin 中完成设计验证，再考虑推广到其他工具

**GSoC 机会**：Ival 建议将部分任务拆分为 Google Summer of Code（GSoC）学生项目，待设计方案确定后可以细化具体任务描述。

### 后续行动

- Jack 将更新 tracker，补充本次讨论内容和可能的推进路径
- Jack 计划先构建一个最小化原型，展示可行的实现方向，推动方案讨论
- 对此感兴趣的成员可在 tracker 中添加评论

## 议题三：GCM 加密实现

### 需求背景

某团队有硬性要求，需要在年底前在 Ceph 中实现 GCM（Galois/Counter Mode）加密。Kyle 也在关注此议题，并已在 Slack 上创建了专门的讨论频道。

### 核心技术问题：加密开销的处理

GCM 加密会为每个 4K 数据块引入 16 字节的额外开销，需要决定如何在 API 层面处理这一差异。

**两种参考实现**：

- **AWS方式**：通过对象属性记录实际（未加密）大小，list、GET、HEAD 等请求均返回逻辑大小，对用户透明
- **MinIO 方式**：直接暴露磁盘上的实际存储大小（含加密开销），用户可见加密带来的大小变化

**团队决策**：采用类似 AWS 的方式，与 RGW 现有的服务端压缩（server-side compression）处理逻辑保持一致——上传 2GB 对象，API 始终返回 2GB，磁盘实际占用的差异通过内部 x-attr 属性记录，不对外暴露。

### deduplication 与加密的交互

- 当前 RGW 的 deduplication 实现会跳过已加密的对象
- Matt 曾提出支持基于块（block-based）的 deduplication，但这与 GCM 加密的交互方式尚不明确
- 团队认为在 block-based dedup 的设计方案明确之前，暂不考虑与 GCM 的集成

### 后续行动

- 团队将在对象上添加内部 x-attr 属性记录未加密大小，参考现有 compression 和 encryption 的实现模式
- 持续跟进上游 Slack GCM 专属频道的讨论
- Kyle 计划推动该功能进入 Ceph 上游版本（umbrella 或后续 release）

## 其他事项

下次会议与 Ceph Developer Monthly 时间冲突，将取消 RGW Refactoring Meeting，建议成员参加 Ceph Developer Monthly 会议。
