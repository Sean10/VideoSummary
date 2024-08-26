---
title: "Ceph Orchestrator Meeting 2020-07-13"
date: 2020-07-13
updated: 2020-07-14
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议时间：** [具体日期]  
**参会人员：** Fezzik, Travis, Oh, Mike, 以及其他相关人员  
**会议主持：** [主持人姓名]  

#### 主要议题及讨论内容：

1. **Rook集成测试问题**
   - 讨论了Rook集成测试因近期更改而中断的问题。
   - 决定暂时禁用该测试，并计划重新启用。
   - Kiefel提交了一个PR，预计将修复该问题。
   - 后续行动：重新启用并监控测试，确保其正常运行。

2. **容器镜像重命名**
   - 讨论了CI构建的容器镜像重命名的问题。
   - Deepika上周完成了相关工作，目前镜像重命名功能已恢复正常。

3. **Drive Groups功能**
   - 讨论了Drive Groups功能的进展，目前仍在等待上游合并。
   - 正在进行私有构建的测试，结果良好。
   - 后续行动：继续等待上游合并，并进行进一步测试。

4. **Rook Monitor模块的Placement Specifications**
   - 讨论了Rook Monitor模块中Placement Specifications的实现问题。
   - 决定使用Kubernetes的Placement Specifications，而非Orchestrator风格的Placement Specifications。
   - 需要进一步的示例和指导。
   - 后续行动：提供更多示例，确保正确实现。

5. **新成员介绍**
   - 介绍了新成员Karen Norma，她将负责文档工作。
   - Karen将专注于Ceph ADM和安装程序的文档，以及与Orchestrator相关的部分。
   - 后续行动：与Karen建立联系，提供必要的资源和支持。

6. **其他事项**
   - 讨论了SEF ADM安装指南的编写，建议与现有文档进行整合。
   - 后续行动：安排会议，讨论具体细节。

#### 决定事项：

- 重新启用并监控Rook集成测试。
- 继续推进Drive Groups功能的测试和合并。
- 提供更多Placement Specifications的示例和指导。
- 与Karen Norma建立联系，支持其文档工作。

#### 后续行动计划：

- 监控Rook集成测试的运行情况。
- 继续跟进Drive Groups功能的上游合并。
- 提供Placement Specifications的示例和指导。
- 安排与Karen Norma的会议，讨论文档编写细节。

**会议结束时间：** [具体时间]  
**下次会议预告：** 下周同一时间  

**备注：** 请各位参会人员关注邮件和IRC频道，获取更多更新和资源。