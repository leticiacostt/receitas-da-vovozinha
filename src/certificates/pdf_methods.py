# -*- coding: utf-8 -*-
import os, sys
base_dir = os.path.abspath(__file__).rsplit('src', 1)[0]
sys.path.append(os.path.join(base_dir, 'src'))

from fpdf import FPDF
from file_methods import get_asset_filename

from paper_elements import A4, Logo, Footer

class CertificatePDF(FPDF):
    utf8_font = 'Arial'
    def header(self):
        # Logo
        self.image(get_asset_filename('ufpa-logo.png'), Logo.left, Logo.top, Logo.width)
        self.set_font(self.utf8_font, '', 12)
        self.ln(40)

    # Page footer
    def footer(self):
        self.image(get_asset_filename('footer.png'), Footer.left, Footer.top, Footer.width, Footer.height)

        # Footer title
        self.set_y(-10)
        self.set_font(self.utf8_font, 'B', 8)
        self.cell(0, 3, 'Universidade Federal do Pará', 0, 0, align='C')
        self.ln(3)

        # Footer line 1
        self.set_font(self.utf8_font, '', 8)
        self.cell(0, 3, 'Rua Augusto Corrêa, 01, Guamá 66075-110, Belém, Pará, Brasil.', 0, 0, align='C')
        self.ln(3)

        # Footer line 2
        self.set_font(self.utf8_font, '', 8)
        self.cell(0, 3, '', 0, 0, align='C')
        self.ln(3)

    def section_title(self, title):
        # Arial bold 12
        self.set_font(self.utf8_font, 'B', 14)

        # centered
        self.cell(w=0, h = 5,
            txt = title, border = 0, ln = 1,
            align = 'C', fill = False, link = '')

        # Line break
        self.ln(20)

    def sub_section_title(self,subsection):
        # Arial bold 12
        self.set_font(self.utf8_font, 'B', 12)

        # centered
        self.cell(w=0, h = 5,
            txt = subsection, border = 0, ln = 1,
            align = 'L', fill = False, link = '')

        # Line break
        self.ln(5)

    def section(self, text):
        # Arial bold 12
        self.set_font(self.utf8_font, '', 14)

        # centered
        self.multi_cell(0, 15, text.replace('\u201c', '"').replace('\u201d', '"').replace('\u2013', '-').replace('\u2019', "'").replace('\u0283','s').replace('\u0301', ''))

        # Line break
        self.ln(5)

    def write_signature(self):
        # Line break
        self.ln(5)
        self.set_font(self.utf8_font, '', 8)
        self.set_y(-80)

        column3 = A4.centerx-120
        image_center = A4.centerx-40
        self.set_x(column3)
        self.image(name=get_asset_filename('Carlos Rafael Fernandes Picanço.jpg'), x=image_center, w=80)
        self.set_x(column3)
        self.cell(w=0, h = 3,
            txt = 'Prof. Dr. Carlos Rafael Fernandes Picanço', border = 0, ln = 1,
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