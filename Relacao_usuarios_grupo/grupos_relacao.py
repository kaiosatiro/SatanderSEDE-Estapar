with open('relacao.csv', 'r') as arq:
    with open('relacao_NOVA.csv', 'a') as rltr:
            for linha in arq.readlines():
                linha = linha.split(';')
                if '(C)' in linha[1]:
                    try:
                        rltr.write(linha[1][:-3] +';'+ linha[3] +';'+ linha[5]
                                   +';'+ linha[10] +';'+ linha[12] +'\n')
                    except IndexError:
                        continue