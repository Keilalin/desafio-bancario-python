menu = '''
========

[1] Depositar
[2] Saque
[3] Extrato de Conta
[0] Sair

Digite a opcao desejada:

======== '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor: .2f}\n"

        else:
            print("Valor informado invalido.")
    
    elif opcao == "2":
        valor = float(input("Informe o valor do saque:"))

        saldo_insuficiente = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("Saldo insuficiente. Saque nao executado.")

        elif excedeu_limite:
            print("Limite de valor excedido. Saque nao executado.")

        elif excedeu_saques:
            print("Limite saque diario atingido. Saque nao executado.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$: {valor: .2f}\n"
            numero_saques += 1
            print ("Saque de {valor} concluido com sucesso.")

        else:
            print("Valor informado invalido.")

    elif opcao == "3":
        print("\n---------- Extrato ----------")
        print("Sem movimentacao." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("----------------------------------")
              
    elif opcao == "0":
        break

    else:
        print("Opcao invalida. Por favor, insira a operacao desejada.")