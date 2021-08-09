from os import walk
import os
import shutil
import Paths
from customMessages import CustomMessage
class TxtFile():
    def executeTransfer(self, main_path):
        print(main_path)
        path = Paths.ReadPath()
        message = CustomMessage.CustomMessage()

        for (dirpath, dirnames, filenames) in walk(main_path):
            break
        for file in filenames:
            if not file.endswith(".TXT") and not file.endswith(".txt"):
                continue
            print(f'2: {file}')
            if file.endswith('.txt'):
                if not os.path.exists(path.txtPath()):
                    try:
                        os.makedirs(path.txtPath())
                        message.successMessage("Diretório criado com sucesso")
                    except OSError:
                        message.errorMessage("Não foi possível criar diretório")
            try:
                old_file_path = os.path.join(main_path, file)
                new_file_path = os.path.join(path.txtPath(), file)
                shutil.move(old_file_path, new_file_path)
                message.successMessage("Arquivos movidos com sucesso")
            except:
                message.errorMessage("Não foi possível mover os arquivos")