from os import walk
import os
import shutil
import Paths
from customMessages import CustomMessage
class PdfFile:

    def execute_transfer_pdf(self, main_path):
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
                if not os.path.exists(path.pdf_path()):
                    try:
                        os.makedirs(path.pdf_path())
                        message.success_message('PDF Directory Created')
                    except:
                        message.error_message("Could not create PDF directory")
                try:
                    old_file_path = os.path.join(main_path, file)
                    new_file_path = os.path.join(path.pdf_path(), file)
                    shutil.move(old_file_path, new_file_path)
                    message.success_message(f"File {file} moved successfully to -> {new_file_path}")
                except:
                    message.error_message("Could not move file")