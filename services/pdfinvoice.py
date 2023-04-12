import fpdf

pdf = fpdf.FPDF("P", "mm", "A4")

pdf.add_page()

# se font to Arial Bold, 14pt
pdf.set_font("Arial", "B", 14)

pdf.image(name="https://www.lecoindesentrepreneurs.fr/wp-content/uploads/2015/02/contrat-de-vente-dun-fonds-de-commerce.jpg", h=20, w=70)
# cell (width, height, text. border, end, align)
pdf.cell(w=130, h=5, txt="Alterell.com", border=1, ln=0)
pdf.cell(w=59, h=5, txt="Invoice", border=1, ln=1)  # end of line

# set font to Arial, regular, 12pt
pdf.set_font("Arial", "", 12)

pdf.cell(w=130, h=5, txt="MANIKA, Q/LATIN", border=1, ln=0)
pdf.cell(w=59, h=5, txt="", border=1, ln=1)  # end of line

pdf.cell(w=130, h=5, txt="[City country]", border=1, ln=0)
pdf.cell(w=25, h=5, txt="Date", border=1, ln=0)
pdf.cell(w=34, h=5, txt="[dd/mm/yyyy]", border=1, ln=1)  # end of line

pdf.cell(w=130, h=5, txt="Phone [ + 243]", border=1, ln=0)
pdf.cell(w=25, h=5, txt="Invoice #", border=1, ln=0)
pdf.cell(w=34, h=5, txt="[123456]", border=1, ln=1)  # end of line

pdf.cell(w=130, h=5, txt="Fax [ +243]", border=1, ln=0)
pdf.cell(w=25, h=5, txt="Customer ID", border=1, ln=0)
pdf.cell(w=34, h=5, txt="[123456]", border=1, ln=1)  # end of line

# make a dumy empty cell as vertical spacer
pdf.cell(w=189, h=10, txt="", border=0, ln=1)  # end of line

pdf.set_font("Arial", "B", 14)
# title
pdf.cell(w=189, h=5, txt="CONTRAT", border=1, ln=1, align="C")

# make a dumy empty cell as vertical spacer
pdf.cell(w=189, h=10, txt="", border=0, ln=1)  # end of line

pdf.set_font("Arial", "", 12)
# publicher adress
pdf.cell(w=34, h=5, txt="Bill to", border=1, ln=1)  # end of line

# add dunny cell at beginning of each line for indentation
pdf.cell(w=10, h=5, txt="", border=1, ln=0)
pdf.cell(w=90, h=5, txt="[Name]", border=1, ln=1)

pdf.cell(w=10, h=5, txt="", border=1, ln=0)
pdf.cell(w=90, h=5, txt="[Email Adress]", border=1, ln=1)

pdf.cell(w=10, h=5, txt="", border=1, ln=0)
pdf.cell(w=90, h=5, txt="[Phone]", border=1, ln=1)

pdf.cell(w=10, h=5, txt="", border=1, ln=0)
pdf.cell(w=90, h=5, txt="[Adress]", border=1, ln=1)

# make a dumy empty cell as vertical spacer
pdf.cell(w=189, h=10, txt="", border=0, ln=1)  # end of line

# Invoice contents
pdf.set_font("Arial", "B", 12)

pdf.cell(w=130, h=5, txt="[Description]", border=1, ln=0)
pdf.cell(w=25, h=5, txt="[Tax]", border=1, ln=0)
pdf.cell(w=34, h=5, txt="[Amount]", border=1, ln=1)  # end of line

pdf.set_font("Arial", "", 12)

# number are right-aligned so we give 'R' after new line parameter
pdf.cell(w=130, h=5, txt="[UltraColl]", border=1, ln=0)
pdf.cell(w=25, h=5, txt="[-]", border=1, ln=0)
pdf.cell(w=34, h=5, txt="[3,250]", border=1, ln=1, align="R")  # end of line

pdf.cell(w=130, h=5, txt="[Super clean ]", border=1, ln=0)
pdf.cell(w=25, h=5, txt="[-]", border=1, ln=0)
pdf.cell(w=34, h=5, txt="[3,250]", border=1, ln=1, align="R")  # end of line

pdf.cell(w=130, h=5, txt="[Super clean ]", border=1, ln=0)
pdf.cell(w=25, h=5, txt="[-]", border=1, ln=0)
pdf.cell(w=34, h=5, txt="[3,250]", border=1, ln=1, align="R")  # end of line

pdf.cell(w=130, h=5, txt="[Super clean ]", border=1, ln=0)
pdf.cell(w=25, h=5, txt="[-]", border=1, ln=0)
pdf.cell(w=34, h=5, txt="[3,250]", border=1, ln=1, align="R")  # end of line

# summary
pdf.cell(w=130, h=5, txt="", border=1, ln=0)
pdf.cell(w=25, h=5, txt="Subtotal", border=1, ln=0)
pdf.cell(w=4, h=5, txt="$", border=1, ln=0)
pdf.cell(w=30, h=5, txt="[3,250]", border=1, ln=1, align="R")  # end of line

pdf.cell(w=130, h=5, txt="", border=1, ln=0)
pdf.cell(w=25, h=5, txt="Subtotal", border=1, ln=0)
pdf.cell(w=4, h=5, txt="$", border=1, ln=0)
pdf.cell(w=30, h=5, txt="[3,250]", border=1, ln=1, align="R")  # end of line

pdf.cell(w=130, h=5, txt="", border=1, ln=0)
pdf.cell(w=25, h=5, txt="Subtotal", border=1, ln=0)
pdf.cell(w=4, h=5, txt="$", border=1, ln=0)
pdf.cell(w=30, h=5, txt="[3,250]", border=1, ln=1, align="R")  # end of line

# make a dumy empty cell as vertical spacer
pdf.cell(w=189, h=30, txt="", border=0, ln=1)  # end of line

# Footer client infos
pdf.cell(w=50, h=10, txt="Signature du client", border=0, ln=0, align="C")
pdf.cell(w=70, h=10, txt="", border=0, ln=0)
pdf.cell(w=69, h=10, txt="Signature",
         border=0, ln=1, align="C")  # enf of line

pdf.cell(w=120, h=10, txt="", border=0, ln=0)
pdf.cell(w=69, h=10, txt="Fait le ..../..../20.....",
         border=0, ln=1, align="C")  # enf of line

pdf.output("./medias/pdf/contrat.pdf")
