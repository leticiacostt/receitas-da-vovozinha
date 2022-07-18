
"""

"""

import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from file_methods import get_recipe_filenames

def load_recipe(receipt_filename):
    print('loading receipt:', receipt_filename)
    with open(receipt_filename, mode='r', encoding='utf8') as recipe_stream:
        return yaml.load(recipe_stream, Loader=Loader)

def dump_recipe(receipt_dictionary):
    return yaml.dump(receipt_dictionary, encoding='utf8', Dumper=Dumper, default_flow_style=False)

def print_all_as_dictionary():
    for filename in get_recipe_filenames():
        print('*'*100)
        print(load_recipe(filename))
        print('*'*100)

def print_all_as_string():
    for filename in get_recipe_filenames():
        print('*'*100)
        print(dump_recipe(load_recipe(filename)))
        print('*'*100)

def find_recipe(search_string):
    def has_search_string(value):
        return search_string.upper() in value.upper()

    for filename in get_recipe_filenames():
        recipe_dict = load_recipe(filename)
        for _, value in recipe_dict.items():
            if type(value) is list:
                for i in value:
                    if has_search_string(i):
                        print('Found recipe!')
                        break
            else:
                if has_search_string(value):
                    print('Found recipe!')
                    break

if __name__ == '__main__':
    # print_all_as_dictionary()
    print_all_as_string()