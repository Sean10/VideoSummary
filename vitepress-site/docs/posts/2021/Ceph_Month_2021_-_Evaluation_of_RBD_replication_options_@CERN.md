---
title: "Ceph Month 2021: Evaluation of RBD replication options @CERN"
date: 2021-06-22
updated: 2021-06-22
tags:
  - "Ceph"
  - "CERN"
categories:
  - "视频总结"
outline: deep
---
CERN的SAFE项目中，Archer作为研究员，对RBD复制选项进行了评估。以下是会议内容的总结：

1. **项目背景与目标**：SAFE项目使用四个Ceph集群，为OpenStack Cinder提供支持，管理约7000个卷，总容量达8TB。目标是实现Cinder卷的灾难恢复，允许用户在不同集群之间进行复制。

2. **技术细节与挑战**：
   - **RBD复制模式**：
     - **日志模式（Journal Mode）**：写入RBD镜像的同时写入日志，导致性能问题，性能下降约50%。通过调整参数，性能可提升至40-50MB/s。
     - **快照模式（Snapshot Mode）**：通过定期快照实现数据复制，非连续复制，性能优于日志模式，每镜像可达200MB/s。OpenStack Cinder不支持快照镜像，但已提交补丁。

3. **测试环境**：使用SAFE Octopus版本，配置包括6台实验机，60个OSDs（混合场景，数据在HDD，DB在SSD），18个OSDs专用于RBD日志。

4. **结论与后续行动**：
   - 团队计划采用快照模式进行进一步测试和优化。
   - 已提交五个补丁以提高RBD复制的可观察性和稳定性。
   - 与OpenStack Cinder开发团队合作，推动快照镜像功能的集成。

5. **问答环节**：
   - 快照频率：初始测试中使用最小频率（1分钟），实际应用中可能会根据FS3S快照工作的进展调整。
   - 文件系统冻结支持：目前尚未遇到因缺乏文件系统冻结支持导致的问题，但预计未来应用中会有所帮助。
   - 日志模式性能：在较大RBD集群中，客户端性能可能受限于集群带宽。

后续行动计划包括继续测试快照模式，与OpenStack Cinder开发团队合作，以及持续提交补丁优化RBD复制的性能和稳定性。