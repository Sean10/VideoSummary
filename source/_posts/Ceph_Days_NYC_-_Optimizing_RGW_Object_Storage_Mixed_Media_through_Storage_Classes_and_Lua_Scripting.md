---
categories:
- 视频总结
date: 2023-05-17
subtitle: Ceph_Days_NYC_-_Optimizing_RGW_Object_Storage_Mixed_Media_through_Storage_Classes_and_Lua_Scripting
tags:
- RGW
- 对象存储
title: "'Ceph Days NYC: Optimizing RGW Object Storage Mixed Media through Storage Classes and Lua Scripting'"
updated: 2023-05-18
---




在Ceph Days NYC会议上，Anthony Daughtry分享了关于如何通过存储类别和Lua脚本优化Ceph RGW对象存储的技巧和策略。以下是会议的关键要点：

**会议参与者**：
- Anthony Daughtry，前Solidine（Intel的NAND部门）员工，现就职于Index Exchange。
- Kurt Bruns，负责编码部分，未参会。

**会议主题**：
- Ceph RGW部署的特性与挑战，特别是对象大小多样性对成本和性能的影响。
- 不同存储介质（如HDD、SSD、QLC SSD）的优缺点及适用场景。
- 使用SNIA的TCO计算器评估存储解决方案的实际成本。
- 在Ceph中配置多存储池以适应不同的工作负载和存储需求。
- 使用Lua脚本动态调整存储类别，优化存储管理。

**关键讨论点**：
1. **对象大小对存储设计的影响**：大对象需要高读取吞吐量，但不易缓存；小对象操作每GB的overhead更大，适合低延迟的快速存储。
2. **存储介质的选择**：HDD成本低但性能有限；SSD性能优越但成本较高；QLC SSD成本低、密度高，性能介于HDD和TLC SSD之间。
3. **TCO分析**：使用SNIA的TCO计算器考虑驱动器成本、数据中心运营成本、维护成本等。
4. **多存储池配置**：通过混合介质，为不同类型的数据提供不同的存储池；S3协议的存储类别可用于对象存储，通过请求头指定。
5. **Lua脚本的应用**：使用Lua脚本来动态调整存储类别，无需用户手动配置；优化存储分配，减少空间放大问题。

**决定事项**：
- 采用Lua脚本来自动化存储类别的分配，提高Ceph RGW的灵活性和效率。
- 使用SNIA的TCO计算器来更准确地评估存储解决方案的成本。

**后续行动计划**：
- 继续优化Lua脚本，确保其在不同工作负载下的稳定性和效率。
- 推广使用SNIA的TCO计算器，帮助用户做出更明智的存储投资决策。
- 探索更多存储介质的组合，以满足不同应用场景的需求。

**结束语**：
会议强调了持续优化和创新在存储管理中的重要性，并欢迎对使用Lua脚本优化Ceph RGW存储管理感兴趣的人士联系Anthony Daughtry。