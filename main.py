from engine import *
import time


if __name__ == "__main__":

    try:
        print('>INICIANDO VARREDURA DE ARQUIVOS...<')
        verify_files()
        print('VARREDURA FINALIZADA, ARQUIVOS ALOCADOS NA MEMÓRIA.')
    except Exception as e_verify_files:
        print('ERRO AO CHAMAR A FUNLÇAO verify_files()')
        print(e_verify_files)

    time.sleep(2)

    print('---------------------------------------------------------\n')

    # ===================================================
    print('RELATÓRIO DE ARQUIVOS VERIFICADOS:')
    try:
        checkout()
        print('RELATÓRIO GERADO COM SUCESSO!')
    except Exception as e_checkout:
        print('ERRO AO CHAMAR A FUNLÇAO checkout()')
        print(e_checkout)

    print('---------------------------------------------------------\n')

    # ===================================================
    print('COLETANDO EXTENSÃO DOS ARQUIVOS DUPLICADOS ENCONTRADOS...')
    try:
        grab_file_extension()
        print('COLETA REALIZADA COM SUCESSO!')
    except Exception as e_grab_file_extension:
        print('ERRO AO CHAMAR A FUNLÇAO grab_file_extension()')
        print(e_grab_file_extension)

    print('---------------------------------------------------------\n')

    # ===================================================
    print('CRIANDO ARQUIVOS E PASTAS NECESSÁRIAS...')
    try:
        create_folders()
        print('CRIAÇÃO REALIZADA COM SUCESSO!')
    except Exception as e_create_folders:
        print('ERRO AO CHAMAR A FUNÇAO create_folders()')
        print(e_create_folders)

    print('---------------------------------------------------------\n')

    # ===================================================
    print('ESCREVENDO INFORMAÇÕES EM ARQUIVOS')
    try:
        write_file()
        print('ARQUIVOS ESCRITOS COM SUCESSO!')
    except Exception as e_write_file:
        print('ERRO AO CHAMAR A FUNLÇAO write_file()')
        print(e_write_file)

    print('---------------------------------------------------------\n')

    # ===================================================
    print('REALIZANDO CÓPIA DOS ARQUIVOS...')
    try:
        copy_files()
        print('CÓPIA DOS ARQUIVOS REALIZADA COM SUCESSO!')
    except Exception as e_copy_files:
        print('ERRO AO CHAMAR A FUNLÇAO copy_files()')
        print(e_copy_files)

