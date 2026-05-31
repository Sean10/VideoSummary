---
categories:
- 视频总结
date: 2019-05-24
subtitle: RGW_S3_-_Feature_Progress_Limitations_Testing_-_Robin_H_Johnson_Ali_Maredia
tags:
- Ceph
- RGW
- 性能
title: "'RGW S3: Feature Progress, Limitations & Testing - Robin H Johnson & Ali Maredia,'"
updated: 2019-05-24
---
会议纪要：

**会议主题**： Ceph RGW中的S3功能及其局限性

**会议参与者**： Robin（Digital Ocean）、Allie（Red Hat）

**会议内容**：

1. **S3术语回顾**：
   - 回顾了S3协议、规范、AWS服务以及Ceph RGW（Rados Gateway）的定义。

2. **S3功能与局限性**：
   - 讨论了Ceph RGW在S3功能方面的局限性，例如S3库存、分析、生命周期管理等。
   - 提到了S3测试套件和其局限性，包括不覆盖RGW后端特定功能、不用于性能测试等。

3. **RGW对象布局与删除**：
   - 解释了RGW如何将对象布局到Redis中，以及删除对象时的同步和异步过程。

4. **垃圾回收**：
   - 分析了垃圾回收设计的问题，例如单线程运行、对OSD的读写压力很大、缺乏监控等。

5. **生命周期管理**：
   - 讨论了生命周期管理存在的问题，如元数据访问昂贵、扫描速度慢、缺乏监控等。

6. **S3测试的未来**：
   - 提出了改进S3测试套件的计划，包括迁移到Python 3、添加更多测试用例、支持其他SDK等。

7. **S3测试的社区贡献**：
   - 鼓励社区贡献S3测试套件，希望所有提供商都能使用并共同改进。

8. **S3 API的扩展**：
   - 考虑扩展S3 API，以提供用户统计、桶统计、用户配额等信息。

**会议决定事项**：

1. 修复垃圾回收设计中的问题。
2. 优化生命周期管理。
3. 将S3测试套件迁移到pytest。
4. 添加更多测试用例，覆盖更多SDK。
5. 鼓励社区贡献S3测试套件。

**后续行动计划**：

1. Robin和Allie将负责修复垃圾回收设计中的问题。
2. Robin和Allie将负责优化生命周期管理。
3. Robin和Allie将负责将S3测试套件迁移到pytest。
4. Robin和Allie将负责添加更多测试用例，覆盖更多SDK。
5. Robin和Allie将鼓励社区贡献S3测试套件。