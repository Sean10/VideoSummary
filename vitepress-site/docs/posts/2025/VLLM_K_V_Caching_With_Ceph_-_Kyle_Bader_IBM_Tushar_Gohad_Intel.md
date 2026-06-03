---
title: "VLLM K/V Caching With Ceph - Kyle Bader, IBM & Tushar Gohad, Intel"
date: 2025-11-19
updated: 2025-11-20
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### Ceph 与 AI 存储优化技术研讨会会议纪要  

#### **会议主题**  
本次研讨会探讨了 Ceph 分布式存储在 AI 大模型推理（LLM Inference）中的应用，特别是通过 KV Cache 缓存优化解决 GPU 内存瓶颈问题，并提升推理效率。

#### **关键讨论内容**  

##### **1. AI 推理中的存储挑战**  
- **KV Cache 的线性增长问题**：随着上下文长度（Context Length）的增加，KV Cache 需求线性增长，导致 GPU 内存不足，影响并发请求数和 GPU 利用率。
- **计算与存储的权衡**：Prefill 阶段的计算复杂度为 O(n²)，而存储 KV Cache 的复杂度为 O(1)，通过将 KV Cache 卸载到共享存储（如 Ceph）可以优化计算资源。

##### **2. Ceph 作为 KV Cache 存储层的优势**  
- **实验架构**：使用 VLLM（Berkeley 推理框架）+ LM Cache（KV Cache 管理器）+ Ceph RGW（S3 接口）。
- **性能**：单客户端可驱动 60GB/s 读取带宽，满足高吞吐需求。
- **内容寻址存储**：KV Cache 块通过哈希映射到 S3 对象，无需元数据库，支持无状态扩展和弹性存储。

##### **3. 性能收益与案例分析**  
- **时间优化**：在 100K Token 上下文场景下，通过 Ceph 读取 KV Cache 可实现 5-10 倍的 Time-to-First-Token（TTFT）加速。
- **成本效益**：存储 KV Cache 的成本远低于 GPU 计算开销。

##### **4. 未来方向**  
- **分布式推理优化**：结合 LLMD（Red Hat/Google 分布式推理框架）实现 Prefill/Decode 解耦，支持异构加速器。
- **技术扩展**：探索 NFS over RDMA 或 GPU Direct Storage 进一步降低延迟，研究 KV Cache 分区加密提升数据安全性。

##### **行动计划**  
1. **Ceph 与 VLLM/LM Cache 集成**：将现有实验成果文档化，推动成为 VLLM 官方支持的存储后端。
2. **性能基准测试**：使用真实 AI 负载 Trace 验证缓存命中率与扩展性。
3. **生态合作**：与 NeoCloud 厂商合作，提供 KV Cache-as-a-Service 解决方案。

#### **会议结论**  
Ceph 的高吞吐和弹性扩展能力使其成为 AI 推理 KV Cache 卸载的理想存储层，未来需进一步优化生态集成与多租户支持。