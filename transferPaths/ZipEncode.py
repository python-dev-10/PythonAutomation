import os
from os import walk
import shutil
import Paths
class Zip:
    def executeTransfer(self, main_path):
        path = Paths.ReadPath()
        files = []

        for (dirpath, dirnames, filenames) in walk(main_path):
            print(f'files.extend(filenames): {files.extend(filenames)}')
            print(f'filenames: {filenames}')
            print(f'files: {files}')
            break
        for file in files:
            if not file.__contains__('.zip'):
                continue
            print(f'{file}')
            if file.__contains__('.zip'):
                if not os.path.exists(path.zipPath()):
                    try:
                        os.makedirs(path.zipPath())
                    except OSError:
                        print("Não foi possível criar o diretório")
            try:
                old_file_path = os.path.join(main_path, file)
                new_file_path = os.path.join(path.zipPath(), file)
                shutil.move(old_file_path, new_file_path)
            except:
                print("Não foi possível mover o arquivo")
