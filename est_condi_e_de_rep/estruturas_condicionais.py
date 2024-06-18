# saldo = 2500.0
# saque = float(input("informe o valor desejado para saque: "))

# if saldo >= saque:
#     print("Saque Realizado!")

# else:
#     print("Saldo insuficiente")

# saldo = 2000

# opcao = int(input("""
# Informe uma opcao:
# [1] Sacar
# [2] Extrato
# [3] Depositar"""))

# if opcao == 1:
#     valor = float(input("Informe o valor do saque: "))
#     print("Saque realizado")
#     print("Obrigado por ser nosso cliente, ótimo dia!")

# elif opcao == 2:
#     print("Exibindo o extrato...")

# elif opcao == 3:
#     valor = float(input("Informe o valor do deposito: "))
#     print("Deposito realizado")
#     print("Obrigado por ser nosso cliente, ótimo dia!")

# else:
#     SyntaxError.exit("Opção inválida")

maior_idade = 18

idade = int(input("Informe sua idade: "))


if idade >= maior_idade:
    print(
        "Parabéns, você já pode tirar sua CNH, \
para continuarmos com seu cadastro:")
    cpf = input("Informe seu CPF: ")
    print("Cadastro realizado!")
    print("fica pronta bebe")

else:
    print("Infelizmente você não tem a idade mínima para tirar sua CNH.")
