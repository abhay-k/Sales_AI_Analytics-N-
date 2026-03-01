from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(chart, insight):

    styles = getSampleStyleSheet()

    report = SimpleDocTemplate("sales_report.pdf")

    content = []

    content.append(Paragraph("Sales Analytics Report", styles["Title"]))

    content.append(Paragraph(insight, styles["Normal"]))

    content.append(Image(chart))

    report.build(content)

    return "sales_report.pdf"
