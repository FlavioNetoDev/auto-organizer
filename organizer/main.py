from pathlib import Path
import shutil
print('====== AUTO-ORGANIZER ======')
downloads = Path.home() / 'Downloads' # Identifica o caminho da pasta downloads do usuario
nome = input('Digite o nome do arquivo: ') # Pede o nome do arquivo que quer organizar
arquivo = downloads / nome # Identifica o arquivo na pasta downloads

if arquivo.is_file(): # Verifica se o conteúdo é um arquivo
    print('Arquivo encontrado!')  # Exibe que o arquivo foi encontrado
    if arquivo.suffix.lower() == '.png' or arquivo.suffix.lower() == '.jpg' or arquivo.suffix.lower() == '.jpeg': # Pega a extensão do arquivo e compara com as extensões citadas e identifica o tipo
        print('O arquivo é uma imagem.') # Exibe o tipo identificado 
        pasta = downloads / 'Imagens' # Mostra o caminho em que a pasta deve ser criada
        pasta.mkdir(exist_ok=True) # Cria a pasta e verifica se ela ja existe
        destino = pasta / nome 
        if destino.exists(): # Verifica se ja contém um arquivo com o mesmo nome na pasta destinada
            print('O arquivo ja existe na pasta') # Exibe que o arquivo ja existe
        else: # Senao existir
            shutil.move(arquivo, pasta) # Move o arquivo da pasta downloads para a pasta relacionada ao tipo do arquivo
            print('Arquivo movido para a pasta {}'.format(pasta)) # Exibe que o arquivo foi movido para a pasta relacionada
    elif arquivo.suffix.lower() == '.pdf' or arquivo.suffix.lower() == '.doc' or arquivo.suffix.lower() == '.txt': # Pega a extensão do arquivo e compara com as extensões citadas e identifica o tipo
        print('O arquivo é um documento') # Exibe o tipo identificado
        pasta = downloads / 'Documentos' # Mostra o caminho em que a pasta deve ser criada
        pasta.mkdir(exist_ok=True) # Cria a pasta e verifica se ela existe
        destino = pasta / nome 
        if destino.exists(): # Verifica se ja contém um arquivo com o mesmo nome na pasta destinada
            print('O arquivo ja existe na pasta') # Exibe que o arquivo ja existe
        else: #Senao existir
            shutil.move(arquivo, pasta) # Move o arquivo da pasta downloads para a pasta relacionada ao tipo do arquivo
            print('Arquivo movido para a pasta {}'.format(pasta)) # Exibe que o arquivo foi movido para pasta relacionada
    elif arquivo.suffix.lower() == '.mp3' or arquivo.suffix.lower() == '.wav': # Pega a extensão do arquivo e compara com as extensões citadas e identifica o tipo
        print('O arquivo é uma faixa de audio') # Exibe o tipo identificado
        pasta = downloads / 'Sons' # Mostra o caminho em que a pasta deve ser criada
        pasta.mkdir(exist_ok=True) # Cria a pasta e verifica se ela existe
        destino = pasta / nome 
        if destino.exists(): # Verifica se ja contém um arquivo como mesmo nome na pasta destinada
            print('O arquivo ja existe na pasta') # Exibe que o arquivo ja existe
        else: #Senao existir
            shutil.move(arquivo, pasta) # Move o arquivo da pasta downloads para a pasta relacionada ao tipo do arquivo
            print('Arquivo movido para a pasta {}'.format(pasta)) # Exibe que o arquivo foi movido para a pasta relacionada
    else: #Senao reconhecer o tipo do arquivo
        print('Tipo de arquivo não reconhecido.') #Exibe
else:
    print('Arquivo não encontrado') # Mostra que o arquivo digitado não foi encontrado 
