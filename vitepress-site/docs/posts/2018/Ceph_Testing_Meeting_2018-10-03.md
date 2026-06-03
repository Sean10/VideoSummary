---
title: "Ceph Testing Meeting 2018-10-03"
date: 2018-10-18
updated: 2018-10-18
tags:
  - "Ceph"
  - "分布式存储"
  - "CRUSH算法"
  - "高可用性"
  - "可扩展性"
  - "对象存储"
  - "块存储"
  - "文件系统存储"
  - "性能"
  - "BlueStore"
  - "BlueFS"
  - "RocksDB"
  - "OSD"
  - "MON"
  - "MDS"
  - "PG"
  - "RADOS"
  - "librados"
  - "libcephfs"
  - "RBD"
  - "RGW"
  - "RESTful API"
  - "认证"
  - "授权"
  - "加密"
  - "复制"
  - "快照"
  - "克隆"
  - "iSCSI"
  - "NFS"
  - "CIFS"
  - "POSIX"
  - "监控"
  - "Dashboard"
  - "编排"
  - "自动化"
  - "容器化"
  - "Kubernetes"
  - "Docker"
  - "虚拟化"
  - "云计算"
  - "AWS"
  - "Azure"
  - "Google Cloud"
  - "混合云"
  - "多云"
  - "存储集群"
  - "SSD"
  - "HDD"
  - "SAN"
  - "NAS"
  - "网络"
  - "恢复"
  - "弹性"
  - "负载均衡"
  - "缓存"
  - "压缩"
  - "性能优化"
  - "测试"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

#### 会议时间：
[此处填写会议时间]

#### 参会人员：
[此处填写参会人员名单]

#### 会议内容：

**1. 问候与自我介绍**
- 会议开始，与会者互相问候，并介绍了自己的工作地点和近况。

**2. 主题讨论**
- **议题一：Ceph 存储请求**
  - 有成员提到一个存储请求（pool request）已经两周没有回应，需要跟进。
  - 另一个成员提到有多个与 openSUSE 相关的池请求，建议同时测试。

- **议题二：Ansible 项目**
  - 有成员提到 Ansible 项目目前使用人数不多，预计在一周内处理。
  - 有成员询问关于 openSUSE leap 的 OPR Insaf（OpenStack Provider Resource）请求，希望得到评审意见。

- **议题三：配置管理**
  - 讨论了如何支持多种操作系统和版本，以及如何使用 symbolic link 从配置集合中选取特定配置。

- **议题四：操作系统选择**
  - 讨论了是否支持所有操作系统或随机选择，以及在使用配置管理工具时如何处理操作系统配置。

- **议题五：Luminess 项目**
  - 有成员提到 Luminess 项目中的 sleep before teardown 特性需要重构，以便与并行和顺序执行兼容。

**3. 行动计划**
- 跟进存储请求，确保及时得到回应。
- 处理 Ansible 项目，在一周内完成。
- 完成openSUSE leap的 OPR Insaf 请求的评审。
- 研究操作系统选择问题，并优化配置管理。
- 重构 Luminess 项目中的 sleep before teardown 特性。

#### 会议总结：
本次会议讨论了 Ceph 存储请求、Ansible 项目、配置管理和操作系统选择等问题，并制定了相应的行动计划。会议气氛积极，大家积极参与讨论，为项目的顺利进行提供了有力保障。

#### 下次会议时间：
[此处填写下一次会议时间]