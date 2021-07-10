import Paths
import DocxFile
import PdfFile
import TxtFile

def run():
    path = Paths.ReadPath()
    docx = DocxFile.DocxFile()
    pdf = PdfFile.PdfFile()
    txt = TxtFile.TxtFile()
    option = input(str('''
    Digite 'Dowload' para executar transferências de arquivos neste local,
                        ou 'Documents' para executar tranferência de arquivo em documentos: '''
                )).lower()
    optionMove = int(input(''' Digite 
    1 para PDF
    2 para DOCX
    3 para TXT: '''))
    print(f"optionMove {optionMove}")
    print(f"option {option}")
    print(f"path.documents(): {path.documents()}")
    documents = path.documents()
    download = path.dowload()
    if optionMove == 1 and option == 'dowload':
        pdf.executeTransfer(download)
    elif optionMove == 2 and option == 'dowload':
        docx.executeTransfer(download)
    elif optionMove == 3 and option == 'dowload':
        txt.executeTransfer(download)
    if optionMove == 1 and option == 'documents':
        pdf.executeTransfer(documents)
    elif optionMove == 2 and option == 'documents':
        docx.executeTransfer(documents)
    elif optionMove == 3 and option == 'documents':
        txt.executeTransfer(documents)
    else: print("Invalid Option")

if __name__ == '__main__':
    run()