import os
import fpdf
import settings
from typing import Protocol
from collections import namedtuple

img = "AterellLogo.jpeg"

ReportClientInfos = namedtuple(
    "ReportClientInfos",
    [
        "contrat_id", "date", "name",
        "tel", "email", "adress", "num_rccm",
        "num_id", "num_p_id", "num_impot",
        "m_total", "m_payer", "m_rest"
    ]
)


class PdfReport(fpdf.FPDF):

    def hspacer(self, h: int = 10):
        # make a dumy empty cell as vertical spacer
        self.cell(w=189, h=h, txt="", border=0, ln=1)  # end of line

    def header_infos_title(self, lefttext: str, content: str, righttext: str = ""):
        # cell (width, height, text. border, end, align)
        self.cell(w=130, h=5, txt=lefttext, border=0, ln=0)
        self.cell(w=25, h=5, txt=righttext, border=0, ln=0)
        self.cell(w=34, h=5, txt=content, border=0, ln=1)  # end of line

    def footer_infos(self):
        # Footer client infos
        self.cell(w=50, h=10, txt="Signature du client",
                  border=0, ln=0, align="C")
        self.cell(w=70, h=10, txt="", border=0, ln=0)
        self.cell(w=69, h=10, txt="Signature",
                  border=0, ln=1, align="C")  # enf of line

        self.cell(w=120, h=10, txt="", border=0, ln=0)
        self.cell(w=69, h=10, txt="Fait le ..../..../20.....",
                  border=0, ln=1, align="C")  # enf of line

    def client_infos(self, text):
        self.cell(w=10, h=5, txt="", border=0, ln=0)
        self.cell(w=90, h=5, txt=text, border=0, ln=1)

    def content_infos_header(self, righttext: str, lefttext: str):
        self.cell(w=135, h=7, txt=lefttext, border=1, ln=0)
        self.cell(w=54, h=7, txt=righttext, border=1,
                  ln=1, align="C")  # end of line

    def content_infos(self, lefttext: str | int, righttext: str | int) -> None:
        self.cell(w=135, h=7, txt=str(lefttext), border=1, ln=0)
        self.cell(w=54, h=7, txt=str(righttext), border=1,
                  ln=1, align="R")  # end of line

    def summary_infos(self, title: str | int, content: str | int) -> None:
        self.cell(w=120, h=5, txt="", border=0, ln=0)
        self.cell(w=35, h=5, txt=str(title), border=0, ln=0)
        self.cell(w=4, h=5, txt="$", border=0, ln=0)
        self.cell(w=30, h=5, txt=str(content), border=0,
                  ln=1, align="R")  # end of line

    def create_document(self, infos: ReportClientInfos) -> None:
        self.add_page()
        # self.set_font("helvetica", "", 16)
        # # pdf.cell(40, 10, text)
        # self.cell(60, 10, text, new_x="LMARGIN", new_y="NEXT", align='C')

        self.image(name=os.path.join(settings.ASSETS_DIR, img), h=17, w=30)

        # set font to Arial, regular, 12pt
        self.set_font("Arial", "", 10)

        self.header_infos_title(
            lefttext="MANIKA, Q/LATIN", righttext="Date", content=f": {infos.date}")
        self.header_infos_title(
            lefttext="VILLE DE KOLWEZI, LUALABA, RDC", righttext="Contrat ID", content=f": {infos.contrat_id}")
        self.header_infos_title(
            lefttext="REF(3e PARCELLE avant CASINO ROYAL)", righttext="", content="")
        self.header_infos_title(
            lefttext="SERVICE CLIENT: +243816994448, +243974406506,+19045720001", righttext="", content="")
        self.header_infos_title(
            lefttext="WHATSAPP: +243972555466", righttext="", content="")
        self.header_infos_title(
            lefttext="FACEBOOK: Aterell solar", righttext="", content="")
        self.header_infos_title(
            lefttext="aterellsolor@gmail.com", righttext="", content="")

        # make a dumy empty cell as vertical spacer
        self.hspacer()

        self.set_font("Arial", "B", 14)
        # title
        self.cell(w=189, h=5, txt="CONTRAT", border=0, ln=1, align="C")

        # make a dumy empty cell as vertical spacer
        self.hspacer()

        self.set_font("Arial", "", 12)
        # publicher adress
        self.cell(w=34, h=5, txt="Contrat avec: ",
                  border=0, ln=1)  # end of line

        # add dunny cell at beginning of each line for indentation
        self.client_infos(text=str(infos.name).capitalize())
        self.client_infos(text=infos.tel)
        self.client_infos(text=infos.email)
        self.client_infos(text=infos.adress)

        # make a dumy empty cell as vertical spacer
        self.hspacer()

        # Invoice contents
        self.set_font("Arial", "B", 12)
        self.content_infos_header(lefttext="Description", righttext="Contenu")
        self.set_font("Arial", "", 12)

        # number are right-aligned so we give 'R' after new line parameter
        self.content_infos(lefttext="ID", righttext=infos.num_id)
        self.content_infos(lefttext="NUMERO PRODUIT ID",
                           righttext=infos.num_p_id)
        self.content_infos(lefttext="NUMERO IMPOT", righttext=infos.num_impot)
        self.content_infos(lefttext="NUMERO RCCM", righttext=infos.num_rccm)

        # make a dumy empty cell as vertical spacer
        self.hspacer(h=5)

        # summary
        self.summary_infos(title="Montant Total", content=infos.m_total)
        self.summary_infos(title="Montant Payer", content=infos.m_payer)
        self.summary_infos(title="Montant Restant", content=infos.m_rest)

        # make a dumy empty cell as vertical spacer
        self.hspacer(h=30)

        # Footer client infos
        self.footer_infos()


class PdfService:
    def __init__(self, pdfreport: PdfReport) -> None:
        self.pdfreport = pdfreport

    def save(self, filename: str) -> None:
        self.pdfreport.output(filename)

    def print(self,) -> None:
        pass
