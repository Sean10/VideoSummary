---
title: "Sudarshan Ramachandran -- When 10GbE is Not Enough"
date: 2015-11-13
updated: 2015-11-14
tags:
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
Sudarshan Ramachandran的演讲主要讨论了在高性能计算和存储领域，10GbE网络带宽已不足以满足需求，并介绍了Mellanox公司在网络解决方案中的应用以及与Ceph存储系统的整合。

**主要内容包括**：

- **Mellanox公司介绍**： Mellanox是一家以色列公司，总部位于美国，提供从网络适配器到交换机、线缆和硅芯片的端到端解决方案，支持多种网络速度，广泛应用于高性能计算、云计算、Web 2.0等领域。
- **Mellanox在存储领域的应用**： Mellanox的产品主要应用于高性能计算、云计算和Web 2.0等场景，旨在提高吞吐量、降低延迟和简化基础设施。其解决方案包括提供高带宽和低延迟的网络连接，提高IOPS和吞吐量，简化基础设施，提高系统可靠性，并通过网络卸载技术释放CPU资源。
- **Mellanox产品介绍**： Mellanox提供多种网络适配器、交换机和线缆，支持10G、40G、25G和50G等速度。其交换机具有低功耗、高线速、高可靠性等特点。RDMA和RoCE技术可以将网络延迟降低到微秒级别，提高系统性能。
- **案例展示**： 会议中展示了Mellanox在OpenStack summit上的视频演示，展示了40G网络和RDMA技术在实际应用中的性能提升。
- **行动计划**： Mellanox将继续加强与Ceph社区的沟通，推动RDMA和RoCE技术在Ceph中的应用，并提供更多的参考架构和解决方案，帮助用户构建高性能的Ceph存储系统。

**讨论事项**：

- 参会人员就Mellanox产品在存储领域的应用进行了深入讨论，并提出了相关建议。

**后续行动**：

- Mellanox将根据会议讨论结果，进一步完善产品方案，并加强与Ceph社区的沟通合作。

**总结**：

Sudarshan Ramachandran的演讲强调了网络带宽在高性能计算和存储领域的重要性，并介绍了Mellanox的解决方案如何提高性能和效率。这对于Ceph社区和存储领域的研究人员都具有重要的参考价值。