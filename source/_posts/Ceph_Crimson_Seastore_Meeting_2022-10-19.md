---
title: "Ceph Crimson/Seastore Meeting 2022-10-19"
date: 2022-10-20
updated: 2022-10-21
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 主要议题与讨论内容

1. **Crimson Suite 重组**
   - 本周已合并一个 PR，将 c-store 相关内容移至 Crimson rados experimental Suite。
   - 目前 RBD 测试尚未通过，主要涉及额外快照支持问题，Erratic 正在处理。

2. **安全特性增强**
   - 提交了一个 PR，增加了 Crimson 和非 Corpson 用户的安全特性。
   - 添加了 OSD map 标志和 pool 标志，以防止 Crimson osds 在未设置标志的情况下创建 pgs。
   - 正在研究添加配置选项，以便在不传递命令行参数的情况下更改 `--s p` 选项。

3. **Scrub 工作进展**
   - 计划继续推进 scrub 工作。

4. **Messenger V2 协议实现**
   - King John 正在审查随机块管理器和 Messenger V2 协议实现。
   - 需要将协议握手阶段和协议就绪阶段分离，以支持 mod core。

5. **Crimson Loop 优化**
   - Junior 发现 Crimson Loop 可能导致栈溢出，正在研究 Sister Loop 的实现并尝试应用到 Crimson。

6. **Open SSO 和 Segmentation 问题**
   - Jensen 发现重复的 Humanity 问题，怀疑是配置差异导致，询问是否有关于 Open SSO 或 Segmentation 的更新。

7. **内存管理问题**
   - 讨论了关于内存存储的 PR，涉及使用分区或多设备的问题，存在一些 bug 需要调试。

8. **LBA 树指针问题**
   - 完成了 LBA 树指针的调试，正在尝试添加 LBA 叶子节点和逻辑扩展之间的指针。

#### 决定事项

- 确保 Crimson rados 测试套件稳定。
- 完成快照实现，确保 ADM 安装和文档完善。
- 推进 scrub 工作。

#### 后续行动计划

- 继续优化和稳定 Crimson rados 测试套件。
- 完成快照实现，确保 Crimson 的功能稳定。
- 推进 scrub 工作，确保 Reef 代码冻结前的准备工作。
- 在明年一月，重点将转向性能优化和 c-store 相关工作。

#### 其他

- 会议中还讨论了关于 Open SSO 和 Segmentation 的问题，以及内存管理和 LBA 树指针的优化工作。
- 强调了确保 Crimson 功能稳定的重要性，以便进行性能测试。

### 会议结束

- 会议结束时，鼓励团队成员继续关注并贡献于上述目标，确保 Crimson 在 Reef 代码冻结前达到稳定状态。
- 会议最后提醒大家有一个愉快的一周，并结束了会议。