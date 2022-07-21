import os

import numpy as np

from paper_elements import A4
from pdf_methods import CertificatePDF
from datetime_methods import get_date_as_str as date

def get_certificate_filename():
    data_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(data_path,'data', 'certificates.csv')

def load_certificate_data():
    data = np.genfromtxt(get_certificate_filename(), skip_header=0, names=True,
        delimiter='\t',
        encoding='utf-8',
        dtype=None
    )
    return data

for row in load_certificate_data():
    name = row['NOME_COMPLETO']
    section_1 = 'CERTIFICADO DE CONCLUSÃO DE CURSO LIVRE'
    sub_section_1_1 = 'Certifico que ' + name + ' concluiu o curso de "Introdução à programação de experimentos comportamentais", em '+ date() +', com aproveitamento de 30 horas distribuídas entre atividades de supervisão técnica, formação teórico conceitual e treinamento prático.'

    paragraphs_to_write = [
        sub_section_1_1
    ]

    # Instantiation of inherited class
    pdf = CertificatePDF(orientation = 'L')
    pdf.set_auto_page_break(True, 25)
    pdf.set_margins(left=A4.margin_left+5/10, top=A4.margin_top/10, right=A4.margin_right/10)
    pdf.alias_nb_pages()
    pdf.add_page()
    for paragraph_title in paragraphs_to_write:
        pdf.section_title(section_1)
        pdf.section(paragraph_title)

    output_path_final = os.path.dirname(os.path.abspath(__file__))
    output_path_final = os.path.join(output_path_final, 'output')
    if not os.path.exists(output_path_final):
        os.makedirs(output_path_final)
    output_path_final = os.path.join(output_path_final, name)

    pdf.write_signature()
    pdf.output(output_path_final+'-certificado.pdf', 'F')