import Paths
from transferPaths import DocxFile, PdfFile, ZipEncode, TxtFile
import WelcomeMessage
from customMessages import CustomMessage
import os


def run():
    path = Paths.ReadPath()
    docx = DocxFile.DocxFile()
    pdf = PdfFile.PdfFile()
    txt = TxtFile.TxtFile()
    zip = ZipEncode.Zip()
    home = path.getMainPathUser()
    message = CustomMessage.CustomMessage()
    option = int(input('''
    Digite 1 para executar transferências de arquivos para downloads,
    ou 2 para executar tranferência de arquivo em documentos: '''
                       ))
    optionMove = int(input(''' Digite :
        1 para PDF
        2 para DOCX
        3 para TXT
        4 para ZIP: '''))
    if os.path.exists(f'{home}{os.sep}PythonMover{os.sep}'):
        if optionMove == 1 and option == 1:
            pdf.executeTransfer(path.dowload(home))
        elif optionMove == 2 and option == 1:
            docx.executeTransfer(path.dowload(home))
        elif optionMove == 3 and option == 1:
            txt.executeTransfer(path.dowload(home))
        elif optionMove == 4 and option == 1:
            zip.executeTransfer(path.dowload(home))
        elif optionMove == 1 and option == 2:
            pdf.executeTransfer(path.documents(home))
        elif optionMove == 2 and option == 2:
            docx.executeTransfer(path.documents(home))
        elif optionMove == 3 and option == 2:
            txt.executeTransfer(path.documents(home))
        elif optionMove == 4 and option == 2:
            zip.executeTransfer(path.documents(home))
        else:
            message.errorMessage('Invalid Option')
    else:
        os.makedirs(f'{home}{os.sep}PythonMover{os.sep}')
        if os.path.exists(f'{home}{os.sep}PythonMover{os.sep}'): return message.successMessage('Directory Created, start the application again')


if __name__ == '__main__':
    WelcomeMessage.welcomeMessage()
    run()
    WelcomeMessage.goodByeMessage()