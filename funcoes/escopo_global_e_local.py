salario_fixo = 3200


def salario_comissao(comissao):
    global salario_fixo
    salario_fixo += comissao
    return salario_fixo


salario_c_comissao = salario_comissao(700)
print(salario_c_comissao)


def salario_comissao(comissao, lista):
    global salario_fixo

    copy_list = lista.copy()
    copy_list.append(4)
    print(f"copia da lista={copy_list}")

    salario_fixo += comissao
    return salario_fixo


lista = [25]
salario_c_comissao = salario_comissao(350, lista)
print(salario_c_comissao)
print(lista)
