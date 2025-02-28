from colorama import init, Fore, Back, Style
init()
from workalendar.america import Brazil
from datetime import date
import calendar

#calculo do plano de saude
def calcdeplano(valor, idadep):
    valor_emercor = 18.73
    if idadep <= 18:
        valor_circ = 151.92
        valor_unim = 274.49
    elif idadep <= 23:
        valor_circ = 167.12
        valor_unim = 288.23
    elif idadep <= 28:
        valor_circ = 189.89
        valor_unim = 315.65
    elif idadep <= 33:
        valor_circ = 212.71
        valor_unim = 356.84
    elif idadep <= 38:
        valor_circ = 250.68
        valor_unim = 411.75
    elif idadep <= 43:
        valor_circ = 319.06
        valor_unim = 521.56
    elif idadep <= 48:
        valor_circ = 407.38
        valor_unim = 686.24
    elif idadep <= 53:
        valor_circ = 486.13
        valor_unim = 905.85
    elif idadep <= 58:
        valor_circ = 654.70
        valor_unim = 1194.09
    else:
        valor_circ = 730.08
        valor_unim = 1647.03

    compra_plano = input("\nQual o plano desejado?\n\n1. Plano Círculo \n2. Unimed\n3. Emercor\n0. Voltar\n\nOpção: ")

    if compra_plano == "1":
        if valor >= valor_circ:
            print(f"Adquirido o plano Círculo pelo valor de R${valor_circ:.2f}")
            valor -= valor_circ
        else:
            print("Saldo insuficiente para compra do plano.\n\nConfira os valores dos planos.")
    elif compra_plano == "2":
        if valor >= valor_unim:
            print(f"Adquirido o plano Unimed pelo valor de R${valor_unim:.2f}")
            valor -= valor_unim
        else:
            print("Saldo insuficiente para compra do plano.\n\nConfira os valores dos planos.")
    elif compra_plano == "3":
        if valor >= valor_emercor:
            print(f"Adquirido o plano Emercor pelo valor de R${valor_emercor:.2f}")
            valor -= valor_emercor
        else:
            print("Saldo insuficiente para compra do plano.\n\nConfira os valores dos planos.")        
    elif compra_plano == "0":
        print("Operação cancelada.")
    else:
        print("Opção inválida. Tente novamente.")
    return valor

#calculo do vale transporte
def calcular_vale_transporte(ano, mes, estado="RS"):
    calendario = Brazil(subdiv=estado)
    ultimo_dia = calendar.monthrange(ano, mes)[1]
    dias_uteis = sum(1 for dia in range(1, ultimo_dia + 1) 
                if (data := date(ano, mes, dia)) and calendario.is_working_day(data))    
    return dias_uteis

valor = float
#c e s são variaveis quaisquer só para usar os loops    
c=1 
s=1

#primeiro loop para pegar as informações do cliente
while s!=0: 
    print(Fore.CYAN+"---------------------\nESCOLHA DE BENEFICIOS:\n---------------------\n"+Fore.RESET)
    nome = str(input("Digite o seu nome completo: "))
    area = int(input("-------\nDigite a area: \n1.Contabil\n2.Fiscal\n3.DP\n4.ADM\n------\nOpção: "))

    if area<1 or area>4:
        print("Numero invalido")
        break
    cargo = int(input("-------\nVocê é: \n1.Auxiliar/Assistente\n2.Analista\n-------\nOpção: "))
    if cargo<1 or cargo>2:
        print("Numero invalido")
        break  
    if cargo==1:
        valor=605
    else:
        valor= 675

    nascimento = input("-------\nDigite sua data de nascimento: ")

#segundo loop para executar o menu
    while c != 0:
        print("\n-------\nEscolha de beneficios:" )
        print(Fore.LIGHTRED_EX+f"Seu Saldo atual é: R${valor:.2f}"+Fore.RESET)    
        menu = input("-------\nDigite a Opção: \n1.Escolher Vales trasporte\n2.Escolher planos de saúde\n3.Consultar valores dos planos\n4.Salvar\n------\nOpção: ")
        if menu == "1":
            passagemdia = int(input("Quantas passagens por dia você precisa? "))
            ano = 2025
            mes = 2  
            valor_passagem = 6.80
            estado = "RS"  
            dias = calcular_vale_transporte(ano, mes, valor_passagem, estado) 
            gasto_total = dias * passagemdia * valor_passagem  
            if valor<gasto_total:
                print(f"Saldo insuficiente para realizar escolha.\n \nSaldo disponivel: R${valor:.2f}\nPreço total: R${gasto_total:.2f}\n")

            else:
                print(f"Gasto total com vale transporte: R${gasto_total:.2f}")
                valor -= gasto_total
        elif menu == "2":
            
            plano = input("\nO plano é para você ou para algum familiar?\n1.Plano pessoal \n2.Plano para dependentes\n0.Voltar\n \nOpção: ")

            if plano == "1":
                idadep = int(input("\nDigite a sua idade: "))
                valor = calcdeplano(valor, idadep)  

            elif plano == "2":
                dependentes = input("Quantos dependentes necessitam de plano? (No máximo 3): ")
#pegar os dados para saida dos dependentes + valor do plano   / idtemp = idade temporaria para fazer o calculo(tem que ser int)
                if dependentes == "1":
                    d1nome = input("Qual o nome do dependente? ")
                    d1CPF = input("Qual o CPF do dependente? ")
                    d1nasc = input("Qual a data de nascimento do dependente? ")
                    idtemp = int(input("Qual a idade dele? "))
                    valor = calcdeplano(valor, idtemp)  

                elif dependentes == "2":
                    d1nome = input("Qual o nome do dependente 1? ")
                    d1nCPF = input("Qual o CPF do dependente 1? ")
                    d1nasc = input("Qual a data de nascimento do dependente 1? ")
                    idtemp = int(input("Qual a idade do dependente 1? "))
                    valor = calcdeplano(valor, idtemp)  
        
                    d2nome = input("Qual o nome do dependente 2? ")
                    d2CPF = input("Qual o CPF do dependente 2? ")
                    d2nasc = input("Qual a data de nascimento do dependente 2? ")
                    idtemp = int(input("Qual a idade do dependente 2? "))
                    valor = calcdeplano(valor, idtemp)  
        
                elif dependentes == "3":
                    d1nome = input("Qual o nome do dependente 1? ")
                    d1nCPF = input("Qual o CPF do dependente 1? ")
                    d1nasc = input("Qual a data de nascimento do dependente 1? ")
                    idtemp = int(input("Qual a idade do dependente 1? "))
                    valor = calcdeplano(valor, idtemp) 
        
                    d2nome = input("Qual o nome do dependente 2? ")
                    d2nCPF = input("Qual o CPF do dependente 2? ")
                    d2nasc = input("Qual a data de nascimento do dependente 2? ")
                    idtemp = int(input("Qual a idade do dependente 2? "))
                    valor = calcdeplano(valor, idtemp)  

                    d3nome = input("Qual o nome do dependente 3? ")
                    d3nCPF = input("Qual o CPF do dependente 3? ")
                    d3nasc = input("Qual a data de nascimento do dependente 3? ")
                    idtemp = int(input("Qual a idade do dependente 3? "))
                    valor = calcdeplano(valor, idtemp) 

                else:
                    print("Opção inválida ou operação cancelada.")
#mostrar tabela de preços
        elif menu == "3":
            print(Fore.RED+"Consulta dos valores: "+Fore.RESET)
            print("              Plano Circulo")
            print("Idade inicial - Idade final - Preço")
            print(Fore.YELLOW+"     0               18       R$151,92"+ Fore.RESET)
            print(Fore.YELLOW+"     19              23       R$167,12"+ Fore.RESET)
            print(Fore.YELLOW+"     24              28       R$189,89"+ Fore.RESET)
            print(Fore.YELLOW+"     29              33       R$212,71"+ Fore.RESET)
            print(Fore.YELLOW+"     34              38       R$250,68"+ Fore.RESET)
            print(Fore.YELLOW+"     39              43       R$319,06"+ Fore.RESET)
            print(Fore.YELLOW+"     44              48       R$407,38"+ Fore.RESET)
            print(Fore.YELLOW+"     49              53       R$486,13"+ Fore.RESET)
            print(Fore.YELLOW+"     54              58       R$654,70"+ Fore.RESET)
            print(Fore.YELLOW+"     59              60+      R$730,08"+ Fore.RESET)
            print("              Plano Unimed")
            print("Idade inicial - Idade final - Preço")
            print(Fore.YELLOW+"     0               18       R$274,49"+ Fore.RESET)
            print(Fore.YELLOW+"     19              23       R$288,23"+ Fore.RESET)
            print(Fore.YELLOW+"     24              28       R$315,65"+ Fore.RESET)
            print(Fore.YELLOW+"     29              33       R$356,84"+ Fore.RESET)
            print(Fore.YELLOW+"     34              38       R$411,75"+ Fore.RESET)
            print(Fore.YELLOW+"     39              43       R$521,56"+ Fore.RESET)
            print(Fore.YELLOW+"     44              48       R$686,24"+ Fore.RESET)
            print(Fore.YELLOW+"     49              53       R$905,85"+ Fore.RESET)
            print(Fore.YELLOW+"     54              58       R$1.194,09"+ Fore.RESET)
            print(Fore.YELLOW+"     59              60+      R$1.1647,03"+ Fore.RESET)   
            print("              Plano Emercor")
            print("        Valor fixo independente da idade:")
            print(Fore.YELLOW+"                   18.73"+ Fore.RESET)
