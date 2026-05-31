---
title: Ceph RGW Refactoring Meeting 2025-10-22
date: 2025-10-23
updated: 2025-10-23
tags:
- Ceph
- RGW
categories: 
- "视频总结"
subtitle: Ceph_RGW_Refactoring_Meeting_2025-10-22
---

### Ceph 社区会议纪要  
**日期**: 2025-10-22  
**参会人员**: Nicholas, Casey, Dan 等  

#### 1. **PR 合并进展（Nicholas）**  
- Nicholas 提交的 PR 在 `RJWS singleton` 子套件测试和本地 `tutology` 测试中均通过，但在 rebase 到 `main` 分支后，部分无关测试失败。
- 讨论了测试失败的原因可能与 `RADOSGW (RGW) admin` 测试的长期问题有关，可能是 `usage show` 输出变更导致的。
- 决定合并 PR，因为早期分支测试通过且风险可控。
- 后续行动包括：Casey 将创建 tracker issue，优化测试用例抽象以支持本地和 `tutology` 模式；Nicholas 需在 PR 中补充成功测试的截图证明。

#### 2. **AI 生成代码政策讨论（Dan）**  
- IBM 新政策允许在开源项目中使用 AI 生成代码，但需满足特定条件，如标注生成代码、使用特定模型。
- 对于非 IBM 拥有的项目（如 Ceph），需由社区决定是否允许此类贡献。
- Dan 计划在 Ceph Steering Committee 上推动讨论，由基金会最终决策。
- 社区需明确是否要求贡献者声明 AI 生成代码。

#### 3. **其他事项**  
- 下周会议取消，因 Sephlacon 会议冲突。

#### **行动计划总结**  
| 责任人 | 任务 | 时间节点 |
|--||-|
| Casey  | 合并 Nicholas 的 PR | 立即 |
| Casey  | 创建测试优化 tracker issue | 本周内 |
| Dan    | 在 Steering Committee 提交 AI 政策讨论 | Sephlacon 之后 |
| 全体   | 审阅 AI 生成代码政策提案 | 待基金会安排 |

