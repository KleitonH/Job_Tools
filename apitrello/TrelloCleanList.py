import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
api_token = os.getenv("API_TOKEN")


# ID da lista para ser limpa
list_id = '65fa582f7e00e41d4d3a8586'

url_list_cards = f"https://api.trello.com/1/lists/{list_id}/cards"

# Parâmetros para autenticação
query = {
    'key': api_key,
    'token': api_token
}

# Requisição para listar os cards da lista
response = requests.get(url_list_cards, params=query)

if response.status_code == 200:
    cards = response.json()
    
    if not cards:
        print("Nenhum card encontrado na lista.")
    else:
        # Iterar sobre os cards e deletá-los
        for card in cards:
            card_id = card['id']
            card_name = card['name']
            
            # URL para deletar cada card
            url_delete_card = f"https://api.trello.com/1/cards/{card_id}"
            
            # Requisição DELETE para apagar o card
            delete_response = requests.delete(url_delete_card, params=query)
            
            if delete_response.status_code == 200:
                print(f"Card '{card_name}' (ID: {card_id}) deletado com sucesso.")
            else:
                print(f"Erro ao deletar o card '{card_name}' (ID: {card_id}): {delete_response.status_code}")
else:
    print(f"Erro ao acessar a lista de cards: {response.status_code}")