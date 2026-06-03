---
title: "Ceph Crimson/SeaStore Meeting 2023-02-08"
date: 2023-02-14
updated: 2023-02-15
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
  - "存储"
  - "SSD"
  - "HDD"
  - "SAN"
  - "NAS"
  - "网络"
  - "弹性"
  - "恢复"
  - "负载均衡"
  - "缓存"
  - "压缩"
  - "去重"
  - "分层"
  - "性能优化"
  - "测试"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

#### 会议时间：2023-02-08
#### 参会人员：[参会人员名单]

#### 主要议题：
1. **Ceph项目更新**
2. **代码合并与修复**
3. **技术讨论与问题解决**
4. **Cephalicon会议准备**

#### 讨论内容：
1. **代码合并与修复**
   - 已合并修复了一些非主要Bug。
   - Ying Jen需要基于当前的Main分支重新提交PR，因为一些故障可能是由之前的Bug导致的。
   - Main分支已合并，应能正常工作。

2. **技术讨论与问题解决**
   - 关于Snap blog的讨论，Dreams的Snap blog现已可用。
   - SeaStar正在进行关于启用IBM的Out of Line Physical Extents的讨论，并持续审查相关代码实现。
   - Messenger的构建问题已修复，并将继续替换相关部分。
   - Tommy正在完成代码修改，包括ping功能的修改和连接指针的调整，计划当天进行调试。
   - 上周主要尝试寻找Io hongbug的根本原因，但进展不大，本周将继续处理。

3. **Cephalicon会议准备**
   - Cephalicon会议将于四月举行，旅行限制普遍，但参会人员计划出席。
   - 鼓励参会人员提交演讲，CFP截止日期在本周末。
   - 关于参会预算，需要进一步确认。

#### 决定事项：
- Ying Jen需基于当前Main分支重新提交PR。
- Tommy将继续完成代码修改并进行调试。
- 参会人员将关注Cephalicon会议的进展，并准备可能的演讲提交。

#### 后续行动计划：
- Ying Jen将重新基于Main分支进行PR，并通知相关人员进行测试。
- Tommy将完成代码修改并进行调试。
- 参会人员将关注Cephalicon会议的进展，并准备可能的演讲提交。

#### 其他事项：
- 无其他特别事项。

#### 会议结束语：
- 祝大家本周工作顺利，期待在Cephalicon会议上见到大家。

#### 会议记录人：[记录人姓名]
#### 会议结束时间：[具体时间]