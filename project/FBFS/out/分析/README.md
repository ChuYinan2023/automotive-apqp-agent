# 结构化分析报告 — FBFS / Stellantis KP1 燃油供给管路

> 生成时间：2026-03-10 | 版本：V1.0

---

## 1. 项目基本信息

| 字段 | 内容 |
|------|------|
| OEM | Stellantis（原 FCA / Fiat Group） |
| 项目代号 | KP1 A&B |
| 零件号 | FC00SAA78530 |
| 零件名称 | Fuel Supply Line（供油管路）— 滤清器至发动机 |
| 零件类型 | 燃油管路束（Fuel Bundle） |
| 发动机/平台 | 2.2 Diesel Engine（最终版本） |
| 包含 DEF 管路 | 是（SSTS Product Description 中提及 DEF Line Assy — Middle） |
| 供应商集成等级 | Level 2（according to RASI 附件） |
| TDR 版本 | Rev.00，2022-03-09 |
| CTS 版本 | Rev.00，2022-03-09 |
| 文件包发布方 | Stellantis ENGINE SYSTEMS / Fuel System 部门 |

---

## 2. 文件角色分类

→ 详见 `文件清单.md`

---

## 3. BOM 结构

基于 CTS + 知识库推断（客户未提供完整 BOM 图纸）：

```
KP1 Fuel Line Assembly
├── Fuel Supply Line（供油管，滤清器→发动机）
│   └── Multi/mono-layer Nylon（SAE J2260）
├── DEF Line Assy — Middle（尿素管路中段）
│   └── 加热型（PF.90068 适用）
├── Quick Connectors（快速接头）
│   └── 金属材质，二次锁止，PF.90298 / SAE J2044
├── Metallic Pipe（金属管段）
│   └── 电焊钢管 9.02145/02，内镀镍（CTS 明确要求）
├── Protection Caps（保护帽）
│   └── 所有管端，参见 L2_CTS_OLE3.pdf 要求
└── Clips & Sleeves（卡扣 + 防磨套）
    └── CS.00050 + PF.90271
```

---

## 4. 性能指标摘要

→ 详见 Agent 2 `特殊特性清单.xlsx` 和 `质量目标表.xlsx`

核心指标概要：

| 类别 | 参数 | 要求值 | 来源 |
|------|------|--------|------|
| 设计寿命 | 整车寿命 | 15年 / 150,000英里 | PF.90197 §1.1 |
| 工作温度（管材，连续） | 最高 | 90°C ± 2°C | PF.90197 §5.2 |
| 工作温度（管材，短期30min） | 最高 | 115°C ± 2°C | PF.90197 §5.2 |
| 工作温度（燃油，连续） | 最高 | 90°C ± 2°C | PF.90197 §5.2 |
| 工作温度（燃油，短期30min） | 最高 | 105°C ± 2°C | PF.90197 §5.2 |
| 爆破压力（常温） | ≥ | 8× 系统工作压力 | PF.90197 §7.4 |
| 爆破压力（115°C） | ≥ | 3× 系统工作压力 | PF.90197 §7.4 |
| 泄漏检测（液体管） | 测试压力 | ≥ 150 PSI | PF.90197 §7.2 |
| 泄漏检测（蒸汽管） | 测试压力 | ≥ 10 PSI | PF.90197 §7.2 |
| 虚拟泄漏直径（液体管） | 检测能力 | ≤15μm × 3mm VLD | PF.90197 §7.2 |
| 拉伸强度（新品） | ≥ | 20 N/mm² | PF.90197 §6.2.1 |
| 拉伸强度（燃油浸泡后） | ≥ | 15 N/mm² | PF.90197 §6.2.1 |
| 接头插入力（<11mm管） | ≤ | 67N | PF.90197 §6.2.4 |
| 接头拔脱力（常温，液体管） | ≥ | 450N | PF.90197 §6.3.5 |
| 接头拔脱力（115°C，液体管） | ≥ | 115N | PF.90197 §6.3.5 |
| 卡扣装配力（两指） | ≤ | 20N | PF.90197 §6.3.4 |
| 卡扣装配力（全手） | ≤ | 40N | PF.90197 §6.3.4 |
| 卡扣拔出力（from vehicle） | ≥ | 100N | PF.90197 §6.3.4 |
| 管路插入卡扣力 | ≤ | 40N（干态） | PF.90197 §6.3.4 |
| 管路拔出卡扣力 | ≥ | 80N（2.5%吸湿后） | PF.90197 §6.3.4 |
| 脉冲耐久（常规Stop/Start） | 300,000 cycles | — | PF.90197 §9.5 |
| 脉冲耐久（S/S+Freewheel） | 600,000 cycles | — | PF.90197 §9.5 |
| 振动耐久 | 5样件×60小时 | R95/C90 | PF.90197 §9.4 |
| 清洁度（汽油/蒸汽管） | ≤ | 1.5 mg/dm² | PF.90197 §7.1 |
| 清洁度（柴油滤清器下游A类） | 粒子限制 | <50/15/2/0（4档粒径） | PF.90197 §7.1 |
| NVH（主观评分） | ≥ | 8（10分制） | PF.90197 §6.3.2 |

---

## 5. 测试矩阵概要

| 类别 | 测试项 | DV/PV 样件数 | 验收标准 | 责任方 |
|------|--------|------------|----------|--------|
| 环境 | 化学浸泡（§5.1） | 15/15 | P99C90 | Supplier |
| 环境 | 腐蚀（§5.3） | 15/15 | P99C90 | Supplier |
| 环境 | CaCl2（§5.4，EMEA only） | 15/15 | P99C90 | Supplier |
| 环境 | ZnCl2（§5.5） | 15/15 | P99C90 | Supplier |
| 物理/机械 | 外观（§6.1） | 100%/100% | 全通过 | Supplier |
| 物理/机械 | 材料层（§6.2.2） | 15/15 | P99C90 | Supplier |
| 物理/机械 | 接头插入力（§6.2.4） | 15/15 | P99C90 | Supplier |
| 物理/机械 | 静电耗散（§6.2.5） | 15/15 | P99C90 | Supplier |
| 物理/机械 | NVH（§6.3.2） | 客户定/客户定 | P99C90 | Stellantis |
| 物理/机械 | 卡扣插拔（§6.3.4） | 15/15 | P99C90 | Supplier |
| 物理/机械 | 接头拔脱（§6.3.5） | 15/15 | P99C90 | Supplier |
| 物理/机械 | 内部燃油浸泡（§6.3.6） | 15/15 | P99C90 | Supplier |
| 物理/机械 | 运输尺寸（§6.3.7） | -/15 | P99C90 | Supplier |
| 物理/机械 | 尺寸验证（§6.3.8） | 15/15 | P99C90 | Supplier |
| 物理/机械 | 弯形塑料管完整性（§6.3.9） | 15/15 | P99C90 | Supplier |
| 功能 | 清洁度（§7.1） | 15/15 | P99C90 | Supplier |
| 功能 | 泄漏（§7.2） | 15/15 | P99C90 | Supplier |
| 功能 | 压降/流阻（§7.3） | 15/15 | P99C90 | Supplier |
| 功能 | 爆破（§7.4） | 15/15 | P99C90 | Supplier |
| 安全 | 碰撞 FMVSS301（§8.1） | 客户定/客户定 | 全通过 | Stellantis |
| 安全 | MiniSHED渗透（§8.2，EMEA） | 15/15 | P99C90/R95C90 | Supplier |
| 耐久 | 系统级（§9.1） | 客户定/客户定 | 全通过 | Stellantis |
| 耐久 | 生命周期（§9.3） | 45/45 | R95C90 | Supplier |
| 耐久 | 振动（§9.4） | 45/45 | R95C90 | Supplier |
| 耐久 | 脉冲压力（§9.5） | 45/45 | R95C90 | Supplier |

---

## 6. 引用规范清单

| 规范编号 | 名称 | 来源文件 | 类型 | 是否已有 |
|----------|------|----------|------|---------|
| PF.90197 | Fuel Bundle – Plastic/Rubber/Metallic（Harmonized）| CTS §2.4 | Stellantis | ✅ 已提供 |
| PF.90298 | Quick Connect – Fuel System | CTS §2.4 | Stellantis | ✅ 已提供 |
| PF.90068 | Diesel Exhaust Fluid Heated Supply Lines | SSTS | Stellantis | ✅ 已提供 |
| MS.50017 | Polyamide (Nylon) Thermoplastic | CTS §2.4 | Stellantis | ❌ 未提供 |
| MS.50015 | EPDM/PP Thermoplastic Vulcanizates | CTS §2.4 | Stellantis | ❌ 未提供 |
| CS-9003 | Restricted/Prohibited Substances | CTS §2.4 | Stellantis | ❌ 未提供 |
| CS.00080 | CAD Drawings Rules | CTS §2.4 | Stellantis | ❌ 未提供 |
| CS.00029 | CAD 3DA Documentation | CTS §2.4 | Stellantis | ❌ 未提供 |
| CS.00050 | Wiring Design & Package Requirements | PF.90197 | Stellantis | ❌ 未提供 |
| CS.00251 | Corrosion Requirements | PF.90197 | Stellantis | ❌ 未提供 |
| CS.00265 | Substances of Concern Requirements | PF.90197 | Stellantis | ❌ 未提供 |
| 9.02145/02 | Electrowelded Steel Pipes for Fuel Circuits | CTS §2.4 | Stellantis | ❌ 未提供 |
| 07740 | Qualification Procedure (含 Annex 2 SVP) | CTS §2.4 | Stellantis | ❌ 未提供（模板已提供） |
| QR.00001 / QR-00001 | Global Product Assurance Testing (GPAT) | CTS §2.4 | Stellantis | ❌ 未提供 |
| QR-10012 | Dimensional Quality Requirements | PF.90197 | Stellantis | ❌ 未提供 |
| SD-11597 | Fuel Compatibility List | PF.90197 | Stellantis | ❌ 未提供 |
| SD-M0008/03 | Plastic Fuel Line Requirements / Approvals | PF.90197 | Stellantis | ❌ 未提供 |
| LP.7A004 | Fuel System – Electrostatic Charge | PF.90197 | Stellantis | ❌ 未提供 |
| LP.7A005 | MiniSHED Test Procedure | PF.90197 | Stellantis | ❌ 未提供 |
| LP.7M114 | Polyamide Moisture Conditioning | PF.90197 | Stellantis | ❌ 未提供 |
| PS.50005/06 | Steel Tube Welding | PF.90197 | Stellantis | ❌ 未提供 |
| PF.90271 | Wiring Harness Protection Sleeves | CTS §2.4 | Stellantis | ❌ 未提供 |
| SAE J2044 | Quick Connect Coupling Specification | PF.90197 | SAE（付费） | ❌ 未提供 |
| SAE J2045 | Fuel System Tubing Performance | PF.90197 | SAE（付费） | ❌ 未提供 |
| SAE J2260 | Nonmetallic Fuel Tubing | PF.90197 | SAE（付费） | ❌ 未提供 |
| SAE J1645 | Fuel System Electrostatic Charge | PF.90197 | SAE（付费） | ❌ 未提供 |
| SAE J2027 | Protective Covers for Fuel Tubing | PF.90197 | SAE（付费） | ❌ 未提供 |
| SAE J2334 | Lab Cyclic Corrosion Test | PF.90197 | SAE（付费） | ❌ 未提供 |
| SAE J400 | Chip Resistance Test | PF.90197 | SAE（付费） | ❌ 未提供 |
| DIN 51604 | FAM Test Fluid | PF.90197 | DIN | ❌ 未提供 |
| FMVSS 301 | Fuel System Integrity | PF.90197 | 法规 | ❌ 未提供 |
| ASME Y14.5-2009 | GD&T | CTS | ASME（付费） | ❌ 未提供 |
| 9.14618 | Rubber O-ring Seals | CTS §2.4 | Stellantis | ❌ 未提供 |
| 9.55253 | Miscellaneous Plastic Components | CTS §2.4 | Stellantis | ❌ 未提供 |
| MS.90111 | Tape | CTS §2.4 | Stellantis | ❌ 未提供 |
| CDS | Component Development Sheet | TDR §CDS | Stellantis | ❌ 未提供（需客户提供） |

---

## 7. 项目时间约束

| 里程碑 | 日期 | 说明 |
|--------|------|------|
| TDR 版本 | 2022-03-09 | 文件包发布日期 |
| TKO | 未知 | CAD 至少提前10天，2D图纸于TKO提交 |
| V.P. 阶段零件 | 未知 | Off-Tools (OT) |
| P.S. 阶段零件 | 未知 | Off-Tools Off-Process (OTOP) + 自验证 |
| SOP | 未知 | 工厂装配支持 |

⚠️ **注意**：客户未提供车辆开发计划，VP/PS/SOP 具体日期均缺失，需向客户 PM 索要。

---

## 8. 联系人/签署信息

| 角色 | 姓名/部门 |
|------|----------|
| PF.90197 主作者 | Fernando Sada（NA，Fuel Systems） |
| PF.90197 合作者 | Bruno Le Moine（EMEA，Fuel Systems） |
| PF.90298 主作者 | Michael Marcon（FCA US，Fuel Systems） |
| PF.90298 合作者 | Bruno Le Moine（FCA Italy，Fuel Systems） |

---

## 9. OLE 嵌入文件识别结果

| 文件 | 内容 |
|------|------|
| L2_CTS_OLE1.jpg | 关键产品特性表（JPG图片） |
| L2_CTS_OLE2.pdf | 材料限制/ELV指令要求（Fiat Group文件） |
| L2_CTS_OLE3.pdf | 保护帽要求（拆卸力2N–15N，颜色区分，密封要求） |
| L3_PPTX_OLE_drawing.tiff | CTS产品描述PPTX中的工程图纸（TIFF） |
| L3_DamperDesc_drawing.tiff | Damper描述PPTX中的工程图纸（TIFF） |
