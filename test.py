from collections import namedtuple

file = namedtuple('arquivos', ['nome', 'caminho'])

arquivo_03 = file('Nome_do_arquivo', r'c:\rodri\documents')

print(arquivo_03)
