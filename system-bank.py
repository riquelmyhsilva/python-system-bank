
menu ="""
|===== menu =====|
|                |
|  [d] Depósito  |
|  [s] Sacar     |
|  [e] Extrato   |
|  [q] Sair      |
|                |
|================|
"""

valor_conta = 0
extrato = ""
saques_feitos = 0
LIMITE_SAQUE = 3
deposito = 0
saque = 0



while True:

    print(menu)
    opcao_menu = input("=> ")

    if opcao_menu == "d":

        deposito = float(input("Insira o valor do depósito: "))

        if deposito < 0:
            print("Valor inválido.")
        else:
            valor_conta += deposito
            extrato += f"Depósito: +R${deposito:.2f}\n"
            print("|===============================|")
            print("|Deposito realizado com sucesso!|")
            print("|===============================|")

    elif opcao_menu == "s":

        if saques_feitos == LIMITE_SAQUE:
            print("Limite de saques diários atingido.")
            continue

        saque = float(input("Insira o valor do saque: "))

        if saque > valor_conta:
            print("Valor para saque indisponivel.")
        elif saque > 500:
            print("Valor máximo de saque: R$500.00")
        else:
            valor_conta -= saque
            extrato += f"Saque:    -R${saque:.2f}\n"
            saques_feitos += 1
            print("|===============================|")
            print("|  Saque realizado com sucesso! |")
            print("|===============================|")

    elif opcao_menu == "e":
        print("============== extrato ==============\n")
        print("Não foram realizadas movimentações.\n" if not extrato else extrato)
        print("-------------------------------------")
        print(f"Valor em conta: {valor_conta:.2f}")
        print("=====================================")

    elif opcao_menu == "q":

        exit()
    
    else:
        print("|====== X ======|")
        print("|Opção inválida.|")
        print("|====== X ======|")