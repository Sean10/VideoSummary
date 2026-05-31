---
title: QoS Demo
date: 2026-04-02
updated: 2026-04-03
tags:
- NFS
- Ceph
- 高可用性
categories: 
- 视频总结
subtitle: QoS_Demo
---

## 概述

本次演讲由 Sha 主讲，介绍了 Ceph NFS 即将推出的四项增强功能：QoS（Quality of Service）、TLS 传输层安全、BYOK（Bring Your Own Key，自带密钥）以及 NFS active-active 高可用支持。演讲者在 Ceph 存储团队工作约一年半，专注于 NFS 相关功能开发。

## 背景与问题

当前大多数组织运行多租户环境，面临以下核心挑战：

- **性能不可预测**：租户之间无法保证公平的带宽分配
- **通信安全**：NFS 客户端与服务端之间缺乏加密保护（明文流量）
- **密钥管理受限**：客户无法自主控制数据加密密钥
- **高可用瓶颈**：active-passive 架构在故障切换时需要人工干预

这四项新功能分别针对上述问题提供解决方案。

## 功能一：QoS（Quality of Service）

### 问题背景

多租户环境中的"noisy neighbor"问题：某个备份任务突然占用大量带宽，导致关键业务工作负载带宽不足。

### 解决方案

QoS 提供两种控制维度：
- **带宽控制（Bandwidth Control）**：限制最大吞吐量（Mbps）
- **IOPS 控制**：限制每秒输入输出操作数

### QoS 类型

| 类型 | 说明 |
|------|------|
| Per Share | 限制设置在 export 级别，每个 export 有独立上限，但不保证客户端级别公平性 |
| Per Client | 限制设置在客户端级别，不限制 export 总量 |
| Per Share Per Client | 双层限制，同时在 export 和客户端两个层面设置上限 |

### 配置层级

- **Cluster 级别**：全局 QoS，适用于该 NFS cluster 下所有 export，需先启用才能配置 export 级别
- **Export 级别**：可覆盖 cluster 级别的值，针对特定 export 单独配置

### 演示结果

- 无 QoS 限制时：写入带宽约 115 Mbps
- 启用 cluster 级别 QoS（50 Mbps）后：实测约 48.4 Mbps
- 进一步设置 export 级别 QoS（30 Mbps）后：实测约 29.8 Mbps

QoS 功能有效保障了多租户间的带宽公平性，防止关键工作负载饥饿。

## 功能二：TLS 传输层安全

### 功能说明

TLS 为 NFS 客户端与服务端之间的网络通信提供加密保护，具备：
- **保密性**：加密所有传输数据
- **完整性**：检测传输过程中的数据篡改
- **认证**：可选的双向认证（mTLS）

### 证书来源配置

支持三种证书来源（`certificate_source`）：
- `inline`：直接在 spec 中指定 SSL key、SSL cert 和 CA cert
- `cephadm_signed`：由 cephadm 自动生成证书
- `reference`：引用 cert manager 中存储的证书（上一版本引入的功能）

### 其他配置项

- **KTLS（Kernel TLS）**：在内核层面完成加密解密，适合性能敏感型工作负载；若硬件加速可用则效果更佳
- **TLS 调试模式**：可指定最低 TLS 版本和 cipher 套件

### Export 安全级别

- `TLS`：仅客户端认证
- `mTLS`：客户端与服务端双向认证

若 cluster 级别启用了 TLS，export 未单独指定时，客户端可使用 TLS 或 mTLS 挂载；若 export 明确设置为 TLS，则客户端必须使用 TLS 才能挂载。

### 演示结果

- 未携带 TLS 证书挂载启用了 TLS 的 export：返回"Operation not permitted"
- 携带客户端证书挂载 mTLS export：成功建立连接，NFS 日志显示"TLS connection established，MTLS=1"

## 功能三：BYOK（Bring Your Own Key，自带密钥）

### 功能说明

允许客户通过 NFS 访问加密存储，加密解密在 CephFS 层完成。客户可完全掌控静态数据的加密密钥，NFS 与外部 KMS（Key Management Server）集成，通信基于 mTLS 保证安全。

### 限制条件

- 仅支持 CephFS export（不支持其他类型）
- 加密粒度为 subvolume 级别
- 每个 export 可使用不同的加密密钥，实现租户数据隔离
- 创建 export 前，对应子目录必须为空
- 加密密钥一旦设置，不可更改

### 配置方式

在 NFS spec 中指定：
- `kmip_cert`、`kmip_key`：与 KMS 服务器通信的客户端证书
- `kmip_cacert`：KMS 服务器的 CA 证书
- `kmip_hostlist`：支持配置多个 KMS 服务器地址（用于 HA）
- 创建 export 时指定 `kmip_key_id`

NFS 服务通过 `libkmip` 库与外部 KMS 服务器通信获取实际加密密钥。

### 演示结果

演示使用 IBM GKLM 作为 KMS 服务器：
- 通过 NFS 挂载后，文件内容以明文可见
- 通过 CephFS FUSE 直接挂载同一 subvolume 后，文件名和目录名均显示为加密状态

## 功能四：NFS Active-Active 高可用增强

### 现有架构

多个 NFS（Ganesha）服务运行在 HAProxy ingress 后端，客户端通过虚拟 IP（VIP，由 Keepalived 维护）访问，HAProxy 将请求转发至后端 NFS 服务器，实现 load balancing。

### 现有问题

当某个后端 NFS 服务器宕机时，HAProxy 会将该服务器的客户端请求转发至其他服务器。但 NFS 协议的 client lease 机制不允许由另一台服务器接管客户端状态，导致客户端永久挂起，必须手动重新挂载。

### 增强方案

1. **HAProxy Stick Table**：在 HAProxy 中维护客户端与服务器的映射关系，多个 HAProxy 实例之间共享该映射。即使 active HAProxy 宕机，其他实例也能继续维持客户端连接，避免客户端挂起。

2. **NFS Daemon Colocation（守护进程同址部署）**：当某台主机上的 NFS 服务宕机后重新上线时，允许在现有主机上重新启动该服务（无需额外主机），HAProxy 无需更改服务器映射，客户端可无感知地继续服务。

3. **HAProxy 健康检查增强**：改进健康检查机制以更好地维护客户端-服务器映射。

## 总结

| 功能 | 解决的问题 |
|------|--------|
| QoS | 多租户带宽公平性，防止 noisy neighbor，保障关键工作负载 |
| TLS | 传输层加密，防止明文流量，支持双向认证 |
| BYOK | 静态数据加密，客户自主控制密钥，与外部 KMS 集成 |
| Active-Active HA | 消除故障切换时的人工干预，提升 high availability |

以上功能目前尚未合并至上游，将在后续版本中发布。演讲者感谢 NFS 团队的实现工作。
