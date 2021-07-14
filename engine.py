# Software created for check repeated files inside directories

import os
from shutil import copy

already_checked = []
double_media = []
double_media_name = []
see_file = []
data_file_dict = {}


def verify_files():
    main_path = r'C:\Users\rodri\Documents\DATABASE - BACKUP DE MIDIAS'

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


def checkout():
    print('Quantidade de arquivos duplicados encontrados: ', len(double_media), '\n')

    if len(double_media) > 15:
        check_double_file = f'./data/Arquivos duplicados encontrados.txt'
        check_double_file_path = f'./data/Arquivos duplicados encontrados com caminho.txt'

        print('Muitos arquivos duplicados foram encontrados')
        print('A lista completa desses arquivos estão localizados em: ', check_double_file)

        with open(check_double_file, 'w+') as check_f:
            for print_to_file in double_media_name:
                check_f.write(print_to_file)
                check_f.write('\n')

        with open(check_double_file_path, 'w+') as check_f_path:
            for print_path_to_file in double_media:
                check_f_path.write(print_path_to_file)
                check_f_path.write('\n')

    else:
        print('Exbindo lista de arquivos duplicados:\n')
        print(double_media)
        print(double_media_name)

    print('\n')
    if len(see_file) > 15:

        check_double_filename = './data/Nome dos arquivos com mais de uma copia.txt'
        print('Nome dos arquivos duplicados encontrados estão presentes no arquivo: ', )

        with open(check_double_filename, 'w+') as check_fname:
            for double_file in see_file:
                check_fname.write(double_file)
                check_fname.write('\n')

    else:
        print("Exibindo nome dos arquivos com mais de uma cópia encontrados:")
        for show_file in see_file:
            print(show_file)

    print('\n')


def grab_file_extension():
    extension_list = []

    for get_extension in see_file:
        file_extension = os.path.splitext(get_extension)[0]
        extension_list.append(file_extension)


def create_folders():

    new_path = r'C:\Users\rodri\Documents\GitHub\Junk File\data\Lista de arquivos duplicados'

    print('Criando pasta para alocar listagem de arquivos duplicados...')
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        print('Diretorio criado no caminho: ', new_path, '\n')

    else:
        print('Pasta ja existe!', '\n')


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
            print('Copiando arquivo:')
            open_file = os.path.join(root, file)
            with open(open_file, 'r') as f:
                for file_from_txt in f.readlines():
                    new_file_from_txt = file_from_txt.rstrip("\n")

                    print(new_file_from_txt)
                    try:
                        copy(new_file_from_txt, path_temp_files)
                        os.remove(new_file_from_txt)

                    except OSError as error:
                        print(error)

            print('\n')

