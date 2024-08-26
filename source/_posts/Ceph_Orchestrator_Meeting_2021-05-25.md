---
title: "Ceph Orchestrator Meeting 2021-05-25"
date: 2021-05-26
updated: 2021-05-26
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Orchestrator 会议

#### 日期：[具体日期]

#### 参会人员：[具体人员名单]

#### 主要议题：

1. **Etsy Hosts 问题**
   - 讨论了 Etsy Hosts 文件的回归问题，涉及 DeepSea、Ansible 和 Cephadm Octopus Tana。
   - 确认了两个相关的 Pull Request。
   - 讨论了 Podman 和 Docker 的行为差异，特别是关于 get fqdn 的处理。
   - 发现 Podman 在特定配置下返回回环地址，导致配置文件生成问题。
   - 讨论了如何处理 DNS 和 Etsy Hosts 的依赖问题，建议在添加主机时强制指定 IP 地址。
   - 提出了在文档中明确说明使用 IP 地址的必要性，并更新相关代码以支持这一变化。

2. **Ganesha 模板冲突问题**
   - 讨论了 Ganesha 模板中的冲突标志问题，该问题导致 NFS EdgeRW 损坏。
   - 确认了需要移除 dirt chunk equal zero 配置。
   - 讨论了是否应该使用单一 Ganesha 实例同时支持 CephFS 和 RGW 导出。
   - 发现不同后端（CephFS 和 RGW）需要不同的配置选项，建议恢复为使用不同的 Ganesha 集群。
   - 讨论了未来可能的改进方向，包括与 Ganesha 开发者的进一步沟通。

#### 决定事项：

1. **Etsy Hosts 问题**
   - 关闭第一个 Etsy Hosts 相关的 Pull Request。
   - 更新文档，明确说明在添加主机时必须指定 IP 地址。
   - 确保 `cephadm` 命令在添加主机时返回使用的 IP 地址。
   - 进行代码审查，确保所有对 resolve ip 的调用都被正确处理。

2. **Ganesha 模板冲突问题**
   - 暂时放弃使用单一 Ganesha 实例同时支持 CephFS 和 RGW 导出的方案。
   - 恢复为使用不同的 Ganesha 集群，分别支持 CephFS 和 RGW。
   - 等待与 Ganesha 开发者的进一步沟通，以确定最佳解决方案。

#### 后续行动计划：

1. **Etsy Hosts 问题**
   - 完成文档更新，明确说明使用 IP 地址的必要性。
   - 更新 `cephadm` 命令，确保在添加主机时返回使用的 IP 地址。
   - 进行代码审查，确保所有对 resolve ip 的调用都被正确处理。

2. **Ganesha 模板冲突问题**
   - 与 Ganesha 开发者沟通，了解 dirt chunk 配置的具体影响。
   - 根据沟通结果，确定是否需要进一步的配置调整或代码修改。
   - 更新相关文档和代码，确保用户明确不同后端需要不同的 Ganesha 配置。

#### 其他讨论：

- 讨论了 Ingress 服务在底层 RGW 服务被删除时的行为，建议保持当前的异常处理方式，避免自动删除服务。

#### 会议总结：

本次会议主要解决了 Etsy Hosts 文件的回归问题和 Ganesha 模板冲突问题，明确了后续的行动计划和改进方向。通过与 Ganesha 开发者的进一步沟通，将有助于确定最佳的技术方案。