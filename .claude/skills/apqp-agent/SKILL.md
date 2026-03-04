---
name: apqp-agent
description: "APQP报价前阶段多Agent工作流。4个Agent按阶段串行执行：文档解析→需求分析→评估支持→交付物生成，最终Gate Review。三层HALT保护确保每步用户确认。触发词：报价准备、APQP、RFQ、询价、报价前、Phase 0、客户文件包、TDR、OEM文件。"
---

读取 `src/workflows/main-flow.md` 并按其指示执行完整工作流。

知识库位于 `src/knowledge/`，共享规则位于 `src/rules/`，检查清单位于 `src/checklist/`，Agent 定义位于 `src/agents/`。
