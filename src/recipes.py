
"""

"""

import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from file_methods import get_recipe_filenames

def load(receipt_filename):
    print('loading receipt:', receipt_filename)
    with open(receipt_filename, mode='r', encoding='utf8') as recipe_stream:
        return yaml.load(recipe_stream, Loader=Loader)

def dump(receipt_dictionary):
    return yaml.dump(receipt_dictionary, encoding='utf8', Dumper=Dumper, default_flow_style=False)

def print_all_as_dictionary():
    for filename in get_recipe_filenames():
        print('*'*100)
        print(load(filename))
        print('*'*100)

def print_all_as_string():
    for filename in get_recipe_filenames():
        print('*'*100)
        print(dump(load(filename)))
        print('*'*100)

if __name__ == '__main__':
    # print_all_as_dictionary()
    print_all_as_string()