# -*- coding: utf-8 -*-

from fpdf import FPDF
from file_methods import professor_signature_filename

from paper_elements import A4, Logo, Footer

utf8_font = 'Arial'

class CertificatePDF(FPDF):
    def header(self):
        # Logo
        self.image('ufpa-logo.png', Logo.left, Logo.top, Logo.width)
        self.set_font(utf8_font, '', 12)
        self.ln(40)

    # Page footer
    def footer(self):
        self.image('footer.jpg', Footer.left, Footer.top, Footer.width, Footer.height)

        # Footer title
        self.set_y(-20)
        self.set_font(utf8_font, 'B', 8)
        self.cell(0, 3, 'Universidade Federal do Pará', 0, 0, align='C')
        self.ln(3)

        # Footer line 1
        self.set_font(utf8_font, '', 8)
        self.cell(0, 3, 'Rua Augusto Corrêa, 01, Guamá 66075-110, Belém, Pará, Brasil.', 0, 0, align='C')
        self.ln(3)

        # Footer line 2
        self.set_font(utf8_font, '', 8)
        self.cell(0, 3, '', 0, 0, align='C')
        self.ln(3)

    def section_title(self, title):
        # Arial bold 12
        self.set_font(utf8_font, 'B', 14)

        # centered
        self.cell(w=0, h = 5,
            txt = title, border = 0, ln = 1,
            align = 'C', fill = False, link = '')

        # Line break
        self.ln(20)

    def sub_section_title(self,subsection):
        # Arial bold 12
        self.set_font(utf8_font, 'B', 12)

        # centered
        self.cell(w=0, h = 5,
            txt = subsection, border = 0, ln = 1,
            align = 'L', fill = False, link = '')

        # Line break
        self.ln(5)

    def section(self, text):
        # Arial bold 12
        self.set_font(utf8_font, '', 14)

        # centered
        self.multi_cell(0, 15, text.replace('\u201c', '"').replace('\u201d', '"').replace('\u2013', '-').replace('\u2019', "'").replace('\u0283','s').replace('\u0301', ''))

        # Line break
        self.ln(5)

    def write_signature(self):
        # Line break
        self.ln(5)
        self.set_font(utf8_font, '', 8)
        self.set_y(60)
        self.set_x(A4.centerx+40)
        image_center = A4.centerx-22
        column3 = A4.centerx-22

        self.image(name=professor_signature_filename(), x=image_center, w=60)
        self.set_x(column3)
        self.cell(w=0, h = 3,
            txt = 'Dr. Carlos Rafael Fernandes Picanço', border = 0, ln = 1,
            align = 'C', fill = False, link = '')
        self.set_x(column3)
        self.cell(w=0, h = 3,
            txt = 'Analista do Comportamento', border = 0, ln = 1,
            align = 'C', fill = False, link = '')
        self.set_x(column3)
        self.cell(w=0, h = 3,
            txt = 'Pesquisador e Desenvolvimentor', border = 0, ln = 1,
            align = 'C', fill = False, link = '')
        self.ln(5)