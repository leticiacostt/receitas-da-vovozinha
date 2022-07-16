from termios import CERASE
from turtle import clear
import yaml
import os
#mostra as receitas contidas na pasta receitas
pasta = './receitas'

for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        print("Aequivo da receita: ",os.path.join(diretorio, arquivo))

        with open(f'{os.path.join(diretorio, arquivo)}', 'r') as r:

            receita=yaml.safe_load(r)
            print("*"*100)
            
            for chave, valor in receita.items():
                
                print(f'\033[34m{chave}\033[m : {valor} \n')
            print("*"*100)