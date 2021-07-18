import Paths
import DocxFile
import PdfFile
import TxtFile
import WelcomeMessage
import ZipEncode
def run():
    path = Paths.ReadPath()
    docx = DocxFile.DocxFile()
    pdf = PdfFile.PdfFile()
    txt = TxtFile.TxtFile()
    zip = ZipEncode.Zip()
    option = int(input('''
    Digite 1 para executar transferências de arquivos para downloads,
    ou 2 para executar tranferência de arquivo em documentos: '''
                ))
    optionMove = int(input(''' Digite :
        1 para PDF
        2 para DOCX
        3 para TXT
        4 para ZIP: '''))
    if optionMove == 1 and option == 1: pdf.executeTransfer(path.dowload())
    elif optionMove == 2 and option == 1:docx.executeTransfer(path.dowload())
    elif optionMove == 3 and option == 1:txt.executeTransfer(path.dowload())
    elif optionMove == 4 and option == 1:
        print("entrou aqui")
        zip.executeTransfer(path.dowload())
    if optionMove == 1 and option == 2:pdf.executeTransfer(path.documents())
    elif optionMove == 2 and option == 2:docx.executeTransfer(path.documents())
    elif optionMove == 3 and option == 2:txt.executeTransfer(path.documents())
    else: print("Invalid Option")

if __name__ == '__main__':
    WelcomeMessage.welcomeMessage()
    run()