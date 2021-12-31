# Criando a base do bibicletario a partir do registro de acesso em 2021:

# with open('Relatórios - Diários 2021.csv', 'r') as arq:
#     dc = {}
#     for linha in arq:
#         linha = linha.split(';')
#         dc[linha[0]] = [linha[1], linha[2]]

# with open('Base_Bicicletario.csv', 'a') as arq:
#     for chave, valor in  dc.items():
#         arq.write(chave + ';' + valor[0] + ';' + valor[1] + '\n')


# Programa principal

import os


# Função de exibição
def exibir(lista, opcao):
    try:   
        contador = 0
        for linha in lista.readlines():
            linha = linha.split(';')
            if opcao == 1:
                print(f'''                      {linha[0]:.<40}|{linha[1]:^15}|{linha[2]:^10}''')
            elif opcao == 2:
                print(f'''              {linha[0]:.<40}|{linha[1]:^15}|{linha[2]:^10}|{linha[3]:^13s}''')            
            contador += 1                
        print(f'\n TOTAL De Registros: {contador}')
        input('''
                Pressione <Enter> para continuar
                ''')
        os.system('cls')
    except:
        input('''
            Erro Desconhecido !
            
            <Enter> para continuar
              ''')
    finally:
        return


# Funções de pesquisa e escrita
def pesquisar(valor, opcao):
     with open('Base_Bicicletario.csv', 'r') as arq:        
        for linha in arq.readlines():
            linha = linha.split(';')
            if valor in linha[opcao]:
                return linha
        return False


def escrever(valor):
    with open('lista_bicicletario.csv', 'a') as arq:
        arq.writelines(valor[0] + ';' + valor[1] + ';' + valor[2][:-1] + ';' + data + '\n')
        #arq.write(f'{valor[0]};{valor[1]};{valor[2:-1]};{data};\n')
        print('''
                          Adicionado !!
                          ''')


def adicionar_novo():
    nome = input('''
                 NOME: ''').upper()
    matricula = input('''
                 MATRICULA: ''').upper()
    prisma = input('''
                 PRISMA: ''').upper()
    with open('Base_Bicicletario.csv', 'a') as arq:
        arq.writelines(f'{nome};{matricula};{prisma}\n')
    with open('lista_bicicletario.csv', 'a') as arq:
        arq.writelines(f'{nome};{matricula};{prisma};{data}\n')
    input('''
          Adicionado na Base e na lista''')
    

#Funções das opções
def pesquisa_prisma():
    while True:
        try:
            prisma = input('''
        <S para sair>            PRISMA: ''').upper()
            os.system('cls')
            if prisma == 'S':
                break
            valor = pesquisar(prisma, 2)
            if valor != False:
                print(f'''
                      
                      
                      
                    {'NOME':.<40}|{'MATRÍCULA':^15}|{'PRISMA':^10}''')
                print(f'''
                    {valor[0]:.<40}|{valor[1]:^15}|{valor[2]:^10}''')
                opcao = input('''
                            Adicionar(S/N): ''').upper()
                if opcao == 'S':
                    escrever(valor)
                continue
            else:
                opcao = input('''
                    Não encontrado
                    Adicionar NOVO (S/N): ''').upper()
                if opcao == 'S':
                    adicionar_novo()        
        except:
            input('Erro')
            break


def pesquisa_matricula():
    while True:
        try:
            matricula = input('''
        <S para sair>            MATRICULA: ''').upper()
            os.system('cls')
            if matricula == 'S':
                break
            valor = pesquisar(matricula, 1)
            if valor != False:
                print(f'''
                    
                    
                    
                    {'NOME':.<40}|{'MATRÍCULA':^15}|{'PRISMA':^10}''')
                print(f'''
                    {valor[0]:.<40}|{valor[1]:^15}|{valor[2]:^10}''')
                opcao = input('''
                            Adicionar(S/N): ''').upper()
                if opcao == 'S':
                    escrever(valor)
                continue
            else:
                opcao = input('''
                    Não encontrado
                    Adicionar NOVO (S/N): ''').upper()
                if opcao == 'S':
                    adicionar_novo()
        except:
            input('Erro')


def pesquisa_nome():
    while True:
        try:
            nome = input('''
        <S para sair>            NOME: ''').upper()
            os.system('cls')
            if nome == 'S':
                break
            valor = pesquisar(nome, 0)
            if valor != False:
                print(f'''
                    
                    
                    
                    {'NOME':.<40}|{'MATRÍCULA':^15}|{'PRISMA':^10}''')
                print(f'''
                    {valor[0]:.<40}|{valor[1]:^15}|{valor[2]:^10}''')
                opcao = input('''
                            Adicionar(S/N): ''').upper()
                if opcao == 'S':
                    escrever(valor)
                continue
            else:
                opcao = input('''
                    Não encontrado
                    Adicionar NOVO (S/N): ''').upper()
                if opcao == 'S':
                    adicionar_novo()
            
        except:
            input('Erro')


#Main do programa e Menus
data = input('''
                     
                DATA: ''').upper()
os.system('cls')
while True:
    try:
        opcao = input('''
            RELATORIO BICICLETARIO
            *** O ARQUIVO 'Base_Bicicletario.csv' DEVE ESTAR SALVO
            NA MESMA PASTA QUE ESSE EXECUTAVEL
            
            Pressione
            <1> Para Exibir
            
            <2> Para Criar uma lista de acessos
                
                
            <S> Para SAIR
            
            >>>>>>> ''').upper()
        os.system('cls')
        if opcao == '1':
            while True:
                try:                    
                    opcao = input('''
            Pressione
            <1> Exibir Base
            <2> Exibir Lista
                                    
            <S> Para VOLTAR
            
            >>>>>>> ''').upper()
                    if opcao == '1':
                        with open('Base_Bicicletario.csv', 'r') as arq:
                            exibir(arq, 1)
                    elif opcao == '2':
                        with open('lista_bicicletario.csv', 'r') as arq:
                            exibir(arq, 2)
                    elif opcao == 'S':
                        break
                    os.system('cls')
                except FileNotFoundError:
                    input('''
                Arquivo não encontrado.
                
                <Enter> para continuar
              ''')
                    os.system('cls')
                except:
                    continue
        elif opcao == '2':
            while True:
                try:
                    opcao = input('''
            Pressione
            <1> Por Nome
            <2> Por Matrícula
            <3> Por Prisma
                
            <S> Para VOLTAR
            
            >>>>>>> ''').upper()
                    if opcao == '1':
                        os.system('cls')
                        pesquisa_nome()
                    elif opcao == '2':
                        os.system('cls')
                        pesquisa_matricula()
                    elif opcao == '3':
                        os.system('cls')
                        pesquisa_prisma()
                    elif opcao == 'S':
                        break
                    os.system('cls')
                except:
                    continue
        elif opcao == 'S':
            print('BYE !!!!!!!!!!!!!!!!!')
            break
        os.system('cls')       
    except:
        continue
