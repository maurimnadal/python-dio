# texto = input("Informe um texto: ")
# VOGAIS = "AIEOU"

# for letra in texto:
#     if letra.upper() in VOGAIS: #upper transforma em maiuscula
#         print(letra, end = "")
# else: #nao é mt comum
#     print()

#funçao range
#usada pra produzir sequencia de numeros  inteiros a partie de um inicio(inclusivo) para um fim(exclusivo)
#ela recebe tre argumentos: stop(obrigatorio), start(opcional), e step(pulo) opcional 

#EX
print(range(4))

print(list(range(4)))
print(list(range(10)))

for numero in range(11):
    print(numero, end = " ")

for numero in range(0, 51, 5): #tabuada do 5
    print(numero, end = " ")