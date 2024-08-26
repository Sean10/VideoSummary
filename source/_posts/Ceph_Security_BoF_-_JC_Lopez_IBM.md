---
title: "Ceph Security BoF - JC Lopez, IBM"
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 参会人员
- **JC Lopez**：与Seth有长期合作历史，曾被IBM收购后离开，现回归IBM，继续从事Fusion和Seth相关工作。

#### 会议主题
- 数据安全
- 存储强化
- Rook项目
- Ceph存储系统

#### 主要讨论内容
1. **Ceph的未来与现状**：
   - Seth（Ceph）被认为是存储的未来，支持块存储和对象存储。
   - Ceph在Kubernetes和OpenShift环境中显示出极高的灵活性、高可用性和可扩展性。

2. **Rook项目**：
   - Rook是由CNCF孵化的项目，旨在通过操作符模型在Kubernetes环境中部署Ceph集群。
   - Rook已被用于OpenShift Data Foundation和IBM的Fusion Data Foundation。

3. **Ceph与Rook的安全性**：
   - IBM在产品生命周期中进行安全活动，旨在减少风险并提高Ceph和Rook的安全性。
   - 使用安全开发生命周期（SDL）进行代码审计和渗透测试。
   - IBM的PSIRT（产品安全事件响应团队）将文档化所有开源材料，确保使用的库和组件的安全性。

4. **加密与密钥管理**：
   - 支持在OSD级别进行数据静态加密，可以使用自管理密钥或外部密钥管理系统。
   - 支持传输层加密，包括在Messenger层和Rados Gateway的加密。

5. **网络卫生与防火墙**：
   - 强调防火墙的重要性，最新版本的Ceph提供了防火墙服务文件。
   - 控制平面SSH的安全性也需要加强。

6. **Rook的具体安全措施**：
   - Rook通过CRD控制部署，支持数据静态加密和传输层加密。
   - CSI驱动支持KMS，允许在PV级别进行加密。

7. **安全最佳实践**：
   - 强调suffix的重要性，不应在生产环境中禁用。
   - 管理客户端密钥和S3用户访问密钥的安全性。

#### 后续行动计划
- 继续审查现有安全措施，定期更新安全代码。
- 遵循IBM的安全标准，修复已知漏洞。
- 加强与IBM同事的合作，学习新的安全流程。

#### 其他信息
- 会议中提到的Ceph和Rook的安全特性将通过后续文档和演示材料进行详细说明。
- 鼓励与会者如有安全相关问题，可随时联系JC Lopez或其他相关人员。

#### 会议结束
- 会议结束时，JC Lopez感谢大家的参与，并表示会将所有相关材料和幻灯片分享给与会者。