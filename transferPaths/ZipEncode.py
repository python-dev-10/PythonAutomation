import os
from os import walk
import shutil
import Paths
from customMessages import CustomMessage
class Zip:
    def executeTransfer(self, main_path):
        message = CustomMessage.CustomMessage()
        path = Paths.ReadPath()
        files = []

        for (dirpath, dirnames, filenames) in walk(main_path):
            break
        for file in files:
            if not file.__contains__('.zip'):
                continue
            print(f'{file}')
            if file.__contains__('.zip'):
                if not os.path.exists(path.zipPath(main_path)):
                    try:
                        os.makedirs(path.zipPath(main_path))
                        message.successMessage("Diretório ZIP criado com sucesso")
                    except OSError:
                        message.errorMessage('Não foi possível criar o diretório')
            try:
                old_file_path = os.path.join(main_path, file)
                new_file_path = os.path.join(path.zipPath(main_path), file)
                shutil.move(old_file_path, new_file_path)
                message.successMessage("Arquivos movidos com sucesso")
            except:
                message.errorMessage('Não foi possível mover o arquivo')
