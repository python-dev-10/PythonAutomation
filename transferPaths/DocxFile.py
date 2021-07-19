from os import walk
import os
import shutil
import Paths
from customMessages import CustomMessage
class DocxFile:
    def executeTransfer(self, main_path):
        message = CustomMessage.CustomMessage()
        path = Paths.ReadPath()
        files = []

        for (dirpath, dirnames, filenames) in walk(main_path):
            break
        for file in files:
            if not file.__contains__(".docx") and not file.__contains__(".pdf") and not file.__contains__(".txt"):
                continue
            print(f'2: {file}')
            if file.__contains__(".docx"):
                if not os.path.exists(path.docxPath(main_path)):
                    try:
                        os.makedirs(path.docxPath(main_path))
                        message.successMessage("Diretório DOCX criado com sucesso")
                    except OSError:
                        message.errorMessage('Não foi possível criar o diretório')
            try:
                old_file_path = os.path.join(main_path, file)
                new_file_path = os.path.join(path.docxPath(main_path), file)
                shutil.move(old_file_path, new_file_path)
            except:
                message.errorMessage("Não foi possível mover o arquivo")