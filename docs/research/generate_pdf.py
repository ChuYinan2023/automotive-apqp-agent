#!/usr/bin/env python3
"""Generate competitive analysis PDF report."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# Register Chinese CID fonts (works without TTF files)
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
# Alias for convenience
FONT_CN = 'STSong-Light'
FONT_CN_BOLD = 'STSong-Light'  # CID font has no bold variant; use same font

# Colors
PRIMARY = HexColor('#1a365d')      # Dark blue
SECONDARY = HexColor('#2b6cb0')    # Medium blue
ACCENT = HexColor('#ed8936')       # Orange
LIGHT_BG = HexColor('#f7fafc')     # Light gray
TABLE_HEADER = HexColor('#2d3748') # Dark gray
TABLE_ALT = HexColor('#edf2f7')    # Alternating row
BORDER = HexColor('#cbd5e0')       # Border gray
GREEN = HexColor('#38a169')
RED = HexColor('#e53e3e')
YELLOW = HexColor('#d69e2e')

# Styles
styles = {}

styles['title'] = ParagraphStyle(
    'Title', fontName=FONT_CN, fontSize=24, leading=32,
    textColor=PRIMARY, alignment=TA_CENTER, spaceAfter=4*mm
)
styles['subtitle'] = ParagraphStyle(
    'Subtitle', fontName=FONT_CN, fontSize=11, leading=16,
    textColor=HexColor('#718096'), alignment=TA_CENTER, spaceAfter=12*mm
)
styles['h1'] = ParagraphStyle(
    'H1', fontName=FONT_CN, fontSize=16, leading=22,
    textColor=PRIMARY, spaceBefore=10*mm, spaceAfter=5*mm,
    borderPadding=(0, 0, 2*mm, 0)
)
styles['h2'] = ParagraphStyle(
    'H2', fontName=FONT_CN, fontSize=13, leading=18,
    textColor=SECONDARY, spaceBefore=7*mm, spaceAfter=3*mm
)
styles['h3'] = ParagraphStyle(
    'H3', fontName=FONT_CN, fontSize=11, leading=15,
    textColor=HexColor('#4a5568'), spaceBefore=5*mm, spaceAfter=2*mm
)
styles['body'] = ParagraphStyle(
    'Body', fontName=FONT_CN, fontSize=9, leading=14,
    textColor=HexColor('#2d3748'), alignment=TA_JUSTIFY, spaceAfter=2*mm
)
styles['bullet'] = ParagraphStyle(
    'Bullet', fontName=FONT_CN, fontSize=9, leading=14,
    textColor=HexColor('#2d3748'), leftIndent=8*mm, bulletIndent=3*mm,
    spaceAfter=1.5*mm
)
styles['small'] = ParagraphStyle(
    'Small', fontName=FONT_CN, fontSize=8, leading=11,
    textColor=HexColor('#718096'), spaceAfter=1*mm
)
styles['table_header'] = ParagraphStyle(
    'TableHeader', fontName=FONT_CN, fontSize=8, leading=11,
    textColor=white, alignment=TA_CENTER
)
styles['table_cell'] = ParagraphStyle(
    'TableCell', fontName=FONT_CN, fontSize=8, leading=11,
    textColor=HexColor('#2d3748')
)
styles['table_cell_center'] = ParagraphStyle(
    'TableCellCenter', fontName=FONT_CN, fontSize=8, leading=11,
    textColor=HexColor('#2d3748'), alignment=TA_CENTER
)
styles['highlight'] = ParagraphStyle(
    'Highlight', fontName=FONT_CN, fontSize=9, leading=14,
    textColor=PRIMARY, spaceAfter=2*mm
)
styles['quote'] = ParagraphStyle(
    'Quote', fontName=FONT_CN, fontSize=9, leading=14,
    textColor=HexColor('#4a5568'), leftIndent=10*mm, rightIndent=5*mm,
    spaceAfter=3*mm, borderPadding=(2*mm, 2*mm, 2*mm, 2*mm),
    backColor=LIGHT_BG
)

def B(text):
    return f'<b>{text}</b>'

def make_table(headers, rows, col_widths=None):
    """Create a styled table."""
    page_width = A4[0] - 30*mm
    if col_widths is None:
        n = len(headers)
        col_widths = [page_width / n] * n

    header_cells = [Paragraph(h, styles['table_header']) for h in headers]
    data = [header_cells]
    for row in rows:
        data.append([Paragraph(str(c), styles['table_cell']) for c in row])

    t = Table(data, colWidths=col_widths, repeatRows=1)
    style_cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_cmds.append(('BACKGROUND', (0, i), (-1, i), TABLE_ALT))
    t.setStyle(TableStyle(style_cmds))
    return t

def add_divider(story):
    """Add a visual divider line."""
    t = Table([['']],  colWidths=[A4[0] - 30*mm], rowHeights=[0.5])
    t.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, 0), 1, BORDER),
    ]))
    story.append(Spacer(1, 3*mm))
    story.append(t)
    story.append(Spacer(1, 3*mm))

def build_cover(story):
    story.append(Spacer(1, 50*mm))
    story.append(Paragraph('AI + APQP', styles['title']))
    title2 = ParagraphStyle('t2', parent=styles['title'], fontSize=20, leading=28)
    story.append(Paragraph('竞品深度分析报告', title2))
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph('Competitive Landscape Analysis for AI-Driven APQP Solutions', styles['subtitle']))

    # Info box
    info_data = [
        [Paragraph(B('调研日期'), styles['table_cell']), Paragraph('2026-03-05', styles['table_cell'])],
        [Paragraph(B('调研范围'), styles['table_cell']), Paragraph('8款产品 + 学术研究前沿', styles['table_cell'])],
        [Paragraph(B('目的'), styles['table_cell']), Paragraph('明确竞争格局，识别差异化机会', styles['table_cell'])],
    ]
    info_t = Table(info_data, colWidths=[40*mm, 80*mm])
    info_t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_BG),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(info_t)
    story.append(PageBreak())

def build_overview(story):
    story.append(Paragraph('一、竞品全景总览', styles['h1']))
    add_divider(story)

    pw = A4[0] - 30*mm
    headers = ['产品', '公司', '成立', '规模', '核心定位', 'AI深度', 'APQP覆盖']
    widths = [pw*0.12, pw*0.14, pw*0.06, pw*0.08, pw*0.24, pw*0.18, pw*0.18]
    rows = [
        ['Omnex AQuA Pro', 'Omnex Systems', '1984', '~158人', '企业级EQMS + AI FMEA', '深 (Agentic AI)', '全阶段'],
        ['Siemens Teamcenter Quality', 'Siemens', '-', '巨型', 'PLM集成闭环质量', '中 (预测+数字孪生)', '全阶段'],
        ['Fabasoft Approve', 'Fabasoft AG (奥地利上市)', '-', '中型', 'AI驱动FMEA+文档管理', '深 (Mindbreeze AI)', 'FMEA为主'],
        ['TacitX', 'Tacit AI', '2022', '10-19人', 'AI自动生成FMEA', '很深 (多模态AI)', '仅FMEA/RCA'],
        ['Praxie', 'upBOARD, Inc.', '2017', '~21人', '无代码业务平台+AI增强', '浅-中', 'APQP/PPAP/FMEA'],
        ['Protrak', 'Prorigo Software (印度)', '-', '中型', '低代码APQP工作流', '浅', '全5阶段'],
        ['AxonTrack AI', 'AxonTrack', '2023', '极小', 'AI PPAP文档验证', '中 (文档审查)', 'PPAP/APQP'],
        ['APQP AI', '不明', '-', '极小', '咨询品牌 (空壳)', '不明', '宣称全覆盖'],
    ]
    story.append(make_table(headers, rows, widths))

def build_detail_omnex(story):
    story.append(Paragraph('二、各产品详细分析', styles['h1']))
    add_divider(story)

    story.append(Paragraph('1. Omnex AQuA Pro - 行业鼻祖', styles['h2']))
    story.append(Paragraph(
        '1984年由Chad Kymal创立（曾在GM和KPMG工作）。核心团队参与编写了QS-9000和AIAG五大核心工具。'
        '总部Ann Arbor，密歇根。全球7个办公室（美/印/中/阿联酋/德/泰/新加坡）。约158名员工。',
        styles['body']))

    story.append(Paragraph(B('AI能力 - O-BOT (2025年升级为Agentic AI)'), styles['h3']))
    for item in [
        'NLP验证整个D/PFMEA文档的一致性',
        '推荐失效原因、严重度/发生度评级、失效模式、控制措施',
        '通过聊天提示生成新的FMEA',
        '从基础FMEA库复用内容，生成上下文感知的PFMEA和DFMEA',
        'ML能力扩展到过程流程图、控制计划等多种文档',
    ]:
        story.append(Paragraph(f'  -  {item}', styles['bullet']))

    story.append(Paragraph(B('核心优势'), styles['h3']))
    for item in [
        '关系型数据库架构 - 修改FMEA时自动同步更新控制计划等关联文档',
        '全球第一个APQP软件（1980年代中期）',
        '支持AIAG VDA第1版、AIAG第4版、SAE J1739三种FMEA格式',
        '全球唯一能将DFMEA与DVPR关联的软件',
        '文档效率提升60-70%',
    ]:
        story.append(Paragraph(f'  -  {item}', styles['bullet']))

    story.append(Paragraph(B('用户评价'), styles['h3']))
    story.append(Paragraph('Gartner 4.8/5.0，G2 4.0/5.0。优点是数据联动强，缺点是界面"笨重"、学习曲线陡。定价未公开，企业级。', styles['body']))

def build_detail_siemens(story):
    story.append(Paragraph('2. Siemens Teamcenter Quality - PLM巨头路线', styles['h2']))
    story.append(Paragraph(
        '产品架构：Teamcenter Quality（规划层）+ Opcenter X Quality（执行层）+ Insights Hub（数据分析层）+ Mendix（低代码定制层）。'
        '核心优势是闭环质量管理（Closed-Loop Quality）：从设计到制造到车间到反馈的完整闭环。',
        styles['body']))

    story.append(Paragraph(B('AI/数字孪生能力'), styles['h3']))
    for item in [
        'Insights Hub的预测性质量分析',
        '数字孪生与质量关联（知道什么零件、什么特性、装在什么产品中）',
        '案例：6个月内缺陷率降低25%',
        '2025年Gartner QMS魔力象限领导者',
    ]:
        story.append(Paragraph(f'  -  {item}', styles['bullet']))

    story.append(Paragraph(
        '目标客户：大型OEM和Tier 1（汽车/航空/半导体/医疗）。定价：~$7K+/用户/年起，企业级。',
        styles['body']))

def build_detail_fabasoft(story):
    story.append(Paragraph('3. Fabasoft Approve - AI FMEA最深入的玩家', styles['h2']))
    story.append(Paragraph(
        '奥地利上市公司Fabasoft AG旗下，AI引擎来自集团的Mindbreeze InSpire。纯云端SaaS，强调欧洲数据主权。',
        styles['body']))

    story.append(Paragraph(B('AI覆盖FMEA全部7个步骤'), styles['h3']))
    pw = A4[0] - 30*mm
    headers = ['FMEA步骤', 'AI能力']
    rows = [
        ['项目规划', '基于技能分析推荐合格专家参与'],
        ['结构分析', '建议合适的结构元素'],
        ['功能分析', '文本识别+语义映射，从文档/图纸自动提取功能'],
        ['失效分析', '审查历史数据，对话式识别典型失效'],
        ['风险分析', '基于经验和现场数据建议优先级'],
        ['优化', '从历史有效FMEA中自动推导缓解措施'],
        ['文档记录', '自动提取Lessons Learned'],
    ]
    story.append(make_table(headers, rows, [pw*0.2, pw*0.8]))

    story.append(Paragraph(B('特色功能'), styles['h3']))
    for item in [
        'Chat with FMEA - 自然语言对话式FMEA交互',
        'AI图像分析缺陷登记（2025年11月新增）- 上传缺陷照片自动识别损坏类型',
        '从投诉/8D报告中自动学习',
        '客户：Siemens Energy、KSB、Georg Fischer、Primetals Technologies',
    ]:
        story.append(Paragraph(f'  -  {item}', styles['bullet']))

def build_detail_tacitx(story):
    story.append(Paragraph('4. TacitX - 技术最激进的初创', styles['h2']))
    story.append(Paragraph(
        '2022年旧金山成立，Pre-Seed阶段，10-19人。创始人Dragos Tudor曾在Amazon和CERN工作。',
        styles['body']))

    story.append(Paragraph(B('核心理念："Built by AI, Updated in Real Time"'), styles['h3']))
    for item in [
        'FMEA由AI从运营数据自动生成（分钟级），工程师做审核者',
        '自动摄取非结构化数据：CMMS、工单、用户手册、BOM、CAD、传感器数据',
        '多模态AI提取56+合规和故障属性',
        '随新数据持续流入，FMEA动态更新',
        '合规：IEC 60812、VDA、AIAG-VDA、ARP4761、ISO 26262',
    ]:
        story.append(Paragraph(f'  -  {item}', styles['bullet']))

    story.append(Paragraph(
        '宣称效果：5x更快FMEA创建、40-60%更少重复故障、15%+故障减少率。'
        '风险：早期初创，稳定性和规模存在不确定性。',
        styles['body']))

def build_detail_others(story):
    story.append(Paragraph('5. Praxie - 包装精美但深度不足', styles['h2']))
    story.append(Paragraph(
        '法律名称upBOARD Inc.，2017年成立，约21人。本质是通用型无代码业务平台，在制造质量管理领域通过模板和AI增强覆盖。'
        '技术亮点是Universal Context Technology（模式无关的多模态索引 + 智能上下文构建引擎 + 多Agent协调）。'
        '覆盖APQP/PPAP/FMEA/DFM，但缺少SPC/MSA。'
        '用户评价褒贬不一，负面反馈："没有一个能超越表面层次"。',
        styles['body']))

    story.append(Paragraph('6. Protrak - 扎实的低代码APQP管理', styles['h2']))
    story.append(Paragraph(
        '印度Prorigo Software开发，在印度/美国/加拿大/日本设有办公室。'
        'APQP全5阶段完整覆盖（从RFQ到SOP），完全对齐IATF 16949。'
        'AI能力较弱，核心卖点是低代码和工作流自动化。宣称手动工作量减少40-60%。'
        '客户含Samsung、Siemens、Dassault Systems。',
        styles['body']))

    story.append(Paragraph('7. AxonTrack AI - 早期创业公司', styles['h2']))
    story.append(Paragraph(
        '2023年加拿大温哥华成立，极小团队，基于FlutterFlow低代码平台构建。'
        '聚焦AI驱动的PPAP/APQP文档审查和验证，定位"审查"而非"生成"。'
        '信息透明度低，无公开定价/客户案例。技术深度待验证。',
        styles['body']))

    story.append(Paragraph('8. APQP AI - 基本是空壳', styles['h2']))
    story.append(Paragraph(
        '网站只有一个页面被搜索引擎收录，SSL证书指向Davin Interactive。'
        '无团队信息、定价、客户案例。宣传内容宏大但无产品实质。',
        styles['body']))

def build_landscape(story):
    story.append(PageBreak())
    story.append(Paragraph('三、竞争格局矩阵', styles['h1']))
    add_divider(story)

    story.append(Paragraph(B('按 AI深度 x APQP覆盖广度 定位'), styles['h3']))
    story.append(Spacer(1, 3*mm))

    pw = A4[0] - 30*mm
    # Visual matrix as table
    headers = ['', 'FMEA单点', '部分工具', '全阶段覆盖']
    rows = [
        [B('AI深度: 很深'), 'TacitX\n(FMEA极深,多模态AI)', '', 'Omnex O-BOT\n(全阶段+Agentic AI)'],
        [B('AI深度: 深'), 'Fabasoft\n(FMEA全流程AI)', '', 'Siemens\n(PLM闭环+预测分析)'],
        [B('AI深度: 中'), '', 'AxonTrack\n(文档验证AI)', 'Praxie\n(无代码+模板)'],
        [B('AI深度: 浅'), '', '', 'Protrak\n(低代码工作流)'],
    ]
    t = make_table(headers, rows, [pw*0.18, pw*0.27, pw*0.27, pw*0.28])
    story.append(t)

def build_insights(story):
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph('四、关键洞察', styles['h1']))
    add_divider(story)

    story.append(Paragraph('1. 赛道现状', styles['h2']))
    for item in [
        f'{B("老牌玩家")}（Omnex、Siemens）在补AI能力',
        f'{B("新锐创业")}（TacitX、AxonTrack）用AI切入但覆盖面窄',
        f'{B("平台型")}（Praxie、Protrak）覆盖广但AI深度不够',
        f'{B("垂直深耕")}（Fabasoft）在FMEA单点做到了极致',
    ]:
        story.append(Paragraph(f'  -  {item}', styles['bullet']))

    story.append(Paragraph('2. 市场空白', styles['h2']))
    story.append(Paragraph(
        f'{B("Phase 0（报价前可行性评审）几乎无人深做")} - Protrak提到了RFQ/可行性研究，但不是AI驱动的。'
        '多数产品从Phase 1（计划与定义）开始，Phase 0被视为"预规划"而非正式阶段。',
        styles['body']))
    story.append(Paragraph(
        f'{B("Agent架构做APQP目前只有Omnex的O-BOT在2025年开始尝试")}，赛道还没成型。',
        styles['body']))

    story.append(Paragraph('3. AI应用的三个层次', styles['h2']))
    pw = A4[0] - 30*mm
    headers = ['层次', '代表', '描述']
    rows = [
        ['L1: AI增强表单', 'Praxie, Protrak', '在传统工作流上加AI辅助填写'],
        ['L2: AI驱动分析', 'Fabasoft, AxonTrack', 'AI深度参与文档审查/风险分析'],
        ['L3: AI自主生成', 'TacitX, Omnex O-BOT', 'AI从数据直接生成FMEA等文档'],
    ]
    story.append(make_table(headers, rows, [pw*0.2, pw*0.25, pw*0.55]))

def build_implications(story):
    story.append(PageBreak())
    story.append(Paragraph('五、对我们的启示', styles['h1']))
    add_divider(story)

    story.append(Paragraph('差异化定位', styles['h2']))
    pw = A4[0] - 30*mm

    advantages = [
        ['Phase 0深扎', '竞品空白地带，报价前可行性评审的AI决策支持'],
        ['Agent工作流架构', '对话驱动而非表单驱动，更灵活'],
        ['知识回写机制', '越用越懂特定OEM x 零件组合，形成数据护城河'],
        ['不替人做工程判断', '清晰的"决策支持"定位，符合行业实际需求'],
        ['本地/灵活部署', '对数据敏感的Tier 1很有吸引力'],
    ]
    headers = ['优势', '说明']
    story.append(make_table(headers, advantages, [pw*0.25, pw*0.75]))

    story.append(Paragraph('可借鉴的最佳实践', styles['h2']))
    benchmarks = [
        ['Fabasoft', 'FMEA全流程AI覆盖（7步），Chat with FMEA对话模式，历史投诉/8D自动学习'],
        ['Omnex O-BOT', 'Agentic AI架构，从基础库复用内容生成上下文感知FMEA'],
        ['TacitX', '多模态数据摄取（BOM/CAD/工单/传感器），FMEA实时更新理念'],
        ['Praxie', 'Universal Context Technology的上下文管理思路'],
        ['Siemens', '闭环质量管理概念，数字孪生与质量关联'],
        ['Protrak', 'Phase 1可行性研究的维度划分（商业/技术/风险）'],
    ]
    headers = ['来源', '借鉴点']
    story.append(make_table(headers, benchmarks, [pw*0.2, pw*0.8]))

    story.append(Paragraph('历史失效模式提示 - 已确认的优先方向', styles['h2']))
    for item in [
        '按零部件类型建立失效模式知识库（参考Fabasoft从历史FMEA/投诉/8D中学习）',
        '结合OEM特殊要求做上下文感知推荐（参考Omnex O-BOT）',
        '输出格式为风险提示清单而非完整FMEA表（符合Phase 0轻量定位）',
    ]:
        story.append(Paragraph(f'  -  {item}', styles['bullet']))

    # Final conclusion box
    story.append(Spacer(1, 8*mm))
    conclusion = Paragraph(
        f'{B("核心结论")}: Phase 0几乎无人深做，Agent架构刚起步，知识回写是护城河。'
        '最值得学习的三家：Fabasoft的FMEA深度、Omnex的Agentic AI、TacitX的多模态数据摄取思路。',
        ParagraphStyle('conclusion', parent=styles['body'], fontSize=10, leading=16,
                       textColor=PRIMARY, backColor=LIGHT_BG,
                       borderPadding=(8, 8, 8, 8))
    )
    story.append(conclusion)


def add_page_number(canvas, doc):
    """Add page number and header/footer."""
    canvas.saveState()
    page_num = canvas.getPageNumber()
    if page_num > 1:
        # Header line
        canvas.setStrokeColor(BORDER)
        canvas.setLineWidth(0.5)
        canvas.line(15*mm, A4[1] - 12*mm, A4[0] - 15*mm, A4[1] - 12*mm)
        # Header text
        canvas.setFont(FONT_CN, 7)
        canvas.setFillColor(HexColor('#a0aec0'))
        canvas.drawString(15*mm, A4[1] - 10*mm, 'AI + APQP 竞品深度分析报告')
        canvas.drawRightString(A4[0] - 15*mm, A4[1] - 10*mm, '2026-03-05')
        # Footer
        canvas.line(15*mm, 12*mm, A4[0] - 15*mm, 12*mm)
        canvas.drawCentredString(A4[0] / 2, 7*mm, f'- {page_num} -')
    canvas.restoreState()


def main():
    output_path = '/home/chu2026/Documents/github/automotive-apqp-agent/docs/research/competitive-analysis.pdf'
    doc = SimpleDocTemplate(
        output_path, pagesize=A4,
        leftMargin=15*mm, rightMargin=15*mm,
        topMargin=18*mm, bottomMargin=18*mm
    )

    story = []
    build_cover(story)
    build_overview(story)
    story.append(PageBreak())
    build_detail_omnex(story)
    build_detail_siemens(story)
    story.append(PageBreak())
    build_detail_fabasoft(story)
    build_detail_tacitx(story)
    story.append(PageBreak())
    build_detail_others(story)
    build_landscape(story)
    build_insights(story)
    build_implications(story)

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f'PDF generated: {output_path}')


if __name__ == '__main__':
    main()
