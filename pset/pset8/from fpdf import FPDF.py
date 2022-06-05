from tkinter import CENTER
from fpdf import FPDF

A4_HEIGHT = 297
A4_WIDTH = 210


name = input("Name: ").title()

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 40)
pdf.ln(h=20)
pdf.set_x((A4_WIDTH - 120)/2)
pdf.cell(120, 30,
         'CS50 Shirtificate',
         new_x="CENTER",
         align="C"
        )

pdf.image("shirtificate.png",
          x=(1-0.95)*A4_WIDTH, y=80,
          w=0.95*pdf.epw, h=0
        )

who = f"{name} took CS50"
s_width = pdf.get_string_width(who)


pdf.set_xy((A4_WIDTH - s_width)/2, A4_HEIGHT/2 - 20)
pdf.set_font("helvetica", "B", 25)
pdf.set_text_color(255, 255, 255)
pdf.cell(s_width, 30,
        who,
        align="C"
        )

pdf.output("tuto1.pdf")
