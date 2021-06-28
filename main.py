# Software created for check repeated files inside directories

import os

main_path = r'C:\Users\rodri\Documents\DATABASE - BACKUP DE MIDIAS'
# main_path = r'C:\Users\rodri\Documents\GitHub\Junk File\test'

already_checked = []
double_media = []


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
                                # print('Arquivo duplicado encontrado: ', check_file)
                                # print('Caminho do arquivo em questão: ', check_root, '\n')
                                double_media.append(check_file)


                                already_checked.append(os.path.join(check_root, check_file))
                            else:
                                pass

def checkout():
    print('Relatório de arquivos verificados:\n')
    print('Quantidade de arquivos duplicados encontrados: ', len(double_media), '\n')

    info = input('Deseja abrir a lista de arquivos duplicados encontrados? (Y or N)')
    if info.upper() == 'Y':
        print('Exbindo lista de arquivos duplicados:\n')
        for dup_file in double_media:
            print(dup_file)

    else:
        print('Não iremos mostrar.')


if __name__ == "__main__":
    verify_files()
    checkout()
