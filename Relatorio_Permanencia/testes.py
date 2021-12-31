import os
import time


# def carrega_arquivo2(arq):
#     lista = []
#     for linha in arq.readlines():
#         linha = linha.split(';')
#         try:
#             if 'Mensalista' in linha[5]:
#                 temp = (f'{linha[2]};{linha[3]};{linha[5]};{linha[8]};{linha[9]};{linha[12]};{linha[14]}')
#                 lista.append(temp)
#         except IndexError:
#                 continue
#     return lista


def carrega_arquivo(arq):
    lista = []
    for linha in arq.readlines():
        linha = linha.split(';')
        try:
            if 'Mensalista' in linha[5]:
                temp = (f'{linha[2]};{linha[3]};{linha[5]};{linha[8]};{linha[9]};{linha[12]};{linha[14]}')
                lista.append(temp)
            else:                
                if '-' in linha[9]:
                    placa = linha[9].rstrip()
                if 'Mensalista' in linha[6]:
                    matricula = linha[2] if linha[2] != '' else linha[1]
                    temp = (f'{matricula};{linha[4]};{linha[6]};{placa};{linha[10]};{linha[12]};{linha[15]}')
                    lista.append(temp)
        except IndexError:
                continue
            
    return lista


def join(rltrPrinc, rltrOliv, arq_final):
    i = 0
    for linhaP in rltrPrinc:
        try:
            dataPrinc = linhaP.split(';')[1]
            dataOliv = rltrOliv[i].split(';')[1]
            if time.strptime(dataOliv, "%d/%m/%y %H:%M:%S") < time.strptime(dataPrinc, "%d/%m/%y %H:%M:%S"):
                arq_final.writelines(f'{rltrOliv[i]}')
                i += 1
                while True:
                    dataOliv = rltrOliv[i].split(';')[1]
                    if time.strptime(dataOliv, "%d/%m/%y %H:%M:%S") < time.strptime(dataPrinc, "%d/%m/%y %H:%M:%S"):
                        arq_final.writelines(f'{rltrOliv[i]}')
                        i += 1
                    else:
                        arq_final.writelines(f'{linhaP}')
                        break
            else:
                arq_final.writelines(f'{linhaP}')
        except IndexError:
            arq_final.writelines(f'{linhaP}')
            continue

with open('relatorioprincipal.csv', 'r') as arquivo_fontePrinc:
    with open('relatoriooliveiras.csv', 'r') as arquivo_fonteOliv:
        relatorio_oliveiras = carrega_arquivo(arquivo_fonteOliv)
        relatorio_principal = carrega_arquivo(arquivo_fontePrinc)
        arquivo_fontePrinc.close()
        arquivo_fonteOliv.close()
        #os.remove('relatorioprincipal.csv')
        #os.remove('relatoriooliveiras.csv')

with open('relacaoFinalPermanencia.csv', 'w') as relacao:
        join(relatorio_principal, relatorio_oliveiras, relacao)
        relacao.close()

# ------------------------ ANTIGOS TESTES ----------------------------
# with open('temp.csv', 'w') as arq_final:
#     with open('relatorioprincipal.csv', 'r') as arquivo_fonte:
#         carrega_arquivo(arquivo_fonte, arq_final)
#         arq_final.close()
#         arquivo_fonte.close() 

# with open('temp.csv', 'a') as arq_final2:
#     with open('relatoriooliveiras.csv', 'r') as arquivo_fonte:
#         carrega_arquivo2(arquivo_fonte, arq_final2)
#         arq_final2.close()
#         arquivo_fonte.close()

# arq =  open('relacaoFinal.csv', 'r').readlines()

# linha = arq[0].split(';')
# linha2 = arq[1].split(';')

# first_date = linha[1]
# second_date = linha2[1]

# formatted_date1 = time.strptime(first_date, "%d/%m/%y %H:%M:%S")
# formatted_date2 = time.strptime(second_date, "%d/%m/%y %H:%M:%S")
# print(formatted_date1 < formatted_date2)

# linha_principal = relatorio_principal[1].split(';')
# print(linha_principal[:])

# linha_principal2 = relatorio_oliveiras[1].split(';')
# print(linha_principal2[:])

# print(relatorio_principal[0:3])
# print(relatorio_oliveiras[0:3])
