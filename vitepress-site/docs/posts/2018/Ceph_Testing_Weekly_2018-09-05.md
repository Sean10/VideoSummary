---
title: "Ceph Testing Weekly 2018-09-05"
date: 2018-09-06
updated: 2018-09-06
tags:
  - "Ceph"
  - "分布式存储"
  - "测试"
  - "自动化"
categories:
  - "视频总结"
outline: deep
---
**会议纪要**

**会议时间**： 2023年11月某日

**参会人员**： Nathan、Greg、Helen等

**会议主题**：

1. Ceph存储集群部署测试的进展与问题讨论
2. OpenSUSE在Ceph集群测试中的应用
3. Ceph集群测试工具的改进与优化

**会议内容**：

**一、Ceph存储集群部署测试的进展与问题讨论**

*   Nathan在尝试将Ceph集群部署到OpenSUSE时遇到了问题，原因是缺少必要的脚本和配置。
*   Greg了解到Nathan曾向Zach寻求帮助，但脚本链接已失效。
*   会议决定由Nathan通过邮件联系Zach，获取相关脚本，以便自动化部署。

**二、OpenSUSE在Ceph集群测试中的应用**

*   Nathan提出将OpenSUSE作为Ceph集群测试的额外支持发行版。
*   Greg表示需要创建Fog镜像和OVH镜像，以便在OpenSUSE上运行测试。
*   会议决定由Nathan与David Galloway联系，寻求帮助创建Fog镜像。

**三、Ceph集群测试工具的改进与优化**

*   Nathan提到在OpenSUSE上运行Ceph集群测试时遇到的问题，包括单元测试失败等。
*   Greg建议尝试在Ubuntu环境中运行测试，并询问是否已在Ubuntu环境中运行测试。
*   会议决定进一步调查测试失败的原因，并尝试在Ubuntu环境中运行测试。

**四、其他事项**

*   Helen提到Red Hat团队正在使用flake工具分析Ceph代码库，并计划在下周会议上分享他们的发现。

**行动计划**：

*   Nathan通过邮件联系Zach，获取相关脚本。
*   Nathan与David Galloway联系，寻求帮助创建Fog镜像。
*   尝试在Ubuntu环境中运行Ceph集群测试，并调查测试失败的原因。
*   准备下周会议，讨论flake工具的分析结果。

**备注**：

*   会议中提到了Ceph集群测试工具的一些关键术语，如CML、Ceph-ansible、Jenkins、Tox等。
*   会议中提到了Ceph集群测试的一些关键功能，如集群部署、验证、单元测试、集成测试等。
*   会议还讨论了Ceph在OpenSUSE上的测试和部署，以及如何改善测试工具和流程。