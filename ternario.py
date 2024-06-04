saldo = 2000
saque = 200
#valor1               #condição           #valor2
status = "sucesso" if saldo >= saque else "falha"
print(f"{status} ao realizar o saque")