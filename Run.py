import Paths
from transferPaths import DocxFile, PdfFile, ZipEncode, TxtFile
from customMessages import CustomMessage
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
import os

def run():
    path = Paths.ReadPath()
    docx = DocxFile.DocxFile()
    pdf = PdfFile.PdfFile()
    txt = TxtFile.TxtFile()
    zip = ZipEncode.Zip()
    home = path.getMainPathUser()
    message = CustomMessage.CustomMessage()
    # option = int(input('''
    # Digite 1 para executar transferências de arquivos para downloads,
    # ou 2 para executar tranferência de arquivo em documentos: '''
    #                    ))
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    showinfo("FileTransfer", "Em sequência abrirá uma tela onde poderá escolher o diretório que deseja verificar os arquivos")
    directory = askdirectory()
    print(directory)
    optionMove = int(input(''' Digite :
        1 para PDF
        2 para DOCX
        3 para TXT
        4 para ZIP: '''))
    if os.path.exists(f'{home}{os.sep}PythonMover{os.sep}'):
        if optionMove == 1 :
            pdf.executeTransfer(directory)
        elif optionMove == 2 :
            docx.executeTransfer(directory)
        elif optionMove == 3 :
            txt.executeTransfer(directory)
        elif optionMove == 4 :
            zip.executeTransfer(directory)
        else:
            message.errorMessage('Invalid Option')
    else:
        if directory == "":
            raise Exception("Diretório não foi Selecionado. Verifique!")
        os.makedirs(f'{home}{os.sep}PythonMover{os.sep}')
        if os.path.exists(f'{home}{os.sep}PythonMover{os.sep}'): return message.successMessage('Directory Created, start the application again')
