from Operations import TxtFile, Paths, WelcomeMessage, DocxFile, PdfFile

def run():
    path = Paths.ReadPath()
    docx = DocxFile.DocxFile()
    pdf = PdfFile.PdfFile()
    txt = TxtFile.TxtFile()
    option = input(str('''
    Digite 'Dowload' para executar transferências de arquivos neste local,
    ou 'Documents' para executar tranferência de arquivo em documentos: '''
                )).lower()
    optionMove = int(input(''' Digite :
        1 para PDF
        2 para DOCX
        3 para TXT: '''))
    if optionMove == 1 and option == 'dowload': pdf.executeTransfer(path.dowload())
    elif optionMove == 2 and option == 'dowload':docx.executeTransfer(path.dowload())
    elif optionMove == 3 and option == 'dowload':txt.executeTransfer(path.dowload())
    if optionMove == 1 and option == 'documents':pdf.executeTransfer(path.documents())
    elif optionMove == 2 and option == 'documents':docx.executeTransfer(path.documents())
    elif optionMove == 3 and option == 'documents':txt.executeTransfer(path.documents())
    else: print("Invalid Option")

if __name__ == '__main__':
    WelcomeMessage.welcomeMessage()
    run()