from os import walk
import os
import shutil
import Paths
from customMessages import CustomMessage
class PdfFile:
    def executeTransfer(self, main_path):
        message = CustomMessage.CustomMessage()
        path = Paths.ReadPath()
        files = []
        print("entrou function")
        for (dirpath, dirnames, filenames) in walk(main_path):
            break
        for file in files:
            if not file.__contains__(".docx") and not file.__contains__(".pdf") and not file.__contains__(".txt"):
                continue
            print(f'2: {file}')
            if file.__contains__(".pdf"):
                if not os.path.exists(path.pdfPath(main_path)):
                    try:
                        os.makedirs(path.zipPath(main_path))
                        message.successMessage('Directory Created')
                    except OSError:
                        message.errorMessage("Erro ao criar o diretório")
            try:
                old_file_path = os.path.join(main_path, file)
                new_file_path = os.path.join(path.pdfPath(main_path), file)
                shutil.move(old_file_path, new_file_path)
                message.successMessage("Arquivos Movidos com sucesso")
            except:
                message.errorMessage("Não foi possível mover arquivos")