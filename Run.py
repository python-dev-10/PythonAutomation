import Paths
from transferPaths import DocxFile, PdfFile, ZipEncode, TxtFile
from customMessages import CustomMessage
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tabulate import tabulate
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
    showinfo("FileTransfer", "In sequence will open a screen, where you can choose the directory you want verify the files")
    directory = askdirectory()
    try:
        d=[["PDF", 1],["DOCX", 2],["TXT", 3],["ZIP", 4]]
        optionMove = int(input(f"Which Operation do you want? Type them value:\n {tabulate(d, headers=['Option', 'Value'])} \n"))

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
        print(message.errorMessage("ERROR, check the input type, this field just accept numbers!"))
