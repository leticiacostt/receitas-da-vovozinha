import os
import yaml
from os import listdir
from os.path import isfile, join
try:
  from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
  from yaml import Loader, Dumper

"""
carregar os arquivos de receita de forma relativa no sistema operacional
"""

# 
receipts_folder = 'receitas'

# obter caminho completo da pasta de receitas
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = os.path.dirname(dir_path)
dir_path = os.path.dirname(dir_path)
dir_path = os.path.join(dir_path, receipts_folder)

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