nome = "Maurício"
idade = 18
profissao = "Desempregado"
linguagem = "Python"
saldo = 45.246345

dados = {"nome": "Maurício", "idade": 28, "saldo": 45.246345 }

#old style(%)
print("Nome: %s, Idade: %d" %(nome, idade))

#método format
print("Nome: {}, Idade: {}".format(nome, idade))

print("Nome: {1}, Idade: {0}".format(idade, nome))
print("Nome: {1}, Idade: {0} Nomes: {1} {1}".format(idade, nome))

print("Nome: {nome}, Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name}, Idade: {age}".format(age=idade, name=nome))
print("Nome: {nome}, Idade: {idade}".format(**dados))

#f-string
print(f"Nome: {nome}, Idade: {idade}")
print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo:.2f}")
print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo:10.3f}")