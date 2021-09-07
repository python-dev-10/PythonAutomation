import os
class ReadPath():

    def __init__(self):
        self._home_path = os.path.expanduser('~')

    def get_home_path(self):
        return self._home_path

    def documents(self):
        return rf"{ReadPath().get_home_path()}{os.sep}Documentos{os.sep}"

    def dowload(self,home_path):
        return rf"{home_path}{os.sep}Downloads{os.sep}"

    def docx_path(self):
        home = ReadPath().get_main_path_user()
        if os.path.exists(f'{home}{os.sep}PythonMover{os.sep}DOCX{os.sep}'):
            return rf"{home}{os.sep}PythonMover{os.sep}DOCX{os.sep}"
        else:
            return os.makedirs(f'{home}{os.sep}PythonMover{os.sep}DOCX{os.sep}')
    def pdf_path(self):
        home = ReadPath().get_main_path_user()
        print(f'{home}{os.sep}PythonMover{os.sep}PDF{os.sep}')
        if os.path.exists(rf'{home}{os.sep}PythonMover{os.sep}PDF{os.sep}'):
            return rf"{home}{os.sep}PythonMover{os.sep}PDF{os.sep}"
        else:
            return os.makedirs(f'{home}{os.sep}PythonMover{os.sep}PDF{os.sep}')
    def txt_path(self):
        home = ReadPath().get_main_path_user()
        if os.path.exists(f'{home}{os.sep}PythonMover{os.sep}TXT{os.sep}'):
            return rf"{home}{os.sep}PythonMover{os.sep}TXT{os.sep}"
        else:
            return os.makedirs(f'{home}{os.sep}PythonMover{os.sep}TXT{os.sep}')
    def zipPath(self):
        home = ReadPath().get_main_path_user()
        if os.path.exists(f'{home}{os.sep}PythonMover{os.sep}ZIP{os.sep}'):
            return rf"{home}{os.sep}PythonMover{os.sep}ZIP{os.sep}"
        else:
            return os.makedirs(f'{home}{os.sep}PythonMover{os.sep}ZIP{os.sep}')

    def ScreenShootPath(self):
        home = ReadPath().get_main_path_user()
        if os.path.exists(f'{home}{os.sep}PythonMover{os.sep}Screenshoot{os.sep}'):
            return rf"{home}{os.sep}PythonMover{os.sep}Screenshoot{os.sep}"
        else:
            return os.makedirs(f'{home}{os.sep}PythonMover{os.sep}Screenshoot{os.sep}')

    def ScreenShootPathWorkFlow(self):
        home = ReadPath().get_main_path_user()
        print(home)
        if os.path.exists(f'{home}{os.sep}OneDrive{os.sep}Área de Trabalho{os.sep}Screenshoot{os.sep}'):
            print("exists")
            print(f"{home}{os.sep}OneDrive{os.sep}Área de Trabalho{os.sep}Screenshoot{os.sep}")
            return rf"{home}{os.sep}OneDrive{os.sep}Área de Trabalho{os.sep}Screenshoot{os.sep}"
        else:
            print("not exists")
            return os.makedirs(f'{home}{os.sep}OneDrive{os.sep}Área de Trabalho{os.sep}Screenshoot{os.sep}')