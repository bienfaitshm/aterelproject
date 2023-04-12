from fpdf import FPDF


pdf = FPDF()
pdf.add_page("P", "A4")
pdf.set_auto_page_break(True, 10)
pdf.set_font('Arial', '', 12)
pdf.set_top_margin(10)
pdf.set_left_margin(10)
pdf.set_right_margin(10)

# MulltiCell
pdf.set_xy(11, 84)
pdf.set_font_size(20)
pdf.cell(189, 8, "CONTRAT", "B", 1, "C", False)
pdf.output("tuto2.pdf")


# MULticell

# ?PHP

# require('fpdf.php');

# $pdf = new FPDF();
# $pdf->AddPage('P', 'A4');
# $pdf->SetAutoPageBreak(true, 10);
# $pdf->SetFont('Arial', '', 12);
# $pdf->SetTopMargin(10);
# $pdf->SetLeftMargin(10);
# $pdf->SetRightMargin(10);


# /* --- MultiCell --- */
# /* --- Cell --- */
# $pdf->SetXY(11, 84);
# $pdf->SetFontSize(20);
# $pdf->Cell(189, 8, 'CONTRAT', 'B', 1, 'C', false);
# /* --- MultiCell --- */


# $pdf->Output('created_pdf.pdf','I');
# ?>

# class PDF(FPDF):
#     def header(self):
#         # Rendering logo:
#         self.image("./medias/img.jpg", 10, 8, 33)
#         # Setting font: helvetica bold 15
#         self.set_font("helvetica", "B", 15)
#         # Moving cursor to the right:
#         self.cell(80)
#         # Printing title:
#         self.cell(30, 10, "Title", border=1, align="C")
#         # Performing a line break:
#         self.ln(20)

#     def footer(self):
#         # Position cursor at 1.5 cm from bottom:
#         self.set_y(-15)
#         # Setting font: helvetica italic 8
#         self.set_font("helvetica", "I", 8)
#         # Printing page number:
#         self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


# # Instantiation of inherited class
# pdf = PDF()
# pdf.add_page()
# pdf.set_font("Times", size=12)
# for i in range(1, 41):
#     pdf.cell(0, 10, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")
# pdf.output("./medias/pdf/new_tuto2.pdf")

# from fpdf import FPDF

# text = """
#     bonjour bienfait\n
#     je suis tres hereux de vous avoir a mes cotes\n
#     ceci est un test de generation du text
# """
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("helvetica","", 16)
# # pdf.cell(40, 10, text)
# pdf.cell(60, 10, text, new_x="LMARGIN", new_y="NEXT", align='C')
# pdf.output("tuto2.pdf")
