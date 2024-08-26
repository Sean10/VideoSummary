---
title: "Ceph RGW Refactoring Meeting 2023-11-08"
date: 2023-11-20
updated: 2023-11-21
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph分布式存储系统中librdkafka库的问题讨论与解决方案

#### 参会人员：Ceph研发团队成员

#### 会议时间：[具体日期]

#### 会议地点：视频会议

#### 主要议题：
1. **librdkafka库存在的问题**
   - 当前使用的librdkafka库版本较旧，存在多个问题，包括崩溃问题和功能缺失。
   - 崩溃问题与librdkafka库中的定义不匹配有关，该问题已在较新版本中修复。
   - 功能缺失包括无法将证书颁发机构（CA）作为字符串传递，以及客户端无法绕过服务器证书检查。

2. **解决方案讨论**
   - 讨论了将librdkafka作为子模块（submodule）引入Ceph项目的可行性。
   - 决定采用静态链接方式解决动态链接可能带来的问题。
   - 需要确保子模块的使用是临时的，并计划向CentOS和Ubuntu提交bug报告，要求更新librdkafka版本。

3. **后续行动计划**
   - 添加librdkafka作为子模块，并确保提交消息中包含子模块名称以获得批准。
   - 向CentOS和Ubuntu提交bug报告，请求更新librdkafka版本。
   - 监控子模块的使用情况，评估是否需要长期保留。

#### 其他讨论：
- **Kraken的提问**：关于在单个RADOS对象中存储所有主题（topics）的问题，讨论了数据模型改进的必要性和潜在的迁移成本。
- **Ali的工作**：关于配置管理和部署的讨论，计划在下次会议中进一步讨论。
- **Kraken的另一个问题**：关于使用Web Identity进行STS（Security Token Service）角色假设时遇到的问题，建议创建Tracker bug并寻求专家帮助。

#### 会议总结：
会议主要解决了Ceph项目中librdkafka库的版本问题和功能缺失，决定采用子模块方式并静态链接解决现有问题。同时，讨论了数据模型改进的必要性和潜在的迁移成本，并计划在后续工作中进一步处理。对于Web Identity的问题，建议创建Tracker bug并寻求专家帮助。

#### 后续行动：
- 实施librdkafka子模块的添加和静态链接。
- 提交bug报告，请求更新librdkafka版本。
- 监控子模块使用情况，评估长期保留的必要性。
- 创建Tracker bug，解决Web Identity问题。

#### 下次会议预告：
- 讨论Standalone部署的编排问题和配置管理。

#### 会议结束：
感谢所有参会人员的积极参与和贡献，会议于[具体时间]结束。