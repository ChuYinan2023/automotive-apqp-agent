# KP1 Fuel Line — 文档解析报告

## 项目基本信息

| 项 | 值 |
|----|-----|
| **OEM** | Stellantis（原 FCA） |
| **项目代号** | KP1 A&B |
| **零件名称** | Fuel Supply Line Filter to Engine（燃油管路 — 滤清器至发动机） |
| **零件号** | FC00SAA78530 |
| **Product Description 编号** | [00] |
| **发布日期** | 2022-03-09 |
| **平台/车型** | 2.2 Diesel Final |
| **供应商集成等级** | Level 2（Supplier Integration Level 2） |
| **市场** | [-]（未指定） |
| **零件类型** | Fuel Line（燃油管路） |

## BOM / 组件描述

| 组件 | 规格 | 说明 |
|------|------|------|
| Feed Line（供油管） | Ø8mm × 6mm | 塑料管（Monolayer or Multilayer Pipe） |
| Return Line（回油管） | Ø10mm × 8mm | 从泵到油箱 |
| QC 接头（发动机侧） | SAE 5/16" / SAE 3/8" | 金属材质，带二次锁止 |
| QC 接头（90°弯头） | PF.90298 / SAE J2044 | Female 90° |
| Damper（阻尼器） | — | 供应商 Nobel Auto，工作压力 4.5 bar |
| 防磨套管 | PF.90271 | Anti-abrasion sleeve |
| 保护帽 | Cap.9.91220 | 所有管端必须加保护帽 |
| Clip（卡扣） | — | 装配力 ≤35N，拔出力 ≥100N |
| 管路插入卡扣 | — | 插入力 ≤40N，拔出力 ≥80N |

## 关键性能参数

### 管材要求（PF.90197）
| 参数 | 要求 |
|------|------|
| 工作温度范围 | -40°C ~ +90°C（连续），短期 115°C（30min） |
| 燃油温度 | 最高 90°C（连续），短期 105°C（30min） |
| 拉伸强度（新品） | ≥20 N/mm² |
| 拉伸强度（燃油浸泡后） | ≥15 N/mm² |
| 泄漏测试压力 | 液体管路 ≥150 PSI，蒸汽管路 ≥10 PSI |
| 爆破压力（室温） | ≥8× 工作压力 |
| 爆破压力（115°C） | ≥3× 工作压力 |
| 化学浸泡后爆破 | ≥75% 原始值，且 ≥3× 工作压力 |
| 压降测试 | 燃油管 400 kPa，蒸汽管 3.4 kPa |
| 设计寿命 | 15 年 / 150,000 miles |

### 脉冲压力测试
| 条件 | 要求 |
|------|------|
| 传统 Start/Stop | 300,000 cycles |
| Start/Stop + Freewheel | 600,000 cycles |
| 压力范围（2-5 bar 级别） | Min 2 bar → Max 工作压力 |
| 压力范围（2-10 bar 级别） | Min 2 bar → Max 2× 10 bar |

### 振动测试
| 参数 | 要求 |
|------|------|
| 可靠性目标 | R95/C90（P95C90） |
| 通用 profile 测试 | 5 samples × 60 hours（加速因子 3） |
| 测试温度 | 22°C ± 5°C |

### 清洁度
| 参数 | 要求 |
|------|------|
| 适用场景 | 滤清器下游、高压泵上游的柴油管路 |
| DV 阶段 | 柴油管路必须合规 |
| PV 阶段 | 所有燃油/蒸汽管路必须合规 |

## 质量目标（SSTS 定义）

| 指标 | 目标值 |
|------|--------|
| CCP（Customer Car Profile） | 0.00 c/1000 vehicles @ 3 months; 0.035 c/1000 vehicles @ 12 months |
| QT（Quality Tracking） | 供应商承诺共享可达性 |
| ICP（Initial Customer Perception） | 0（单个零件） |
| 可靠性验证 | 见 PF.90068 Annex A（样本数与 Stellantis 规范工程师确定） |
| 目标重量 | 预估值（整体燃油管路） |

## 引用规范清单

### Stellantis 内部规范
| 规范编号 | 名称 | 类别 |
|----------|------|------|
| PF.90197 | Fuel Bundle and Fuel System Jumpers – Plastic, Rubber and Metallic | 性能标准（主标准） |
| PF.90068 | DEF Line 性能标准 | 性能标准 |
| PF.90298 | Quick Connect - Fuel System（QC 接头要求） | 接口标准 |
| PF.90271 | Electrical System Insulating Components Wiring Harness Protection Sleeves | 材料标准 |
| 9.01102 | Supplier Quality | 质量体系 |
| 9.01103 | Product Quality and Conformity Certificate | 质量体系 |
| 07740 | Qualification Procedure | 验证流程 |
| 00270 (CS.00133) | Product FMEA | FMEA |
| 00271 | Process FMEA | FMEA |
| 07610 | Supplier Code | 供应商管理 |
| 07611 | Supplier Alphanumeric Code Marking | 标识 |
| 08034 | Integration Level Procedure | 集成等级 |
| 0.00013 | Vehicle Part Marking Procedure | 标识 |
| CS.11000 | Motor Vehicle Part Marking "sol. F" | 标识 |
| MS.90074 | Pressure-sensitive Adhesive Labels | 标识 |
| QR-00001 | Global Product Assurance Testing (GPAT) | 验证 |
| MS.50017 | Plastics - Thermoplastic - Polyamide (Nylon) | 材料标准 |
| MS.50015 | Thermoplastic Vulcanizates - EPDM/PP | 材料标准 |
| 9.14618 | Rubber O-rings Seals | 材料标准 |
| MS.90111 | Tape | 材料标准 |
| 9.55253 | Miscellaneous Plastic Component | 材料标准 |
| 9.02145/02 | Electrowelded Steel Pipes for Fuel Circuits | 材料标准 |
| CS-9003 | Restricted and Prohibited Substances / IMDS | 环保合规 |
| 07416 | Recycling Markings for Plastic/Composite/Elastomer | 环保合规 |
| 00256 | Recyclability and Recoverability of a Vehicle | 环保合规 |
| MS-AO-0001 | VOC, Odor and Prohibited Substances | 环保合规 |
| CS.00080 | CAD Drawings / Modelling Rules | 图纸标准 |
| 07264 | CAD Drawings Types and Lines | 图纸标准 |
| 07226 | TcAE System and CAD Part Management | 图纸标准 |
| CS.00029 | 3DA Documentation Definition | 图纸标准 |
| 07247 | CAD Self-certification Checklist | 图纸标准 |
| 07247/01 | CAD Self-certification for E&D | 图纸标准 |
| CS.00003 | Drawing Title Block | 图纸标准 |
| 07265 | CAD Library Symbols | 图纸标准 |
| CS.00019 | Dimensioning and Tolerancing (ASME addendum) | 图纸标准 |
| ASME Y14.5-2009 | Dimensioning and Tolerancing | 外部标准 |
| 9.01108 | Supplies Quality – Forbidden Substances | 环保合规 |
| Cap.9.91220 | Protection Caps | 零件标准 |

### 外部标准
| 标准编号 | 名称 |
|----------|------|
| SAE J2044 | Quick Connector Standard |
| SAE J2045 | Fuel System Testing |
| SAE J2260 | Multi/Mono-layer Nylon Fuel Lines |
| SAE J1645 | Fuel Line Assembly Testing |
| SAE J2027 | Thermoplastic Elastomer Covers |
| CS.00251 | Corrosion Testing (15-year life) |

## 时间节点

| 节点 | 要求 |
|------|------|
| CAD Step Release | TKO 前至少 10 天 |
| VP 阶段零件 | Off-Tools (OT) |
| PS 阶段零件 | Off-Tools Off-Process (OTOP) + Auto-Qualified (AQF) |
| 零件交付 | VP/PS 日期前 15 天 |
| 自验证计划 | 每年重复 |

## Stellantis 工程团队

| 角色 | 姓名 |
|------|------|
| FCA Engineer Lead | — |
| PC | Yuhan Zhang |
| PR | Grace Tan |
| VIR | — |
| MR | — |
| Affidabilità | — |

## 知识产权

基于本 Product Description 开发的零件技术方案，知识产权归属需符合 Stellantis 标准条款。

## 特殊说明

1. **金属管内表面要求镀镍处理**（Metallic pipe requires internal nickel plate treatment）
2. **DEF Line 另有独立规范** PF.90068，本次 RFQ 同时包含 DEF 管路
3. **虚拟分析不适用**（Virtual Analysis: Not applicable）
4. **UG/Teamcenter 3D 能力为必须项**（Deliverable #1: Native Unigraphics and Team Center capability）
5. **供应商需支持 SOP 阶段装配厂现场支持**（Deliverable #15）
6. **材料必须通过 IMDS 系统提交**
