"""
inicializa uma variável (receipts_folder) com o caminho completo da pasta de receitas

para saber mais sobre a função os.path.abspath ver:

https://stackoverflow.com/questions/37863476/why-would-one-use-both-os-path-abspath-and-os-path-realpath
"""
import os

base_dir = os.path.abspath(__file__).rsplit('src', 1)[0]
recipes_folder = os.path.join(base_dir, 'receitas')
assets_folder = os.path.join(base_dir, 'src', 'certificates', 'assets')

if __name__ == '__main__':
    print(recipes_folder)