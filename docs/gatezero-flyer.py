#!/usr/bin/env python3
"""Generate GateZero one-page product flyer PDF using weasyprint."""

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
    font-size: 9pt;
    line-height: 1.5;
}

/* Hero */
.hero {
    text-align: center;
    padding: 14mm 0 5mm 0;
}
.hero h1 {
    font-size: 30pt;
    color: #1a365d;
    letter-spacing: 2px;
    margin-bottom: 2mm;
}
.hero .tagline {
    font-size: 11pt;
    color: #718096;
}
.hero .sub {
    font-size: 10pt;
    color: #718096;
    margin-top: 1mm;
}

.divider {
    border: none;
    border-top: 2px solid #ed8936;
    margin: 4mm 0;
}

/* Section titles */
.section-title {
    font-size: 12pt;
    font-weight: bold;
    color: #ed8936;
    margin: 4mm 0 3mm 0;
}

/* Pain points */
.pains {
    margin: 0 2mm;
}
.pains .item {
    margin-bottom: 1.5mm;
    font-size: 9pt;
    line-height: 1.6;
}
.pains .num {
    color: #ed8936;
    font-weight: bold;
}

/* Solution table */
.sol-table {
    width: 100%;
    border-collapse: collapse;
    margin: 2mm 0;
    font-size: 8pt;
}
.sol-table th {
    background: #1a365d;
    color: white;
    padding: 2mm 2mm;
    text-align: center;
    font-weight: bold;
    font-size: 8pt;
}
.sol-table td {
    padding: 2mm 2mm;
    border-bottom: 0.5px solid #e2e8f0;
    vertical-align: top;
    line-height: 1.5;
}
.sol-table tr:nth-child(even) {
    background: #f7fafc;
}
.sol-table .pain-col {
    width: 18%;
    color: #1a202c;
}
.sol-table .sol-col {
    width: 52%;
}
.sol-table .result-col {
    width: 30%;
    color: #2b6cb0;
    font-weight: bold;
}

/* Knowledge base */
.kb-table {
    width: 100%;
    border-collapse: collapse;
    margin: 2mm 0;
    font-size: 7.5pt;
}
.kb-table th {
    background: #2b6cb0;
    color: white;
    padding: 1.5mm 2mm;
    text-align: center;
    font-weight: bold;
    width: 25%;
}
.kb-table th.highlight {
    background: #ed8936;
}
.kb-table td {
    background: #f7fafc;
    padding: 2mm 2.5mm;
    border: 0.5px solid #e2e8f0;
    vertical-align: top;
    line-height: 1.6;
    font-size: 7.5pt;
}
.kb-note {
    font-size: 7.5pt;
    color: #718096;
    margin-top: 1.5mm;
}

/* Flow */
.flow-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 2mm 0;
}
.flow-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
}
.flow-table td {
    text-align: center;
    vertical-align: middle;
    font-size: 8pt;
    padding: 2.5mm 1mm;
    line-height: 1.4;
}
.flow-box {
    border: 1px solid #cbd5e0;
    border-radius: 3px;
    background: #f7fafc;
    padding: 2mm 2mm;
    font-size: 8pt;
    line-height: 1.5;
    text-align: center;
}
.flow-box.ai {
    border-color: #2b6cb0;
    background: #ebf8ff;
}
.flow-box.human {
    border-color: #cbd5e0;
    background: #f7fafc;
}
.flow-box.output {
    border-color: #38a169;
    background: #f0fff4;
}
.flow-arrow {
    color: #a0aec0;
    font-size: 14pt;
    padding: 0 1mm;
}
.flow-note {
    font-size: 7.5pt;
    color: #718096;
    text-align: center;
    margin-top: 1.5mm;
}

/* Footer */
.footer {
    text-align: center;
    font-size: 11pt;
    font-weight: bold;
    color: #1a365d;
    padding-top: 3mm;
}
</style>
</head>
<body>

<div class="hero">
    <h1>GateZero</h1>
    <div class="tagline">AI驱动的APQP报价前引擎</div>
    <div class="sub">帮你更快、更准、更完整地完成报价准备</div>
</div>

<hr class="divider">

<div class="section-title">你是不是也遇到这些问题？</div>
<div class="pains">
    <div class="item"><span class="num">1.</span> 拍脑袋报价，接了单才发现做不了，亏钱甚至面临召回风险</div>
    <div class="item"><span class="num">2.</span> OEM要求越来越高，评审材料准备不到位，好项目接不到</div>
    <div class="item"><span class="num">3.</span> 老工程师一走，新人两眼一抹黑，同样的坑反复踩</div>
    <div class="item"><span class="num">4.</span> 客户文件包一大堆，翻来翻去还是怕漏了什么，一个报价准备好几天</div>
</div>

<div class="section-title" style="margin-top: 4mm;">GateZero 怎么帮你？</div>
<table class="sol-table">
    <tr>
        <th>你头疼的</th>
        <th>GateZero帮你做的</th>
        <th>结果</th>
    </tr>
    <tr>
        <td class="pain-col">不知道有没有风险</td>
        <td class="sol-col">技术/制造/质量/成本四维度系统性评审，提示历史同类项目踩过的坑</td>
        <td class="result-col">接单前就看清风险，不再拍脑袋</td>
    </tr>
    <tr>
        <td class="pain-col">OEM评审要求搞不定</td>
        <td class="sol-col">自动匹配OEM特殊要求，按标准生成合规交付物</td>
        <td class="result-col">通过更多OEM的门槛</td>
    </tr>
    <tr>
        <td class="pain-col">老师傅走了没人带</td>
        <td class="sol-col">历史经验沉淀在系统里，自动提示该注意什么</td>
        <td class="result-col">人走经验不走</td>
    </tr>
    <tr>
        <td class="pain-col">报价准备太慢</td>
        <td class="sol-col">自动解析客户文件包，自动生成交付物初稿</td>
        <td class="result-col">天级变小时级</td>
    </tr>
</table>

<div class="section-title" style="margin-top: 4mm;">凭什么能做到？</div>
<div style="font-size: 8.5pt; margin-bottom: 2mm;">GateZero整合了四类知识，让每个人都能调用整个组织的最佳实践：</div>
<table class="kb-table">
    <tr>
        <th>行业规范</th>
        <th>OEM要求</th>
        <th class="highlight">组织经验</th>
        <th>标准流程</th>
    </tr>
    <tr>
        <td>IATF 16949<br>AIAG五大核心工具<br>零部件技术标准<br>环保法规</td>
        <td>Stellantis SSTS<br>VW Formel-Q<br>BMW QMT<br>GM BIQS ...</td>
        <td>历史项目经验<br>失效模式库<br>OEM x 零件组合经验<br>工艺能力边界<br><b>越用越多</b></td>
        <td>可行性评审框架<br>标准化工作流<br>多轮人工确认<br>模板与一致性校验</td>
    </tr>
</table>
<div class="kb-note">其中"组织经验"是GateZero的独特之处——每做完一个项目，经验自动沉淀，系统越用越懂你的业务。</div>

<div class="section-title" style="margin-top: 4mm;">怎么用？</div>
<table class="flow-table">
    <tr>
        <td><div class="flow-box">收到客户<br>RFQ文件包</div></td>
        <td class="flow-arrow">&#10132;</td>
        <td><div class="flow-box ai"><b>GateZero</b><br>自动解析 / 提取要求<br>识别风险 / 生成初稿</div></td>
        <td class="flow-arrow">&#10132;</td>
        <td><div class="flow-box human">你来审核<br>补充判断 / 确认决策</div></td>
        <td class="flow-arrow">&#10132;</td>
        <td><div class="flow-box output"><b>输出完整</b><br>报价准备包</div></td>
    </tr>
</table>
<div class="flow-note">AI负责整理信息、提示风险、生成文档；工程判断和商务决策，始终由你来做。</div>

<hr class="divider" style="margin-top: 4mm;">
<div class="footer">让每个人都能拿出资深工程师水平的报价准备</div>

</body>
</html>
"""


def main():
    output = '/home/chu2026/Documents/github/automotive-apqp-agent/docs/gatezero-flyer.pdf'
    HTML(string=html_content).write_pdf(output)
    print(f'PDF generated: {output}')


if __name__ == '__main__':
    main()
