import os
import datetime


def carrega_arquivo(arq, temp):
    for linha in arq.readlines():
        linha = linha.split(';')
        try:
            if 'Mensalista' in linha[5]:
                temp.writelines(f'{linha[2]};{linha[3]};{linha[5]};{linha[8]};{linha[9]};{linha[12]};{linha[14]}')
        except IndexError:
                continue


def carrega_arquivo2(arq, temp):
    for linha in arq.readlines():
        linha = linha.split(';')
        try:
            if 'Mensalista' in linha[6]:
                temp.writelines(f'{linha[2]};{linha[4]};{linha[6]};{linha[9]};{linha[10]};{linha[12]};{linha[15]}')
        except IndexError:
                continue


def join(origem, final):
    for linha in origem:
        final.writelines(linha)
    pass


with open('temp.csv', 'a') as arq_final:
    with open('relatorioprincipal.csv', 'r') as arquivo_fonte:
        carrega_arquivo(arquivo_fonte, arq_final)
        arq_final.close()
        carregar_temp = open('tempprinc.csv')
        relatorio_principal = carregar_temp.readlines()
        carregar_temp.close()
        os.remove('tempprinc.csv')

with open('temp.csv', 'a') as arq_final2:
    with open('relatoriooliveiras.csv', 'r') as arquivo_fonte:
        carrega_arquivo2(arquivo_fonte, arq_final2)
        arq_final2.close()
        carregar_temp2 = open('tempoliv.csv')
        relatorio_oliveiras = carregar_temp2.readlines()
        carregar_temp2.close()
        os.remove('tempoliv.csv')

with open('relacaoFinal.csv', 'w') as relacao:
    with open('temp.csv', 'r') as temp:
        join(temp, relacao)
        relacao.close()
        temp.close()
        os.remove('temp.csv')


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
