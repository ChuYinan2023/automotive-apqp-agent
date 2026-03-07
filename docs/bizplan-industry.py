#!/usr/bin/env python3
"""Generate GateZero one-page business plan (industry investor version) PDF."""

from weasyprint import HTML

html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@page {
    size: A4;
    margin: 10mm 14mm 10mm 14mm;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    font-family: "Noto Sans CJK SC", "Noto Sans SC", sans-serif;
    color: #1a202c;
    font-size: 8.5pt;
    line-height: 1.55;
}

/* Header */
.header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding: 8mm 0 3mm 0;
    border-bottom: 2.5px solid #1a365d;
    margin-bottom: 4mm;
}
.header h1 {
    font-size: 26pt;
    color: #1a365d;
    letter-spacing: 1.5px;
}
.header .meta {
    text-align: right;
    font-size: 8pt;
    color: #718096;
    line-height: 1.6;
}

.tagline {
    font-size: 11pt;
    color: #4a5568;
    text-align: center;
    margin: 2mm 0 4mm 0;
    font-weight: bold;
}

/* Two column layout */
.row {
    display: flex;
    gap: 5mm;
    margin-bottom: 3mm;
}
.col-left { width: 48%; }
.col-right { width: 52%; }

/* Section */
.section {
    margin-bottom: 3.5mm;
}
.section-title {
    font-size: 10pt;
    font-weight: bold;
    color: #1a365d;
    border-bottom: 1.5px solid #ed8936;
    padding-bottom: 1mm;
    margin-bottom: 2mm;
}

/* Pain list */
.pain-item {
    margin-bottom: 1mm;
    padding-left: 3mm;
    position: relative;
    font-size: 8.5pt;
}
.pain-item::before {
    content: "▸";
    color: #e53e3e;
    position: absolute;
    left: 0;
}

/* Solution list */
.sol-item {
    margin-bottom: 1mm;
    padding-left: 3mm;
    position: relative;
    font-size: 8.5pt;
}
.sol-item::before {
    content: "✓";
    color: #38a169;
    position: absolute;
    left: 0;
    font-weight: bold;
}

/* Highlight box */
.highlight-box {
    background: #ebf8ff;
    border: 1px solid #bee3f8;
    border-radius: 3px;
    padding: 2.5mm 3mm;
    margin: 2mm 0;
    font-size: 8.5pt;
}

/* Synergy table */
.synergy-table {
    width: 100%;
    border-collapse: collapse;
    margin: 2mm 0;
    font-size: 8pt;
}
.synergy-table th {
    background: #1a365d;
    color: white;
    padding: 2mm 2.5mm;
    text-align: center;
    font-weight: bold;
    font-size: 8pt;
}
.synergy-table td {
    padding: 2mm 2.5mm;
    border-bottom: 0.5px solid #e2e8f0;
    vertical-align: top;
    line-height: 1.5;
}
.synergy-table tr:nth-child(even) {
    background: #f7fafc;
}
.synergy-table .type-col {
    width: 24%;
    font-weight: bold;
    color: #1a365d;
}
.synergy-table .give-col {
    width: 37%;
}
.synergy-table .get-col {
    width: 39%;
    color: #2b6cb0;
}

/* Market cards */
.market-grid {
    display: flex;
    gap: 3mm;
    margin: 2mm 0;
}
.market-card {
    flex: 1;
    background: #f7fafc;
    border: 1px solid #e2e8f0;
    border-radius: 3px;
    padding: 2mm 2.5mm;
    text-align: center;
}
.market-card .num {
    font-size: 16pt;
    font-weight: bold;
    color: #1a365d;
    line-height: 1.2;
}
.market-card .label {
    font-size: 7pt;
    color: #718096;
}

/* Team */
.team-grid {
    display: flex;
    gap: 2mm;
    margin: 2mm 0;
}
.team-card {
    flex: 1;
    background: #f7fafc;
    border: 1px solid #e2e8f0;
    border-radius: 3px;
    padding: 2mm 2.5mm;
    text-align: center;
    font-size: 7.5pt;
    line-height: 1.5;
}
.team-card .role {
    font-weight: bold;
    color: #1a365d;
    font-size: 8pt;
}

/* Moat */
.moat-item {
    margin-bottom: 1mm;
    padding-left: 3mm;
    position: relative;
    font-size: 8.5pt;
}
.moat-item::before {
    content: "◆";
    color: #ed8936;
    position: absolute;
    left: 0;
    font-size: 6pt;
    top: 1pt;
}

/* Collab box */
.collab-box {
    background: #1a365d;
    color: white;
    border-radius: 4px;
    padding: 3.5mm 4mm;
    margin-top: 3mm;
}
.collab-box .title {
    font-size: 12pt;
    font-weight: bold;
    margin-bottom: 2mm;
}
.collab-box .content {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.collab-box .terms {
    font-size: 8.5pt;
    line-height: 1.8;
}
.collab-box .amount {
    font-size: 18pt;
    font-weight: bold;
    text-align: right;
}
.collab-box .amount-sub {
    font-size: 8pt;
    font-weight: normal;
    color: #bee3f8;
}

/* Traction */
.traction-tag {
    display: inline-block;
    background: #f0fff4;
    border: 1px solid #c6f6d5;
    border-radius: 3px;
    padding: 1mm 2.5mm;
    font-size: 8pt;
    color: #276749;
    font-weight: bold;
    margin-right: 2mm;
}
</style>
</head>
<body>

<div class="header">
    <h1>GateZero</h1>
    <div class="meta">产业合作方案<br>2026年3月</div>
</div>

<div class="tagline">AI驱动的APQP报价前引擎 —— 与产业伙伴共建汽车供应链AI基础设施</div>

<div class="row">
    <div class="col-left">
        <div class="section">
            <div class="section-title">行业痛点</div>
            <div class="pain-item">报价前缺乏系统评审，接单后发现做不了，亏钱甚至召回</div>
            <div class="pain-item">OEM评审门槛越来越高，中小Tier 1管理能力跟不上</div>
            <div class="pain-item">老工程师流失，经验断层，同样的坑反复踩</div>
            <div class="pain-item">报价准备耗时长，多个RFQ同时来只能挑着做，丢单</div>
            <div class="highlight-box">
                <b>核心矛盾：</b>OEM对供应商管理能力要求持续提高，但中小Tier 1的能力建设跟不上。这个缺口就是GateZero的机会。
            </div>
        </div>

        <div class="section">
            <div class="section-title">我们的方案</div>
            <div class="sol-item">AI四维度可行性评审（技术/制造/质量/成本）</div>
            <div class="sol-item">自动匹配OEM特殊要求，生成合规交付物</div>
            <div class="sol-item">组织经验自动沉淀，系统越用越懂客户业务</div>
            <div class="sol-item">自动解析客户文件包，报价准备从天级缩短到小时级</div>
            <div style="font-size: 8pt; color: #718096; margin-top: 2mm;">
                AI整合行业规范、OEM要求、组织经验、标准流程四类知识底座。<br>工程判断和商务决策由人把关，AI是能力放大器。
            </div>
        </div>

        <div class="section">
            <div class="section-title">目标市场</div>
            <div class="market-grid">
                <div class="market-card">
                    <div class="num">~4,000</div>
                    <div class="label">中国Tier 1供应商</div>
                </div>
                <div class="market-card">
                    <div class="num">5亿内</div>
                    <div class="label">目标画像（中小型）</div>
                </div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">当前进展</div>
            <div style="margin: 2mm 0;">
                <span class="traction-tag">产品Demo已完成</span>
                <span class="traction-tag">付费试点客户</span>
            </div>
        </div>

    </div>

    <div class="col-right">

        <div class="section">
            <div class="section-title">产业协同价值</div>
            <table class="synergy-table">
                <tr>
                    <th>合作伙伴类型</th>
                    <th>您带来的资源</th>
                    <th>您获得的价值</th>
                </tr>
                <tr>
                    <td class="type-col">OEM/主机厂</td>
                    <td class="give-col">评审标准、供应商网络</td>
                    <td class="get-col">供应商能力整体提升，减少供应链质量风险</td>
                </tr>
                <tr>
                    <td class="type-col">Tier 1龙头</td>
                    <td class="give-col">行业经验、标杆案例</td>
                    <td class="get-col">赋能自身供应链(Tier 2)，强化供应链管控</td>
                </tr>
                <tr>
                    <td class="type-col">咨询/培训</td>
                    <td class="give-col">客户渠道、行业知识</td>
                    <td class="get-col">AI工具增强服务能力，提升客单价</td>
                </tr>
                <tr>
                    <td class="type-col">软件商</td>
                    <td class="give-col">客户基础、集成接口</td>
                    <td class="get-col">产品线延伸到APQP前端，增加粘性</td>
                </tr>
            </table>
        </div>

        <div class="section">
            <div class="section-title">核心团队</div>
            <div class="team-grid">
                <div class="team-card">
                    <div class="role">AI CTO</div>
                    技术架构<br>AI产品落地
                </div>
                <div class="team-card">
                    <div class="role">OEM背景</div>
                    管理层经验<br>懂评审逻辑
                </div>
                <div class="team-card">
                    <div class="role">Tier 1管理</div>
                    供应商管理<br>懂业务痛点
                </div>
                <div class="team-card">
                    <div class="role">Tier 1执行</div>
                    一线APQP<br>懂落地细节
                </div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">竞争壁垒</div>
            <div class="moat-item"><b>组织经验网络效应</b>——越多客户使用，知识沉淀越深，竞品无法复制</div>
            <div class="moat-item"><b>行业纵深</b>——聚焦APQP Phase 0，不做泛化质量管理</div>
            <div class="moat-item"><b>团队</b>——OEM+Tier 1+AI三方背景，真正懂行业痛点</div>
            <div class="moat-item"><b>先发优势</b>——市场空白，尚无针对报价前阶段的AI产品</div>
        </div>

    </div>
</div>

<div class="collab-box">
    <div class="content">
        <div class="terms">
            <div class="title">合作模式</div>
            <b>投资不参与经营 · 共享资源</b><br>
            您的行业资源 + 我们的AI产品能力 = 共同提升汽车供应链质量基础设施
        </div>
        <div>
            <div class="amount">种子轮 ¥200万</div>
            <div class="amount-sub">产品开发 · 市场拓展</div>
        </div>
    </div>
</div>

</body>
</html>
"""


def main():
    output = '/home/chu2026/Documents/github/automotive-apqp-agent/docs/bizplan-industry.pdf'
    HTML(string=html_content).write_pdf(output)
    print(f'PDF generated: {output}')


if __name__ == '__main__':
    main()
