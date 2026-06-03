---
title: "2019-01-02 :: Ceph Developer Monthly"
date: 2019-01-02
updated: 2019-01-04
tags:
  - "Ceph"
  - "分布式存储"
  - "CRUSH算法"
  - "可扩展性"
  - "对象存储"
categories:
  - "视频总结"
outline: deep
---
本次Ceph开发者月度会议于2023年5月19日举行，主要讨论了以下议题：

1. **新Monitor添加问题**：David指出在添加新Monitor时，需要指定公共地址，但当前无法指定。会议决定通过Orchestrator命令要求指定公共网络，并在CLI中实现该功能。

2. **Ceph应用功能需求**：讨论了Ceph应用在RadosOS上构建的一些功能需求，包括自定义操作、可扩展性解决方案以及元数据管理。

3. **Skyhook应用功能需求**：讨论了Skyhook应用在Ceph存储上的一些功能需求，包括集合级别锁定和元数据管理。

4. **多对象操作**：讨论了在Ceph中实现多对象操作的需求，包括PG级别操作和原子性。

5. **返回数据**：讨论了在对象操作中返回数据的可行性，包括返回数据大小和用途。

会议决定后续行动计划如下：

* David将研究如何通过Orchestrator命令指定公共网络。
* Jeff和Southern Cal将研究如何实现自定义操作和可扩展性解决方案。
* Brad将研究如何在Skyhook中实现集合级别锁定和元数据管理。
* 全体参与者将继续讨论多对象操作和返回数据的需求。

会议中提到的Ceph组件包括Monitor、OSD、PG、Rados、CLI等，使用了Ceph术语，例如原子性、可扩展性、元数据、集合级别锁定等。