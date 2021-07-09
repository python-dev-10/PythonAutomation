import os
import QuantumTransfer
import Paths

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
            transfer.executeTransfer(path.dowload(), path.docxPath(), path.pdfPath(), path.txtPath())
        elif option == 'documents':
            transfer.executeTransfer(path.documents(), path.docxPath(), path.pdfPath(), path.txtPath())
        else:
            print("Opção Inválida")
            break
        input_user = input(str("Deseja sair? (S/N)")).upper()