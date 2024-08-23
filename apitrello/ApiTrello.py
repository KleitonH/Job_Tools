import requests

api_key = ''
api_token = ''
board_id = '65fa58235477f5d74517cfcb'
list_id = '66c8e8e8897ef3397ee466b9'

# Seu dicionário de grupos e subgrupos
dicionario = {
    'limpadores': {
        'codigo': '0079',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['PARAFUSO FIXACAO ESTEPE', 'PARAFUSO FIXACAO BANDEJA ESTEPE']},
            'pivos_limpadores': {'codigo': '0001', 'itens': ['PIVO LIMPADOR']},
            'barras_limpadores': {'codigo': '0255', 'itens': ['BARRA LIMPADOR']},
        }
    },    

    # Continue com o restante do seu dicionário...
}

# Função para criar um card
def create_card(list_id, card_name):
    url = f"https://api.trello.com/1/cards"
    query = {
        'idList': list_id,
        'name': card_name,
        'key': api_key,
        'token': api_token
    }
    response = requests.post(url, params=query)
    if response.status_code == 200:
        return response.json()['id']
    else:
        print(f"Erro ao criar card '{card_name}': {response.text}")
        return None

# Função para criar uma checklist
def create_checklist(card_id, checklist_name):
    url = f"https://api.trello.com/1/checklists"
    query = {
        'idCard': card_id,
        'name': checklist_name,
        'key': api_key,
        'token': api_token
    }
    response = requests.post(url, params=query)
    if response.status_code == 200:
        return response.json()['id']
    else:
        print(f"Erro ao criar checklist '{checklist_name}': {response.text}")
        return None

# Função para adicionar itens na checklist
def add_item_to_checklist(checklist_id, item_name):
    url = f"https://api.trello.com/1/checklists/{checklist_id}/checkItems"
    query = {
        'name': item_name,
        'key': api_key,
        'token': api_token
    }
    response = requests.post(url, params=query)
    if response.status_code == 200:
        print(f"Item '{item_name}' adicionado com sucesso!")
    else:
        print(f"Erro ao adicionar '{item_name}': {response.text}")

# Criar cards, checklists e adicionar itens
for grupo, dados_grupo in dicionario.items():
    card_name = f"{grupo.upper()} - {dados_grupo['codigo']}"
    card_id = create_card(list_id, card_name)
    
    if card_id:
        for subgrupo, dados_subgrupo in dados_grupo['subgrupos'].items():
            checklist_name = f"{subgrupo.upper()} - {dados_subgrupo['codigo']}"
            checklist_id = create_checklist(card_id, checklist_name)
            
            if checklist_id:
                for item in dados_subgrupo['itens']:
                    add_item_to_checklist(checklist_id, item)
