import os
from variables import recipes_folder

def get_recipe_filenames():
    def filename(i):
        return os.path.join(recipes_folder, i)

    def is_file(filename):
        return os.path.isfile(filename)
    return [filename(i) for i in os.listdir(recipes_folder) if is_file(filename(i))]

if __name__ == '__main__':
    print(get_recipe_filenames())