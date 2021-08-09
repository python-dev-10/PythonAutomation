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
    Tk().withdraw()
    showinfo("FileTransfer", "Em sequência abrirá uma tela onde poderá escolher o diretório que deseja verificar os arquivos")
    directory = askdirectory()
    try:
        optionMove = int(input(''' Digite :
            1 para PDF
            2 para DOCX
            3 para TXT
            4 para ZIP: '''))
        if os.path.exists(f'{home}{os.sep}PythonMover{os.sep}'):
            if optionMove == 1:
                pdf.executeTransfer(directory)
            elif optionMove == 2:
                docx.executeTransfer(directory)
            elif optionMove == 3:
                txt.executeTransfer(directory)
            elif optionMove == 4:
                zip.executeTransfer(directory)
            else:
                message.errorMessage('Invalid Option')
        else:
            os.makedirs(f'{home}{os.sep}PythonMover{os.sep}')
            if os.path.exists(f'{home}{os.sep}PythonMover{os.sep}'): return message.successMessage('Directory Created, start the application again')
    except ValueError:
        print(message.errorMessage("ERRO, verifique o tipo de entrada, este campo apenas aceita números!"))
