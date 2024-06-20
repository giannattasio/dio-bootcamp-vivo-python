opcao = -5

while opcao != 0:
    print("""
[1] Sacar
[2] Extrato
[3] Depositar
[0] Sair""")
    opcao = int(input(" => "))

    if opcao == 1:
        print("Saque realizado!")
    elif opcao == 2:
        print("Exibindo extrato...")
    elif opcao == 3:
        print("Deposito Realizado!")
    elif opcao == 0:
        print("Tenha um ótimo dia, até a proxima!")
    else:
        print("Por favor, digite uma das opções acima")
