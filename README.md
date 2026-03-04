# Automotive APQP Agent

> AI Agent framework for automotive parts supplier APQP management.
> 面向汽车零部件厂商的 APQP 全流程 AI Agent 框架。

## 当前阶段

**聚焦：报价前阶段（Pre-Quotation Phase）**

从 RFQ 接收到报价包输出的完整 AI 辅助流程，涵盖：
- RFQ 解读与客户需求分析
- 技术可行性 / DFM 评估
- 初步工艺路线规划
- 成本分解估算（CBS）
- 三维风险矩阵评估
- 内部 Gate Review 门控
- 报价包输出

## 路线图

- [ ] Phase 0：报价前阶段（Pre-Quotation） ← **当前**
- [ ] Phase 1：产品设计开发（Product Design & Development）
- [ ] Phase 2：过程设计开发（Process Design & Development）
- [ ] Phase 3：产品和过程验证（Product & Process Validation）
- [ ] Phase 4：量产反馈与持续改进（Launch & Continuous Improvement）

## 项目结构

```
automotive-apqp-agent/
├── docs/                    # 项目文档与规划
│   ├── architecture/        # 架构设计
│   ├── research/            # 调研与参考资料
│   └── decisions/           # 架构决策记录（ADR）
├── src/
│   ├── agents/              # Agent 角色定义（YAML）
│   ├── workflows/           # 工作流定义
│   │   ├── 0-rfq-intake/
│   │   ├── 1-feasibility/
│   │   ├── 2-costing/
│   │   └── 3-risk-quotation/
│   ├── templates/           # 文档输出模板
│   └── knowledge/           # 领域知识库
│       ├── oem/             # 各 OEM 特殊要求
│       ├── component/       # 零部件类型经验
│       ├── combo/           # OEM × 零部件组合经验
│       └── standards/       # 行业标准摘要（IATF/AIAG）
└── .claude/
    └── skills/              # Claude Code 技能定义
```

## 框架参考

本项目架构借鉴 [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) 的 Agent/Workflow/Module 设计模式，结合 APQP 汽车行业规范（IATF 16949、AIAG APQP Manual）进行垂直化设计。

## License

MIT
