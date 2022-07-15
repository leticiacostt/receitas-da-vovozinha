import os
import yaml
from os import listdir
from os.path import isfile, join
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

receipts_folder = 'receitas'

## carregar os arquivos de receita de forma relativa no sistema operacional ##

# obter caminho completo da pasta de receitas
print('1:', __file__)
dir_path = os.path.dirname(os.path.realpath(__file__))
print('2:', dir_path)
dir_path = os.path.dirname(dir_path)
print('3:', dir_path)
dir_path = os.path.dirname(dir_path)
print('4:', dir_path)
dir_path = os.path.join(dir_path, receipts_folder)
print('5:', dir_path)

def full_path(i):
  return join(dir_path, i)

# carregar os caminhos dos arquivos em uma lista
only_receipt_files = [full_path(i) for i in listdir(dir_path) if isfile(full_path(i))]

# lista os arquivos no terminal
for receipt_file in only_receipt_files:
  print(receipt_file)
  receipt = open(receipt_file, 'r').read()
  receipt = yaml.load(receipt, Loader=Loader)
  # print(yaml.dump(receipt))