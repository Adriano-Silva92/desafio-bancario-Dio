saldo = 0
extrato = []
saque_diario = 3

def sacar(valor):
    global saldo
    global saque_diario

    if valor > saldo:
        print("Operação não realizada, saldo insuficiente!")
        print(f"Saldo Atual é de R${saldo:.2f}")

    elif valor <= 0 or valor > 500:
        print("Operação não realizada, valor deve ser maior que R$0 e menor que R$500")
        print(f"Saldo Atual é de R${saldo:.2f}")


    elif saque_diario == 0:
        print("Operação não realizada, você atingiu o limite de 3 saques diários")
        print(f"Saldo Atual é de R${saldo:.2f}")

    else:
        saldo -= valor
        saque_diario -= 1
        extrato.append(f"Saque: -R${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso!")

def depositar(valor):
    global saldo
    saldo += valor
    extrato.append(f"Depósito: +R${valor:.2f}")
    print(f"Depósito no valor de R${valor:.2f} foi realizado com sucesso!")

def mostrar_extrato():
    print("\n Extrato:")
    if not extrato:
        print("Nenhuma movimentação foi realizada!")
    else:
        for item in extrato:
            print(item)
    print(f"Saldo atual: R${saldo:.2f}\n")

while True:
    menu = """
====== MENU BANCÁRIO ======
[1] SACAR
[2] DEPOSITAR
[3] EXTRATO
[0] SAIR
Escolha uma opção: """
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor para saque: R$"))
        sacar(valor)
    elif opcao == "2":
        valor = float(input("Informe o valor para depósito: R$"))
        depositar(valor)
    elif opcao == "3":
        mostrar_extrato()
    elif opcao == "0":
        print("Encerrando o sistema. Obrigado!!!")
        break
    else:
        print("Opção inválida! Informe uma opção do MENU BANCÁRIO.")
