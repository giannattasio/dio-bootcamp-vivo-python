# (True and False = False)
# (True or False = True)

saldo = 1200
saque = 300
limite = 250
conta_especial = True

expr_1 = saldo >= saque and saque <= limite or conta_especial and \
    saldo >= saque
print(expr_1)

expr_2 = (
    saldo >= saque and saque <= limite) or (
    conta_especial and saldo >= saque)
print(expr_2)

# Tornar meu código cada vez mais fácil de se visualizar é muito importante,
# como fiz hoje, por exemplo, no exemplo abaixo a visualização está muito
# mais clara do que acima.


conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

expr_3 = conta_normal_com_saldo_suficiente or \
    conta_especial_com_saldo_suficiente
print(expr_3)
