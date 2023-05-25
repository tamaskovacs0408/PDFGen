
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

pdf.set_font(family="Arial", size=16)

pdf.cell(w=0, h=12, txt="Hello there!", align="C", border=3)

pdf.add_page()

pdf.set_font(family="Times", size=14)

pdf.cell(w=0, h=8, txt="Next page", align="L", border=1)

pdf.output("output.pdf")