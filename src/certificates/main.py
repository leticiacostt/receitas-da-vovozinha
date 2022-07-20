from paper_elements import C

for row in load_certificates_csv():
    nome = row['NOME_COMPLETO']
    section_1 = 'CERTIFICADO DE FORMAÇÃO CONTINUADA EM ANÁLISE DO COMPORTAMENTO APLICADA AO AUTISMO'
    horas = row['HORAS_TOTAIS']
    sub_section_1_1 = 'Certificamos que ' + nome + ', até à presente data, dia '+date+', recebeu da equipe de mestres e doutores em Análise do Comportamento da Imagine Tecnologia Comportamental LTDA ' + horas + ' horas de capacitação em Análise do Comportamento Aplicada (ABA) ao Autismo, incluindo (1) atividades de supervisão técnica em grupo; (2) formação teórico conceitual em ABA; (3) treinamento prático para execução de procedimentos ABA baseados em evidência; e (4) orientação em ética e diretrizes profissionais.' 

    paragraphs_to_write = [
        sub_section_1_1
    ]

    # Instantiation of inherited class
    pdf = CertificatePDF(orientation = 'L')
    pdf.set_auto_page_break(True, 25)
    pdf.set_margins(left=margin_left+5/10, top=margin_top/10, right=margin_right/10)
    pdf.alias_nb_pages()
    pdf.add_page()
    for paragraph_title in paragraphs_to_write:
        pdf.section_title(section_1)
        pdf.section(paragraph_title)

    output_path_final = os.path.dirname(os.path.abspath(__file__))
    output_path_final = os.path.join(output_path_final, 'certificates')
    output_path_final = os.path.join(output_path_final, nome)

    pdf.write_signature()
    pdf.output(output_path_final+'-certificado.pdf', 'F')