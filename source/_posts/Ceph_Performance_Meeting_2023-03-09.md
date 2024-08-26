---
title: "Ceph Performance Meeting 2023-03-09"
date: 2023-03-14
updated: 2023-03-15
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议时间：** [具体日期]  
**参会人员：** [参会人员列表]  
**会议主持：** [主持人姓名]  

#### 关键细节
- 会议开始时，主持人因与Josh讨论碎片整理而迟到。
- 讨论了本周的两个新PR，均与Crimson Suite相关。
- 讨论了更新PR，包括qat batch PR、Corey的PR（roxdb iterator bounds for collection list）和Igor的PR（pr4 not resetting the pre-fetched buffer while doing multi-chunk reads）。
- 讨论了关于Blue Store buffered IO的性能问题，特别是与roxdb的交互和预取缓冲区的使用。
- 讨论了CBT的一个PR，关于禁用现有结果目录检查的问题。

#### 讨论的主要议题
1. **新PR讨论**
   - Matan的PR：修复了Crimson性能测试中的collect all安装问题。
   - Intel开发者的PR：增加了细粒度缓存，并提供了基准测试结果。

2. **更新PR讨论**
   - qat batch PR：来自Intel，有一些额外的审查。
   - Corey的PR：关于roxdb迭代器边界，有一些新的修复。
   - Igor的PR：关于预取缓冲区的重置问题，可能有助于改善roxdb的预取行为。

3. **Blue Store Buffered IO问题**
   - 讨论了是否可以在禁用Blue Store buffered IO的同时，通过BlueFS层进行预取缓存。
   - 讨论了roxdb的块缓存问题，以及是否可以通过改进BlueFS层来解决。

4. **CBT PR讨论**
   - 讨论了一个关于禁用现有结果目录检查的PR，目的是防止重复运行测试。

#### 决定的事项
- 对于新PR和更新PR，将继续进行审查和测试。
- 对于Blue Store buffered IO问题，将继续探索在BlueFS层进行预取缓存的可能性。
- 对于CBT PR，将寻找更细致的解决方案，而不是完全禁用现有目录检查。

#### 后续行动计划
- 继续审查和测试本周的新PR和更新PR。
- 进一步研究和测试Blue Store buffered IO的性能问题。
- 与Nissan跟进CBT PR的问题，寻找更细致的解决方案。

**会议结束时间：** [具体时间]  
**下次会议预告：** [具体日期]  

**会议记录人：** [记录人姓名]  
**审核人：** [审核人姓名]  

**备注：** 会议中提到的技术细节和讨论点需要进一步的技术验证和代码审查。