#!/usr/bin/env python3
"""Generate GateZero one-page business plan (financial investor version) PDF."""

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
.col-half { width: 50%; }

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

/* Market */
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

/* Business model */
.biz-flow {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 2mm;
    margin: 2mm 0;
}
.biz-stage {
    background: #f7fafc;
    border: 1px solid #e2e8f0;
    border-radius: 3px;
    padding: 2mm 3mm;
    text-align: center;
    font-size: 8pt;
    flex: 1;
}
.biz-stage.current {
    background: #ebf8ff;
    border-color: #2b6cb0;
}
.biz-arrow {
    color: #a0aec0;
    font-size: 12pt;
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

/* Ask box */
.ask-box {
    background: #1a365d;
    color: white;
    border-radius: 4px;
    padding: 3mm 4mm;
    margin-top: 3mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.ask-box .amount {
    font-size: 18pt;
    font-weight: bold;
}
.ask-box .detail {
    font-size: 8.5pt;
    line-height: 1.6;
    text-align: right;
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
    <div class="meta">商业计划摘要<br>2026年3月 · 种子轮</div>
</div>

<div class="tagline">AI驱动的APQP报价前引擎 —— 帮Tier 1接对的单、接得起单</div>

<div class="row">
    <div class="col-left">
        <div class="section">
            <div class="section-title">行业痛点</div>
            <div class="pain-item">报价前缺乏系统评审，接单后发现做不了，亏钱甚至召回</div>
            <div class="pain-item">OEM评审要求越来越高，管理能力跟不上，接不到高价值订单</div>
            <div class="pain-item">有经验的工程师流失，组织能力断层，同样的坑反复踩</div>
            <div class="pain-item">报价准备耗时长、效率低，多个RFQ同时来只能挑着做</div>
        </div>

        <div class="section">
            <div class="section-title">解决方案</div>
            <div class="sol-item">AI四维度可行性评审：技术/制造/质量/成本风险前置识别</div>
            <div class="sol-item">自动匹配OEM特殊要求，生成合规交付物</div>
            <div class="sol-item">组织经验自动沉淀，越用越懂客户业务</div>
            <div class="sol-item">自动解析客户文件包，报价准备从天级到小时级</div>
            <div class="highlight-box">
                AI整合行业规范、OEM要求、组织经验、标准流程四类知识底座。<br>工程判断和商务决策由人把关，AI是能力放大器。
            </div>
        </div>

        <div class="section">
            <div class="section-title">竞争壁垒</div>
            <div class="moat-item"><b>组织经验网络效应</b>——每个项目沉淀经验，系统越用越强，竞品无法复制</div>
            <div class="moat-item"><b>行业纵深</b>——聚焦APQP Phase 0，不做泛化质量管理</div>
            <div class="moat-item"><b>团队</b>——OEM+Tier 1+AI三方背景，真正懂行业痛点</div>
            <div class="moat-item"><b>先发优势</b>——市场空白，尚无针对报价前阶段的AI产品</div>
        </div>
    </div>

    <div class="col-right">
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
                <div class="market-card">
                    <div class="num">高频</div>
                    <div class="label">每家每年数十个RFQ</div>
                </div>
            </div>
            <div style="font-size: 8pt; color: #718096; margin-top: 1mm;">
                中小型Tier 1管理能力最薄弱、对AI辅助需求最迫切、付费意愿明确
            </div>
        </div>

        <div class="section">
            <div class="section-title">商业模式</div>
            <div class="biz-flow">
                <div class="biz-stage current"><b>现阶段</b><br>定制开发<br>实施服务</div>
                <div class="biz-arrow">→</div>
                <div class="biz-stage"><b>中期</b><br>按项目<br>收费</div>
                <div class="biz-arrow">→</div>
                <div class="biz-stage"><b>远期</b><br>按接单标的<br>提佣</div>
            </div>
            <div style="font-size: 8pt; color: #718096; margin-top: 1mm;">
                从服务收入起步验证价值，逐步过渡到与客户收益绑定的分成模式
            </div>
        </div>

        <div class="section">
            <div class="section-title">当前进展</div>
            <div style="margin: 2mm 0;">
                <span class="traction-tag">产品Demo已完成</span>
                <span class="traction-tag">付费试点客户</span>
            </div>
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
                    管理层经验<br>懂OEM逻辑
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
            <div class="section-title">投资回报逻辑</div>
            <div style="font-size: 8.5pt; line-height: 1.7;">
                <b>短期：</b>定制服务收入覆盖运营，验证产品价值<br>
                <b>中期：</b>标准化产品复制到更多客户，收入规模化<br>
                <b>远期：</b>提佣模式与客户利益深度绑定，天花板极高——<br>
                <span style="color: #2b6cb0;">单家Tier 1年接单额数千万至数亿，提佣空间远超SaaS订阅</span>
            </div>
        </div>
    </div>
</div>

<div class="ask-box">
    <div>
        <div class="amount">种子轮 ¥200万</div>
    </div>
    <div class="detail">
        产品开发 · 市场拓展<br>
        从付费试点到规模化复制
    </div>
</div>

</body>
</html>
"""


def main():
    output = '/home/chu2026/Documents/github/automotive-apqp-agent/docs/bizplan-financial.pdf'
    HTML(string=html_content).write_pdf(output)
    print(f'PDF generated: {output}')


if __name__ == '__main__':
    main()
