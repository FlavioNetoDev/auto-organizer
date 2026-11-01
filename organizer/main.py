from pathlib import Path
import shutil
print('====== AUTO-ORGANIZER ======')
downloads = Path.home() / 'Downloads'
nome = input('Digite o nome do arquivo: ')
arquivo = downloads / nome

if arquivo.is_file():
    print('Arquivo encontrado!')
    if arquivo.suffix.lower() == '.png' or arquivo.suffix.lower() == '.jpg':
        print('O arquivo é uma imagem.')
        pasta = downloads / 'Imagens'
        pasta.mkdir(exist_ok=True)
        destino = pasta / nome
        if destino.exists():
            print('O arquivo ja existe na pasta')
        else:
            shutil.move(arquivo, pasta)
            print('Arquivo movido para a pasta {}'.format(pasta))
    elif arquivo.suffix.lower() == '.pdf' or arquivo.suffix.lower() == '.doc' or arquivo.suffix.lower() == '.txt':
        print('O arquivo é um documento')
        pasta = downloads / 'Documentos'
        pasta.mkdir(exist_ok=True)
        destino = pasta / nome
        if destino.exists():
            print('O arquivo ja existe na pasta')
        else:
            shutil.move(arquivo, pasta)
            print('Arquivo movido para a pasta {}'.format(pasta))
    elif arquivo.suffix.lower() == '.mp3' or arquivo.suffix.lower() == '.wav':
        print('O arquivo é uma faixa de audio')
        pasta = downloads / 'Sons'
        pasta.mkdir(exist_ok=True)
        destino = pasta / nome
        if destino.exists():
            print('O arquivo ja existe na pasta')
        else:
            shutil.move(arquivo, pasta)
            print('Arquivo movido para a pasta {}'.format(pasta))
    else:
        print('Tipo de arquivo não reconhecido.')
else:
    print('Arquivo não encontrado')
