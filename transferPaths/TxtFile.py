from os import walk
import os
import shutil
import Paths
from customMessages import CustomMessage
class TxtFile:
    def execute_transfer_txt(self, main_path):
        path = Paths.ReadPath()
        message = CustomMessage.CustomMessage()

        for (dirpath, dirnames, filenames) in walk(main_path):
            break
        for file in filenames:
            if not file.endswith(".TXT") and not file.endswith(".txt"):
                continue
            print(f'2: {file}')
            if file.endswith('.txt'):
                if not os.path.exists(path.txt_path()):
                    try:
                        os.makedirs(path.txt_path())
                        message.success_message("TXT directory created successfully")
                    except:
                        message.error_message("Could not create TXT directory")
            try:
                old_file_path = os.path.join(main_path, file)
                new_file_path = os.path.join(path.txt_path(), file)
                shutil.move(old_file_path, new_file_path)
                message.success_message(f"File {file} moved successfully to -> {new_file_path}")
            except:
                message.error_message("Could not move file")