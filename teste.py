import requests

# input() pega o que a pessoa digitar no terminal
# está sempre dentro de aspas, então ele volta como TEXTO (string)
moeda_origem = input("De qual moeda? (ex: USD): ")
moeda_destino = input("Para qual moeda? (ex: BRL): ")
valor = input("Qual valor? (ex: 100): ")

# monta a URL "colando" as variáveis dentro do texto
url = f"https://api.frankfurter.dev/v2/rate/USD/BRL"

resposta = requests.get(url)
dados = resposta.json()

cotacao = dados["rates"][moeda_destino]

print(f"{valor} {moeda_origem} equivale a {cotacao} {moeda_destino}")