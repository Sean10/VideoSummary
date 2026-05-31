---
categories:
- 视频总结
date: 2021-11-03
subtitle: Ceph_Crimson_SeaStore_2021-10-27
tags:
- Ceph
- CRUSH算法
- 分布式存储
- 高可用性
- 可扩展性
- 对象存储
title: "Ceph Crimson/SeaStore 2021-10-27"
updated: 2021-11-04
---




1. **Ceph PR审核与合并**
   - 完成了多项Ceph PR的审核工作。
   - 成功合并了首个Random Block Manager（RBM）的PR，并修复了lower bound fix的问题。

2. **Crimson测试与问题反馈**
   - 正在测试Crimson，但遇到问题，已报告上游bug。
   - 配置Crimson时遇到问题，可能源于文档指令错误，Radik正在努力使Crimson与Rook兼容。

3. **OSD Metadata问题**
   - 已修复OSD Metadata问题，但单元测试中仍有错误，PR将更新。

4. **Journal Submitter与Metrics问题**
   - 调试Journal Submitter，特别是Metrics Matrix注册失败的问题，影响了LBA测试，正深入调查。

5. **EPM Sprel Sprite LFS Strategy测试**
   - 上周处理了相关问题，下周将继续进行测试。

#### 决定事项
- 修正Crimson配置文档中的错误指令。
- 持续跟进OSD Metadata和Journal Submitter的问题，深入调查。

#### 后续行动计划
- 更新并修正Crimson配置文档。
- 继续进行Crimson与Rook的兼容性测试。
- 深入调查并解决OSD Metadata和Journal Submitter问题。
- 完成EPM Sprel Sprite LFS Strategy的测试工作。