from turtle import clear
import yaml
import os
from pathlib import Path

#mostra as receitas contidas na pasta receitas
def ListarReceitas(pasta_receitas):
    #utiliza a classe Path pra que o sistema operacional reconheça o caminho do arquivo 
    caminho_arquivo= Path(pasta_receitas)
    #acessa os arquivos da pasta 
    for diretorio, subpastas, arquivos in os.walk(f'{caminho_arquivo}'):
        for arquivo in arquivos:
            print("\033[33mArquivo da receita: ",os.path.join(diretorio, arquivo),"\033[m")
            #realiza a leitura do arquivo
            with open(f'{os.path.join(diretorio, arquivo)}', 'r') as r:

                receita=yaml.safe_load(r)
                print("*"*100)
                #mostra as chaves e os valores contidos no dicionário da receita
                for chave, valor in receita.items():       
                    print(f'\033[34m{chave}\033[m : {valor} \n')
                print("*"*100)

ListarReceitas(input("Insira o caminho da pasta que contém as receitas: "))