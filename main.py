# Software created for check repeated files inside directories

import os
from shutil import copy
from collections import namedtuple
import uuid

main_path = r'D:\DATABASE - BACKUP DE MIDIAS'
# main_path = r'C:\Users\rodri\Documents\GitHub\Junk File\test'

already_checked = []
double_media = []
double_media_name = []
see_file = []
data_file_dict = {}


def verify_files():


    print('Iniciando varredura de arquivos...')

    for root, dirs, files in os.walk(main_path):

        for check_root, check_dirs, check_files in os.walk(main_path):

            if check_root == root:
                pass

            else:
                for file in files:

                    for check_file in check_files:
                        marked_file = os.path.join(check_root, check_file)

                        if marked_file in already_checked:
                            pass

                        else:
                            if file == check_file:
                                double_media.append(marked_file)
                                double_media_name.append(check_file)

                                if file in see_file:
                                    pass

                                else:
                                    see_file.append(file)

                                already_checked.append(os.path.join(check_root, check_file))
                            else:
                                pass

    checkout()


def checkout():
    print('Relatório de arquivos verificados:\n')
    print('Quantidade de arquivos duplicados encontrados: ', len(double_media), '\n')

    print('Exbindo lista de arquivos duplicados:\n')
    print(double_media)
    print(double_media_name)

    print('Arquivos duplicados encontrados sem repetição:')
    for dup_file2 in see_file:
        print(dup_file2)

    print('\n')
    grab_file_extension()


def grab_file_extension():
    extension_list = []

    for get_extension in see_file:
        file_extension = os.path.splitext(get_extension)[0]
        extension_list.append(file_extension)

    create_folders(use_extension_list=extension_list)


def create_folders(use_extension_list):

    new_path = r'C:\Users\rodri\Documents\GitHub\Junk File\data\Lista de arquivos duplicados'

    print('Criando pasta para alocar listagem de arquivos duplicados...')
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        print('Diretorio criado no caminho: ', new_path, '\n')

    else:
        print('Pasta ja existe!', '\n')

    """for get_folder in use_extension_list:
        new_folder = os.path.join(new_path, get_folder)

        print('Verificando possibilidade de criação da pasta ', '"', get_folder.upper(), '"')
        if not os.path.exists(new_folder):
            print('Criando pasta com o nome do arquivo duplicado: ', get_folder)
            os.makedirs(new_folder)
            print('Diretorio criado no caminho: ', new_folder, '\n')

        else:
            print('Pasta ja existe!', '\n')"""

    write_file()


def write_file():

    for get_file_name in see_file:

        create_path = f'./data/Lista de arquivos duplicados/{get_file_name}.txt'
        with open(create_path, 'w+') as f:
            for get_full_file in double_media:
                if get_file_name in get_full_file:
                    f.write(get_full_file)
                    f.write('\n')
                else:
                    pass

    copy_files()


def copy_files():
    verify_this_path = 'data/Lista de arquivos duplicados'
    path_temp_files = 'data/Arquivos_duplicados'

    print('Criando pasta para alocar todos os arquivos duplicados...')
    if not os.path.exists(path_temp_files):
        os.makedirs(path_temp_files)
        print('Diretorio criado no caminho: ', path_temp_files, '\n')

    else:
        print('Pasta ja existe!', '\n')

    for root, dirs, files in os.walk(verify_this_path):
        for file in files:
            print('Copiando arquivo: ', file.upper())
            open_file = os.path.join(root, file)
            with open(open_file, 'r') as f:
                for file_from_txt in f.readlines():
                    new_file_from_txt = file_from_txt.rstrip("\n")

                    try:

                        copy(new_file_from_txt, path_temp_files)

                    except OSError as error:
                        print(error)


if __name__ == "__main__":
    verify_files()

