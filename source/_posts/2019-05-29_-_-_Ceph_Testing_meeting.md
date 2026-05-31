---
categories:
- 视频总结
date: 2019-05-29
subtitle: 2019-05-29_-_-_Ceph_Testing_meeting
tags:
- 分布式存储
- 编排
title: "'2019-05-29 :: Ceph Testing meeting'"
updated: 2019-05-30
---




### 会议纪要

**会议时间**： 2019年5月29日

**参会人员**： Vacuum, Pakrac, Gretchen, Yuri, Yuki, Danka, DTRS, Zach, others

**会议主题**： Ceph分布式存储的测试与部署工具讨论

**关键细节**：

* **Orchestrator测试**： Vacuum表示将参与每周会议，直到Orchestrator测试完善。目前对Orchestrator的最终进展并不自信。
* **Barcelona会议**： Pakrac分享了参加Barcelona会议的经验，认为会议内容丰富，但在测试方面遇到了一些挑战。
* **降级与回滚**： 讨论了降级与回滚的区别，并决定在每次点发布前进行测试，以确保新旧版本的数据兼容性。
* **部署工具**： 讨论了Ceph的部署工具，包括Leap和Terraform。Yuki提到Leap目前仅适用于OpenStack，但可以考虑扩展到其他平台。
* **KVM测试**： 讨论了使用KVM进行测试的可能性，以及如何将部署工具与Terraform集成。

**主要议题**：

* **Orchestrator测试完善**： 确保Orchestrator的稳定性和可靠性。
* **降级与回滚测试**： 确保每次点发布前进行测试，确保新旧版本的数据兼容性。
* **部署工具优化**： 优化Ceph的部署工具，使其更易于使用和扩展。

**决定的事项**：

* Vacuum将定期参与会议，直到Orchestrator测试完善。
* 在每次点发布前进行测试，确保新旧版本的数据兼容性。
* 探索使用KVM进行测试的可能性，以及将部署工具与Terraform集成。

**后续行动计划**：

* Vacuum将完善Orchestrator的测试。
* 团队成员将进行降级与回滚测试。
* 探索使用KVM进行测试的可能性，以及将部署工具与Terraform集成。

**关键词**：

- Orchestrator
- 测试
- 降级
- 回滚
- 部署工具
- KVM
- Terraform
- Leap
- OpenStack