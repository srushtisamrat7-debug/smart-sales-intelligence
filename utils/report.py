from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO


def generate_pdf_report(total_sales, total_profit, total_orders, total_customers, avg_order_value, insights, recommendations):
    buffer = BytesIO()

    pdf = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    y = height - 50

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(50, y, "Smart Sales Intelligence Report")

    y -= 40
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y, "Executive Summary")

    y -= 30
    pdf.setFont("Helvetica", 11)
    pdf.drawString(50, y, f"Total Revenue: ${total_sales:,.0f}")
    y -= 20
    pdf.drawString(50, y, f"Total Profit: ${total_profit:,.0f}")
    y -= 20
    pdf.drawString(50, y, f"Total Orders: {total_orders:,}")
    y -= 20
    pdf.drawString(50, y, f"Total Customers: {total_customers:,}")
    y -= 20
    pdf.drawString(50, y, f"Average Order Value: ${avg_order_value:,.0f}")

    y -= 40
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y, "Business Insights")

    pdf.setFont("Helvetica", 10)
    for insight in insights:
        y -= 20
        pdf.drawString(50, y, f"- {insight}")

    y -= 40
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y, "Recommendations")

    pdf.setFont("Helvetica", 10)
    for rec in recommendations:
        y -= 20
        pdf.drawString(50, y, f"- {rec}")

    pdf.save()

    buffer.seek(0)
    return buffer