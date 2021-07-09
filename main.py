import os
import QuantumTransfer
import Paths
import DocxFile
import PdfFile
import TxtFile

if __name__ == '__main__':
    path = Paths.ReadPath()
    transfer = QuantumTransfer.fileTransfer()
    input_user =""
    while input_user != 'S':
        option = input(str('''
        Digite 'Dowload' para executar transferências de arquivos neste local,
                            ou 'Documents' para executar tranferência de arquivo em documentos: '''
                        )).lower()
        if option == 'dowload':
            while input_user != 'S':
                optionMove = int(input(''' Digite 
                1 para PDF
                2 para DOCX
                3 para TXT: '''))
                if optionMove == 1:
                    PdfFile.PdfFile.executeTransfer(path.dowload())
                elif optionMove == 2:
                    DocxFile.DocxFile.executeTransfer(path.dowload())
                elif optionMove == 3:
                    TxtFile.TxtFile.executeTransfer(path.dowload())
                else:
                    print("Invalid Option")
                break
        elif option == 'documents':
            while input_user != 'S':
                optionMove = int(input(''' Digite 
                1 para PDF
                2 para DOCX
                3 para TXT: '''))
                print(optionMove == 1)
                if optionMove == 1:
                    PdfFile.PdfFile.executeTransfer(path.documents())
                elif optionMove == 2:
                    DocxFile.DocxFile.executeTransfer(path.documents())
                elif optionMove == 3:
                    TxtFile.TxtFile.executeTransfer(path.documents())
                else:
                    print("Invalid Option")
                break
        else:
            print("Opção Inválida")
            break
        input_user = input(str("Deseja sair? (S/N)")).upper()