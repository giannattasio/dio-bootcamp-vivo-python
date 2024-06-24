# método também não mt recomendado
Nome = "Augusto"
Idade = 20
Profissão = "Jovem aprendiz"
Linguagem = "Python"

# Definindo um dicionario p facilitar no método format
dados = {"nome": "Augusto", "Idade": 20, "Profissão": "Aprendiz"}

print("Nome: {nome} Idade: {Idade} Profissão: {Profissão}".format(**dados))


print("Boa noite, me chamo {}, tenho {} anos de idade \
e atualmente estou atuando como {} na Porto seguro, \
a linguagem que estou aprendendo no momento é {}.".format(
    Nome, Idade, Profissão, Linguagem))


# Método util quando irá repetir variaveis
print("Boa noite, me chamo {2}, tenho {0} anos de idade \
e atualmente estou atuando como {3} na Porto seguro, \
a linguagem que estou aprendendo no momento é {1}. \
Pretendo continuar em {1} no decorrer da minha carreira.".format(
    Idade, Linguagem, Nome, Profissão))


# Método mais detalhado, especificando a variavel
print("Boa noite, me chamo {Nome}, tenho {Idade} anos de idade \
e atualmente estou atuando como {Profissão} na Porto seguro, \
a linguagem que estou aprendendo no momento é {Linguagem}.".format(
    Nome=Nome, Idade=Idade, Profissão=Profissão, Linguagem=Linguagem))
