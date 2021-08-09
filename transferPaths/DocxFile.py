from os import walk
import os
import shutil
import Paths
from customMessages import CustomMessage
class DocxFile:

    def executeTransfer(self, main_path):
        message = CustomMessage.CustomMessage()
        path = Paths.ReadPath()

        for (dirpath, dirnames, filenames) in walk(main_path):
            break
        for file in filenames:
            if not file.__contains__(".docx") and not file.__contains__(".DOCX"):
                continue
            if file.__contains__(".docx"):
                if not os.path.exists(path.docxPath()):
                    try:
                        os.makedirs(path.docxPath())
                        message.successMessage("DOCX directory created successfully")
                    except OSError:
                        message.errorMessage('Could not create the directory DOCX')
            try:
                old_file_path = os.path.join(main_path, file)
                new_file_path = os.path.join(path.docxPath(), file)
                shutil.move(old_file_path, new_file_path)
                message.successMessage(f"File {file} moved successfully to -> {new_file_path}")
            except:
                message.errorMessage("Could not move file")