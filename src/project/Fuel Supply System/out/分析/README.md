# 文档解析报告 — Fuel Supply System

## 项目基本信息

| 项目 | 值 |
|------|-----|
| OEM | Volkswagen AG (VWAG) |
| 文档类型 | Systemlastenheft / System Performance Specification (SyS-LAH) |
| 文档编号 | LAH.3WA.201.B |
| 文档标题 | Kraftstoffförderung inkl. Füllstandmessung — Konzernversion |
| 作者 | Preuße, Ulf [Leiter Entwicklung Kraftstoffversorgung] |
| 部门 | EFAT/011/1509 |
| 版本 | <K6> |
| 首次发布 | 28.01.2019 |
| 最后修改 | 09.09.2021 |
| 页数 | 76页（含封面） |
| 语言 | 德文/英文混合（主体为英文，部分表头和注释为德文） |
| 保密等级 | Volkswagen AG Confidential |

## 零件信息

| 项目 | 值 |
|------|-----|
| 系统名称 | Kraftstoffförderung inkl. Füllstandmessung (Fuel Supply System incl. Fuel Level Measurement) |
| 零件名称 | Fuel supply module ASSY |
| 零件号 | 由客户（VW）提供，供应商必须使用客户指定的零件号 |
| 适用平台 | MQB48W, MQB37W PA, MQB37AW/48W（已更新至 EU7 版本） |
| 适用发动机 | 汽油（FSI/MPI）和柴油（TDI）发动机系列 |
| 发动机家族 | Motor-Familie "EA211" / Motor-Familie "EA888" |

## 系统范围 (Scope of Supply)

### 主要组件
- **Fördereinheit (Fuel Supply Module ASSY)** — 主供油模块
- **Kraftstoffpumpenelektronik / KPE (Fuel Pump Electronics)** — 燃油泵电子控制单元
- **Tankgeber (Fuel Level Sensor)** — 油位传感器
- **Saugstrahlpumpe (Suction Jet Pump)** — 射流泵
- **Filter (Fuel Fine Filter)** — 燃油精滤器
- **Absaugkäfig (Extraction Strainer)** — 抽吸滤网
- **Leckage-Schutzventile (Leakage Protection Valves)** — 泄漏保护阀
- **Druckbegrenzungsventil (Pressure Limitation Valve)** — 压力限制阀
- **Druckhalteventil (Pressure Holding Valve)** — 保压阀（仅汽油系统）
- **Standheizungsventil (Parking Heater Stop Valve)** — 驻车加热器截止阀

### 不在供应范围内（但有接口要求）
- 油箱 (Fuel Tank)
- 车辆电气系统
- 发动机控制模块 (ECM)
- 外部供回油管路
- 显示仪表

## 系统架构变体

| 变体 | 说明 | 控制方式 |
|------|------|---------|
| MPI 机械闭环 | 机械压力控制 — **已删除 (Entfall)** | — |
| FSI/MPI 电子闭环 | 低压燃油压力传感器反馈 | 闭环电子压力控制 |
| FSI 电子开环 | 无低压传感器 | 开环预控制特性曲线 |
| TDI | 低压电子控制 | 闭环/开环电子压力控制 |

## 关键技术参数

### 压力系统
- **FSI/MPI 闭环**：运行电压 6-16V，最大电流 12A
- **TDI 运行压力**：50-700 kPa (供油)，0-100 kPa (回油)
- **汽油 FSI 运行压力**：通过预控制特性曲线
- **压力限制阀**：开启压力 620-640 kPa，关闭压力 > 600 kPa

### 泵电子控制 (KPE)
- EC 泵：三相换向驱动，PWM 频率 9-25 kHz
- DC 泵：单相 PWM 电压控制
- 支持 EC 和 DC 两种泵型

### 效率要求
- DC 流量泵 汽油 > 20% (430 kPa)
- EC 流量泵 汽油 > 30% (430 kPa)
- EC 容积泵 柴油 > 35% (450 kPa)
- 非闭环/非开环系统 100%

### 油位测量
- 杠杆式油位传感器 (Lever-type) 或 TKN 厚膜传感器
- 电阻范围：300 ±X Ω (满) — 50 ±X Ω (空)（VW规格）
- 3线制传感器支持
- 总电阻 340 ±1 Ω（VW品牌）
- 采样率 20 Hz，延迟 < 50 μs

### 耐久性
- 10 台燃油供应模块用于耐久试验
- 压力调节器标称值 660 ±20 kPa
- 温度-时间耐久试验谱含 DK7-DK8 循环，总计 4000+4000 小时
- 老化条件：FAM-B 测试燃油，168h，60°C

### 功能安全 (Functional Safety)
- 文档明确要求 ASIL 等级评估 (ISO 26262)
- DIA (Design Impact Analysis) 模板需填写
- 供应商安全案例 (Safety Case) 需在客户释放前创建
- Fault Tolerance Time 概念需协商确认

## 诊断系统

### EC 故障定义 (Table 3)
| 故障号 | 名称 | 优先级 | 测试时间 |
|--------|------|--------|---------|
| 1 | 内部故障 (Internal Fault) | 8 | 100 ms |
| 2 | 过温预警 (Overtemperature Warning) | 2 | 200 ms |
| 3 | 相电流过流 (Phase Overcurrent) | 4 | 300 ms |
| 4 | 转子堵转 (Blocked Rotor) | 5 | 400 ms |
| 5 | 相线短路 (Short Circuit) | 6 | 500 ms |
| 6 | 相线断路 (Phase Open) | 7 | 600 ms |
| 7 | 转速偏差 (Speed Deviation) | 3 | 700 ms |
| 8 | 过温终态 (Final Stage Temp) | 1 | 800 ms |
| 9 | 转速偏差(电压相关) | 3 | 900 ms |

### DC 故障定义 (Table 4)
| 故障号 | 名称 | 优先级 | 测试时间 |
|--------|------|--------|---------|
| 1 | 内部故障 | 7 | 100 ms |
| 2 | 过温预警 | 2 | 200 ms |
| 3 | 相电流过流 | 3 | 300 ms |
| 4 | 转子堵转 | 4 | 400 ms |
| 5 | 相线短路 | 5 | 500 ms |
| 6 | 相线断路 | 6 | 600 ms |
| 7 | 过温终态 | 1 | 800 ms |

## 引用规范清单

### 核心引用文件（项目必须遵循）
| 编号 | 名称 | 是否已有 |
|------|------|---------|
| BT-LAH | Organizational and Basic Conditions for Development of Fuel Systems | ❌ 未提供 — **关键缺失** |
| LAH.DUM.201.C | Electric Fuel Pump for Gasoline Fuels | ❌ 未提供 |
| LAH.DUM.201.E | Electric Fuel Pump for Diesel Fuels | ❌ 未提供 |
| LAH.DUM.201.AB | Spezifikation (特性值填写模板) | ❌ 未提供 |
| LAH.DUM.201.F | Fuel Level Sensor for Fuel Supply Systems, Lever-Type | ❌ 未提供 |
| LAH.DUM.201.G | Alternative Fuel Level Sensor | ❌ 未提供 |
| NNC.201.021.xx | 各类试验规范（大量引用） | ❌ 未提供 |
| EP 21xxx.xx | 各类试验计划 | ❌ 未提供 |

### 通用标准引用
| 编号 | 说明 | 是否已有 |
|------|------|---------|
| TL 82253 | Fuel line ASSYs and connections | ❌ |
| TL 82421 | Quick couplings | ❌ |
| TL 52719 | Polyamide tubes | ❌ |
| SAE J2044 | Quick couplings | ❌ |
| ISO 26262 | Functional Safety | ❌ |
| ISO 19438 | Fine filter testing | ❌ |
| DIN EN 590 | Diesel fuel specification | ❌ |
| VW 80000 | Electrical system requirements | ❌ |
| VW 80106 | Device connector design | ❌ |
| VW 99000 | IP rights | ❌ |
| Q-LAH LAH.893.910.A | Standard Software | ❌ |
| Q-LAH LAH.5G0.907 | ECU Capability | ❌ |

## 🚨 关键发现与风险标注

### 1. 缺少 TDR / 交付物清单
**严重**：客户文件包中仅含一份技术规范（SyS-LAH），未提供：
- BT-LAH（组织与基本条件文件）— 几乎每一节都引用此文件
- TDR（Technical Documents Required / 交付物清单）
- 项目时间表（SOP / TKO 日期等）
- 报价模板 / 成本模板

**影响**：无法确定完整的交付物需求，后续 Step 2-4 的交付物生成将受限。

### 2. 大量引用规范未提供
文档引用了 20+ 个 VW 内部规范（LAH.DUM.201.x, NNC.201.021.x, EP 21xxx 等），这些规范定义了具体的测试方法、验收标准和特性值模板。

### 3. 文档为 Konzernversion（集团版本）
适用于整个 VW 集团（VW/Audi/Porsche 等品牌），部分条目标注了品牌差异（如油位传感器电阻值 VW vs Audi/Porsche）。

### 4. EU7 更新版本
文档已更新至 EU7 排放法规版本（09.09.2021），新增了功能安全 (Section 2.10) 和 DC 故障定义等内容。
