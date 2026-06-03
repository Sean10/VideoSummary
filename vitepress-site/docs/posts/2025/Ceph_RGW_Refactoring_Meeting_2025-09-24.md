---
title: "Ceph RGW Refactoring Meeting 2025-09-24"
date: 2025-09-29
updated: 2025-09-29
tags:
  - "Ceph"
  - "RGW"
categories:
  - "视频总结"
outline: deep
---
### Ceph 社区会议纪要  
**日期**: 2025-09-24  
**主题**: S3 测试迁移、Admin REST API 贡献及 Copy Object 加密更新  



#### **1. S3 测试迁移（Boto2 → Boto3）**  
**关键讨论**: 
- **背景**: 由于 YUbuntu 24 的 Python 版本升级，部分遗留的 `Boto2` S3 测试无法运行，需要迁移至 `Boto3`。
- **现状**: 多数测试已完成迁移，但部分遗留用例（`Boto2`）仍阻塞测试流程。
- **PR 提案**: 直接移除未迁移的测试，可能导致测试覆盖率下降。
- **争议点**: 渐进式迁移 vs 一次性移除。
- **决策**: 若短期内无志愿者完成迁移，将接受移除遗留测试的 PR，后续通过新测试补充覆盖率。
- **后续行动**: Yehuda 推进移除 PR，标记为阻塞解决；Bloomberg 团队评估迁移或新测试开发。

**关键词**: Boto2/Boto3, S3 tests, migration, Boto3



#### **2. Admin REST API 贡献（Bloomberg）**  
**关键讨论**:  
- **贡献内容**: Nick（Bloomberg）提交了针对账户管理的 Admin REST API 修改。  
- **测试需求**: 通过 `Toothology` 验证，当前测试脚本仅在此环境运行。  
- **标签问题**: `needs QA` 标签可能导致延迟，建议直接手动验证。  

**后续行动**: Bloomberg 团队协调手动测试并反馈结果；Yehuda 协助迭代修改（如需）。  

**关键词**: Admin REST API, Bloomberg, Toothology, needs QA



#### **3. Copy Object 加密功能更新**  
**关键进展**: 
- **最新状态**: 代码已重构并 rebase，准备移除 `DNM`/`Draft` 标签，进入合并评审阶段。
- **支持承诺**: Yehuda 协助推送至 FCI 并触发测试。

**后续行动**: Yehuda 提交代码并通知测试团队；测试团队运行 `Toothology` 回归测试。

**关键词**: Copy Object encryption, rebasing, FCI, Toothology



#### **其他事项**  
- **Java SDK 测试**: 现有 Java S3 测试仓库未维护，但部分用例依赖 Java SDK，未来可考虑整合。  

**关键词**: Java SDK, S3 tests



**会议结束**  
**下次会议待定**  
**参与人**: Yehuda, Bloomberg 团队代表等

**注**: 请各负责人更新行动项进展至相关 issue/PR。