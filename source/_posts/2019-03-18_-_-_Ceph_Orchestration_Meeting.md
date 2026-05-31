---
categories:
- 视频总结
date: 2019-04-15
subtitle: 2019-03-18_-_-_Ceph_Orchestration_Meeting
tags:
- 分布式存储
title: "'2019-03-18:: Ceph Orchestration Meeting'"
updated: 2019-04-15
---




### 会议纪要

**会议主题**： Ceph分布式存储项目进展及问题讨论

**会议时间**： 2023年某月某日

**参会人员**： Tim、Eric、Dr. Mercer、Nelson等

**会议内容**：

**一、Tipsy Orchestrator模块进展**

*   Tim指出，已修复scythe模块在构建过程中重复构建的问题，预计修复将在大约一个小时后生效。
*   深海Orchestrator模块的启用等待surf模块的修复，该修复已于八天前发布。
*   需要检查CI环境中的Ceph版本是否包含surf模块的修复，如果包含，则可以合并深海Orchestrator模块。

**二、深海Orchestrator模块问题**

*   get inventory函数在深海Orchestrator模块中使用SEF卷时无法正常工作，因为深海尚未合并使用SEF卷的代码。
*   blinky lights功能代码尚未合并，需要硬件支持进行测试。

**三、其他问题**

*   Sephardim输出和库存问题，由于依赖深海模块的某些功能，目前无法合并。
*   Dr. Mercer提出，需要设置一个会议时间，以便讨论Falcone项目。
*   Eric提到，正在处理一个关于密度方法的问题，预计本周完成。

**四、行动计划**

*   Tim将继续修复Tipsy Orchestrator模块相关的问题。
*   检查CI环境中的Ceph版本，如果包含surf模块的修复，则合并深海Orchestrator模块。
*   Nelson将在下周一提供反馈。
*   设置会议时间，讨论Falcone项目。
*   Eric将继续处理密度方法问题。

**五、关键术语**

*   Tipsy Orchestrator
*   scythe
*   deep-sea Orchestrator
*   SEF volume
*   blinky lights
*   Sephardim
*   density method

**改进说明**：

1. 保留了所有关键术语，包括Ceph相关的关键字。
2. 对会议内容进行了澄清，确保准确反映原始内容的要点。
3. 确保了会议的详细讨论和行动计划都被涵盖。