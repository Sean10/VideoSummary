---
categories:
- 视频总结
date: 2022-10-20
subtitle: Ceph_Crimson_Seastore_Meeting_2022-10-19
tags:
- Ceph
- 分布式存储
- 性能
title: "Ceph Crimson/Seastore Meeting 2022-10-19"
updated: 2022-10-21
---




### 改进后的中文总结内容

本次会议主要讨论了Ceph Crimson Suite的开发进度和相关议题。以下是会议的主要内容：

#### 主要议题与讨论内容

1. **Crimson Suite 重组**
   - 已合并一个PR，将c-store相关内容移至Crimson rados experimental Suite。
   - RBD测试尚未通过，主要涉及额外快照支持问题，Erratic正在处理。

2. **安全特性增强**
   - 提交了一个PR，增加了Crimson和非Corpson用户的安全特性。
   - 添加了OSD map标志和pool标志，以防止Crimson osds在未设置标志的情况下创建pgs。
   - 研究添加配置选项，以便在不传递命令行参数的情况下更改`--s p`选项。

3. **Scrub工作进展**
   - 计划继续推进scrub工作。

4. **Messenger V2协议实现**
   - King John正在审查随机块管理器和Messenger V2协议实现。
   - 需要将协议握手阶段和协议就绪阶段分离，以支持mod core。

5. **Crimson Loop优化**
   - Junior发现Crimson Loop可能导致栈溢出，正在研究Sister Loop的实现并尝试应用到Crimson。

6. **Open SSO和Segmentation问题**
   - Jensen发现重复的 Humanity问题，怀疑是配置差异导致，询问是否有关于Open SSO或Segmentation的更新。

7. **内存管理问题**
   - 讨论了关于内存存储的PR，涉及使用分区或多设备的问题，存在一些bug需要调试。

8. **LBA树指针问题**
   - 完成了LBA树指针的调试，正在尝试添加LBA叶子节点和逻辑扩展之间的指针。

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