---
title: "Ceph Developer Monthly 2022-06-01"
date: 2022-06-03
updated: 2022-06-03
tags:
categories:
- "视频总结"
subtitle: tech
---


- **问题**: 对于客户来说，一个对象内部有洞和对象内部有洞但被分配之间的区别是什么？
- **答案**: 区别在于加密用例。如果一个区域被分配但没有数据（即有洞），在读取时不需要解密，直接返回零；但如果这个区域实际包含了加密后的数据，即使这些数据是全零，也需要先解密再返回给用户。