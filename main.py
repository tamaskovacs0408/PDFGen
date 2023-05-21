
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

pdf.set_font(family="Arial", size=16)

pdf.cell(w=0, h=12, txt="Hello there!", align="C", border=3)

pdf.output("output.pdf")