import requests

api_key = '99026117ada802b40108037ee1933a6d'
api_token = 'ATTAb773be4a883d29f30ac34951dfa32853b43ed8d30d378e73e1b2c5c5f83f9681FA4F614F'
board_id = '65fa58235477f5d74517cfcb'
list_id = '66c8e799fafd5b925749197a'

# Seu dicionário de grupos e subgrupos
dicionario = {
    'farois': {
        'codigo': '0081',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['']},
            'farois': {'codigo': '0259', 'itens': ['FAROL']},
            'faroletes': {'codigo': '0260', 'itens': ['FAROL AUXILIAR', 'FAROLETE']},
            'lentes_farois': {'codigo': '0268', 'itens': ['LENTE FAROL', 'LENTE FAROL AUXILIAR', 'LENTE FAROLETE']},
            
        }
    },
    'lanternas': {
        'codigo': '0082',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['LANTERNA', 'LANTERNA PILOTO', 'LANTERNA TIJOLINHO']},
            'lanternas_dianteiras': {'codigo': '0261', 'itens': ['LANTERNA DIANT', 'LANTERNA DIANTEIRA']},
            'lanternas_laterais': {'codigo': '0264', 'itens': ['LANTERNA LATERAL']},
            'lentes_lanternas': {'codigo': '0267', 'itens': ['LENTE LANTERNA', 'LENTE LANTERNA DIANT', 'LENTE LANTERNA DIANTEIRA', 'LENTE LANTERNA TRAS', 'LENTE LANTERNA TRASEIRA', 'LENTE LANTERNA PLACA', 'LENTE LANTERNA TIJOLINHO', 'LENTE TRASEIRA']},
            'lanternas_parachoques': {'codigo': '0263', 'itens': ['LANTERNA REFLETOR', 'LANTERNA (REFLETOR)', 'LANTERNA PARACHOQUE']},
            'lanternas_placa': {'codigo': '0265', 'itens': ['LANTERNA PLACA']},
            'lanternas_teto': {'codigo': '0266', 'itens': ['LANTERNA TETO']},
            'lanternas_traseiras': {'codigo': '0262', 'itens': ['LANTERNA TRASEIRA', 'LANTERNA TRAS']},
            
        }
    },
    'parachoques': {
        'codigo': '0080',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['PARACHOQUE']},
            'parachoques_dianteiros': {'codigo': '0257', 'itens': ['PARACHOQUE DIAN', 'PARACHOQUE DIANTEIRO', 'PARACHOQUE IMPULSAO']},
            'parachoques_traseiros': {'codigo': '0258', 'itens': ['PARACHOQUE TRAS', 'PARACHOQUE TRASEIRO']},
        }
    },
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
