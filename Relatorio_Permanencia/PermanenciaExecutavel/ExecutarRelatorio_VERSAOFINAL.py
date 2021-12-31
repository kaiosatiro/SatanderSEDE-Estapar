import os


def carrega_arquivo(arq, temp):
    temp.writelines(f'Cartão;Data;Evento;Placa;Usuário;Descrição;Grupo\n')
    lista = arq.readlines()
    radar = True if 'RADAR'in lista[1] else False
    sede = True if 'SEDE' in lista[0] else False
    gd = True if not (radar or sede) else False
    for linha in  lista:
        linha = linha.split(';')
        try:
            if radar or gd:
                if 'Mensalista' in linha[5]:
                    temp.writelines(f'{linha[2]};{linha[3]};{linha[5]};{linha[8]};{linha[9]};{linha[12]};{linha[14]}')
                else:                    
                    if '-' in linha[9]:
                        placa = linha[9].rstrip()
                    if 'Mensalista' in linha[6]:
                        if linha[1] == '' and linha[3] == '':                            
                            matricula = linha[2]
                        else:                                                         
                            if linha[1] == '' and linha[3] != '':
                                matricula = linha[3]
                            elif linha[3] == '' and linha[1] != '':
                                matricula = linha[1]
                        temp.writelines(f'{matricula};{linha[4]};{linha[6]};{placa};{linha[10]};{linha[12]};{linha[15]}')
                        placa = ''
            elif sede:
                if 'Mensalista' in linha[5]:
                    temp.writelines(f'{linha[2]};{linha[3]};{linha[5]};{linha[8]};{linha[9]};{linha[12]};{linha[14]}')     
                else:                        
                    if '-' in linha[9]:
                        placa = linha[9].rstrip()
                    if 'Mensalista' in linha[6]:
                        matricula = linha[2] if linha[2] != '' else linha[1]
                        temp.writelines(f'{matricula};{linha[4]};{linha[6]};{placa};{linha[10]};{linha[12]};{linha[15]}')
                        placa = ''
        except IndexError:
            continue


while True:
    try:
        opcao = input('''
              Relatorio PERMANENCIA Credenciados
              
              ***ATENÇÃO
              O Relatorio Extraido do Manager deve ser salvo na MESMA pasta deste Executavel
              com o nome 'relatorio.csv'
              Pressione <ENTER> para continuar ou <S> para sair
              ''').upper()
        if opcao == 'S':
            break
        else:
            try:
                with open('relatorio.csv', 'r') as arquivo_fonte:
                    with open('PERMANENCIA.csv', 'w') as arq_final:
                        print('''
                              Aguarde...
                              ''')
                        carrega_arquivo(arquivo_fonte, arq_final)
                        arq_final.close()
                        arquivo_fonte.close()
                        input('''
                              Concluido ! <ENTER>
                              ''')
                        # os.remove('relatorio.csv')
            except FileNotFoundError:
                    input('''
                          AQUIVO NÃO ENCONTRADO -  Siga as intruções ACIMA
                          ''')
                    os.system('cls')
                    continue
            else:
                break
    except:
        os.system('cls')
        break
  
