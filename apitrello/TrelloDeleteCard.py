import requests

# Suas credenciais de API
api_key = 'c9ba71549ffc1f275c196225e8e848ae'
api_token = 'ATTA244285dccb53ad4eca57419045307b86920dc3ef8f85a3b57d6e7833d3ad88fd07D7E5A9'

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
