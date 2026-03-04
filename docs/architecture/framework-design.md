# APQP 报价前阶段 — 多 Agent 框架整体设计

## Context

现有单体 Skill（`APQP/.claude/skills/apqp-quotation/skill.md`）已能跑通报价前文件处理流程，但存在三个局限：
1. 单一 AI 角色，无法体现多角色协作的业务节奏
2. 可行性评估只是文档对比，缺少结构化的人机决策支持
3. 交付物之间无依赖约束，一致性靠末尾检查兜底

新框架将现有 Skill 的能力拆散到 5 个工具型 Agent 中，核心定位不变：**帮人整理信息、降低遗漏，不替人做工程判断**。

不设独立协调 Agent，用 workflow 文件（main-flow.md）直接编排各 Agent 的执行顺序。

---

## 一、Agent 详细定义

### Agent 1：📋 文档解析 Agent（Doc Parser）

**定位**：所有后续工作的数据源头。把客户发来的一堆文件变成结构化信息。

**输入**：
- 用户指定的客户文件目录（PDF/DOCX/XLSX/PPTX 混合）
- `knowledge/oem/{oem}.md`（自动匹配或首次创建）
- `knowledge/component/{type}.md`（自动匹配或用 fallback）

**执行步骤**：
1. 读取全部文件 + 嵌入检测（对应现有 A1）
2. 递归嵌入提取，最多 3 层（对应 A1b）
3. OEM 自动识别（对应 A2）
4. 文件角色分类（6 类）（对应 A3）
5. 结构化数据提取（零件号/BOM/性能指标/测试矩阵/引用规范/时间节点）（对应 A4）
6. 客户模板检测（对应 A5）

**输出**：
- `out/_嵌入文件/` — 递归提取的所有嵌入文件（重命名后）
- `out/README.md` — 结构化分析报告（后续所有 Agent 的核心数据源）
- `out/文件清单.md` — 全部文件的角色分类表
- `out/客户模板清单.md` — 检测到的客户模板 + 对应交付物编号

**人工确认点**：展示分析摘要，问"分析结果对吗？有遗漏或错误吗？"

**共享规则引用**：无（本 Agent 自包含）

---

### Agent 2：🔍 需求分析 Agent（Requirement Analyzer）

**定位**：从已解析的文档中提取"客户到底要什么"——缺什么、有什么特殊要求、质量目标是多少。

**输入**：
- `out/README.md`（来自文档解析 Agent）
- `out/文件清单.md`
- `knowledge/component/{type}.md`（常见缺口章节）

**执行步骤**：
1. **完整性检查**（对应现有 B1）
   - 从 README 的引用规范清单逐条核对文件包
   - 按 4 级紧急度分类（最高/高/中/低）
   - 标注每项缺失的获取来源（向客户要/自行购买/内部收集）
2. **特殊特性提取**（对应现有 B2 前半）
   - CC（Critical）：影响安全/法规
   - SC（Significant）：影响功能/耐久
   - 每项标注：规范要求值、来源章节、验证方法、控制方法建议
3. **质量目标提取**（对应现有 B2 后半）
   - 市场故障率/PPM、可靠性指标、过程能力、清洁度、安全法规

**输出**：
- `out/缺失项跟踪表.xlsx`
- `out/特殊特性清单.xlsx`
- `out/质量目标表.xlsx`

**人工确认点**：
- 完整性检查后：展示缺失项汇总，确认优先级分类
- 特性提取后：展示 CC/SC 清单，确认是否遗漏

**共享规则引用**：`rules/excel-style.md`

---

### Agent 3：📊 评估支持 Agent（Assessment Support）

**定位**：把客户要求和公司能力放在一起对比，汇总风险项，**供人做决策**。不做工程判断。

**输入**：
- `out/README.md`
- `out/特殊特性清单.xlsx`
- `out/质量目标表.xlsx`
- `company-profile/能力声明.xlsx`（可选）
- `knowledge/component/{type}.md`（常见缺口 + OEM 特有要求章节）
- `knowledge/combo/{oem}--{type}.md`（历史项目经验，如有）

**执行步骤**：
1. **能力对比**（对应现有 B3）
   - 有能力声明 → 逐条对比，判定 ✅/❌/🔵
   - 无能力声明 → 输出空模板，等用户填写后再对比
2. **历史经验匹配**（新增）
   - 从 combo 知识库匹配同 OEM + 同类零件的历史项目
   - 提示"上次这个组合的常见问题是 XXX"
3. **风险项汇总**（新增）
   - 技术风险：从特殊特性 + 能力对比中提取
   - 商务风险：从缺失项 + 时间约束中提取
   - 质量风险：从质量目标 + 能力对比中提取
   - 每项风险标注严重度，但**不做 Go/No-Go 判断**（那是人的事）

**输出**：
- `out/例外事项清单.xlsx`
- `out/风险提示清单.md`（结构化列表，供 Gate Review 使用）
- 路径 B 额外：`out/能力声明模板.xlsx`

**人工确认点**：
- 展示例外项 + 风险提示
- 提示人做决策：哪些例外可接受？需要什么替代方案？
- **这里是人做工程判断的核心环节**（DFM 可行吗？工艺走哪条？成本能接受吗？）

**共享规则引用**：`rules/excel-style.md`

---

### Agent 4：📝 交付物生成 Agent（Deliverable Generator）

**定位**：按人确认的结论 + 模板优先级规则，生成全套报价交付物。

**输入**：
- `out/README.md`（核心数据源）
- `out/客户模板清单.md`（决定用客户模板还是自建）
- `out/特殊特性清单.xlsx`、`out/质量目标表.xlsx`、`out/例外事项清单.xlsx`
- `out/_嵌入文件/` 中的客户模板（如有）
- `company-profile/`（SDT 团队表、成本费率）
- 人在评估支持阶段的决策结论

**执行步骤**：
1. 确定交付物清单（从客户 TDR 提取，或问用户）
2. 按**依赖顺序**逐个生成（见下方依赖图）
3. 每个交付物生成前检查模板优先级（铁律）
4. 每个交付物生成后等用户确认
5. 全部完成后执行**最终一致性检查**（8 项）
6. 检查通过后**触发知识回写**

**交付物依赖顺序**：
```
无依赖（可并行）:
  Q3 团队表
  Q6 补充材料清单
  A5 特殊特性清单（已有，可重新生成）
  A6 质量目标表（已有，可重新生成）
  MIS 缺失项跟踪表（已有，可重新生成）

依赖 README BOM:
  Q1 成本分解

依赖 Q3:
  Q5 职责分配矩阵（RASI）

依赖 A5:
  Q4 例外事项清单（已有，可重新生成）

依赖 README:
  L1 工程特性清单

依赖 L1:
  L2 零部件特性清单
  Q2 开发计划表

依赖 L1 + L2:
  QFD 质量屋矩阵
```

**输出**：
- `out/{交付物名}.xlsx` — 全套交付物
- `out/最终检查报告.md` — 一致性检查结果

**人工确认点**：每个交付物生成后确认

**共享规则引用**：
- `rules/excel-style.md`（Excel 样式）
- `rules/template-priority.md`（模板优先级铁律）
- `rules/deliverable-order.md`（交付物依赖顺序）
- `checklist/final-consistency.md`（最终一致性检查 8 项）

---

---

## 二、HALT 机制

在 Claude Code 环境里没有代码级的流程控制，HALT 靠 prompt 指令实现。为了防止单层 HALT 被 LLM 在长上下文中忽略，采用**三层 HALT 保护**：

### 第一层：Agent 定义文件内的 HALT

每个 Agent 定义文件的**头部**和**尾部**都写明 HALT 条件。

**头部（前置检查）**：
```markdown
## 前置检查

🛑 **HALT — 以下文件必须存在，否则禁止执行本 Agent：**

- [ ] `out/README.md` 存在且内容非空
- [ ] 用户已确认上一阶段结果

**如果任何一项不满足，立即停止并告知用户原因。不得跳过。**
```

**尾部（完成检查）**：
```markdown
## 完成检查

🛑 **HALT — 以下条件全部满足后，才可告知用户本阶段完成：**

- [ ] 所有产出文件已写入 `out/`
- [ ] 已向用户展示本阶段摘要
- [ ] 用户已明确回复确认（"OK"/"确认"/"继续"等肯定表达）

**未收到用户确认前，禁止执行下一阶段。不得自行跳过等待。**
```

### 第二层：Workflow 主流程中的 HALT

`main-flow.md` 在每个阶段转换处设置 HALT：

```markdown
## Step 2: 需求分析

### 前置检查
🛑 **HALT — 确认以下条件全部满足：**
- [ ] `out/README.md` 存在
- [ ] `out/文件清单.md` 存在
- [ ] 用户已确认文档解析结果

**任何一项不满足 → 停止，提示用户需先完成 Step 1。**

### 执行
加载 `agents/req-analyzer.md` 并按其步骤执行。

### 完成检查
🛑 **HALT — 等待用户确认特性提取结果后，才可进入 Step 3。**
```

### 第三层：独立 Checklist 文件中的 HALT

`checklist/final-consistency.md` 作为独立文件被交付物生成 Agent 加载执行：

```markdown
## 执行规则

🛑 **逐条检查，每条必须明确判定 PASS 或 FAIL。**
🛑 **任何一条 FAIL → 停止 → 输出失败项 → 等用户决定修复方案 → 修复后重新检查。**
🛑 **不得跳过任何检查项。不得将未验证项标为 PASS。**
🛑 **全部 PASS 之前，禁止触发知识回写。**

### 检查项

- [ ] 1. 数字一致性 — PASS / FAIL
      特殊特性值 = 例外事项引用值 = 补充材料验收标准
- [ ] 2. 特性覆盖 — PASS / FAIL
      每项 CC/SC 在例外事项清单都有对应行
- [ ] 3. 人员一致 — PASS / FAIL
      团队表人名 = 职责分配矩阵（RASI）列头
- [ ] 4. 测试覆盖 — PASS / FAIL
      补充材料测试项覆盖所有需验证的特性
- [ ] 5. BOM 一致 — PASS / FAIL
      成本分解 BOM = README 中提取的 BOM
- [ ] 6. 模板合规 — PASS / FAIL
      发现客户模板的交付物是否使用了客户模板格式
- [ ] 7. 嵌入完整性 — PASS / FAIL
      递归提取层级统计，确认无遗漏
- [ ] 8. 缺失项状态 — PASS / FAIL
      所有"最高"优先级缺失项已有处理方案
```

### 知识回写的 HALT

`rules/knowledge-writeback.md` 末尾设置独立 HALT：

```markdown
## 回写完成检查

🛑 **HALT — 以下条件全部满足后，项目才可标记为完成：**

- [ ] OEM 知识文件已创建或更新（`knowledge/oem/{oem}.md` 有 diff）
- [ ] 零部件知识文件已创建或更新（`knowledge/component/{type}.md` 有 diff）
- [ ] combo 知识文件已创建或更新（`knowledge/combo/{oem}--{type}.md` 有 diff）
- [ ] 三个文件均不含项目特有数据（零件号、具体日期、具体人名）
- [ ] 三个文件的内容可直接用于下次同类项目

**知识回写未完成 → 禁止关闭项目。必须完成回写。**
```

### HALT 触发点汇总

| 位置 | 条件 | 后果 |
|------|------|------|
| 文档解析 → 需求分析 | README.md 不存在或用户未确认 | 不加载 req-analyzer.md |
| 需求分析 → 评估支持 | 特性清单不存在或用户未确认 | 不加载 assessment.md |
| 评估支持 → 交付物生成 | 例外事项不存在或用户未做决策 | 不加载 deliverable-gen.md |
| 交付物全部生成后 | 一致性检查任何一项 FAIL | 不触发知识回写 |
| 知识回写后 | 知识文件无 diff | 不关闭项目 |

---

## 三、Workflow 设计

不设独立协调 Agent。`main-flow.md` 直接编排 4 个业务 Agent 的执行顺序，同时承担项目初始化、Gate Review 组织、进度跟踪的职责。

### 主流程（main-flow.md）

```markdown
# APQP 报价前阶段 — 主工作流

## 项目初始化
1. 用户提供客户文件目录
2. 创建 `{目录}/out/` 输出目录
3. 搜索 company-profile/（三级路径）
4. 预加载知识库（OEM 待识别，零件类型待识别）

## Step 1: 文档解析
🛑 前置：用户已提供文件目录
加载 agents/doc-parser.md 执行
🛑 完成：README.md + 嵌入文件 + 文件清单 + 模板清单 已输出，用户已确认

## Step 2: 需求分析
🛑 前置：Step 1 产出文件存在 + 用户已确认
加载 agents/req-analyzer.md 执行
🛑 完成：缺失项 + 特殊特性 + 质量目标 已输出，用户已确认

## Step 3: 评估支持
🛑 前置：Step 2 产出文件存在 + 用户已确认
加载 agents/assessment.md 执行
🛑 完成：例外事项 + 风险提示 已输出，用户已做工程判断

## Step 4: 交付物生成
🛑 前置：Step 3 产出文件存在 + 用户决策结论已记录
加载 agents/deliverable-gen.md 执行
  → 按 rules/deliverable-order.md 的依赖顺序生成
  → 加载 checklist/final-consistency.md 逐条检查
  → 🛑 全部 PASS 后加载 rules/knowledge-writeback.md 执行回写
🛑 完成：全套交付物 + 检查报告 + 知识回写 已完成

## Step 5: Gate Review
加载 checklist/gate-review.md
汇总 Step 1-4 所有产出，整理 Gate Review 纪要
输出：out/Gate-Review纪要.md
用户决策：Go / No-Go / 条件 Go
```

### 各阶段之间的数据流

```
文档解析 ──produces──→ README.md (核心数据源，后续所有 Agent 读这个)
         ──produces──→ _嵌入文件/
         ──produces──→ 文件清单.md
         ──produces──→ 客户模板清单.md

需求分析 ──requires──→ README.md
         ──produces──→ 缺失项跟踪表.xlsx
         ──produces──→ 特殊特性清单.xlsx
         ──produces──→ 质量目标表.xlsx

评估支持 ──requires──→ README.md + 特殊特性 + 质量目标
         ──optional──→ company-profile/
         ──optional──→ knowledge/combo/
         ──produces──→ 例外事项清单.xlsx
         ──produces──→ 风险提示清单.md

交付物   ──requires──→ 以上全部产出 + 人的决策结论
         ──produces──→ Q1~Q6, L1, L2, QFD 等
         ──produces──→ 最终检查报告.md
         ──triggers──→ 知识回写
```

### 关于并行

4 个业务 Agent 是**串行**的（每个等人确认后才进下一步），这是有意为之：
- 需求分析依赖文档解析的 README
- 评估支持依赖需求分析的特性清单
- 交付物生成依赖评估支持的例外事项 + 人的决策

**阶段内**的并行（如 B1 完整性检查和 B2 特性提取可以同时做）由各 Agent 内部自行安排。

---

## 三、知识库设计

### 目录结构

```
knowledge/
├── oem/                          # OEM 知识（已有，直接复用）
│   ├── _oem-template.md
│   ├── stellantis.md             # ✅ 已有
│   └── {其他OEM}.md
├── component/                    # 零部件类型知识（已有，直接复用）
│   ├── _component-template.md
│   ├── _generic-fallback.md
│   ├── fuel-line.md              # ✅ 已有
│   └── {其他类型}.md
├── combo/                        # OEM × 零件 组合经验（新增）
│   ├── _combo-template.md
│   └── {oem}--{type}.md
└── standards/                    # 行业标准摘要（新增，可选）
    ├── iatf-16949.md
    └── aiag-apqp-manual.md
```

### 现有知识文件的复用

`oem/` 和 `component/` 下的文件**格式和内容完全不变**，直接从现有 Skill 复制过来。知识回写规则也保持一致。

### combo/ 层的定位

记录**特定 OEM + 特定零件类型**组合的项目经验，是 oem/ 和 component/ 的交叉补充。

**combo 模板结构**：
```markdown
# 组合经验：{OEM} × {零部件类型}

## 项目历史摘要
- 累计处理次数
- 最近一次处理日期

## 文档组合模式
（该 OEM 发这类零件的 RFQ 时，文件包通常长什么样）

## 典型例外项
（这个组合下反复出现的例外事项）

## 成本参考范围
（脱敏后的量级参考，如"材料占比通常 35-40%"）

## 历史踩坑记录
（这个组合特有的问题）
```

**回写时机**：与 oem/ 和 component/ 一起，在最终一致性检查通过后回写。

**回写原则**：只记录可复用经验，不记录项目特有数据（零件号、人名、日期等）。

### standards/ 层的定位

IATF 16949、AIAG APQP Manual 等行业标准的**摘要**，供 Agent 快速查阅。这些内容相对稳定，不需要回写。

MVP 阶段可暂不填充，Agent 靠自身知识 + oem/component 知识库即可工作。

---

## 四、共享规则文件

从现有 Skill 中抽出，供多个 Agent 共同遵守的规则：

```
rules/
├── excel-style.md              # Excel 生成规则（字体/颜色/边框/冻结）
├── template-priority.md        # 模板优先级铁律（客户模板 > 自建）
├── deliverable-order.md        # 交付物依赖顺序约束
└── knowledge-writeback.md      # 知识回写规则

checklist/
├── final-consistency.md        # 最终一致性检查 8 项（独立文件，不塞在 Agent 定义里）
└── gate-review.md              # Gate Review 检查项清单
```

---

## 五、项目目录结构（最终）

```
automotive-apqp-agent/
├── .claude/
│   └── skills/                   # 入口 Skill 定义
│       └── apqp-agent/
│           └── SKILL.md          # 触发入口
├── src/
│   ├── agents/                   # 4 个 Agent 定义（.md 格式）
│   │   ├── doc-parser.md         # 📋 文档解析
│   │   ├── req-analyzer.md       # 🔍 需求分析
│   │   ├── assessment.md         # 📊 评估支持
│   │   └── deliverable-gen.md    # 📝 交付物生成
│   ├── workflows/                # 工作流定义
│   │   ├── main-flow.md          # 主流程（串行 5 Agent）
│   │   └── quick-flow.md         # C 类项目快速通道
│   ├── rules/                    # 共享规则
│   │   ├── excel-style.md
│   │   ├── template-priority.md
│   │   ├── deliverable-order.md
│   │   └── knowledge-writeback.md
│   ├── checklist/                # 独立检查清单
│   │   ├── final-consistency.md
│   │   └── gate-review.md
│   ├── templates/                # 输出文档模板（combo 模板等）
│   │   └── _combo-template.md
│   └── knowledge/                # 领域知识库（从现有 Skill 复制）
│       ├── oem/
│       │   ├── _oem-template.md
│       │   └── stellantis.md
│       ├── component/
│       │   ├── _component-template.md
│       │   ├── _generic-fallback.md
│       │   └── fuel-line.md
│       ├── combo/
│       │   └── _combo-template.md
│       └── standards/
├── docs/                         # 项目文档（保留现有）
│   ├── architecture/
│   ├── research/
│   └── decisions/
└── README.md
```

---

## 六、实现顺序

1. **搭建目录结构** — 创建 agents/、rules/、checklist/、workflows/ 等目录
2. **写共享规则和 checklist** — excel-style、template-priority、deliverable-order、knowledge-writeback、final-consistency、gate-review
3. **写 Agent 定义** — 按顺序：doc-parser → req-analyzer → assessment → deliverable-gen
4. **写主工作流** — main-flow.md 串联 4 个 Agent，含三层 HALT
5. **写入口 Skill** — SKILL.md 作为 Claude Code 的触发入口
6. **验证** — 用 Stellantis fuel-line 的实际文件包跑一遍
