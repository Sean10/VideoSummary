---
title: Ceph S3 – Dynamic Placement and Optimized Retention
date: 2026-04-02
updated: 2026-04-03
tags:
- Ceph
- RGW
- 对象存储
categories: 
- 视频总结
subtitle: Ceph_S3_Dynamic_Placement_and_Optimized_Retention
---

## 演讲背景

本次演讲来自一位在高等教育与科研环境中工作超过 20 年、自 2014 年（Firefly 版本）起便深度使用 Ceph 的工程师。演讲主题聚焦于 Ceph S3（即 RGW/radosgw）的动态数据放置（Dynamic Placement）与优化数据保留（Optimized Retention）两大核心能力。


## 一、S3 Storage Classes 与 Placement Targets

Ceph 集群支持配置多个 S3 storage classes，每个 storage class 可以映射到不同的 pool 和数据放置策略。常见的差异化维度包括：

- **性能**：NVMe SD vs HDD
- **访问频率**：热数据 vs 冷数据
- **持久性与成本**：replication pool vs erasure coding pool
- **压缩**：可借助 Intel QAT 等硬件卸载压缩计算

S3 客户端在写入对象时可以指定 storage class，但实际场景中客户端经常不指定，或定不当。这正是动态放置需要解决的问题。


## 二、Dynamic Placement：Lua 脚本驱动的动态存储类分配

### 核心思路

当客户端未指定 storage class，或指定不合理时，RGW 可以通过 Lua 脚本在请求处理过程中自动为对象分配合适的 storage class。

### 可用的判断维度

- 对象扩展名（如 `.mp4`、`.pdf`）
- 对象大小（如是否超过 1 MB、2 MB 阈值）
- Tenant 名称
- Bucket 名称
- 上传方式（multipart upload vs单次 PUT）

### Lua 脚本执行时机

RGW 支持在以下请求阶段执行 Lua 脚本：

- `pre-request`
- `post-request`
- `background`
- `get data` / `put data`

脚本可以读取并修改对象的 metadata，从而在写入时动态设置 storage class，确保存储效率和访问性能从数据落盘的第一刻起就得到保障。

### 典型用例：VM 备份与恢复

以 VM backup and replication 软件为例：

- 数据对象大小通常在 1 MB 到 8 MB 之间
- 索引、日志、指针等元数据对象大小仅为 0 字节到 64 KB

Lua 脚本可以将小对象路由到 replicated pool（低延迟），将大对象路由到 erasure coding pool（高效率），实现自动分层。

### 其他 Lua 脚本用例

- 在 bucket ACL 之上增加额外的访问控制层（如强制只读或只写），防止 ACL 配置错误导致数据泄露
- 为特定 bucket 的请求添加追踪日志
- 在客户端未指定时自动补充默认 metadata
- 仅在发生错误时记录操作日志
- 采集操作 trace 用于分析

### Lua 性能与可靠性

- 初步测试显示 Lua 脚本引入的延迟极低，通常在微秒级别
- 每个执行上下文最多消耗约 120 KB RAM（可通过配置调整）
- 脚本超时默认为 1 秒；脚本执行失败（超时或语法错误）对 S3 客户端请求是**非致命的**，客户端会收到正常响应，如同脚本未执行
- 近期合并的优化：通过缓存 Lua 字节码来提升性能，同时减少读取存储 Lua 脚本的 RADOS 对象所需的网络调用次数


## 三、Optimized Retention：基于 Lifecycle Policy 的优化数据保留

### Lifecycle Policy 的过渡条件

Ceph Squid 版本新增了基于对象大小的过渡条件：

- `object size greater than`
- `object size less than`

即使在写入时未使用 Lua 脚本，也可以通过 lifecycle policy 将数据从 replicated pool 迁移到 erasure coding pool，或反向迁移。

### 压缩与解压缩联动

本周（演讲当周）社区合并了一个新特性：在 lifecycle过渡时同步执行压缩或解压缩。此前存在一个问题：对象从一个 storage class 过渡到另一个启用了压缩的 storage class 时，压缩并不会被应用。经过与社区成员（Casey、Matthew Eller）的快速讨论，当天即完成了修复，是社区高效协作的典型案例。

### 其他 Lifecycle 能力

- 过期非当前版本（non-current versions），同时保留指定数量的历史版本
- 自动清理未完成的 multipart upload 分片（tailed/incomplete parts）
- 支持通过 tag 或 prefix 选择性地应用 lifecycle 规则

> **注意**：lifecycle 的expire 规则会永久删除数据，使用时务必谨慎。建议配合 versioning 使用，并至少保留一个版本。


## 四、配置方法

### Pool 与 Storage Class 配置

1. 创建多个 pool，配置不同的 erasure coding profile
2. 使用 `radosgw-admin zonegroup` 命令将新 storage class 添加到 zone group
3. 将 storage class 绑定到对应的 pool，并配置是否启用压缩

### Lua 脚本配置方式

**方式一（静态）**：将规则直接写入 RGW 服务配置，重启 RGW 后生效。

**方式二（动态）**：在 RGW 配置中引用本地文件系统路径，规则配置文件可在不重启 RGW 的情况下直接修改，实时生效。

### Lifecycle 配置

使用 AWS S3 兼容命令（如 `put-bucket-lifecycle-configuration`）按 bucket 粒度上传 lifecycle 配置文件。

### 调试与验证

- 使用 `debug rgw 20` 查看 Lua 脚本执行的详细 trace 和日志
- 使用 `rados df` 和 `ceph df` 监控各 pool 的对象数量和容量占用
- 使用 `rgw_lc_debuginterval=1` 加速 lifecycle 测试（1 秒 = 1 天），**仅限测试环境**


## 五、现场演示

演讲者进行了实时演示，展示了以下流程：

1. 使用 `rclone` 向 bucket 上传不同大小的文件
2. 观察对象根据 2 MB 阈值分别落入 **warm data pool**（小对象，replicated）和 **hot data pool**（大对象，EC）
3. 15 秒后（对应 lifecycle 配置的 15 天）触发过渡，约 1 GB 数据迁移至 **S3 archive pool**
4. 运行 GC（garbage collector）命令，清理原 pool 中的旧数据
5. 30 秒后（对应 30 天）对象被 expire 删除，archive pool 清空

演示从德国远程连接到集群完成，展示了 Ceph 跨地域管理的可行性。


## 六、最佳实践建议（来自社区经验）

基于 VM backup and replication 软件的实际使用经验，推荐以下配置策略：

- **使用 Amazon 标准 storage class 名称**（如 `STANDARD`、`STANDARD_IA`、`DEEP_ARCHIVE`），以确保与 S3 客户端的兼容性
- 对于小 64 KB 的对象，使用 `STANDARD` storage class，映射到 NVMe SSD 上的 replicated pool
- 对于较大的对象，使用 `STANDARD_IA` storage class，映射到 HDD 或混合驱动器上的 pool
- 将 `STANDARD` 设置为默认 storage class，确保小对象始终获得最优性能


## 七、致谢

演讲者特别感谢以下贡献者：

- **Casey、Eric、Matt**：长期维护 RGW
- **Greg Farnum**：多年来对 RGW 的持续贡献
- **Yubo**：在 radosgw 中实现 Lua scripting 支持
- **Matthew Eller**：本周实现 lifecycle 过渡时的压缩/解压缩功能
- **Stephen Ambio**（OS Nixis）：RGW zoning 相关工作
- **Anthony Dri 和 Kurt Burns**：RGW scripting 演讲
- **Casperis**：分享 VM backup and replication 与 S3 storage 结合使用的实战经验
