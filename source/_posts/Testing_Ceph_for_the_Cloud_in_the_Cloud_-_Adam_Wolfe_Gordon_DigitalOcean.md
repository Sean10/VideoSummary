---
categories:
- 视频总结
date: 2019-05-24
subtitle: Testing_Ceph_for_the_Cloud_in_the_Cloud_-_Adam_Wolfe_Gordon_DigitalOcean
tags:
- 测试
- 分布式存储
title: "Testing Ceph for the Cloud, in the Cloud - Adam Wolfe Gordon, DigitalOcean"
updated: 2019-05-24
---



## 改进后的中文总结内容

Adam Wolfe Gordon，来自DigitalOcean存储团队，在KubeCon会议上分享了他们如何使用云资源搭建Ceph测试环境的过程和挑战。

**会议背景**

DigitalOcean是一家公有云提供商，基于Ceph技术构建了其存储产品。随着业务规模扩大，DigitalOcean开始需要更多控制权，以满足服务质量要求，并解决对象存储中的扩展限制和bug。

**主要议题**

1. **Ceph测试环境搭建**：
    - DigitalOcean决定搭建自己的Ceph测试环境，并开发内部工具以实现自动化测试。
    - 由于Toothology框架的限制，DigitalOcean需要进行一些调整，例如解决DNS名称通信和网络配置问题。

2. **搭建测试环境遇到的挑战**：
    - **Toothology框架的限制**：DigitalOcean通过安装DNS Masq和配置hosts文件来解决DNS通信问题，通过黑名单规则解决网络配置问题，通过创建符号链接解决Ceph包路径问题，修改代码以跳过SHA-1验证。
    - **自动化测试环境搭建**：DigitalOcean使用Terraform和Ansible自动化脚本搭建Ceph测试环境，包括Droplets、Paddles服务器、Head节点和Test节点，用户可以通过运行单个命令来启动测试环境。

**行动计划**

- DigitalOcean将继续优化Ceph测试环境，并开源其自动化脚本，以帮助社区成员快速搭建测试环境。
- DigitalOcean将继续向Ceph社区贡献代码，并积极参与社区活动。

**会议总结**

本次会议介绍了DigitalOcean如何搭建Ceph测试环境，并分享了在搭建过程中遇到的挑战和解决方案。DigitalOcean的自动化脚本为Ceph社区提供了宝贵的资源，有助于促进Ceph技术的发展和应用。