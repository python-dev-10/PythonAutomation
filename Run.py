import Paths
from transferPaths import DocxFile, PdfFile, ZipEncode, TxtFile
from transferPaths import ScreenShoot
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
    home = path.get_home_path()
    message = CustomMessage.CustomMessage()
    Tk().withdraw()
    showinfo("FileTransfer", "In sequence will open a screen, where you can choose the directory you want verify the files")
    directory = askdirectory()
    try:
        d=[["PDF", 1],["DOCX", 2],["TXT", 3],["ZIP", 4]]
        optionMove = int(input(f"Which Operation do you want? Type them value:\n {tabulate(d, headers=['Option', 'Value'])} \n"))
        try:
            if os.path.exists(f'{home}{os.sep}PythonMover{os.sep}'):
                if optionMove == 1:
                    pdf.execute_transfer_pdf(directory)
                elif optionMove == 2:
                    docx.execute_transfer_docx(directory)
                elif optionMove == 3:
                    txt.execute_transfer_txt(directory)
                elif optionMove == 4:
                    zip.execute_transfer_zip(directory)
                else:
                    message.error_message('Invalid Option')
            else:
                os.makedirs(f'{home}{os.sep}PythonMover{os.sep}')
                if os.path.exists(f'{home}{os.sep}PythonMover{os.sep}'): return message.success_message('Directory Created, start the application again')
        except Exception:
            print("Error in the Directory")
    except ValueError:
        print(message.error_message("ERROR, check the input type, this field just accept numbers!"))
