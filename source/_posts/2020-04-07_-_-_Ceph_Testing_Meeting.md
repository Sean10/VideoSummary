---
title: "2020-04-07 :: Ceph Testing Meeting"
date: 2020-04-13
updated: 2020-04-14
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议参与者：** Yuri, Undine

**会议日期：** [具体日期未提供]

**会议主要议题：**
1. **Ceph项目新功能讨论**
   - Yuri正在测试一个由Nathan引入的新功能，该功能允许在集群关闭前无限期睡眠。
   - 该功能旨在允许用户在集群部署后进行调试或实验，通过在任务调度时添加“sleep before tear down”选项实现。
   - 目前该功能尚未合并到主分支，Yuri正在对其进行审查和测试。

**决定事项：**
- Yuri计划在功能测试完成后，通过邮件通知团队成员。
- 考虑增加通知功能，如在Rocket Chat或通过邮件通知。

**后续行动计划：**
- Yuri将继续测试“sleep before tear down”功能，并确保其稳定性和可用性。
- 功能测试完成后，Yuri将通知团队成员，并考虑增加通知机制。

**其他讨论内容：**
- 讨论了当前的工作环境和生活方式，特别是在疫情期间的居家工作和社交限制。
- 分享了个人的健康状况和家庭情况，以及疫情对个人和家庭的影响。

**会议总结：**
会议主要围绕Ceph项目的新功能“sleep before tear down”进行了讨论，Yuri负责该功能的测试和后续通知工作。此外，会议还涉及了疫情期间的工作和生活状态，以及个人和家庭的情况。