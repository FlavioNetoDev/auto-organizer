from pathlib import Path
import shutil
print('====== AUTO-ORGANIZER ======')
downloads = Path.home() / 'Downloads' # Identifica o caminho da pasta downloads do usuario
nome = input('Digite o nome do arquivo: ') # Pede o nome do arquivo que quer organizar
arquivo = downloads / nome # Identifica o arquivo na pasta downloads

if arquivo.is_file(): # Verifica se o conteúdo é um arquivo
    print('Arquivo encontrado!')  # Exibe que o arquivo foi encontrado
    if arquivo.suffix.lower() == '.png' or arquivo.suffix.lower() == '.jpg': # Pega a extensão do arquivo e compara com as extensões citadas e identifica o tipo
        print('O arquivo é uma imagem.') # Exibe o tipo identificado 
        pasta = downloads / 'Imagens' # Mostra o caminho em que a pasta deve ser criada
        pasta.mkdir(exist_ok=True) # Cria a pasta e verifica se ela ja existe ou não, retorna True ou False
        destino = pasta / nome # 
        if destino.exists(): # Verifica se ja contém um arquivo com o mesmo nome na pasta destinada
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
