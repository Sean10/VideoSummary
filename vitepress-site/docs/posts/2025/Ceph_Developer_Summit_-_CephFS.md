---
title: "Ceph Developer Summit - CephFS"
date: 2025-09-11
updated: 2025-09-12
tags:
  - "CephFS"
  - "分布式存储"
  - "存储集群"
categories:
  - "视频总结"
outline: deep
---
### **Ceph 分布式存储会议纪要 - CephFS 组件讨论**

**会议主题**: CephFS 组件讨论（伞形发布）
**时间**: [会议时间]
**参与人员**: [与会人员列表]



#### **1. Mirror Daemon CLI 增强与健康状态报告**
- **讨论内容**: 
  - 当前 Mirror Daemon 的状态报告功能较为基础，缺乏管理员所需的详细信息。
  - 计划通过 `service daemon` 接口将状态信息推送至 `ceph-mgr`，并支持通过 `ceph CLI` 查询。
  - 讨论是否将 Mirror Daemon 的错误状态反映到集群健康状态。
- **决策**: 
  - 优先实现通过 `service daemon` 接口上报状态至 `ceph-mgr`。
  - 需进一步讨论是否修改集群健康状态。
- **后续行动**: 
  - Jos 和 Weni 负责推进 CLI 改进。
  - 联系 Dashboard 团队讨论数据展示需求。

#### **2. CephFS 灾难恢复工具的进度反馈**
- **讨论内容**: 
  - 当前灾难恢复工具（如 `data-scan`）缺乏进度反馈，用户无法预估完成时间。
  - 利用 `ceph-mgr` 的 `progress module` 上报进度，支持多工作线程独立统计。
  - 若 `ceph-mgr` 不可用，直接输出进度至 `stdout/stderr`。
- **决策**: 
  - 采用 `progress module` 作为主要方案，`stdout` 回退为辅。
  - 每个工作线程独立上报进度，不聚合统计。
- **后续行动**: 
  - Ed 和 Mahesh 完善进度跟踪实现，优先提交 PR。

#### **3. CephFS Subvolume 隔离（Quarantine）功能**
- **讨论内容**: 
  - 需求场景：应对勒索软件攻击，隔离特定 Subvolume 禁止读写。
  - 技术挑战：协议修改、客户端处理、会话密钥吊销。
- **决策**: 
  - 优先修改 CAP 协议，支持返回隔离错误码。
  - 旧客户端回退至 Blocklist 或挂起操作。
- **后续行动**: 
  - Milind 和 Weni 设计协议变更方案，提交社区讨论。

#### **4. Subvolume V3 状态更新**
- **讨论内容**: 
  - 目标：V3 为最终版 Subvolume 布局，修复 V1/V2 的设计缺陷。
  - 升级计划：支持从 V1/V2 自动升级至 V3。
- **后续行动**: 
  - Rishab 完善 PR 并推动 Review，目标纳入伞形发布。

#### **5. 其他议题**
- **Op Tracker 增强**: Greg 计划改进 MDS Op Tracker，增加 Cap 更新的可视性，辅助调试卡死问题。
- **终端 UI 工具提案**: Eager 提议基于 C++ 库开发交互式 CLI 工具，提升用户体验。

### **行动计划总结**
| **负责人** | **任务** | **时间节点** |
||-|--|
| Jos/Weni   | Mirror Daemon CLI 改进 | 下一个版本 |
| Ed/Mahesh  | 灾难恢复工具进度反馈 | PR 进行中 |
| Milind     | Subvolume Quarantine 协议设计 | 待定 |
| Rishab     | Subvolume V3 代码 Review | 伞形发布 |
| Greg       | MDS Op Tracker 改进 | 进行中 |

**备注**: 未决事项需通过邮件列表进一步讨论。



**关键词保留**:  
- Mirror Daemon, CRUSH algorithm, RADOS, ceph-mgr, CAP protocol, Subvolume, Quarantine, Op Tracker,灾备恢复（disaster recovery）, cephfs-mirror.