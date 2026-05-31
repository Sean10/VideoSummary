---
categories:
- 视频总结
date: 2021-08-26
subtitle: Ceph_Tech_Talk_-_Going_NATS
tags:
- Ceph
title: "'Ceph Tech Talk: Going NATS'"
updated: 2021-08-27
---



Ceph Tech Talk: Going NATS会议纪要：

本次技术会谈的主题是使用Lua脚本与NATS Blue客户端集成，以实现Ceph存储桶的通知功能。

**会议内容概述**：

1. **背景介绍**：Martin Brisman介绍了如何通过Lua脚本在Ceph中集成NATS Blue客户端，实现存储桶通知功能。存储桶通知可以在特定事件（如添加或删除对象）发生时，向外部系统发送通知。

2. **应用场景**：展示了数据管道的示例，其中上传的X光照片在Ceph存储桶中触发通知，通过Knative事件组件处理，评估疾病风险，并将结果返回给诊所或研究人员。

3. **技术细节**：目前Ceph支持向Kafka、AMQP和HTTP端点发送通知，但希望通过Lua脚本集成NATS，而无需修改源代码。Lua脚本可以在Ceph中上传，并在每次收到存储桶请求时执行。

4. **演示环节**：Martin展示了如何上传Lua脚本到Ceph，并使用rgw admin命令安装所需的Lua包。通过s3cmd命令向存储桶发送请求，演示了Lua脚本如何捕获请求并将其发送到NATS服务器。

5. **未来展望**：讨论了Lua脚本的潜在集成机会，如与Elasticsearch和Prometheus的集成。提到了正在开发中的背景脚本，这将有助于监控和在请求之间保存缓存。

6. **问题与讨论**：讨论了Lua脚本的优势，如无需修改源代码即可集成新系统，以及其简单易用的特点。也提到了一些限制，如无法在运行之间缓存数据，以及需要改进的地方，如背景数据结构的持久化。

**会议决定**：

- 鼓励社区成员尝试使用Lua脚本进行集成和调试，并提供反馈以指导未来功能的开发。

**后续行动计划**：

- 继续开发背景脚本和数据结构，以支持更复杂的监控和集成需求。
- 收集社区反馈，优化Lua脚本功能。

**标签**：

- Ceph
- Lua scripting
- NATS
- Storage notifications
- Open source