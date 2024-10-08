---
title: "Ceph Crimson/SeaStore 2021-10-13"
date: 2021-10-18
updated: 2021-10-19
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **多设备PR合并**：上周主要工作是合并多设备PR，目前已成功合并。
- **缓存LRU工作**：继续进行缓存LRU的工作，并开始审查三星Chennai的大随机写入PR。
- **技术测试**：开始进行技术测试，但由于无法设置OpenVPN，使用团队内部的Tesla测试环境进行测试。
- **代码构建与系统测试**：仍在构建代码并尝试运行系统测试，但尚未完成构建。
- **DB's Messenger审查**：花费时间审查DB's Messenger，未发现重大问题，计划开始研究watch notify机制。
- **LFS策略测试**：尝试测试spreader LFS策略，但尚未成功运行，仍在解决遇到的问题。
- **性能优化与PR审查**：审查多设备PR，并继续工作于合并日志头以减少写入开销，同时关注批处理和自动化压力测试工具。
- **测试场景准备**：准备了测试场景并与团队共享，计划本周继续进行相关测试。

#### 讨论的主要议题
- **技术测试环境**：讨论了技术测试环境的设置问题，决定使用团队内部的Tesla测试环境。
- **代码构建与测试**：讨论了代码构建和系统测试的进展，强调了测试的重要性。
- **性能优化与PR审查**：讨论了性能优化和PR审查的进展，强调了批处理和自动化压力测试工具的重要性。
- **测试场景准备**：讨论了测试场景的准备和共享，强调了测试场景的重要性。

#### 决定的事项
- **使用团队内部的Tesla测试环境进行技术测试**。
- **继续进行代码构建和系统测试**。
- **开始研究watch notify机制**。
- **继续进行性能优化和PR审查**。
- **继续进行测试场景的准备和共享**。

#### 后续的行动计划
- **继续进行多设备PR的审查和合并**。
- **继续进行缓存LRU的工作**。
- **继续进行技术测试，并解决遇到的问题**。
- **继续进行代码构建和系统测试**。
- **开始研究watch notify机制**。
- **继续进行性能优化和PR审查**。
- **继续进行测试场景的准备和共享**。

#### 其他
- **会议结束时，团队成员互相祝愿有一个愉快的一周**。

### 关键词
- **Multi-device PR**
- **Cache LRU**
- **Random Write PR**
- **OpenVPN**
- **Tesla Testing**
- **System Testing**
- **DB's Messenger**
- **Watch Notify**
- **Spreader LFS**
- **Performance Optimization**
- **PR Review**
- **Test Scenarios**

### 会议总结
本次会议主要讨论了多设备PR的合并、缓存LRU的工作、技术测试环境的设置、代码构建与系统测试、性能优化与PR审查以及测试场景的准备。团队成员分享了各自的进展和遇到的问题，并讨论了后续的行动计划。会议结束时，团队成员互相祝愿有一个愉快的一周。