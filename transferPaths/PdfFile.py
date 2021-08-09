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
            if file.endswith(".PDF") or file.endswith(".pdf"):
                if not os.path.exists(path.pdfPath()):
                    try:
                        os.makedirs(path.pdfPath())
                        message.successMessage('PDF Directory Created')
                    except OSError:
                        message.errorMessage("Could not create PDF directory")
                try:
                    old_file_path = os.path.join(main_path, file)
                    new_file_path = os.path.join(path.pdfPath(), file)
                    shutil.move(old_file_path, new_file_path)
                    message.successMessage(f"File {file} moved successfully to -> {new_file_path}")
                except:
                    message.errorMessage("Could not move file")