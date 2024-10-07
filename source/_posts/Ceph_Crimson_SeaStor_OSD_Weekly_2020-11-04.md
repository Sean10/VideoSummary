---
title: "Ceph Crimson/SeaStor OSD Weekly 2020-11-04"
date: 2020-11-16
updated: 2020-11-17
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
1. **对象上下文锁定恢复问题**：
   - 讨论了在PG（Placement Group）活动集更改时解锁对象上下文的问题。
   - 提出了使用`with lock`原语来确保解锁操作总是被调用的解决方案。

2. **EIO处理**：
   - 讨论了在PG后端处理EIO（输入/输出错误）的适当位置。
   - 决定将EIO处理移至`pg.cc`，并在客户端请求中处理重启逻辑。

3. **PG状态修复**：
   - 讨论了在遇到EIO时将PG状态设置为修复的原因和后果。
   - 确认修复状态是为了触发后续的 scrub 和修复操作。

4. **文档编写**：
   - 建议编写文档来解释设计目标和计划的上传位置，以帮助评审人员理解。

5. **性能测试**：
   - 讨论了将新功能添加到性能测试中的可能性，以确保代码路径的持续优化。

6. **集合树的需求**：
   - 讨论了是否需要为Ceph存储节点信息创建单独的树。
   - 提出了使用现有接口和对象存储来处理集合信息的建议。

7. **线程池处理**：
   - 讨论了线程池处理和心跳计时器的使用，以防止长时间操作导致的心跳问题。

8. **测试和分布式问题**：
   - 讨论了测试的覆盖范围和特定分布的限制。

9. **事务管理器和性能**：
   - 讨论了事务管理器的性能测试和需要修复的问题。

10. **Messenger更改**：
    - 讨论了Messenger在多核环境下的运行问题和可能的设计变更。

#### 决定事项
1. **EIO处理位置**：决定将EIO处理逻辑移至`pg.cc`。
2. **文档编写**：决定编写详细的设计文档来解释EIO处理的设计和实现。
3. **集合树的需求**：决定不创建单独的树，而是使用现有接口来处理集合信息。
4. **Messenger更改**：决定进一步研究Messenger在多核环境下的运行问题，并考虑设计变更。

#### 后续行动计划
1. **编写设计文档**：编写详细的设计文档，包括EIO处理和Messenger更改的设计。
2. **性能测试**：将新功能添加到性能测试中，以确保代码路径的持续优化。
3. **集合树的研究**：进一步研究集合树的需求和现有接口的使用。
4. **Messenger更改的研究**：进一步研究Messenger在多核环境下的运行问题，并考虑设计变更。

### 结论
本次会议主要讨论了Ceph存储系统中的多个关键问题，包括EIO处理、对象上下文锁定恢复、集合树的需求和Messenger的更改。通过详细的讨论和决策，确定了后续的行动计划，以确保系统的稳定性和性能优化。