# APQP Agent 设计草案 — 报价前阶段

> 状态：草稿（2026-03-03）
> 阶段：设计讨论，尚未实现

## Agent 清单

| Agent | 角色名 | 图标 | 核心职责 | 触发器 |
|-------|--------|------|---------|--------|
| RFQ Analyst | 需求分析师 | 📋 | RFQ 解读、客户需求识别、CSR 检查 | `RR`（RFQ Review） |
| Application Engineer | 应用工程师 | 🔧 | 技术可行性、DFM 分析、图纸解读 | `TF`（Tech Feasibility） |
| Process Engineer | 工艺工程师 | ⚙️ | 初步工艺路线、产能初评 | `PR`（Process Route） |
| Cost Engineer | 成本工程师 | 💰 | 材料/加工/模具成本估算（CBS） | `CE`（Cost Estimate） |
| Quality Engineer | 质量工程师 | ✅ | 初步风险评估、质量计划框架 | `QR`（Quality Risk） |
| Program Manager | 项目经理 | 🎯 | 时间节点、Gate 评审主持、报价审批 | `GR`（Gate Review） |

## 工作流结构

```
src/workflows/
├── 0-rfq-intake/
│   ├── rfq-review/           # RFQ 需求解读（几何/材料/量纲/标准）
│   └── customer-csr-check/   # 客户特殊要求（CSR）识别
├── 1-feasibility/
│   ├── technical-dfm/        # 技术可行性 + DFM 分析
│   ├── process-routing/      # 初步工艺路线
│   └── capacity-check/       # 产能初评
├── 2-costing/
│   ├── material-cost/        # 材料成本
│   ├── process-cost/         # 加工成本（人工 + 制造费）
│   ├── tooling-cost/         # 模具 / 工装成本
│   └── cbs-summary/          # CBS 汇总输出
├── 3-risk-quotation/
│   ├── risk-matrix/          # 三维风险矩阵（技术/商务/质量）
│   ├── gate-review/          # 内部 Gate Review（Go/No-Go/条件Go）
│   └── quotation-package/    # 报价包最终输出
└── quick-flow/
    └── simple-rfq/           # C 类项目快速通道（精简版）
```

## 知识库结构

```
src/knowledge/
├── oem/                      # 整车厂（客户）知识
│   ├── _oem-template.md
│   └── stellantis.md         # 示例
├── component/                # 零部件类型知识
│   ├── _component-template.md
│   └── diesel-filter.md      # 示例
├── combo/                    # OEM × 零部件组合经验
│   └── stellantis--diesel-filter.md
└── standards/                # 行业标准摘要
    ├── iatf-16949.md
    ├── aiag-apqp-manual.md
    └── oem-specific/         # OEM 内部标准
```

## 关键设计决策

### 1. 强制 Gate Review 机制

与 BMAD（建议型）不同，APQP 需要显式 Gate 节点：

```yaml
# gate-review/workflow.yaml 示意
gate:
  inputs_required:
    - technical-feasibility-report
    - cbs-summary
    - risk-matrix
  decision:
    options: [Go, No-Go, 条件Go]
  blockers:
    - 技术可行性未确认
    - CBS 未完成
```

### 2. 结构化输出模板

成本分解、风险矩阵等需要半结构化模板，而非自由 Markdown。

### 3. OEM 差异化配置

通过 `module.yaml` 承载不同 OEM 要求：
- Stellantis：双文档模式（PF.xxxxx + CTS）
- VW：Lastenheft 格式
- Toyota：TSH/TSM 体系

## 待决问题

- [ ] Agent 之间的协作机制（是否需要 Party Mode 类似功能）
- [ ] 结构化数据（BOM、CBS）的存储格式（YAML / CSV / JSON）
- [ ] 报价包输出格式（Markdown → Word/PDF 的转换需求）
- [ ] 与现有 APQP Skill（已有知识库）的集成方式
