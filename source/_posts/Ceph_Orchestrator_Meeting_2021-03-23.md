---
title: "Ceph Orchestrator Meeting 2021-03-23"
date: 2021-03-23
updated: 2021-03-24
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 主要议题与讨论内容

1. **OC服务拉取请求（Pull Request）**
   - 讨论了关于OC服务的拉取请求，决定将所有非托管的OSD（Object Storage Daemon）钻石整合到一个OS服务中。
   - 决定在尝试删除该服务时，显示消息提示用户需要先删除相关的OSD。
   - 讨论了OSD.unmanaged的命名问题，认为这是一个合适的名称。

2. **卷设置（Set Volume）的容器版本问题**
   - 讨论了关于卷设置时使用与管理器相同容器版本的问题，询问了Sebastian关于该拉取请求的状态。
   - 确认该拉取请求尚未合并，但认为当前的实现方式是可行的。

3. **HA RGW服务的设计问题**
   - 讨论了HA RGW服务的设计，特别是HAProxy和Keepalived部分是否应该分开成两个独立的服务。
   - 提出了将HAProxy和Keepalived分开成两个服务的建议，以便更灵活地使用它们。
   - 讨论了服务的配置和密码管理问题，建议自动生成密码并存储在配置文件中。

4. **OSD内存自动配置**
   - 提到了OSD内存自动配置的问题，但目前该议题被暂时搁置。

5. **Rook Orchestrator的状态**
   - 讨论了Rook Orchestrator的状态，确认其基本功能可用，但需要进一步的测试和功能完善。

#### 决定事项

- 将所有非托管的OSD钻石整合到一个OS服务中，并在删除服务时提示用户先删除相关OSD。
- 考虑将HA RGW服务中的HAProxy和Keepalived分开成两个独立的服务。
- 自动生成密码并存储在配置文件中，以简化用户配置。

#### 后续行动计划

- 继续跟进OC服务的拉取请求，确保其顺利合并。
- 对HA RGW服务进行重构，将其分为HAProxy和Keepalived两个独立的服务。
- 测试和完善Rook Orchestrator的功能，确保其稳定性和可用性。
- 关注OSD内存自动配置的问题，适时重启相关工作。

#### 其他事项

- 确认了Pacific版本的预期发布日期，并讨论了与OpenStack Wallaby版本的集成问题。
- 感谢OpenStack团队的支持，并讨论了未来可能的合作方向。

### 会议结束

会议在确认所有议题讨论完毕后结束，感谢所有参与者的贡献，并祝愿大家工作顺利。