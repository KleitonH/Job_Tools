
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
api_token = os.getenv("API_TOKEN")

board_id = '65fa58235477f5d74517cfcb'

url = f"https://api.trello.com/1/boards/{board_id}/lists"

query = {
    'key': api_key,
    'token': api_token
}

response = requests.get(url, params=query)

if response.status_code == 200:
    listas = response.json()
    
    if not listas:
        print("Nenhuma lista encontrada.")
    else:
        # Itera sobre as listas e exibe os detalhes
        for lista in listas:
            print(f"ID: {lista['id']}")
            print(f"Nome: {lista['name']}")
            print(f"Fechada: {'Sim' if lista['closed'] else 'Não'}\n")
else:
    print(f"Erro ao acessar a API do Trello: {response.status_code}")