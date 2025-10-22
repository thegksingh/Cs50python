from fpdf import FPDF

def main():
    name = input("Name: ")
    make_pdf(name)

def make_pdf(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.image("ps8/shirtificate.png", x=0, y=60, w=210)
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 40, "CS50 Shirtificate", align="C")
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(135)
    pdf.cell(0, 10, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()