from os import walk
import os
import shutil
import Paths
from customMessages import CustomMessage
class TxtFile():
    def executeTransfer(self, main_path):
        path = Paths.ReadPath()
        files = []
        message = CustomMessage.CustomMessage()

        for (dirpath, dirnames, filenames) in walk(main_path):
            break
        for file in files:
            if not file.__contains__(".docx") and not file.__contains__(".pdf") and not file.__contains__(".txt"):
                continue
            print(f'2: {file}')
            if file.__contains__('.txt'):
                if not os.path.exists(path.txtPath(main_path)):
                    try:
                        os.makedirs(path.txtPath(main_path))
                        message.successMessage("Diretório criado com sucesso")
                    except OSError:
                        message.errorMessage("Não foi possível criar diretório")
            try:
                old_file_path = os.path.join(main_path, file)
                new_file_path = os.path.join(path.txtPath(main_path), file)
                shutil.move(old_file_path, new_file_path)
                message.successMessage("Arquivos movidos com sucesso")
            except:
                message.errorMessage("Não foi possível mover os arquivos")