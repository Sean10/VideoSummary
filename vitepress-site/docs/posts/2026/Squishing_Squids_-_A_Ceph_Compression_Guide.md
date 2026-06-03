---
title: "Squishing Squids - A Ceph Compression Guide"
date: 2026-04-20
updated: 2026-04-21
tags:
  - "BlueStore"
  - "RGW"
  - "性能优化"
  - "对象存储"
categories:
  - "视频总结"
outline: deep
---
## 演讲概述

本次演讲由 Clearsight 公司的 Ceph Solutions Architect Brian主讲，他拥有 14 年 Ceph 使用经验。演讲围绕 Ceph 中压缩技术的应用展开，涵盖压缩的经济价值、适用场景、算法选择、监控方法及常见陷阱。

## 为什么压缩很重要

### 经济效益

- **降低 CapEx**：相同硬件可存储更多数据，减少采购成本
- **降低 OpEx**：所需磁盘更少，功耗和散热成本随之降低

### 性能与效率

- **减少 SD 磨损**：写入字节数减少，延长闪存寿命
- **优化网络带宽**：数据压缩后再传输，对带宽受限环境（如家用 1Gbps 网络）效果显著
- **提升吞吐量**：以 3x 压缩比为例，100 MB/s 的磁盘实际可达到 300 MB/s 的有效写入速度

## Ceph 中压缩的应用层次

压缩可在以下多个层次启用：

1. **BlueStore 层**：在每个 OSD 上独立进行压缩
2. **RocksDB 层**：对 OSD 内部的元数据数据库进行压缩，最新版本已默认启用
3. **Messenger 层**：对 daemon 间通信进行压缩，适用于 stretch cluster等场景，但通常不推荐
4. **OSD 服务器层**：使用 ZRAM 实现压缩 swap，在内存价格高涨的背景下可有效扩展可用内存（Android 手机已广泛使用）
5. **RGW 层**：在对象网关侧压缩后再写入集群，效果最佳

## 压缩前的数据评估

在启用压缩之前，建议先评估数据的可压缩性。演讲者提供了一个 Python 脚本（托管于 GitHub，借助 Gemini 辅助编写），可随机抽取指定 pool 中的 RADOS 对象并尝试 Gzip 压缩，从而判断数据是否值得开启压缩。

## 压缩算法对比

演讲使用 Silesia 标准压缩基准测试集对多种算法进行了横向对比，评估维度为压缩比（纵轴，越高越好）与压缩速度（横轴，越右越快）。

| 算法 | 特点 |
|------|------|
| **Gzip** | 经典算法，9 个压缩级别，level 1 最快但压缩比最低，level 3 到 4 有明显跳跃 |
| **Bzip2** | 压缩比显著提升，但速度极慢，各级别差异不大 |
| **LZ4**（2011） | 速度大幅提升，level 1 可达约 400 MB/s，提高级别对压缩比改善有限 |
| **Snappy**（2011） | 仅一个压缩级别，速度快但压缩比较低（约 2:1） |
| **XZ**（2014） | 压缩比超过 Bzip2，但速度更慢 |
| **Brotli** | Google 出品，改进自 Gzip，窗口从 64 KB扩展至约 8 MB，速度约为最快 Gzip 的两倍，压缩比也有提升 |
| **ISA-L / IGzip** | Intel 优化版 Gzip，已集成进 Ceph，提升性能但不改善压缩比 |
| **Zstandard（zstd）** | Facebook 出品，与 LZ4 同一作者，**兼顾高压缩比与高速度，综合表现最佳** |

### 解压速度对比

- Snappy 和 LZ4 解压最快
- Zstandard 在几乎所有压缩级别下解压速度仍可达约 800 MB/s
- Gzip 压缩比越高解压越快；Bzip2 则相反

**结论：Zstandard 是大多数场景下的最优选择。**

## 压缩配置方法

### BlueStore 压缩

```bash
# 推荐在 pool 级别配置，而非集群全局
ceph osd pool set <pool-name> compression_mode aggressive
ceph osd pool set <pool-name> compression_algorithm zstd
```

- 支持 `passive`、`aggressive`、`force 三种模式，`aggressive` 会尽量压缩
- 每个 pool 可独立配置不同算法
- 使用 `ceph df detail` 验证压缩效果
- 禁用时将 mode 和 algorithm 均设为 `none`

> 注意：演讲者建议在 pool 级别而非集群级别配置，因为历史上曾出现过全局启用导致的严重 bug。

### RGW 压缩

```bash
# 在 default placement 上配置
radosgw-admin zone placement modify --placement-id default-placement \
  --compression zstd
# 修改后需重启 RGW
```

- 禁用时设为 `none`
- 可调整压缩级别（Zlib 默认 level 5，演讲者已将 Zstandard 默认从 5 改为 1，性能提升显著）
- LZ4 和 Snappy 在Ceph 中不支持调整压缩级别

## 实测基准数据

测试环境：Raspberry Pi 5作为 RGW，1 Gbps 网络，使用 enwik9（约 1 GB Wikipedia 数据，可压缩性强）

| 场景 | 上传速度 | 存储对象数 | 实际占用空间 |
|------|------------
| 无压缩（3x replication） | 85 MB/s | 249 | 2.8 GiB |
| BlueStore + Zstandard | 48 MB/s | 249 | 1.5 GiB（节省约 50%） |
| RGW + Zstandard | 更高 | **97** | 1,022 MiB（压缩后 341 MiB） |

**关键发现：**

- BlueStore 压缩会在每个 OSD 上独立执行，3x replication 意味着压缩三次，CPU 开销是 RGW 压缩的三倍
- RGW 压缩在写入 RADOS 前完成，对象数从 249 降至 97，大幅减少 recovery 时的对象传输量
- **最佳实践**：在上传到 RGW 之前客户端侧压缩 > RGW 侧压缩 > BlueStore 压缩

## 存储类（Storage Classes）与生命周期策略

参考 Amazon S3 的多存储类设计，Ceph RGW 同样支持自定义存储类：

```
Express（NVMe SD）→ Standard（HDD）→ Infrequent Access（Erasure Coded + Zstandard）
```

**智能分层（Intelligent Tiering）应用场景：**

1. 数据写入时使用 3x replication
2. 30 天后通过 lifecycle policy 自动迁移至 8+3 erasure coding 并启用高压缩级别
3. 可为生命周期处理专门部署压缩能力强的 RGW 节点，避免与正常访问竞争资源

> 注意：当前版本的 lifecycle迁移功能仅支持跨 pool 移动，**不会重新压缩数据**。演讲者已提交 bug report，修复补丁正在测试中。

## 监控压缩效果

```bash
# RGW 层：查看 bucket 统计
radosgw-admin bucket stats --bucket=<bucket-name>
# 输出包含未压缩大小与实际占用大小

# BlueStore 层：集群级别
ceph df detail

# BlueStore 层：单个 OSD
ceph tell osd.<id> perf dump | grep compress
```

## 常见陷阱

1. **已压缩数据**：JPEG、MPEG 等格式本身已压缩，再次压缩无效
2. **加密数据**：加密后熵值极高，无规律可循，无法压缩
3. **CPU 资源不足**：若 RGW CPU 使用率已达 90%，启用压缩会导致性能下降
4. **存量数据不会被重新压缩**：启用压缩只对新写入数据生效，已有数据保持原状
5. **小对象效果有限**：8 KB 压缩至 1 KB，但 OSD 最小分配单元仍为 4 KB，节省空间有限

## 未来方向

- **AMD AOCL**：AMD 优化压缩库，与 Intel ISA-L 类似，可集成进 Ceph
- **Intel QuickAssist**：硬件压缩卸载，新一代处理器已内置，支持 Zstandard，吞吐量极高
- **Nvidia NVComp**：GPU 侧压缩
- **UADK**：ARM64 硬件卸载，已在 Tentacle 版本中集成，首个支持平台为 HiSilicon Kunpeng 920
- **AI/神经网络压缩**：Fabrice Bellard（QEMU、FFmpeg 作者）开发的 NNCP 压缩比极高但速度极慢，代表未来探索方向

## 总结

1. 启用压缩前先验证数据的可压缩性
2. **Zstandard 通常是最佳选择**：速度快、压缩比高
3. **RGW 侧压缩优于 BlueStore 压缩**：更高吞吐、更少对象、更低 CPU 开销
4. 不要对不可压缩数据启用压缩，徒耗 CPU 资源
5. 合理利用 lifecycle policy 实现数据的自动分层与压缩迁移
