# FILTER 项目 — 文档解析分析报告

## 项目概览

| 项目 | 内容 |
|------|------|
| **OEM** | Stellantis（文档中以"S"代替） |
| **零件类型** | Smart Fuel Filter（智能柴油滤清器） |
| **应用** | S K0 平台 |
| **发动机** | FamB 2.2L Mjet（柴油） |
| **排量** | 2.2 dm³ |
| **燃油类型** | Diesel |
| **目标市场** | Enlarged Europe & LATAM |
| **排放标准** | Euro 7 / PL8 |
| **性能标准** | PF.90150 (01446_24_00041)，Change Level C，2024-01-12 |
| **供应商集成等级** | Level 2 |
| **工作压力范围** | 0 ~ 700 kPa (0 ~ 101.5 psi) |

## 功能描述

Smart Fuel Filter 是一个集成多功能的柴油滤清器总成，需提供以下功能：
1. **燃油过滤** — 保证发动机所需流量和压力
2. **水分离** — 分离柴油中的水分
3. **油位指示** — 水位报警功能
4. **电加热** — 低温条件下防止石蜡结晶堵塞（PTC 加热器）
5. **温度传感** — NTC 温度传感器，通过 SENT 协议与 ECU 通信
6. **水位传感** — Water-in-Fuel (WiF) 传感器，数字输出

## 关键性能参数

### 工作条件

| 参数 | 值 |
|------|-----|
| 工作环境温度 | +45°C ~ +120°C |
| 工作燃油温度 | -45°C ~ +90°C |
| 工作燃油压力 | 450 ~ 700 kPa |
| 使用相对湿度 | 0 ~ 100% |
| 存储相对湿度 | ≤ 60% |
| 存储温度 | -30°C ~ +70°C |

### 滤清器性能

| 参数 | 值 | 标准 |
|------|-----|------|
| 标称流量 | 190 l/h | — |
| 压降（新品） | ≤ 10 kPa @ ISO 4020 | CTS §3.1 |
| 压降（新品通用） | ≤ 30 kPa @ 200 l/h | PF.90150 §7.7 |
| 过滤效率（初始） | ≥ 98% @ 4µm | PF.90150 §7.1 / ISO 19438 |
| 过滤效率（>5µm） | ≥ 95% | PF.90150 Table 5 |
| 过滤效率（>10µm） | ≥ 99% | PF.90150 Table 5 |
| 过滤效率（>20µm） | ≥ 99.9% | PF.90150 Table 5 |
| 单次通过颗粒保留率 | ≥ 95% @ 5µm | PF.90150 §7.2 |
| 容尘量 (DHC) | ≥ 30g @ 500kPa @ 寿命终点 | CTS §3.1 / ISO 4020 |
| 水分离效率 | ≥ 93% @ 标称流量 | CTS §3.1 / ISO 16332 |
| 水分离效率（PF.90150） | ≥ 95% | PF.90150 §7.12 |
| 储水容量 | 150 ml | CTS §3.1 |
| 水位报警量 | 100 ml | CTS §3.1 |
| 滤清器清洁度 | ≤ 0.5 mg/part | PF.90150 §7.8 |
| 滤芯塌陷压力 | > 800 kPa | PF.90150 §7.9 |
| 爆破压力 | ≥ 20 bar | PF.90150 §7.10 |

### 密封性

| 参数 | 值 | 标准 |
|------|-----|------|
| 空气密封泄漏 | < 3 cm³/min @ 工作压力 | PF.90150 §7.4.1 |
| 燃油密封 | 零泄漏 @ 10.3 bar (150 psi) | PF.90150 §7.4.2 |
| 内部密封（气泡测试） | < 100 cm³/min @ 1.3 kPa | PF.90150 §7.6 |
| 密封温度范围 | -40°C / +23°C / +80°C | PF.90150 §7.4 |

### 机械

| 参数 | 值 | 标准 |
|------|-----|------|
| 金属接头扭矩（壳体压入） | ≥ 7.3 Nm | PF.90150 §7.11.1 |
| 塑料接头（侧向载荷） | SAE J2044 §6.4 | PF.90150 §7.11.2 |
| 紧固件扭矩 | 按图纸 | PF.90150 §7.15 |
| 静电荷消散 | SAE J1645 | PF.90150 §7.16 |

### 电加热器

| 参数 | 值 | 标准 |
|------|-----|------|
| 加热器效率 | η ≥ 0.75 @ 6min | PF.90150 §6.4.10 |
| 最大峰值电流 | 40A | CTS 示例 |
| 峰值持续时间 | 2.5s | CTS 示例 |
| 最大工作电流 | 30A | CTS 示例 |
| ΔT 最小 | 3°C @ 6min | CTS 示例 |
| 关断时间（满油） | < 10 min | PF.90150 §6.4.9 |
| 关断时间（空滤） | < 3 min | PF.90150 §6.4.9 |
| 生命周期 | 5000 cycles @ 14V, 500 @ 18V, 10 @ 24V | PF.90150 §9.7 |
| 供电电压 | 12.5V 标称 | CTS 示例 |

### NTC 温度传感器

| 参数 | 值 | 标准 |
|------|-----|------|
| 工作温度范围 | -40°C ~ +125°C | PF.90150 §7.19 |
| 供电电压 | 5V ±2% (ECU 供电) | PF.90150 §7.19 |
| 通信协议 | SENT Protocol | CTS §3.3 |
| NTC 特性曲线 | 见 PF.90150 Table 7 | 从 45.3kΩ@-40°C 到 0.071kΩ@140°C |

### Water-in-Fuel 传感器

| 参数 | 值 | 标准 |
|------|-----|------|
| 传感器类型 | Active | PF.90150 §7.21 |
| 正常状态电压 | > 5.5V | PF.90150 §7.21 |
| 报警状态电压 | < 2.2V | PF.90150 §7.21 |
| 最大吸收电流 | < 50 mA | PF.90150 §7.21 |
| 自检时间（-30~110°C） | 3s ±20% | PF.90150 §7.21 |
| 自检时间（-40~125°C） | 1.7~4.5s | PF.90150 §7.21 |
| 供电电压 | 10V ~ 16V (A1 分类) | PF.90150 §7.21 |

### 接口

| 接口 | 类型 | 参考标准 |
|------|------|---------|
| 进口 | 10mm diameter | B12 2813 |
| 出口 | 10mm diameter | B12 2813 |
| 电气连接器 | APTIV P/N 211FT0523, 6-pin | CTS §3.3 |

#### 连接器引脚定义
| Pin | 功能 |
|-----|------|
| 1 | +5V Power Supply |
| 2 | WiF Digital Output |
| 3 | PTC - |
| 4 | PTC + |
| 5 | SENT Protocol |
| 6 | GROUND (Sensors) |

## 环境分类（CS.00056）

| 描述 | Heater | Water in Fuel Sensor | Temperature Sensor |
|------|--------|---------------------|-------------------|
| Device type | E2/E3 | E2/E3 | E2/E2-S |
| Functional | FC1 | FC1 | FC1/FC2 |
| Installation-based | CI1/CI4 | CI1/CI4 | CI1/CI4 |
| Max Temp | TC3 | TC3 | TC3 |
| Min Temp | TN1 | TN1L (-30) | TN1 |
| Vibration | V2 | V2 | V2 |
| Power supply voltage | A1 | A1/NA | NA (Supplied by ECU) |
| ESD | SE2 | SE2 | SE2 |
| Water-penetration | IP6K9K | IP6K9K | IP6K9K |

## 测试矩阵

### DV/PV 验证测试（Annex A）

| # | 测试项 | 章节 | DV 样件 | PV 样件 | DV 接收准则 | PV 接收准则 |
|---|--------|------|--------|--------|-----------|-----------|
| 1 | Environmental (CS.00056) | §5 | Note 2 | Note 2 | Meets Req | Meets Req |
| 2 | Resistance to Corrosion | §5.2 | 15 | 15 | P99C90 | P99C90 |
| 3 | Resistance to Fluids in Engine Compartment | §5.3 | 15 | 15 | P99C90 | P99C90 |
| 4 | Appearance/Physical/Mechanical/Electrical | §6 | Note 2 | Note 2 | Meets Req | Meets Req |
| 5 | Filtering Efficiency | §7.1 | 15 | 15 | P99C90 | P99C90 |
| 6 | DHC (Dust Holding Capacity) | §7.3 | 15 | 15 | P99C90 | P99C90 |
| 7 | Outwards Sealing | §7.4 | 15 | 15 | P99C90 | P99C90 |
| 8 | Seal of Filter Element Gasket | §7.5 | 15 | 15 | P99C90 | P99C90 |
| 9 | Inner Seal (Bubble-Test) | §7.6 | 15 | 15 | P99C90 | P99C90 |
| 10 | Pressure Drop on New Product | §7.7 | 15 | 15 | P99C90 | P99C90 |
| 11 | Filter Cleanliness | §7.8 | 15 | 15 | P99C90 | P99C90 |
| 12 | Filter Element Collapse Test | §7.9 | 15 | 15 | P99C90 | P99C90 |
| 13 | Burst Test | §7.10 | 15 | 15 | P99C90 | P99C90 |
| 14 | Fuel Fitting Torque Test | §7.11 | 15 | 15 | P99C90 | P99C90 |
| 15 | Water Separation Efficiency | §7.12 | 15 | 15 | P99C90 | P99C90 |
| 16 | Functionality at Cold Condition | §7.13 | 15 | 15 | P99C90 | P99C90 |
| 17 | Resistance at Cold with Paraffin | §7.14 | 15 | 15 | P99C90 | P99C90 |
| 18 | Electrostatic Charge Resistance | §7.16 | 15 | 15 | P99C90 | P99C90 |
| 19 | Emulsified Water Separation | §7.17 | 15 | 15 | P99C90 | P99C90 |
| 20 | Thermostatically Controlled Heater On/Off | §7.18 | 15 | 15 | P99C90 | P99C90 |
| 21 | NTC Temperature Sensor | §7.19 | 15 | 15 | P99C90 | P99C90 |
| 22 | Fuel Temp Measurement Accuracy | §7.20 | 15 | 15 | P99C90 | P99C90 |
| 23 | Water in Fuel Sensor | §7.21 | 15 | 15 | P99C90 | P99C90 |
| 24 | Resistance to Thermal Cycles | §9.3 | 45 | 45 | R95C90 | R95C90 |
| 25 | Resistance to Pulsating Pressure | §9.4 | 45 | 45 | R95C90 | R95C90 |
| 26 | Resistance to Vibrations | §9.5 | 45 | 45 | R95C90 | R95C90 |
| 27 | Resistance to Fuels (Dynamic Ageing) | §9.6 | 45 | 45 | R95C90 | R95C90 |
| 28 | Heater Life Cycle Test | §9.7 | 45 | 45 | R95C90 | R95C90 |

### 持续合规测试 (Continuing Conformance)

| # | 测试项 | 章节 | 样件数 | 接收准则 | 频次 |
|---|--------|------|--------|----------|------|
| 1 | Heater General Performance | §6.4.10.1 | 3 | No Failure | Weekly |
| 2 | Dimensional Check of Fuel Fittings | §6.4.7 | 1/Cavity | No Failure | Daily |
| 3 | Water-in-Fuel Signal Level | §6.4.8 | 6 | No Failure | Weekly |
| 4 | Outwards Sealing | §7.4 | 1 | No Failure | 100% |
| 5 | Filter Efficiency | §7.1 | 6 | No Failure | Quarterly |
| 6 | Dust Holding Capacity | §7.3 | 6 | No Failure | Quarterly |
| 7 | Pressure Drop on New Product | §7.7 | 6 | No Failure | Quarterly |
| 8 | Burst Test | §7.10 | 6 | No Failure | Quarterly |
| 9 | Fuel Fitting Torque | §7.11 | 6 | Within Tolerance | Quarterly |
| 10 | Water Separation Efficiency | §7.12 | 6 | No Failure | Quarterly |
| 11 | Emulsified Water Separation | §7.17 | 6 | No Failure | Quarterly |
| 12 | NTC Temperature Sensor | §7.19 | 3 | Within Tolerance | Daily |
| 13 | Water in Fuel Sensor | §7.21 | 3 | Within Tolerance | Quarterly |

## 引用规范清单

### Stellantis 内部标准

| 编号 | 名称 | 供应商可下载 | 状态 |
|------|------|-----------|------|
| PF.90150 | Diesel Filters for Injection Engines (本文件) | Y | ✅ 已有 |
| CS.00056 | Environmental Specification for E/E Components | Y | ❌ 未提供 |
| 01552_16_03847 | Electrical Requirements - P PG CT | Y | ❌ 未提供 |
| CS.00244 | S Electrical and EMC Performance Requirements for EE Components | Y | ❌ 未提供 |
| CS.00251 | Corrosion Requirements - Vehicle Systems and Components | Y | ❌ 未提供 |
| CS.00050 | Wiring Design and Package Requirements | Y | ❌ 未提供 |
| PF.90012 | Standard for Automotive Electrical Connection Systems | Y | ❌ 未提供 |
| PF.90303 | Wiring Harness - Assembly Performance | Y | ❌ 未提供 |
| QR.00001 | Global Product Assurance Testing (GPAT) | Y | ❌ 未提供 |
| QR-10012 | Dimensional Quality Requirements | Y | ❌ 未提供 |
| SD-12219 | EE Interface Checklist | Y | ❌ 未提供 |
| PS-11346 | Warranty Returned Parts Testing and Analysis Procedures | Y | ❌ 未提供 |
| CS.00263 | Environmental Spec for E/E Components (CTS ref) | — | ❌ 未提供 |
| PF.90298 | Quick Connect - Fuel System | — | ❌ 未提供 |
| 07740 | Qualification Procedure | — | ❌ 未提供 |
| CS.00133 | Product FMEA | — | ❌ 未提供 |

### 外部标准

| 编号 | 名称 | 状态 |
|------|------|------|
| ISO 19438 | Diesel Fuel and Petrol Filters for ICE | ❌ 需购买 |
| ISO 12103 | Road Vehicles - Test Dust for Filter Evaluation | ❌ 需购买 |
| ISO 16332 | Diesel Engines - Fuel Filters - Water Separation Efficiency | ❌ 需购买 |
| ISO 2942 | Hydraulic Fluid Power - Filter Elements Verification | ❌ 需购买 |
| ISO 4020 | Road Vehicles - Fuel Filters for Diesel Engines - Test Methods | ❌ 需购买 |
| ISO 4113 | Road Vehicles - Calibration Fluids for Diesel Injection | ❌ 需购买 |
| SAE J1645 | Fuel System - Electrostatic Charge | ❌ 需购买 |
| SAE J2044 | Quick Connect Coupling Specification | ❌ 需购买 |
| SAE J2334 | Laboratory Cyclic Corrosion Test | ❌ 需购买 |
| SAE/USCAR-2 | Performance Spec for Automotive Electrical Connector Systems | ❌ 需购买 |
| SAE/USCAR-21 | Performance Spec for Cable-to-Terminal Electrical Crimps | ❌ 需购买 |
| SAE/USCAR-25 | Ergonomics Spec for Electrical Connections | ❌ 需购买 |
| EN590 | Automotive Fuels - Diesel | ❌ 需购买 |
| EN14214 | Automotive Fuels - FAME for Diesel Engines | ❌ 需购买 |
| ASTM D971 | Standard Test Method for Interfacial Tension | ❌ 需购买 |
| ASME Y14.5-2009 | Dimensioning and Tolerancing | ❌ 需购买 |

## CTS 附加要求摘要

### 可维护性
- 免维护里程 ≥ 240,000 km
- 可作为模块整体更换
- 不需要特殊工具维修
- 使用 Hex-head 或 Torx-bolts 紧固件

### 材料要求
- 避免使用 PVC（有替代方案优先）
- 符合 S 9.01102 annex CK 材料一致性
- 最大允许再研磨比例 10%
- 标记符合 S 07416，可回收性按 S 00256 计算
- 必须使用 IMDS 系统提交材料数据表

### 设计要求
- CAD 标准：UG/Teamcenter 或 CATIA（S 最新版本）
- 3D 注释模型 (3DA) 按 CS.00029
- 共用化策略：尽量使用通用件降低成本
- 人因工程：手动装配力 ≤ 8.2 kg（目标 ≤ 4.5 kg）
- 卡扣力 ≤ 4.5 kg（目标 ≤ 1.0 kg）

### 验证要求
- 按 07740 annex 2 格式提供 DV 和 PV 验证计划
- 测试清单必须按 PF.90150 编制，所有测试必须列出
- 鼓励复用已有验证数据（其他 S 应用）
- 补充零部件（如 ICV 等）也需提供 DV/PV 计划
