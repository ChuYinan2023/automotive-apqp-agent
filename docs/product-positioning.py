#!/usr/bin/env python3
"""Generate GateZero product positioning PDF using weasyprint."""

from weasyprint import HTML

html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@page {
    size: A4;
    margin: 18mm 15mm 18mm 15mm;
    @bottom-center {
        content: "- " counter(page) " -";
        font-size: 8pt;
        color: #a0aec0;
    }
    @top-left {
        content: "GateZero 产品定位文档";
        font-size: 7pt;
        color: #a0aec0;
    }
}
@page :first {
    @bottom-center { content: none; }
    @top-left { content: none; }
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    font-family: "Noto Sans CJK SC", "Noto Sans SC", sans-serif;
    color: #2d3748;
    font-size: 9.5pt;
    line-height: 1.7;
}

/* Cover */
.cover {
    text-align: center;
    padding-top: 80mm;
    page-break-after: always;
}
.cover h1 {
    font-size: 36pt;
    color: #1a365d;
    letter-spacing: 3px;
    margin-bottom: 4mm;
}
.cover .tagline {
    font-size: 13pt;
    color: #718096;
    margin-bottom: 2mm;
}
.cover .sub {
    font-size: 10pt;
    color: #a0aec0;
    margin-top: 8mm;
}
.cover .info-box {
    margin: 15mm auto 0 auto;
    width: 60%;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    background: #f7fafc;
    padding: 5mm 8mm;
    text-align: left;
    font-size: 9pt;
    color: #4a5568;
    line-height: 2;
}
.cover .info-box b { color: #1a365d; }

/* Headings */
h2 {
    font-size: 16pt;
    color: #1a365d;
    margin-top: 8mm;
    margin-bottom: 4mm;
    padding-bottom: 2mm;
    border-bottom: 2px solid #ed8936;
}
h3 {
    font-size: 12pt;
    color: #2b6cb0;
    margin-top: 6mm;
    margin-bottom: 3mm;
}
h4 {
    font-size: 10pt;
    color: #4a5568;
    margin-top: 4mm;
    margin-bottom: 2mm;
}

/* Paragraphs */
p {
    margin-bottom: 3mm;
    text-align: justify;
}
.emphasis {
    color: #1a365d;
    font-weight: bold;
}
.highlight-box {
    background: #ebf8ff;
    border-left: 3px solid #2b6cb0;
    padding: 4mm 5mm;
    margin: 4mm 0;
    font-size: 9.5pt;
    color: #1a365d;
}
.conclusion-box {
    background: #f0fff4;
    border: 1px solid #38a169;
    border-radius: 4px;
    padding: 5mm 6mm;
    margin: 5mm 0;
    font-size: 10pt;
    color: #1a365d;
    text-align: center;
    font-weight: bold;
}

/* APQP diagram */
.apqp-flow {
    width: 100%;
    border-collapse: collapse;
    margin: 4mm 0;
    font-size: 8.5pt;
}
.apqp-flow td {
    text-align: center;
    padding: 3mm 1mm;
    vertical-align: middle;
}
.apqp-flow .phase-box {
    border: 1px solid #cbd5e0;
    border-radius: 3px;
    background: #f7fafc;
    padding: 2mm 2mm;
}
.apqp-flow .phase-box.active {
    border: 2px solid #ed8936;
    background: #fffaf0;
    font-weight: bold;
    color: #1a365d;
}
.apqp-flow .arrow {
    color: #a0aec0;
    font-size: 12pt;
}

/* Pain list */
.pain-item {
    margin-bottom: 4mm;
    padding-left: 3mm;
}
.pain-item .pain-title {
    font-weight: bold;
    color: #1a365d;
    font-size: 10pt;
}
.pain-item .pain-num {
    color: #ed8936;
    font-weight: bold;
}
.pain-item ul {
    margin: 1mm 0 1mm 6mm;
    font-size: 9pt;
    color: #4a5568;
}
.pain-item ul li {
    margin-bottom: 1mm;
}
.pain-item .essence {
    color: #2b6cb0;
    font-weight: bold;
    font-size: 9pt;
}

/* Risk chain */
.risk-chain {
    background: #fff5f5;
    border-left: 3px solid #e53e3e;
    padding: 4mm 5mm;
    margin: 4mm 0;
    font-size: 8.5pt;
    color: #4a5568;
    line-height: 2;
}
.risk-chain .step { margin-left: 4mm; }
.risk-chain .step:before { content: "→ "; color: #e53e3e; font-weight: bold; }

/* Value table */
.value-table {
    width: 100%;
    border-collapse: collapse;
    margin: 4mm 0;
    font-size: 8.5pt;
}
.value-table th {
    background: #1a365d;
    color: white;
    padding: 2.5mm 3mm;
    text-align: center;
    font-size: 8.5pt;
}
.value-table td {
    padding: 2.5mm 3mm;
    border-bottom: 0.5px solid #e2e8f0;
    vertical-align: top;
    line-height: 1.6;
}
.value-table tr:nth-child(even) {
    background: #f7fafc;
}
.value-table .pain-header td {
    background: #edf2f7;
    font-weight: bold;
    color: #1a365d;
    border-bottom: 1px solid #cbd5e0;
}

/* Knowledge base */
.kb-table {
    width: 100%;
    border-collapse: collapse;
    margin: 4mm 0;
    font-size: 8.5pt;
}
.kb-table th {
    background: #2b6cb0;
    color: white;
    padding: 2mm 3mm;
    text-align: center;
    font-weight: bold;
    width: 25%;
}
.kb-table th.highlight {
    background: #ed8936;
}
.kb-table td {
    background: #f7fafc;
    padding: 3mm 3mm;
    border: 0.5px solid #e2e8f0;
    vertical-align: top;
    line-height: 1.8;
}

/* Goal diagram */
.goal-table {
    width: 100%;
    border-collapse: collapse;
    margin: 4mm 0;
    font-size: 9pt;
}
.goal-table td {
    text-align: center;
    vertical-align: top;
    padding: 3mm 2mm;
    width: 33.33%;
}
.goal-box {
    border: 1px solid #cbd5e0;
    border-radius: 4px;
    padding: 3mm;
    background: #f7fafc;
}
.goal-box .goal-title {
    font-size: 11pt;
    font-weight: bold;
    color: #1a365d;
    margin-bottom: 2mm;
}
.goal-box .goal-desc {
    font-size: 8.5pt;
    color: #4a5568;
}

/* AI vs Human */
.role-table {
    width: 100%;
    border-collapse: collapse;
    margin: 4mm 0;
    font-size: 8.5pt;
}
.role-table th {
    padding: 2.5mm 3mm;
    text-align: center;
    font-size: 9pt;
    color: white;
}
.role-table th.ai { background: #2b6cb0; }
.role-table th.human { background: #38a169; }
.role-table td {
    padding: 2mm 3mm;
    border-bottom: 0.5px solid #e2e8f0;
    vertical-align: top;
    line-height: 1.6;
    width: 50%;
}
.role-table tr:nth-child(even) { background: #f7fafc; }

/* FAQ */
.faq-item {
    margin-bottom: 4mm;
}
.faq-item .q {
    font-weight: bold;
    color: #1a365d;
    font-size: 10pt;
    margin-bottom: 1mm;
}
.faq-item .a {
    color: #4a5568;
    padding-left: 3mm;
    font-size: 9pt;
}
</style>
</head>
<body>

<!-- Cover Page -->
<div class="cover">
    <h1>GateZero</h1>
    <div class="tagline">AI驱动的APQP Phase 0</div>
    <div class="sub">帮Tier 1更好地完成报价、管控前期风险、赢得订单</div>
    <div class="info-box">
        <b>产品定位文档</b><br>
        <b>文档类型：</b>产品定位与价值主张<br>
        <b>目标读者：</b>团队内部 / 投资人 / 合作伙伴<br>
        <b>日期：</b>2026-03-05
    </div>
</div>

<!-- Section 1: Position in APQP -->
<h2>一、GateZero在APQP中的位置</h2>
<p>GateZero聚焦APQP的第零阶段——<span class="emphasis">报价前可行性评审</span>。这是整个APQP生命周期的起点，决定了一个项目"接不接、能不能接、该怎么接"。</p>

<table class="apqp-flow">
    <tr>
        <td><div class="phase-box active"><b>GateZero</b><br>Phase 0<br>报价前<br>可行性评审</div></td>
        <td class="arrow">&#10132;</td>
        <td><div class="phase-box">Phase 1<br>计划<br>与定义</div></td>
        <td class="arrow">&#10132;</td>
        <td><div class="phase-box">Phase 2<br>产品设计<br>与开发</div></td>
        <td class="arrow">&#10132;</td>
        <td><div class="phase-box">Phase 3<br>过程设计<br>与开发</div></td>
        <td class="arrow">&#10132;</td>
        <td><div class="phase-box">Phase 4<br>验证<br>PPAP</div></td>
        <td class="arrow">&#10132;</td>
        <td><div class="phase-box">Phase 5<br>量产<br>与改进</div></td>
    </tr>
</table>

<div class="highlight-box">
    Phase 0为什么重要：它是后面所有阶段的前提。报价前没看清的风险，会在后续每个阶段放大成本。越早发现问题，修正成本越低——这是APQP"左移"的核心逻辑。
</div>

<!-- Section 2: Problems -->
<h2>二、解决什么问题</h2>
<p>Tier 1在报价前阶段面临的真实痛点：</p>

<div class="pain-item">
    <p><span class="pain-num">1.</span> <span class="pain-title">风险盲区，从亏钱到召回</span></p>
    <ul>
        <li>低估技术难度，报了价才发现做不了或亏钱</li>
        <li>没有系统性的可行性评审，靠拍脑袋</li>
        <li>勉强接单后，设计或工艺上的隐患带入量产</li>
        <li>最严重的后果：产品召回——一次召回可能是几百万到上亿的损失，甚至直接出局OEM供应商名录</li>
    </ul>
    <p class="essence">本质：越早发现问题，修正成本越低</p>
</div>

<div class="pain-item">
    <p><span class="pain-num">2.</span> <span class="pain-title">管理能力不足，丢单</span></p>
    <ul>
        <li>很多Tier 1的报价前APQP只做了一小部分（填几张表就报价了）</li>
        <li>OEM要求越来越高（Stellantis的SSTS、VW的Formel-Q、BMW的QMT……）</li>
        <li>管理能力跟不上，通不过OEM的供应商评审，接不到高价值订单</li>
    </ul>
    <p class="essence">本质：能力门槛挡住了业务增长</p>
</div>

<div class="pain-item">
    <p><span class="pain-num">3.</span> <span class="pain-title">人才流失，能力断层</span></p>
    <ul>
        <li>有经验的工程师走了，报价质量直接下降</li>
        <li>新人不知道"上次给这个OEM报价时要注意什么"</li>
        <li>同一家公司，A来做和B来做，输出水平差距巨大</li>
    </ul>
    <p class="essence">本质：组织能力依赖个人，不可持续</p>
</div>

<div class="pain-item">
    <p><span class="pain-num">4.</span> <span class="pain-title">信息散落，效率低，耗时长</span></p>
    <ul>
        <li>客户文件包翻半天，关键要求还是可能漏掉</li>
        <li>重复劳动多，每次报价都从头来</li>
        <li>报价准备周期长，响应慢——OEM给的窗口期有限，准备慢就错过机会</li>
        <li>多个RFQ同时来的时候，人手不够，只能挑着做，丢掉潜在订单</li>
    </ul>
    <p class="essence">本质：快就是竞争力，慢就丢单</p>
</div>

<p>以上所有痛点，最终都可能汇入同一条风险链：</p>

<div class="risk-chain">
    <div>报价前没看清风险</div>
    <div class="step">接了不该接的单</div>
    <div class="step">开发中发现问题，成本超支</div>
    <div class="step">赶工期妥协质量</div>
    <div class="step">量产后暴露问题</div>
    <div class="step">客户投诉 / 0公里故障</div>
    <div class="step">召回</div>
    <div class="step">巨额损失 + 失去客户</div>
</div>

<div class="conclusion-box">GateZero的价值就是在最前端截断这条链。</div>

<!-- Section 3: Value -->
<h2>三、创造什么价值</h2>

<table class="value-table">
    <tr>
        <th style="width:20%">痛点</th>
        <th style="width:45%">AI做了什么</th>
        <th style="width:35%">业务结果</th>
    </tr>
    <tr class="pain-header"><td colspan="3">1. 风险盲区</td></tr>
    <tr>
        <td>拍脑袋接单，做到一半发现做不了</td>
        <td>系统性可行性评审，技术/制造/质量/成本四维度风险前置识别</td>
        <td>接对的单不亏钱，从源头避免召回</td>
    </tr>
    <tr class="pain-header"><td colspan="3">2. 管理能力不足</td></tr>
    <tr>
        <td>OEM要求高，评审通不过</td>
        <td>自动匹配OEM评审要求，生成合规交付物</td>
        <td>满足更多OEM门槛，扩大接单范围</td>
    </tr>
    <tr class="pain-header"><td colspan="3">3. 人才流失</td></tr>
    <tr>
        <td>老工程师走了，新人不知道坑在哪</td>
        <td>提示历史失效模式和风险经验</td>
        <td>人走经验不走，组织能力不断层</td>
    </tr>
    <tr>
        <td>不同人做出来水平参差不齐</td>
        <td>标准化流程+AI引导，统一输出质量</td>
        <td>每个人都能拿出资深工程师水平的报价</td>
    </tr>
    <tr class="pain-header"><td colspan="3">4. 效率与耗时</td></tr>
    <tr>
        <td>客户文件包复杂，翻半天还可能漏</td>
        <td>自动解析全部文件，结构化提取要求，标记缺失项</td>
        <td>需求零遗漏，避免漏看关键要求</td>
    </tr>
    <tr>
        <td>报价准备耗时长，窗口期紧</td>
        <td>自动生成交付物初稿，人只做审核和判断</td>
        <td>响应速度从天级到小时级</td>
    </tr>
</table>

<!-- Section 4: Knowledge Base -->
<h2>四、AI的知识底座</h2>
<p>AI把四类知识整合在一起，让每个人都能调用整个组织的最佳实践：</p>

<table class="kb-table">
    <tr>
        <th>行业规范</th>
        <th>OEM要求</th>
        <th class="highlight">组织经验</th>
        <th>标准流程</th>
    </tr>
    <tr>
        <td>IATF 16949<br>AIAG五大核心工具<br>零部件技术标准<br>环保法规(REACH等)</td>
        <td>Stellantis SSTS<br>VW Formel-Q<br>BMW QMT<br>GM BIQS</td>
        <td>历史项目与教训<br>失效模式库<br>OEM×零件组合经验<br>工艺能力边界<br><b style="color:#ed8936;">越用越多</b></td>
        <td>可行性评审框架<br>标准化工作流<br>人工确认机制<br>模板与一致性校验</td>
    </tr>
</table>

<p>其中，<span class="emphasis">组织经验</span>是GateZero的独特护城河——每完成一个项目，经验自动沉淀回知识库，系统越用越懂你的业务。</p>

<div class="highlight-box">
    AI整合知识、提示风险、生成初稿；工程判断和商务决策始终由人把关。
</div>

<!-- Section 5: Business Goals -->
<h2>五、GateZero的业务目标</h2>

<table class="goal-table">
    <tr>
        <td>
            <div class="goal-box">
                <div class="goal-title">接得到单</div>
                <div class="goal-desc">满足OEM评审要求<br>通过能力门槛</div>
            </div>
        </td>
        <td>
            <div class="goal-box">
                <div class="goal-title">接对的单</div>
                <div class="goal-desc">识别风险，避免踩坑<br>不接亏钱的项目</div>
            </div>
        </td>
        <td>
            <div class="goal-box">
                <div class="goal-title">接得起单</div>
                <div class="goal-desc">准确报价，不亏钱<br>成本心中有数</div>
            </div>
        </td>
    </tr>
</table>

<div class="highlight-box" style="text-align: center; font-size: 10pt;">
    <b>拉平能力差距 &middot; 沉淀组织经验 &middot; 系统化风险评审 &middot; 加速报价响应</b><br>
    为后续APQP奠定高质量起点
</div>

<!-- Appendix: FAQ -->
<h2>附录：常见问题</h2>

<div class="faq-item">
    <p class="q">Q：AI会替我做工程判断吗？</p>
    <p class="a">不会。GateZero的AI负责信息整理、风险提示和文档生成，所有工程判断（能不能做、用什么方案）和商务决策（报多少价、接不接单）始终由人做出。AI是你的能力放大器，不是替代者。</p>
</div>

<table class="role-table">
    <tr>
        <th class="ai">AI做的</th>
        <th class="human">人做的</th>
    </tr>
    <tr>
        <td>"客户要求了什么"</td>
        <td>"这个能不能做"</td>
    </tr>
    <tr>
        <td>"哪些要求还没覆盖"</td>
        <td>"用什么工艺方案"</td>
    </tr>
    <tr>
        <td>"这类零件常见失效模式是什么"</td>
        <td>"报多少价"</td>
    </tr>
    <tr>
        <td>"这个OEM通常关注什么"</td>
        <td>"接不接这个单"</td>
    </tr>
    <tr>
        <td>"按模板生成交付物初稿"</td>
        <td>"我们承诺达到这个标准"</td>
    </tr>
    <tr>
        <td>"检查文档间一致性"</td>
        <td>"这个例外项我们接受"</td>
    </tr>
</table>

<div class="faq-item">
    <p class="q">Q：AI生成的文档可以直接用吗？</p>
    <p class="a">AI生成的是初稿，每一步都需要人工审核确认后才进入下一步。GateZero内置多轮确认机制，确保最终输出经过人的把关。</p>
</div>

<div class="faq-item">
    <p class="q">Q：我们的项目数据安全吗？</p>
    <p class="a">GateZero支持本地部署，数据不离开企业环境。组织经验和知识库完全属于客户自己。</p>
</div>

<div class="faq-item">
    <p class="q">Q：新人上手难吗？</p>
    <p class="a">GateZero的核心价值之一就是降低对个人经验的依赖。AI引导标准化流程，提示该注意什么、该检查什么，新人也能按资深工程师的标准完成报价准备。</p>
</div>

</body>
</html>
"""


def main():
    output = '/home/chu2026/Documents/github/automotive-apqp-agent/docs/product-positioning.pdf'
    HTML(string=html_content).write_pdf(output)
    print(f'PDF generated: {output}')


if __name__ == '__main__':
    main()
