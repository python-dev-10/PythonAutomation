from os import walk
import os
import shutil
import Paths
from customMessages import CustomMessage
class PdfFile:
    def executeTransfer(self, main_path):
        message = CustomMessage.CustomMessage()
        path = Paths.ReadPath()
        for (dirpath, dirnames, filenames) in walk(main_path):
            print(f"filenames {filenames}")
            break
        for file in filenames:
            print(f"file {file}")
            if not file.__contains__(".PDF") and not file.__contains__(".pdf"):
                continue
            if file.endswith(".PDF"):
                if not os.path.exists(path.pdfPath()):
                    try:
                        os.makedirs(path.pdfPath())
                        message.successMessage('Directory Created')
                    except OSError:
                        message.errorMessage("Erro ao criar o diretório")
                try:
                    old_file_path = os.path.join(main_path, file)
                    new_file_path = os.path.join(path.pdfPath(), file)
                    shutil.move(old_file_path, new_file_path)
                    message.successMessage("Arquivos Movidos com sucesso")
                except:
                    message.errorMessage("Não foi possível mover arquivos")