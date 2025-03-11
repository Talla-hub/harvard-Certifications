from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica","I", 30)
        self.set_x(90)
        self.cell(10, 20, "CS50 Shirtificate", align="C")
        self.ln(2)
        image_width = pdf.epw / 2  # Width of the image (or set your custom width)
        x_position = (pdf.epw - image_width) / 2  # Centered x position
        self.set_xy(0,30)
        self.image("./shirtificate.png", h=100, w=image_width, x=x_position)
        self.set_font("helvetica","B", 13)
        self.set_xy(90,55)
        self.set_text_color(255,255,255)
        name=input("Name: ")
        self.cell(10, 20, f"{name} took CS50 ",align="C")
        self.set_draw_color(r=255, g=255, b=255)





pdf = PDF("P",format=(210,150))
pdf.add_page()
pdf.output("shirtificate.pdf")
