# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo):
  if(consumo <= 10):
    return "Plano Essencial Fibra - 50Mbps"
  elif(consumo > 10 and consumo <= 20):
    return "Plano Prata Fibra - 100Mbps"
  else:
    return "Plano Premium Fibra - 300Mbps"
    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Insira seu consumo médio mensal de dados em GB: "))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
recomendar_plano(consumo)
print(recomendar_plano(consumo))

# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
# itens = []

# # TODO: Crie um loop para solicita os itens ao usuário:
# while True:
#     while (len(itens) < 3):
#         item = str(input("Insira o equipamento: "))
#         itens.append(item)
#     break
        
    

# # TODO: Solicite o item e armazena na variável "item":

# # TODO: Adicione o item à lista "itens":


# # Exibe a lista de itens
# print("Lista de Equipamentos:")  
# for item in itens:
#     # Loop que percorre cada item na lista "itens"
#     print(f"- {item}")

# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
# import re


#  # TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
# def validate_numero_telefone(phone_number):
#     pattern = r'\(\d{2}\) 9\d{4}-\d{4}'
#     if re.match(pattern, phone_number):  
#         return "Número de telefone válido."
#     else: 
#         return "Número de telefone inválido."
        
#         # TODO: Agora crie um return, para retornar que o número de telefone é válido:
       
#        # TODO: Crie um else e return, caso não o número de telefone seja inválido:
    

# # Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
# phone_number = input("Informe o número de telefone: ")  

# # TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
# validate_numero_telefone(phone_number)
# result = validate_numero_telefone(phone_number)

# # Imprime o resultado:
# print(result)