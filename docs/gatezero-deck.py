#!/usr/bin/env python3
"""Generate GateZero solution deck (10-page PDF) using weasyprint."""

from weasyprint import HTML

html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@page {
    size: A4 landscape;
    margin: 0;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    font-family: "Noto Sans CJK SC", "Noto Sans SC", sans-serif;
    color: #1a202c;
    font-size: 10pt;
    line-height: 1.6;
}

/* Slide container */
.slide {
    width: 297mm;
    height: 210mm;
    padding: 14mm 20mm;
    page-break-after: always;
    position: relative;
    overflow: hidden;
}
.slide:last-child {
    page-break-after: auto;
}

/* Slide header bar */
.slide-header {
    border-bottom: 2.5px solid #ed8936;
    padding-bottom: 3mm;
    margin-bottom: 6mm;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}
.slide-title {
    font-size: 20pt;
    font-weight: bold;
    color: #1a365d;
}
.slide-logo {
    font-size: 10pt;
    color: #a0aec0;
    font-weight: bold;
}

/* Page number */
.page-num {
    position: absolute;
    bottom: 8mm;
    right: 20mm;
    font-size: 8pt;
    color: #a0aec0;
}

/* ========== Page 1: Cover ========== */
.cover {
    background: #1a365d;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}
.cover h1 {
    font-size: 52pt;
    letter-spacing: 4px;
    margin-bottom: 5mm;
}
.cover .tagline {
    font-size: 18pt;
    color: #ed8936;
    margin-bottom: 3mm;
}
.cover .sub {
    font-size: 13pt;
    color: #bee3f8;
    margin-bottom: 15mm;
}
.cover .meta-info {
    font-size: 10pt;
    color: #a0aec0;
}

/* ========== Common elements ========== */
.two-col {
    display: flex;
    gap: 8mm;
}
.col-50 { width: 50%; }
.col-45 { width: 45%; }
.col-55 { width: 55%; }
.col-40 { width: 40%; }
.col-60 { width: 60%; }

.subtitle {
    font-size: 11pt;
    color: #718096;
    margin-bottom: 5mm;
}

/* Card */
.card {
    background: #f7fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 4mm 5mm;
    margin-bottom: 3mm;
}
.card-title {
    font-size: 11pt;
    font-weight: bold;
    color: #1a365d;
    margin-bottom: 1.5mm;
}
.card-body {
    font-size: 9.5pt;
    color: #4a5568;
    line-height: 1.6;
}

/* Highlight card */
.card.highlight {
    border-color: #ed8936;
    border-left: 3px solid #ed8936;
}
.card.blue {
    border-color: #2b6cb0;
    border-left: 3px solid #2b6cb0;
}
.card.green {
    border-color: #38a169;
    border-left: 3px solid #38a169;
}
.card.red {
    border-color: #e53e3e;
    border-left: 3px solid #e53e3e;
}

/* Pain item */
.pain-card {
    background: #fff5f5;
    border: 1px solid #fed7d7;
    border-left: 3px solid #e53e3e;
    border-radius: 4px;
    padding: 3.5mm 5mm;
    margin-bottom: 3mm;
}
.pain-card .num {
    font-size: 14pt;
    font-weight: bold;
    color: #e53e3e;
    margin-right: 2mm;
}
.pain-card .title {
    font-size: 11pt;
    font-weight: bold;
    color: #1a202c;
}
.pain-card .desc {
    font-size: 9.5pt;
    color: #4a5568;
    margin-top: 1mm;
}

/* Risk chain */
.risk-chain {
    background: #1a365d;
    color: white;
    border-radius: 4px;
    padding: 4mm 5mm;
    font-size: 9pt;
    line-height: 1.8;
    margin-top: 3mm;
}
.risk-chain .chain-arrow {
    color: #ed8936;
    font-weight: bold;
}

/* Solution table */
.sol-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 9.5pt;
}
.sol-table th {
    background: #1a365d;
    color: white;
    padding: 3mm 4mm;
    text-align: left;
    font-size: 9.5pt;
}
.sol-table td {
    padding: 3mm 4mm;
    border-bottom: 0.5px solid #e2e8f0;
    vertical-align: top;
}
.sol-table tr:nth-child(even) {
    background: #f7fafc;
}

/* Knowledge base grid */
.kb-grid {
    display: flex;
    gap: 4mm;
}
.kb-card {
    flex: 1;
    background: #f7fafc;
    border: 1px solid #e2e8f0;
    border-top: 3px solid #2b6cb0;
    border-radius: 4px;
    padding: 4mm;
    text-align: center;
}
.kb-card.highlight {
    border-top-color: #ed8936;
    background: #fffaf0;
}
.kb-card .kb-title {
    font-size: 12pt;
    font-weight: bold;
    color: #1a365d;
    margin-bottom: 2mm;
}
.kb-card .kb-items {
    font-size: 9pt;
    color: #4a5568;
    text-align: left;
    line-height: 1.7;
}

/* Flow */
.flow-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 3mm;
    margin: 5mm 0;
}
.flow-box {
    border: 1.5px solid #cbd5e0;
    border-radius: 5px;
    padding: 4mm 5mm;
    text-align: center;
    font-size: 9.5pt;
    line-height: 1.5;
    width: 20%;
}
.flow-box.ai {
    border-color: #2b6cb0;
    background: #ebf8ff;
}
.flow-box.human {
    border-color: #ed8936;
    background: #fffaf0;
}
.flow-box.output {
    border-color: #38a169;
    background: #f0fff4;
}
.flow-box .flow-label {
    font-size: 8pt;
    color: #718096;
    margin-bottom: 1mm;
}
.flow-box b {
    font-size: 10pt;
    color: #1a365d;
}
.flow-arrow {
    color: #a0aec0;
    font-size: 18pt;
}

/* Demo placeholder */
.demo-placeholder {
    background: #edf2f7;
    border: 2px dashed #cbd5e0;
    border-radius: 6px;
    height: 55mm;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #a0aec0;
    font-size: 12pt;
    margin-bottom: 4mm;
}

/* Value metric */
.metric-grid {
    display: flex;
    gap: 5mm;
}
.metric-card {
    flex: 1;
    text-align: center;
    background: #f7fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 5mm 3mm;
}
.metric-card .metric-num {
    font-size: 24pt;
    font-weight: bold;
    color: #1a365d;
    line-height: 1.2;
}
.metric-card .metric-unit {
    font-size: 10pt;
    color: #ed8936;
    font-weight: bold;
}
.metric-card .metric-label {
    font-size: 9pt;
    color: #718096;
    margin-top: 2mm;
}

/* Team */
.team-grid {
    display: flex;
    gap: 5mm;
}
.team-card {
    flex: 1;
    background: #f7fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 5mm;
    text-align: center;
}
.team-card .team-role {
    font-size: 13pt;
    font-weight: bold;
    color: #1a365d;
    margin-bottom: 2mm;
}
.team-card .team-desc {
    font-size: 9.5pt;
    color: #4a5568;
    line-height: 1.6;
}

/* Milestone */
.milestone-row {
    display: flex;
    align-items: center;
    gap: 3mm;
    margin: 4mm 0;
}
.milestone-dot {
    width: 8mm;
    height: 8mm;
    border-radius: 50%;
    background: #2b6cb0;
    flex-shrink: 0;
}
.milestone-dot.done {
    background: #38a169;
}
.milestone-dot.current {
    background: #ed8936;
}
.milestone-line {
    width: 15mm;
    height: 2px;
    background: #e2e8f0;
    flex-shrink: 0;
}
.milestone-text {
    font-size: 9.5pt;
}

/* Cooperation steps */
.coop-step {
    display: flex;
    align-items: center;
    gap: 4mm;
    margin-bottom: 4mm;
}
.coop-num {
    width: 12mm;
    height: 12mm;
    border-radius: 50%;
    background: #1a365d;
    color: white;
    font-size: 14pt;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.coop-content {
    flex: 1;
}
.coop-content .coop-title {
    font-size: 12pt;
    font-weight: bold;
    color: #1a365d;
}
.coop-content .coop-desc {
    font-size: 9.5pt;
    color: #4a5568;
}

/* AI boundary table */
.boundary-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 9.5pt;
}
.boundary-table th {
    padding: 3mm 4mm;
    text-align: center;
    font-size: 11pt;
    color: white;
}
.boundary-table th.ai-col {
    background: #2b6cb0;
    width: 50%;
}
.boundary-table th.human-col {
    background: #ed8936;
    width: 50%;
}
.boundary-table td {
    padding: 2.5mm 4mm;
    border-bottom: 0.5px solid #e2e8f0;
    vertical-align: top;
    font-size: 9.5pt;
}
.boundary-table td.ai-cell {
    background: #ebf8ff;
}
.boundary-table td.human-cell {
    background: #fffaf0;
}

/* Last page */
.closing {
    background: #1a365d;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}
.closing .cta {
    font-size: 10pt;
    color: #a0aec0;
    margin-top: 8mm;
}
.contact-placeholder {
    margin-top: 8mm;
    padding: 4mm 8mm;
    border: 1px dashed #4a5568;
    border-radius: 4px;
    color: #718096;
    font-size: 10pt;
}
</style>
</head>
<body>

<!-- ==================== Page 1: Cover ==================== -->
<div class="slide cover">
    <h1>GateZero</h1>
    <div class="tagline">AI驱动的APQP报价前引擎</div>
    <div class="sub">帮Tier 1更快、更准、更完整地完成报价准备</div>
    <div class="meta-info">方案介绍 · 2026年3月</div>
</div>

<!-- ==================== Page 2: Pain Points ==================== -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">行业痛点</div>
        <div class="slide-logo">GateZero</div>
    </div>
    <div class="subtitle">Tier 1在报价前阶段面临的真实挑战</div>

    <div class="two-col">
        <div class="col-55">
            <div class="pain-card">
                <div><span class="num">1</span><span class="title">风险盲区，从亏钱到召回</span></div>
                <div class="desc">低估技术难度，报价后才发现做不了或亏钱；隐患带入量产，最严重导致召回——一次召回可能上亿损失</div>
            </div>
            <div class="pain-card">
                <div><span class="num">2</span><span class="title">管理能力不足，丢单</span></div>
                <div class="desc">OEM评审要求越来越高（Stellantis SSTS、VW Formel-Q、BMW QMT……），管理能力跟不上，通不过评审</div>
            </div>
            <div class="pain-card">
                <div><span class="num">3</span><span class="title">人才流失，能力断层</span></div>
                <div class="desc">老工程师走了，新人不知道坑在哪；同一家公司，不同人做出来的水平参差不齐</div>
            </div>
            <div class="pain-card">
                <div><span class="num">4</span><span class="title">效率低，响应慢</span></div>
                <div class="desc">客户文件包翻半天还可能漏；多个RFQ同时来人手不够，窗口期有限，慢就丢单</div>
            </div>
        </div>
        <div class="col-45">
            <div class="risk-chain">
                <div style="font-size: 10pt; font-weight: bold; margin-bottom: 2mm; color: #ed8936;">所有痛点汇入同一条风险链：</div>
                报价前没看清风险<br>
                <span class="chain-arrow">→</span> 接了不该接的单<br>
                <span class="chain-arrow">→</span> 开发中发现问题，成本超支<br>
                <span class="chain-arrow">→</span> 赶工期妥协质量<br>
                <span class="chain-arrow">→</span> 量产后暴露问题<br>
                <span class="chain-arrow">→</span> 客户投诉 / 0公里故障<br>
                <span class="chain-arrow">→</span> 召回<br>
                <span class="chain-arrow">→</span> 巨额损失 + 失去客户
                <div style="margin-top: 4mm; padding-top: 3mm; border-top: 1px solid #4a5568; font-size: 11pt; color: #ed8936; font-weight: bold;">
                    越早发现问题，修正成本越低。<br>GateZero在最前端截断这条链。
                </div>
            </div>
        </div>
    </div>
    <div class="page-num">2 / 10</div>
</div>

<!-- ==================== Page 3: What is GateZero ==================== -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">GateZero是什么</div>
        <div class="slide-logo">GateZero</div>
    </div>
    <div class="subtitle">聚焦APQP第零阶段——报价前可行性评审</div>

    <div class="two-col">
        <div class="col-50">
            <div class="card blue" style="margin-bottom: 5mm;">
                <div class="card-title">在APQP中的位置</div>
                <div class="card-body" style="font-size: 9.5pt; line-height: 1.8;">
                    <b style="color: #ed8936; font-size: 11pt;">Phase 0 报价前可行性评审</b> ← GateZero<br>
                    Phase 1 计划与定义<br>
                    Phase 2 产品设计与开发<br>
                    Phase 3 过程设计与开发<br>
                    Phase 4 产品和过程验证<br>
                    Phase 5 量产与持续改进
                </div>
            </div>
            <div class="card highlight">
                <div class="card-title">为什么Phase 0最关键</div>
                <div class="card-body">
                    Phase 0是所有后续阶段的前提。报价前没看清的风险，会在每个阶段放大成本。<b>这是APQP"左移"的核心逻辑。</b>
                </div>
            </div>
        </div>
        <div class="col-50">
            <div style="font-size: 11pt; font-weight: bold; color: #1a365d; margin-bottom: 3mm;">AI与人的分工</div>
            <table class="boundary-table">
                <tr>
                    <th class="ai-col">AI负责</th>
                    <th class="human-col">人来决策</th>
                </tr>
                <tr>
                    <td class="ai-cell">客户要求了什么</td>
                    <td class="human-cell">这个能不能做</td>
                </tr>
                <tr>
                    <td class="ai-cell">哪些要求还没覆盖</td>
                    <td class="human-cell">用什么工艺方案</td>
                </tr>
                <tr>
                    <td class="ai-cell">这类零件常见失效模式</td>
                    <td class="human-cell">报多少价</td>
                </tr>
                <tr>
                    <td class="ai-cell">这个OEM通常关注什么</td>
                    <td class="human-cell">接不接这个单</td>
                </tr>
                <tr>
                    <td class="ai-cell">按模板生成交付物初稿</td>
                    <td class="human-cell">承诺达到什么标准</td>
                </tr>
                <tr>
                    <td class="ai-cell">检查文档间一致性</td>
                    <td class="human-cell">例外项是否接受</td>
                </tr>
            </table>
            <div style="font-size: 9pt; color: #718096; margin-top: 3mm; text-align: center;">
                AI是能力放大器，不是替代者
            </div>
        </div>
    </div>
    <div class="page-num">3 / 10</div>
</div>

<!-- ==================== Page 4: Core Capabilities ==================== -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">核心功能</div>
        <div class="slide-logo">GateZero</div>
    </div>
    <div class="subtitle">四大能力，对应解决四大痛点</div>

    <table class="sol-table">
        <tr>
            <th style="width: 18%;">你头疼的</th>
            <th style="width: 42%;">GateZero怎么帮你</th>
            <th style="width: 22%;">业务结果</th>
            <th style="width: 18%;">关键能力</th>
        </tr>
        <tr>
            <td style="font-weight: bold; color: #e53e3e;">风险盲区</td>
            <td>技术/制造/质量/成本四维度系统性评审<br>提示历史同类项目踩过的坑</td>
            <td style="color: #2b6cb0; font-weight: bold;">接单前看清风险<br>不再拍脑袋</td>
            <td>系统性可行性评审</td>
        </tr>
        <tr>
            <td style="font-weight: bold; color: #e53e3e;">OEM门槛高</td>
            <td>自动匹配OEM特殊要求（SSTS/Formel-Q/QMT等）<br>按标准生成合规交付物</td>
            <td style="color: #2b6cb0; font-weight: bold;">通过更多OEM评审<br>扩大接单范围</td>
            <td>OEM要求匹配</td>
        </tr>
        <tr>
            <td style="font-weight: bold; color: #e53e3e;">人才断层</td>
            <td>历史经验沉淀在系统里，自动提示该注意什么<br>标准化流程+AI引导，统一输出质量</td>
            <td style="color: #2b6cb0; font-weight: bold;">人走经验不走<br>新人也能上手</td>
            <td>组织经验沉淀</td>
        </tr>
        <tr>
            <td style="font-weight: bold; color: #e53e3e;">效率低</td>
            <td>自动解析客户文件包，结构化提取要求<br>自动生成交付物初稿，人只做审核</td>
            <td style="color: #2b6cb0; font-weight: bold;">天级变小时级<br>需求零遗漏</td>
            <td>智能文档处理</td>
        </tr>
    </table>

    <div style="margin-top: 6mm; text-align: center;">
        <div class="card highlight" style="display: inline-block; padding: 3mm 8mm;">
            <span style="font-size: 11pt; color: #1a365d; font-weight: bold;">每个人都能拿出资深工程师水平的报价准备</span>
        </div>
    </div>
    <div class="page-num">4 / 10</div>
</div>

<!-- ==================== Page 5: Knowledge Base ==================== -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">知识底座</div>
        <div class="slide-logo">GateZero</div>
    </div>
    <div class="subtitle">整合四类知识，让每个人都能调用整个组织的最佳实践</div>

    <div class="kb-grid">
        <div class="kb-card">
            <div class="kb-title">行业规范</div>
            <div class="kb-items">
                · IATF 16949<br>
                · AIAG五大核心工具<br>
                · 零部件技术标准<br>
                · 环保法规(REACH等)
            </div>
        </div>
        <div class="kb-card">
            <div class="kb-title">OEM要求</div>
            <div class="kb-items">
                · Stellantis SSTS<br>
                · VW Formel-Q<br>
                · BMW QMT<br>
                · GM BIQS ...
            </div>
        </div>
        <div class="kb-card highlight">
            <div class="kb-title" style="color: #c05621;">组织经验</div>
            <div class="kb-items">
                · 历史项目经验<br>
                · 失效模式库<br>
                · OEM×零件组合经验<br>
                · 工艺能力边界<br>
                · <b>越用越多</b>
            </div>
        </div>
        <div class="kb-card">
            <div class="kb-title">标准流程</div>
            <div class="kb-items">
                · 可行性评审框架<br>
                · 标准化工作流<br>
                · 多轮人工确认<br>
                · 模板与一致性校验
            </div>
        </div>
    </div>

    <div class="two-col" style="margin-top: 6mm;">
        <div class="col-60">
            <div class="card highlight">
                <div class="card-title">组织经验——GateZero的独特护城河</div>
                <div class="card-body">
                    每完成一个项目，经验自动沉淀回知识库。用得越多，系统越懂你的业务。<br>
                    这是竞品无法复制的——因为<b>经验来自你自己的项目</b>。
                </div>
            </div>
        </div>
        <div class="col-40">
            <div class="card blue">
                <div class="card-title">知识回写机制</div>
                <div class="card-body">
                    项目完成 → 自动提取经验<br>
                    人工确认 → 写入知识库<br>
                    下次遇到同类项目自动调用
                </div>
            </div>
        </div>
    </div>
    <div class="page-num">5 / 10</div>
</div>

<!-- ==================== Page 6: Workflow ==================== -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">使用流程</div>
        <div class="slide-logo">GateZero</div>
    </div>
    <div class="subtitle">从收到RFQ到输出完整报价准备包，AI与人协作完成</div>

    <div class="flow-row">
        <div class="flow-box">
            <div class="flow-label">输入</div>
            <b>收到客户<br>RFQ文件包</b>
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-box ai">
            <div class="flow-label">AI自动</div>
            <b>文档解析</b><br>
            读取全部文件<br>识别OEM/零件类型<br>结构化提取数据
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-box ai">
            <div class="flow-label">AI自动</div>
            <b>需求分析</b><br>
            完整性检查<br>特性提取<br>质量目标识别
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-box human">
            <div class="flow-label">人工确认</div>
            <b>审核补充</b><br>
            确认分析结果<br>补充工程判断
        </div>
    </div>

    <div class="flow-row">
        <div class="flow-box ai">
            <div class="flow-label">AI自动</div>
            <b>评估支持</b><br>
            能力对比/历史匹配<br>风险汇总/例外提示
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-box human">
            <div class="flow-label">人工确认</div>
            <b>决策判断</b><br>
            确认风险评级<br>做出接单决策
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-box ai">
            <div class="flow-label">AI自动</div>
            <b>交付物生成</b><br>
            按模板生成文档<br>一致性检查
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-box output">
            <div class="flow-label">输出</div>
            <b>完整报价<br>准备包</b>
        </div>
    </div>

    <div style="text-align: center; margin-top: 4mm;">
        <div class="card" style="display: inline-block; padding: 3mm 8mm; background: #fffaf0; border-color: #ed8936;">
            <span style="font-size: 10pt; color: #1a365d;">
                <b>三层HALT保护：</b>每个关键节点都需人工确认后才进入下一步，确保AI不会"自作主张"
            </span>
        </div>
    </div>
    <div class="page-num">6 / 10</div>
</div>

<!-- ==================== Page 7: Demo ==================== -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">产品展示</div>
        <div class="slide-logo">GateZero</div>
    </div>
    <div class="subtitle">GateZero实际工作界面</div>

    <div class="two-col">
        <div class="col-50">
            <div style="font-weight: bold; color: #1a365d; font-size: 10pt; margin-bottom: 2mm;">文档解析与需求提取</div>
            <div class="demo-placeholder">[ 产品截图占位 ]</div>
            <div style="font-weight: bold; color: #1a365d; font-size: 10pt; margin-bottom: 2mm;">风险评估与历史匹配</div>
            <div class="demo-placeholder">[ 产品截图占位 ]</div>
        </div>
        <div class="col-50">
            <div style="font-weight: bold; color: #1a365d; font-size: 10pt; margin-bottom: 2mm;">交付物自动生成</div>
            <div class="demo-placeholder">[ 产品截图占位 ]</div>
            <div style="font-weight: bold; color: #1a365d; font-size: 10pt; margin-bottom: 2mm;">输出报价准备包</div>
            <div class="demo-placeholder">[ 产品截图占位 ]</div>
        </div>
    </div>
    <div class="page-num">7 / 10</div>
</div>

<!-- ==================== Page 8: Customer Value ==================== -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">客户价值</div>
        <div class="slide-logo">GateZero</div>
    </div>
    <div class="subtitle">使用GateZero后的预期收益</div>

    <div class="metric-grid">
        <div class="metric-card">
            <div class="metric-num">天 → 小时</div>
            <div class="metric-unit">报价准备效率</div>
            <div class="metric-label">自动解析+自动生成<br>大幅缩短准备周期</div>
        </div>
        <div class="metric-card">
            <div class="metric-num">↓ 系统性</div>
            <div class="metric-unit">风险遗漏率</div>
            <div class="metric-label">四维度评审+历史匹配<br>不再靠拍脑袋</div>
        </div>
        <div class="metric-card">
            <div class="metric-num">↑ 标准化</div>
            <div class="metric-unit">输出质量一致性</div>
            <div class="metric-label">AI引导+模板规范<br>不因人而异</div>
        </div>
        <div class="metric-card">
            <div class="metric-num">0 流失</div>
            <div class="metric-unit">组织经验沉淀</div>
            <div class="metric-label">人走经验不走<br>越用越强</div>
        </div>
    </div>

    <div style="margin-top: 8mm;">
        <div style="font-size: 11pt; font-weight: bold; color: #1a365d; margin-bottom: 4mm;">业务成果</div>
        <div class="two-col">
            <div class="col-50">
                <div class="card green">
                    <div class="card-title" style="color: #276749;">接得到单</div>
                    <div class="card-body">满足更多OEM的评审门槛，扩大可竞标范围</div>
                </div>
                <div class="card green">
                    <div class="card-title" style="color: #276749;">接对的单</div>
                    <div class="card-body">系统性风险评审，避免接了不该接的单</div>
                </div>
            </div>
            <div class="col-50">
                <div class="card green">
                    <div class="card-title" style="color: #276749;">接得起单</div>
                    <div class="card-body">准确识别成本风险，报价不亏钱</div>
                </div>
                <div class="card green">
                    <div class="card-title" style="color: #276749;">为后续APQP奠基</div>
                    <div class="card-body">Phase 0做扎实，后续阶段事半功倍</div>
                </div>
            </div>
        </div>
    </div>
    <div class="page-num">8 / 10</div>
</div>

<!-- ==================== Page 9: Team & Status ==================== -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">团队与现状</div>
        <div class="slide-logo">GateZero</div>
    </div>

    <div style="font-size: 11pt; font-weight: bold; color: #1a365d; margin-bottom: 4mm;">核心团队</div>
    <div class="team-grid">
        <div class="team-card">
            <div class="team-role">AI CTO</div>
            <div class="team-desc">技术架构<br>AI产品落地</div>
        </div>
        <div class="team-card">
            <div class="team-role">OEM背景</div>
            <div class="team-desc">管理层经验<br>懂OEM逻辑</div>
        </div>
        <div class="team-card">
            <div class="team-role">Tier 1管理</div>
            <div class="team-desc">供应商管理<br>懂业务痛点</div>
        </div>
        <div class="team-card">
            <div class="team-role">Tier 1执行</div>
            <div class="team-desc">一线APQP<br>懂落地细节</div>
        </div>
    </div>

    <div style="font-size: 11pt; font-weight: bold; color: #1a365d; margin: 8mm 0 4mm 0;">团队优势</div>
    <div class="card blue">
        <div class="card-body" style="font-size: 10pt;">
            OEM + Tier 1 + AI 三方背景互补：<b>既懂OEM怎么审，也懂Tier 1怎么做，还懂AI怎么落地。</b>
        </div>
    </div>

    <div style="font-size: 11pt; font-weight: bold; color: #1a365d; margin: 8mm 0 4mm 0;">当前进展</div>
    <div class="two-col">
        <div class="col-50">
            <div class="card green" style="text-align: center; padding: 5mm;">
                <div style="font-size: 14pt; font-weight: bold; color: #276749;">产品Demo已完成</div>
                <div class="card-body">核心功能可演示</div>
            </div>
        </div>
        <div class="col-50">
            <div class="card green" style="text-align: center; padding: 5mm;">
                <div style="font-size: 14pt; font-weight: bold; color: #276749;">付费试点客户</div>
                <div class="card-body">已进入实际业务验证</div>
            </div>
        </div>
    </div>
    <div class="page-num">9 / 10</div>
</div>

<!-- ==================== Page 10: Cooperation ==================== -->
<div class="slide">
    <div class="slide-header">
        <div class="slide-title">合作方式</div>
        <div class="slide-logo">GateZero</div>
    </div>
    <div class="subtitle">从了解到落地，简单三步</div>

    <div style="max-width: 220mm;">
        <div class="coop-step">
            <div class="coop-num">1</div>
            <div class="coop-content">
                <div class="coop-title">需求沟通</div>
                <div class="coop-desc">了解你的业务场景、主要OEM客户、零件类型和当前痛点，评估匹配度</div>
            </div>
        </div>
        <div class="coop-step">
            <div class="coop-num">2</div>
            <div class="coop-content">
                <div class="coop-title">试点验证</div>
                <div class="coop-desc">选取1-2个真实RFQ项目进行试点，用实际业务验证GateZero的价值</div>
            </div>
        </div>
        <div class="coop-step">
            <div class="coop-num">3</div>
            <div class="coop-content">
                <div class="coop-title">正式部署</div>
                <div class="coop-desc">根据试点结果定制部署方案，导入组织知识库，支持本地部署，数据不离开企业</div>
            </div>
        </div>
    </div>

    <div class="two-col" style="margin-top: 8mm;">
        <div class="col-50">
            <div class="card blue">
                <div class="card-title">部署特点</div>
                <div class="card-body">
                    · 支持本地部署，数据安全可控<br>
                    · 组织知识库完全属于客户<br>
                    · 按需定制，适配不同OEM体系
                </div>
            </div>
        </div>
        <div class="col-50">
            <div class="card highlight">
                <div class="card-title">为什么现在开始</div>
                <div class="card-body">
                    · OEM对供应商的要求只会越来越高<br>
                    · 越早沉淀组织经验，竞争优势越大<br>
                    · AI能力在快速进化，早用早受益
                </div>
            </div>
        </div>
    </div>

    <div style="text-align: center; margin-top: 8mm;">
        <div class="contact-placeholder">[ 联系方式占位 ]</div>
    </div>
    <div class="page-num">10 / 10</div>
</div>

</body>
</html>
"""


def main():
    output = '/home/chu2026/Documents/github/automotive-apqp-agent/docs/gatezero-deck.pdf'
    HTML(string=html_content).write_pdf(output)
    print(f'PDF generated: {output}')


if __name__ == '__main__':
    main()
