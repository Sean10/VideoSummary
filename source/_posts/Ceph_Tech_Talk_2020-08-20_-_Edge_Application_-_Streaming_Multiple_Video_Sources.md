---
categories:
- 技术会议
date: 2020-08-20
subtitle: Ceph_Tech_Talk_2020-08-20_-_Edge_Application_-_Streaming_Multiple_Video_Sources
tags:
- Ceph
- 分布式存储
title: Ceph Tech Talk 2020-08-20- Edge Application - Streaming Multiple Video Sources
updated: 2020-08-21
---


### 会议纪要

#### 会议主题：Ceph Tech Talk - 边缘应用多视频源流式传输项目介绍

#### 会议时间：2020年8月20日

#### 会议地点：线上会议

#### 主持人：Mike Perez（社区经理，Red Hat新兴技术部门）

#### 参会人员：Jason Wang、Niharika Kompala（Red Hat实习生）、其他未具名观众

#### 会议内容总结：

1. **项目介绍**：
   - Jason Wang和Niharika Kompala作为Red Hat的实习生，介绍了他们在夏季实习期间开发的边缘应用项目，该项目涉及多视频源的流式传输。
   - 项目目标是通过边缘计算技术改善视频流的质量和延迟问题，特别是处理大量摄像头数据时。

2. **技术背景**：
   - 讨论了边缘计算的重要性，特别是在预计到2025年将有750亿连接设备的大数据量背景下。
   - 强调了边缘计算在提供低延迟和高速度处理方面的优势。

3. **项目架构与技术实现**：
   - 项目使用了GStreamer框架来处理视频流，并开发了自定义的GStreamer插件来上传视频到Ceph存储系统。
   - 利用Ceph的多部分上传功能和S3 API，实现了视频数据的同步和存储。
   - 通过Knative函数触发器，实现了视频的拼接和分析处理，使用了OpenCV进行视频拼接。

4. **演示与代码展示**：
   - 展示了项目的实际运行情况，包括视频流的上传和拼接过程。
   - 讨论了在Fedora系统上运行GStreamer时遇到的问题，并介绍了使用Ubuntu容器作为解决方案。

5. **未来工作与感谢**：
   - 提出了未来可能的扩展，如创建RGW NFS网关以支持RTMP视频流。
   - 感谢Warman、Harrison以及Ceph团队的支持和帮助。

#### 后续行动计划：
- 继续优化和扩展项目功能，特别是在Knative和Ceph的集成方面。
- 探索更多的边缘计算应用场景，以支持更广泛的视频流处理需求。

#### 会议结束：
- 会议在感谢和告别中结束，主持人预告了下一次的Tech Talk主题。

#### 备注：
- 会议中提到的GitHub项目URL未在纪要中提供，建议后续补充。



以上是本次Ceph Tech Talk的会议纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。