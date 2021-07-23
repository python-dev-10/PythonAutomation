import os
class ReadPath():
    def getMainPathUser(self):
        home = os.path.expanduser('~')
        return home
    def documents(self,home_path):
        return rf"{home_path}{os.sep}Documentos{os.sep}"

    def dowload(self,home_path):
        return rf"{home_path}{os.sep}Downloads{os.sep}"

    def docxPath(self,home_path):
        if os.path.exists(f'{home_path}{os.sep}PythonMover{os.sep}DOCX{os.sep}'):
            return rf"{home_path}{os.sep}PythonMover{os.sep}DOCX{os.sep}"
        else:
            return os.makedirs(f'{home_path}{os.sep}PythonMover{os.sep}DOCX{os.sep}')
    def pdfPath(self,home_path):
        if os.path.exists(f'{home_path}{os.sep}PythonMover{os.sep}PDF{os.sep}'):
            return rf"{home_path}{os.sep}PythonMover{os.sep}PDF{os.sep}"
        else:
            return os.makedirs(f'{home_path}{os.sep}PythonMover{os.sep}PDF{os.sep}')
    def txtPath(self,home_path):
        if os.path.exists(f'{home_path}{os.sep}PythonMover{os.sep}TXT{os.sep}'):
            return rf"{home_path}{os.sep}PythonMover{os.sep}TXT{os.sep}"
        else:
            return os.makedirs(f'{home_path}{os.sep}PythonMover{os.sep}TXT{os.sep}')
    def zipPath(self,home_path):
        if os.path.exists(f'{home_path}{os.sep}PythonMover{os.sep}ZIP{os.sep}'):
            return rf"{home_path}{os.sep}PythonMover{os.sep}ZIP{os.sep}"
        else:
            return os.makedirs(f'{home_path}{os.sep}PythonMover{os.sep}ZIP{os.sep}')