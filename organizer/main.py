import pathlib
import shutil
print('====== AUTO ORGANIZADOR ======')
print()
print('1 - Organizar imagens \n2 - Organizar documentos \n3 - Sair')

opc = int(input('Escolha uma opção: '))

if opc == 1:
    print('Você escolheu organizar imagens')
    arqv = input('Digite o nome do arquivo que deseja organizar: ').lower()
    if arqv.endswith('.png') or arqv.endswith('.jpg'):
        print('Tipo de arquivo: Imagem ')
        print('Esse arquvio deve ficar na pasta imagens ')
    else:
        print('O arquivo não é uma imagem ')
        exit()
elif opc == 2:
    print('Você escolheu organizar documentos')
    arqv2 = input('Digite o nome do arquivo que deseja organizar: ').lower()
    if arqv2.endswith('.pdf') or arqv2.endswith('.txt'):
        print('Tipo de arquivo: Documento ')
        print('Esse arquivo deve ficar na pasta documentos. ')
    else:
        print('O arquivo não é um documento ')
        exit()
elif opc == 3:
    print('Fechando o programa...')
    exit()
else:
    print('Número inválido ')
    exit()