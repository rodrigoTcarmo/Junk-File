# Software created for check repeated files inside directories

import os

main_path = r'C:\Users\rodri\Documents\GitHub\Junk File\test'
file_path_list = []
file_list = []
root_list = []

already_checked = []


def verify_files():

    for root, dirs, files in os.walk(main_path):

        for check_root, check_dirs, check_files in os.walk(main_path):

            if check_root == root:
                pass

            else:
                for file in files:

                    for check_file in check_files:
                        if check_file in already_checked:
                            pass

                        else:
                            if file == check_file:
                                print('Arquivo duplicado encontrado: ', check_file)
                                print('Caminho do arquivo em questão: ', check_root, '\n')

                                already_checked.append(os.path.join(check_root, file))
                            else:
                                pass


if __name__ == "__main__":
    verify_files()
