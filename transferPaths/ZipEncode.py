import os
from os import walk
import shutil
import Paths
from customMessages import CustomMessage

class Zip:

    def execute_transfer_zip(self, main_path):
        message = CustomMessage.CustomMessage()
        path = Paths.ReadPath()

        for (dirpath, dirnames, filenames) in walk(main_path):
            break
        for file in filenames:
            if not file.__contains__('.zip') and not file.__contains__('.ZIP'):
                continue
            print(f'{file}')
            if file.__contains__('.zip'):
                if not os.path.exists(path.zipPath()):
                    try:
                        os.makedirs(path.zipPath())
                        message.success_message("ZIP directory created successfully")
                    except:
                        message.error_message('Could not create ZIP directory')
            try:
                old_file_path = os.path.join(main_path, file)
                new_file_path = os.path.join(path.zipPath(), file)
                shutil.move(old_file_path, new_file_path)
                message.success_message(f"File {file} moved successfully to -> {new_file_path}")
            except:
                message.error_message('Could not move file')