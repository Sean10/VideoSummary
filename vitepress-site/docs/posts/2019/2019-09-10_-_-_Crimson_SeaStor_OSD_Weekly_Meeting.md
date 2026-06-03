---
title: "2019-09-10 :: Crimson SeaStor OSD Weekly Meeting"
date: 2019-09-20
updated: 2019-09-21
tags:
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2023年11月某日

**参会人员**： Jemaine（Ceph存储负责人）、Tom（集成测试负责人）、Dr. Merlin（代码调试）、Conscious（测试）、其他相关人员

**会议内容**：

**一、Ceph存储集成测试**

*   Jemaine正在努力将Ceph存储集成到Jenkins中，并已取得一些进展。
*   Tom提出关于如何对Commission进行CBD测试的疑问，建议使用CBT进行测试。
*   Jemaine将继续测试Jenkins集成，并与Riddick合作启用RBD和日志恢复功能。

**二、代码调试**

*   Dr. Merlin在调试代码时发现，在GDB环境中，某些代码修改后会导致promise broken异常消失。
*   Conscious提出，在OST启动时出现网络问题，导致get future失败。
*   Dr. Merlin认为这是一个bug，需要进一步调查。

**三、测试问题**

*   Conscious在测试中发现，某些测试输出被Jenkins控制台吞没，导致无法查看完整日志。
*   Jemaine建议尝试重现问题，并希望Conscious提供更多信息。

**四、其他事项**

*   Conscious提出，在编译单元测试时，存在大量无法丢弃的future警告，建议进行审计和注释。
*   Jemaine表示，已修复大部分future non discard future问题，但仍需关注OSD部分。
*   Conscious建议记录丢弃future的原因，例如使用gate确保实例的生命周期。

**五、行动计划**

*   Jemaine继续测试Jenkins集成，并与Riddick合作启用RBD和日志恢复功能。
*   Dr. Merlin和Conscious继续调查promise broken异常问题。
*   Conscious尝试重现Jenkins测试问题，并提供更多信息。
*   Conscious和Jemaine对无法丢弃的future进行审计和注释。

**六、后续会议**

*   下次会议时间待定。

**关键词**：

*   Ceph存储
*   Jenkins集成
*   CBD测试
*   CBT测试
*   RBD
*   日志恢复
*   GDB
*   promise broken
*   future non discard future
*   gate
*   OSD