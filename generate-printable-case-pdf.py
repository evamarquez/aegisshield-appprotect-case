from html import escape
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Image, KeepTogether, LongTable, PageBreak, Paragraph, Preformatted, SimpleDocTemplate, Spacer, TableStyle
from reportlab.lib.utils import ImageReader

CASE = Path(__file__).resolve().parent
OUTPUT = CASE / "aegisshield-appprotect-case.pdf"
DOCS = sorted([p for p in CASE.glob("*.md") if p.name not in {"README.md"}], key=lambda p: p.name)
IMAGE_FILES = [CASE / "screenshots" / name for name in ["appprotect-prototype.png", "github-board-week-02.png", "github-board-week-06.png", "github-board-week-08.png"]]

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CaseTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=22, leading=27, textColor=colors.HexColor("#173b3b"), spaceAfter=12))
styles.add(ParagraphStyle(name="CaseH1", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=17, leading=21, textColor=colors.HexColor("#173b3b"), spaceBefore=16, spaceAfter=8))
styles.add(ParagraphStyle(name="CaseH2", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=12, leading=15, textColor=colors.HexColor("#0d7569"), spaceBefore=12, spaceAfter=5))
styles.add(ParagraphStyle(name="CaseBody", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.5, leading=13, spaceAfter=7))
styles.add(ParagraphStyle(name="CaseSmall", parent=styles["BodyText"], fontName="Helvetica", fontSize=8, leading=10, textColor=colors.HexColor("#5f7774"), spaceAfter=5))
styles.add(ParagraphStyle(name="CaseBullet", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.5, leading=13, leftIndent=14, firstLineIndent=-8, spaceAfter=4))
styles.add(ParagraphStyle(name="CaseQuote", parent=styles["BodyText"], fontName="Helvetica-Oblique", fontSize=9, leading=13, leftIndent=14, borderPadding=8, backColor=colors.HexColor("#f1f8e9"), borderColor=colors.HexColor("#d8e8cb"), borderWidth=0.5, spaceBefore=5, spaceAfter=8))
styles.add(ParagraphStyle(name="CaseTable", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.4, leading=9.5))
styles.add(ParagraphStyle(name="CaseTableHead", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=7.4, leading=9.5, textColor=colors.HexColor("#0d7569")))

def text_value(value):
    value = value.strip()
    value = value.replace("**", "").replace("__", "").replace("`", "")
    return escape(value)

def para(value, style="CaseBody"):
    return Paragraph(text_value(value), styles[style])

def is_table_line(line):
    return line.strip().startswith("|") and line.strip().endswith("|")

def table_rows(lines):
    rows = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and all(set(cell.replace(" ", "")) <= set("-:") for cell in cells):
            continue
        rows.append(cells)
    return rows

def document_story(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    story = [para(path.stem.replace("-", " ").title(), "CaseSmall")]
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            index += 1
            continue
        if line.startswith("# "):
            story.append(para(line[2:], "CaseTitle"))
            index += 1
            continue
        if line.startswith("## "):
            story.append(para(line[3:], "CaseH1"))
            index += 1
            continue
        if line.startswith("### "):
            story.append(para(line[4:], "CaseH2"))
            index += 1
            continue
        if line.startswith(">"):
            story.append(para(line.lstrip("> "), "CaseQuote"))
            index += 1
            continue
        if line.startswith("```"):
            code = []
            index += 1
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code.append(lines[index])
                index += 1
            index += 1
            story.append(Preformatted("\n".join(code), styles["Code"]))
            continue
        if line.startswith("- ") or line.startswith("1. "):
            marker = "- " if line.startswith("- ") else "1. "
            while index < len(lines) and lines[index].strip().startswith(marker):
                story.append(para("• " + lines[index].strip()[len(marker):], "CaseBullet"))
                index += 1
            continue
        if is_table_line(line):
            rows = []
            while index < len(lines) and is_table_line(lines[index]):
                rows.append(lines[index])
                index += 1
            parsed = table_rows(rows)
            if parsed:
                converted = [[para(cell, "CaseTableHead" if row_index == 0 else "CaseTable") for cell in row] for row_index, row in enumerate(parsed)]
                column_count = max(len(row) for row in parsed)
                widths = [((letter[0] - 1.2 * inch) / column_count)] * column_count
                table = LongTable(converted, colWidths=widths, repeatRows=1, hAlign="LEFT")
                table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eaf1ed")), ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#c8d9d2")), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
                story.append(table)
                story.append(Spacer(1, 6))
            continue
        paragraph = [line]
        index += 1
        while index < len(lines) and lines[index].strip() and not lines[index].strip().startswith(("# ", "## ", "### ", ">", "- ", "1. ", "```")) and not is_table_line(lines[index]):
            paragraph.append(lines[index].strip())
            index += 1
        story.append(para(" ".join(paragraph)))
    return story

story = [Spacer(1, 1.6 * inch), para("AegisShield AppProtect", "CaseTitle"), para("Fictional product discovery and controlled pilot case", "CaseH1"), para("Prepared by Eva Marquez", "CaseSmall"), Spacer(1, 0.2 * inch), para("This case is fictional. The company, customer, research, costs, dates, board states, prototype, decisions, and outcomes are simulated for portfolio demonstration."), PageBreak(), para("Contents", "CaseTitle")]
for path in DOCS:
    title = next((line[2:].strip() for line in path.read_text(encoding="utf-8").splitlines() if line.startswith("# ")), path.stem)
    story.append(para(f"{path.stem} - {title}"))

for path in DOCS:
    story.append(PageBreak())
    story.extend(document_story(path))

story.append(PageBreak())
story.append(para("Evidence images", "CaseTitle"))
story.append(para("These images support the fictional case. The board captures are generated from the linked GitHub Projects data, and the prototype is a visual, non-functional concept."))
for image_path in IMAGE_FILES:
    if image_path.exists():
        story.append(PageBreak())
        width, height = ImageReader(str(image_path)).getSize()
        display_width = letter[0] - 1.3 * inch
        display_height = display_width * height / width
        max_height = 6.2 * inch
        if display_height > max_height:
            display_width = display_width * max_height / display_height
            display_height = max_height
        story.append(para(image_path.stem.replace("-", " ").title(), "CaseH2"))
        story.append(Image(str(image_path), width=display_width, height=display_height))
        story.append(Spacer(1, 10))

def footer(canvas, document):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#5f7774"))
    canvas.drawString(0.65 * inch, 0.35 * inch, "AegisShield AppProtect | Fictional case study")
    canvas.drawRightString(letter[0] - 0.65 * inch, 0.35 * inch, str(document.page))
    canvas.restoreState()

SimpleDocTemplate(str(OUTPUT), pagesize=letter, leftMargin=0.65 * inch, rightMargin=0.65 * inch, topMargin=0.65 * inch, bottomMargin=0.65 * inch, title="AegisShield AppProtect - Fictional Case", author="Eva Marquez").build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)
