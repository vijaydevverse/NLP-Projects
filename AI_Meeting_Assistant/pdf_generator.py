from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font(
    "Arial",
    size=12
)

with open(
        "summary.txt",
        "r",
        encoding="utf-8"
) as file:

    text = file.read()

pdf.multi_cell(
    0,
    10,
    text
)

pdf.output(
    "Meeting_Summary.pdf"
)

print("PDF Created")