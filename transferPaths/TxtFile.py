from os import walk
import os
import shutil
import Paths
class TxtFile():
    def executeTransfer(self, main_path):
        path = Paths.ReadPath()
        files = []

        for (dirpath, dirnames, filenames) in walk(main_path):
            # files.extend(filenames)
            print(f'files.extend(filenames): {files.extend(filenames)}')
            print(f'filenames: {filenames}')
            print(f'files: {files}')
            break
        for file in files:
            if not file.__contains__(".docx") and not file.__contains__(".pdf") and not file.__contains__(".txt"):
                continue
            print(f'2: {file}')
            if file.__contains__('.txt'):
                print(main_path)
                old_file_path = os.path.join(main_path, file)
                new_file_path = os.path.join(path.txtPath(main_path), file)
                shutil.move(old_file_path, new_file_path)