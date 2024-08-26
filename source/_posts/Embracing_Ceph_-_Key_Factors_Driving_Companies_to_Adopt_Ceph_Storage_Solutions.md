---
title: "Embracing Ceph: Key Factors Driving Companies to Adopt Ceph Storage Solutions"
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议是在Cephlacon上举办的“拥抱Ceph”专题讨论会。会议由Laura Flores和Dan主持，Laura Flores是RADOS工程师，也是用户开发月度会议的主席，Dan是Ceph执行委员会的成员。会议邀请了五位来自不同组织的Ceph用户作为嘉宾，分享他们选择使用Ceph的关键因素、面临的挑战以及对新组织的建议。

#### 嘉宾介绍
- **Wasil**：Workday的高级软件工程师，负责存储团队，Workday是一个用于人力资源应用的云平台。
- **Andres**：Flatiron Institute的高级数据科学家，该机构是Simons基金会的研究机构，专注于计算科学。
- **Luca**：Posey超级计算中心的架构师，该中心支持澳大利亚所有大学，并将成为SKA望远镜的主要操作基地。
- **Matthew Leonard**：Bloomberg工程的存储工程负责人，负责为全球7000名工程师提供存储资产。
- **Frank Yang**：Patina Systems的首席技术官，该公司提供私有云解决方案和软件。

#### 讨论内容
1. **选择Ceph的关键因素**
   - **Wasil**：从AWS迁移到数据中心时需要块和对象存储，Ceph是OpenStack存储的默认选择，具有成本效益和灵活性。
   - **Andres**：Ceph的开源社区、可靠性优先设计、灵活性和活跃的社区支持是关键因素。
   - **Luca**：Ceph的可靠性、可扩展性无 downtime 以及社区支持使其成为首选。
   - **Matthew Leonard**：Bloomberg早期采用OpenStack和Ceph，社区和开源特性使其持续使用Ceph。
   - **Frank Yang**：Ceph的S3支持、TCO优势、开源社区支持以及灵活性使其成为明显选择。

2. **Ceph的开源特性带来的价值**
   - **Wasil**：能够自主实现安全特性并贡献给社区，Red Hat的支持加速了开源贡献过程。
   - **Andres**：技术人员喜欢能够深入代码，调试和实验的自由，无供应商锁定。
   - **Luca**：开源避免了与HPC供应商的沟通问题，社区支持快速解决问题。
   - **Matthew Leonard**：社区的知识库和活跃的开发者社区提供了强大的支持网络。
   - **Frank Yang**：社区支持、文档丰富，软件开发者可以直接访问源代码。

3. **集成Ceph时的挑战**
   - **Wasil**：自动化工具的集成挑战，安全增强的需求。
   - **Andres**：硬件选择的不确定性，大规模系统的问题。
   - **Luca**：硬件选择和配置的复杂性，大规模系统的挑战。
   - **Matthew Leonard**：硬件和文档的复杂性，应用程序对S3协议的挑战。
   - **Frank Yang**：Ceph内部许多可调参数，硬件和环境差异带来的挑战。

4. **吸引新组织的建议**
   - **Wasil**：Ceph需要更多成熟的基本功能，如RBD设备的复制支持。
   - **Andres**：改进文档，特别是入门指南，确保发布版本的数据可靠性。
   - **Luca**：改进文档，提供针对不同用户群体的指南，明确硬件建议。
   - **Matthew Leonard**：简化Ceph的使用流程，关注用户的工作流程和业务需求。
   - **Frank Yang**：使Ceph更易消费，提供基于工作流的文档和指南，增强安全性检查。

5. **对决策者的建议**
   - **Wasil**：尝试运行POC，了解Ceph的维护和集成需求。
   - **Andres**：从小规模开始，理解Ceph的基本原理，考虑支持选项。
   - **Luca**：与社区沟通，避免硬件选择的错误，根据经验调整集群规模。
   - **Matthew Leonard**：Ceph是生活方式的选择，需要深入理解文档和硬件，社区支持至关重要。
   - **Frank Yang**：尝试Ceph，但需意识到生产环境中的长期承诺和投资。

#### 后续行动计划
- 改进Ceph的文档，特别是入门指南和硬件建议。
- 简化Ceph的使用流程，关注用户的工作流程和业务需求。
- 增强Ceph的安全性检查和错误预防机制。

#### 会议总结
会议涵盖了Ceph用户选择、价值、挑战和建议等多个方面，强调了Ceph的开源社区、灵活性和可靠性。同时，也指出了Ceph在文档、硬件选择和使用流程上的改进空间。会议最后，主持人感谢所有嘉宾的参与和贡献。