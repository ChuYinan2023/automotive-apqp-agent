# BMAD-METHOD 框架借鉴分析

> 来源：对 BMAD-METHOD v6.0.4 的深度分析（2026-03-03）
> 用途：评估其 Agent/Workflow/Skill 架构用于 APQP 垂直领域的可行性

## 结论

**框架思路 80% 适用，但领域知识体系需从头构建。**
建议以 BMAD 为设计蓝图，不 fork 代码。

---

## BMAD-METHOD 核心架构

### 四层架构

| 层 | 实现方式 | 文件格式 |
|----|---------|---------|
| **Agent** | 专业角色人格 + 触发器 + 约束 | YAML |
| **Workflow** | 阶段化步骤 + 模板输出 | YAML + Markdown |
| **Module** | 可配置参数（客户/语言/目录） | YAML |
| **Skill** | 独立工具（.claude/skills/） | Markdown |

### Agent YAML 结构参考

```yaml
name: Application Engineer
persona:
  name: Alex
  icon: 🔧
  style: 技术严谨，量化表达，结论导向
triggers:
  TF: 技术可行性分析
  DFM: DFM 风险评估
  DR: 图纸审查
constraints:
  - 必须基于客户图纸和技术规范
  - 必须输出量化的可行性结论（Go/No-Go/条件Go）
workflows:
  - technical-feasibility
  - dfm-analysis
```

### 工作流文件结构

```
workflow-name/
├── workflow.yaml    # 元数据：触发器、阶段、描述
├── steps/           # 步骤 Markdown（含 AI 提示词）
├── templates/       # 输出文档模板
└── data/            # 引用数据
```

---

## 适用性评估

### ✅ 可直接借鉴

| 能力 | BMAD 实现 | APQP 用途 |
|------|-----------|----------|
| Agent 角色定义 | YAML 人格 + 触发器 + 约束 | 定义 RFQ 分析师、应用工程师、成本工程师等 |
| 阶段化工作流 | workflow.yaml + steps/ | 完美映射 APQP 四阶段 + Gate Review |
| 模板输出 | templates/ 目录 | 可行性表、CBS、风险矩阵、报价单 |
| 模块配置 | module.yaml | 承载不同 OEM 的 CSR 差异配置 |
| Skill 系统 | .claude/skills/ | 承载 APQP 专用工具 |

### ❌ 需重新设计

| 问题 | 原因 | 解决方向 |
|------|------|---------|
| 领域知识体系 | BMAD 内嵌软件开发知识 | 嵌入 IATF 16949、AIAG APQP、各 OEM CSR |
| 结构化数据 | BMAD 处理非结构化 Markdown | 设计半结构化模板（BOM/CBS/风险矩阵） |
| 强制门控 | BMAD 是建议型 | 工作流中显式定义 Go/No-Go 节点 |
| 合规约束 | 无强制性 | APQP 部分步骤为强制，不可跳过 |

---

## BMAD Agent 到 APQP Agent 的映射

| BMAD 角色 | APQP 对应角色 |
|-----------|-------------|
| Analyst (Mary) | RFQ 分析师（客户需求、CSR 识别） |
| Architect (Winston) | 应用工程师（技术可行性、DFM） |
| Developer (Amelia) | 制造 / 工艺工程师 |
| QA Engineer (Quinn) | 质量工程师 / APQP Coordinator |
| Product Manager (John) | 项目工程师 / Program Manager |
| Scrum Master (Bob) | Gate Review 协调员 |

---

## APQP 阶段 vs BMAD Phase 映射

```
BMAD Phase            →    APQP Pre-Quotation 映射
─────────────────────────────────────────────────
Phase 1: Analysis      →   RFQ 解读 & 客户需求分析
Phase 2: Planning      →   技术可行性 & 初步工艺规划
Phase 3: Solutioning   →   成本估算 & 风险评估
Phase 4: Implementation→   报价包输出 & 内部审批 Gate
```

---

## BMAD-METHOD 项目数据（参考）

- 版本：v6.0.4
- Agent 数量：9 个
- 工作流数量：34+
- 代码规模：233 文件，36,636 行
- 格式：YAML + Markdown
- 文档框架：Diataxis（Tutorials / How-To / Explanation / Reference）
- 支持 IDE：Claude Code、Cursor、Copilot、CodeBuddy 等 6 种
