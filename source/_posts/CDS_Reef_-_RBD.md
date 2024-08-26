---
title: "CDS Reef: RBD"
date: 2022-04-22
updated: 2022-04-23
tags:
categories:
- "视频总结"
subtitle: tech
---


1. **Mirroring Schedule Stagger**：尝试错开快照计划和镜像计划，以在一段时间内产生一致的性能影响。
2. **State Machine Documentation**：改善关于rbd mirroring的状态机文档，以便更好地为开发者提供一些部分的文档。
3. **Rbd Suite Movement to Using Sap Area**：将rbd套件迁移到使用sap area，目前仍在进行中，但需要完成多集群支持的工作。
4. **Lack of State Machine Diagrams**：在rv mirror代码库中缺少状态机图，这是一个相对容易解决的问题，并且对于刚熟悉代码库的人来说也是一个好任务，因为它有助于从高层次了解代码并整合这些高级状态图。
5. **Sfadm Migration for the Qa Suite**：关于qa套件的sfadm迁移，有一个pr正在进行中，但启动它的人已经不再参与其中。将来，这也可以作为新手参与topology和rbd套件的一个很好的起点。