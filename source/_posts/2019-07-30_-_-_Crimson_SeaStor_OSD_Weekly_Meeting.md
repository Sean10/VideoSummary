---
categories:
- 视频总结
date: 2019-08-02
subtitle: 2019-07-30_-_-_Crimson_SeaStor_OSD_Weekly_Meeting
tags:
- Ceph
- 分布式存储
- CRUSH算法
- 高可用性
- 对象存储
title: "'2019-07-30 :: Crimson SeaStor OSD Weekly Meeting'"
updated: 2019-08-03
---


会议纪要

会议时间：[请填写具体时间]
会议地点：[请填写具体地点]
参会人员：[请填写参会人员名单]

一、会议关键细节

1. 会议因部分成员迟到而延迟开始。
2. 多位成员汇报了各自的工作进展和遇到的问题。

二、讨论的主要议题

1. Ceph存储系统相关：
   - 成员汇报了在Ceph存储系统中遇到的14octuple问题，第一轮测试案例仍失败，但已取得进展。
   - 讨论了基于meaning change实现lucid connection的replica优化方案。
   - 分享了针对POSIX接口的修改和any store API的改进。
   - 讨论了dirt class的支持修复，已提交PR。
   - 分享了Ceph存储系统中object class DPI的实现和crimson的优化方案。
2. 视频会议字幕翻译及总结：
   - 分享了字幕翻译的实践经验，包括英译中和总结工作。
   - 讨论了翻译过程中遇到的问题，以及提高翻译质量的方法。
3. 其他议题：
   - 汇报了back off功能的实现，以及避免频繁连接到manager的方法。
   - 讨论了admin console interface的实现和UNIX domain sockets的支持。
   - 分享了Protocol v2 looseness policy的实现和测试情况。
   - 讨论了rocksDB在Ceph存储系统中的应用，以及与C-store的集成。

三、决定的事项

1. 针对Ceph存储系统：
   - 继续优化14octuple问题，并提交相关PR。
   - 完善replica优化方案，并提交相关PR。
   - 完善POSIX接口的修改，并提交相关PR。
   - 修复dirt class问题，并提交相关PR。
   - 优化object class DPI的实现，并提交相关PR。
2. 针对视频会议字幕翻译及总结：
   - 提高翻译质量，分享翻译经验。
   - 完善翻译流程，确保翻译准确性和时效性。
3. 针对其他议题：
   - 完成back off功能的实现，并提交相关PR。
   - 支持UNIX domain sockets，实现admin console interface。
   - 完成Protocol v2 looseness policy的测试，并提交相关PR。
   - 探索rocksDB在Ceph存储系统中的应用，并与C-store进行集成。

四、后续行动计划

1. 各成员按照决定的事项，继续推进各自的工作。
2. 定期召开会议，汇报工作进展和讨论相关问题。
3. 加强团队协作，共同推进Ceph存储系统和视频会议字幕翻译及总结工作。