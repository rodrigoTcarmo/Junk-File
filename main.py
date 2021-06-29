# Software created for check repeated files inside directories

import os
from collections import namedtuple
import uuid

# main_path = r'D:\DATABASE - BACKUP DE MIDIAS'
main_path = r'C:\Users\rodri\Documents\GitHub\Junk File\test'

already_checked = []
double_media = []
double_media_name = []
see_file = []


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

                                data_file = namedtuple('data_file', ['name', 'path'])
                                arquivos = data_file(check_file, check_root)

                                if file in see_file:
                                    pass

                                else:
                                    see_file.append(file)

                                already_checked.append(os.path.join(check_root, check_file))
                            else:
                                pass

    checkout(use_arquivos=arquivos)


def checkout(use_arquivos):
    print('Relatório de arquivos verificados:\n')
    print('Quantidade de arquivos duplicados encontrados: ', len(double_media), '\n')

    # info = input('Deseja abrir a lista de arquivos duplicados encontrados? (Y or N)')
    # if info.upper() == 'Y':
    print('Exbindo lista de arquivos duplicados:\n')
    """for dup_file in double_media:
        print(dup_file)
    print('\n')"""

    print(use_arquivos)

    print('Arquivos duplicados encontrados sem repetição:')
    for dup_file2 in see_file:
        print(dup_file2)

    # else:
        # print('Não iremos mostrar.')


if __name__ == "__main__":
    verify_files()

