import requests
import csv

# Solicita os dados do cliente
cliente = {}
cliente["nome"] = input("Digite o nome do cliente: ")
cliente["cep"] = input("Digite o CEP do cliente (no formato 00000-000): ")
cliente["numero_casa"] = input("Digite o número da casa do cliente: ")

# Faz a requisição GET para a API do ViaCEP
response = requests.get("https://viacep.com.br/ws/{}/json/".format(cliente["cep"]))

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Converte a resposta para um dicionário Python
    endereco = response.json()
    
    # Formata o endereço de acordo com os requisitos mencionados na pergunta
    endereco_formatado = "{} rua: {}, numero casa: {}, cep: {}, cidade: {}".format(
        endereco["logradouro"], endereco["bairro"], cliente["numero_casa"], endereco["cep"], endereco["localidade"])
    
    # Adiciona o endereço do cliente ao dicionário
    cliente["endereco"] = endereco_formatado
    
    print("Endereço encontrado:")
    print(endereco_formatado)
else:
    print("Não foi possível encontrar o endereço para o CEP informado.")

# Escreve os dados do cliente no arquivo CSV
with open("Cadastro.csv", mode="a", newline="", encoding="utf8") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow([cliente["nome"], cliente["cep"], cliente["numero_casa"], cliente["endereco"]])
