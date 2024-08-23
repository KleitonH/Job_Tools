import requests

# Suas credenciais de API
api_key = ''
api_token = ''

# O ID do card que você quer excluir
card_id = 'XppkW0J4'

# URL para a requisição DELETE
url = f"https://api.trello.com/1/lists/{card_id}"

# Parâmetros da API
query = {
    'key': api_key,
    'token': api_token
}

# Fazendo a requisição DELETE para excluir o card
response = requests.delete(url, params=query)

# Verificando o resultado
if response.status_code == 200:
    print(f"Card {card_id} excluído com sucesso.")
else:
    print(f"Falha ao excluir o card: {response.status_code}")
