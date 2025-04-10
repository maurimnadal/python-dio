from datetime import datetime

def extrair_anos(datas):
    # Divide a string de datas em uma lista
    lista_datas = datas.split(", ")
    # TODO: Extraia o ano de cada data e cria uma nova lista com os anos
    lista_datas = [datetime.strptime(data, "%Y-%m-%d") for data in lista_datas]
    anos = [str(data.year) for data in lista_datas]
    
    # Junta os anos em uma string separada por vírgula e retorna
    return ", ".join(anos)


entrada = input()

# TODO: Chame a função para imprimir o resultado:
saida = extrair_anos(entrada)

print(saida)

# datas = "2023-10-01, 2022-05-15, 2021-12-31"
# lista_datas = datas.split(", ")
# # TODO: Extraia o ano de cada data e cria uma nova lista com os anos
# lista_datas = [datetime.strptime(data, "%Y-%m-%d") for data in lista_datas]
# anos = [data.year for data in lista_datas]
# print(anos)