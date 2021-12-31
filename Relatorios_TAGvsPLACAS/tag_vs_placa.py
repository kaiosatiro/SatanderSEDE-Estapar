import os


def total_placas():
    try:
        with open('relatorio.csv', 'r') as arq:
            try:                
                for linha in arq.readlines()[-2:-1]:
                    linha = linha.split(';')
                    input(f'''
                    
                    Total LPR.... {linha[3]}
                    
                    Pressione <ENTER> para VOLTAR
                    
                    ''')
            except IndexError:
                input('Erro de indexação.')
            except:
                input('Erro Desconhecido!')
    except FileNotFoundError:
        input('\n Aquivo não encontrado !! (Siga as instruções do menu principal)')
    except:
        input('Erro Desconhecido')
    finally:
        return os.system('cls' if os.name == 'nt' else 'clear')


def total_cartao():
    try:
        with open('relatorio.csv', 'r') as arq:
            com_placa = 0
            sem_placa = 0
            for linha in arq.readlines()[7:]:
                linha = linha.split(';')
                try:
                    if linha[1] == 'TOTAL':
                        input(f'''
                            
                    Total Com Placa..... {com_placa}
                    Total Sem Placa..... {sem_placa}
                    
                    Pressione <ENTER> para VOLTAR
                        ''')
                        break
                    elif not ('OPERACAO' in linha[14] or 'MOTO' in linha[14]) and (linha[2] != ''):
                        if linha[8] == '':
                            sem_placa += 1
                        elif linha[8] != '':
                            com_placa += 1
                except LookupError:
                    print('.')
                    continue
                except IndexError:
                    input('\n Erro de indexação.') 
                except:
                    input('\n Erro Desconhecido!')
    except FileNotFoundError:
        input('\n Aquivo não encontrado !! (Siga as instruções do menu principal)')
    except:
        input('Erro Desconhecido')
    finally:
        return os.system('cls' if os.name == 'nt' else 'clear')
              

while True:
    try:
        opcao = input('''
            INDICE DE TAG VS PLACA
            *** O ARQUIVO DO RELATORIO DEVE ESTAR SALVO NA MESMA PASTA QUE ESSE EXECUTAVEL
            EM FORMATO '.csv' COM O NOME DE 'relatorio.csv'
            
            Pressione
            <1> Para Obter o total de acessos via LPR (PLACA)
            
            <2> Para Obter o total de acessos via crachá (TAG)
                *Separado por COM ou SEM placa
                
                
            <S> Para SAIR
            
            >>>>>>> ''').upper()
        if opcao == '1':
            total_placas()
        elif opcao == '2':
            total_cartao()
        elif opcao == 'S':
            print('BYE !!!!!!!!!!!!!!!!!')
            break
        os.system('cls' if os.name == 'nt' else 'clear')       
    except:
        continue