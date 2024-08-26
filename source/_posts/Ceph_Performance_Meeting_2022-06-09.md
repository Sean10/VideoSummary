---
title: "Ceph Performance Meeting 2022-06-09"
date: 2022-06-27
updated: 2022-06-28
tags:
categories:
- "视频总结"
subtitle: tech
---


- **项目1**：不需要ropes保护snap mapper，在系统关闭时将其保存到文件中，这会增加几百毫秒的关闭时间，但在启动时通过从文件中读取可以节省时间。
- **项目2**：处理删除操作，通过批量处理删除请求来减少与roxdb的交互次数，从而减少性能开销。
- **项目3**：将snap marker从一个单一的大型实体更改为每个pg维护自己的snap mapper集合，这可以减少锁冲突并提高性能。