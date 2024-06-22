nome = "AuGuStO"

print(nome.upper())
print(nome.lower())
print(nome.title())


# eliminando espaços em branco
titulo = "    Olá, tudo bem?     "

print(titulo)
print(titulo.strip() + ".")  # remove espaços da esq e dir
print(titulo.lstrip() + ".")  # remove somente da esq
print(titulo.rstrip() + ".")  # remove somente da dir

# junções e centralização
curso = "Python"

print(curso.center(8, "*"))
print("--".join(curso))
""" print(curso.center(8, "*")) = centraliza, add a
quantidade de caracteres que vc desejae adiciona caracter
especial no começo e fim """
""" print("--".join(curso)) = add um caracter
especial a cada letra da palavra desejada """
