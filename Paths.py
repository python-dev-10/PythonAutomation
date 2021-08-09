import os
class ReadPath():
    def getMainPathUser(self):
        home = os.path.expanduser('~')
        return home
    def documents(self):
        return rf"{ReadPath.getMainPathUser()}{os.sep}Documentos{os.sep}"

    def dowload(self,home_path):
        return rf"{home_path}{os.sep}Downloads{os.sep}"

    def docxPath(self):
        home = ReadPath().getMainPathUser()
        if os.path.exists(f'{home}{os.sep}PythonMover{os.sep}DOCX{os.sep}'):
            return rf"{home}{os.sep}PythonMover{os.sep}DOCX{os.sep}"
        else:
            return os.makedirs(f'{home}{os.sep}PythonMover{os.sep}DOCX{os.sep}')
    def pdfPath(self):
        home = ReadPath().getMainPathUser()
        print(f'{home}{os.sep}PythonMover{os.sep}PDF{os.sep}')
        if os.path.exists(rf'{home}{os.sep}PythonMover{os.sep}PDF{os.sep}'):
            return rf"{home}{os.sep}PythonMover{os.sep}PDF{os.sep}"
        else:
            return os.makedirs(f'{home}{os.sep}PythonMover{os.sep}PDF{os.sep}')
    def txtPath(self):
        home = ReadPath().getMainPathUser()
        if os.path.exists(f'{home}{os.sep}PythonMover{os.sep}TXT{os.sep}'):
            return rf"{home}{os.sep}PythonMover{os.sep}TXT{os.sep}"
        else:
            return os.makedirs(f'{home}{os.sep}PythonMover{os.sep}TXT{os.sep}')
    def zipPath(self):
        home = ReadPath().getMainPathUser()
        if os.path.exists(f'{home}{os.sep}PythonMover{os.sep}ZIP{os.sep}'):
            return rf"{home}{os.sep}PythonMover{os.sep}ZIP{os.sep}"
        else:
            return os.makedirs(f'{home}{os.sep}PythonMover{os.sep}ZIP{os.sep}')