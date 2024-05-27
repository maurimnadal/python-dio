nome = 'Maurício'
idade = 18

nome, idade = 'Cláudio', 20
print(nome, idade)

limite_saque_diario = 1000

BRAZILIAN_STATES = {'RJ', 'RS', 'SC', 'SP'}

print(BRAZILIAN_STATES)

#conversão de tipos

#INTEIRO PARA FLOAT
preco = 10 
print(preco)
#>>>10

preco = float(preco)
print(preco)
#10.0
#or
preco = 10 / 2 
print(preco)
#>>>5.0

#FLOAT PARA INTEIRO 

preco = 10.30
print(preco)
#>>>10.3
#or
preco = int(preco)
print(preco)
#>>>10

#Conversão por divisão
preco = 10
print(preco)
#>>>10
print(preco / 2)
#>>>5.0

print(preco // 2)
#>>>5

#NUMÉRICO PARA STRING
preco = 10.50
idade = 28
print(str(preco))
#>>>10.5

print(str(idade))
#>>>28

texto = f"idade {idade} preco {preco}"
print(texto)
#>>>idade 28 preço 10.5

#STRING PARA NUMERO
preco = "10.50"
idade = "28"

print(float(preco))
#>>>10.50
print(float(preco))
#>>>28

