nome = "Maurício"

print(nome.upper())
print(nome.lower())
print(nome.title())

#apagar espaços em branco
texto = "  Olá Mundo!    "

print(texto.strip() + ".")
print(texto.lstrip()+ ".")
print(texto.rstrip() + ".")

#junções e centralização
menu = "Python"
            #width / #caractere nos espeaços brancos
print(menu.center(30))
print(menu.center(30, "#"))
print(".".join(menu))

