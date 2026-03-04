# ADR-001: 框架选型 — 借鉴 BMAD-METHOD 而非 Fork

- **日期**: 2026-03-03
- **状态**: 已决定

## 背景

构建汽车零部件厂商 APQP 管理 Agent 框架，需要决定是从零构建、Fork BMAD-METHOD，还是借鉴其设计模式。

## 决定

**借鉴 BMAD-METHOD 的设计模式，不 Fork 代码，从头构建领域专属框架。**

## 理由

| 维度 | Fork BMAD | 借鉴设计模式 |
|------|-----------|------------|
| 领域知识 | 需大量删改软件开发内容 | 从零注入 APQP 领域知识 |
| 合规约束 | 无强制 Gate 机制，改造复杂 | 自行设计 Go/No-Go 节点 |
| 数据结构 | BMAD 是 Markdown 为主 | 可设计结构化 CBS/BOM 模板 |
| 维护成本 | 跟随 BMAD 版本升级 | 完全自主控制 |
| 启动速度 | 快（有现成框架） | 慢（需从头设计） |

**权衡**：APQP 领域差异过大，Fork 后改造量不亚于重写，且背负原有框架的技术债。

## 借鉴内容

- YAML 格式的 Agent 定义结构
- workflow.yaml + steps/ + templates/ 的工作流组织方式
- 三层知识库（OEM / Component / Combo）— 已在现有 APQP Skill 中实现
- Diataxis 文档框架（Tutorials / How-To / Explanation / Reference）
