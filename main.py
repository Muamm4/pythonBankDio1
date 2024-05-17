import os

menu = """
######## Menu de Operações: ########

[1] Depositar
[2] Sacar
[3] Saldo/Extrato
[4] Sair

Escolha uma das opções acima:
==>"""

def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    console_clear()
    opcao = int(input(menu))
    match opcao:
        case 1:
            valor = float(input("Quanto deseja depositar? "))
            if valor > 0:
                saldo += valor
                extrato += f"Deposito: R$ {valor:.2f}\n"
                console_clear()
                print('################# DEPOSITO REALIZADO COM SUCESSO  #################\n\n')
                print(f'Deposito de R$ {valor:.2f} realizado com sucesso')
            else:
                console_clear()
                print("Operação inválida, tente novamente")
            
        case 2:
            valor = float(input("Quanto deseja sacar? "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES
            if excedeu_saldo:
                console_clear()
                print("Operação inválida, tente novamente")
            elif excedeu_limite:
                console_clear()
                print("Operação inválida, tente novamente")
            elif excedeu_saques:
                console_clear()
                print("Limite de saques excedido")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                console_clear()
                print('################# SAQUE REALIZADO COM SUCESSO  #################\n\n')
                print(f"Saque de R$ {valor:.2f} realizado com sucesso")
            else:
                console_clear()
                print("Operação inválida, tente novamente")
            
        case 3:
            console_clear()
            print('################# SALDO #################\n\n')
            print("Seu saldo: R$ {:.2f}".format(saldo))
            print()
            print()
            print('################# EXTRATO #################\n\n')
            print("Seu extrato: \n{}".format(extrato))
            
            
        case 4:
            console_clear()
            print("Saindo...")
            break;
        case _:
            console_clear()
            print("Operação inválida, tente novamente")
    input('\nPressione <enter> para continuar')
    console_clear()