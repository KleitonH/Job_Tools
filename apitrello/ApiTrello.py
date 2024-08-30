import requests

api_key = '99026117ada802b40108037ee1933a6d'
api_token = 'ATTAb773be4a883d29f30ac34951dfa32853b43ed8d30d378e73e1b2c5c5f83f9681FA4F614F'
board_id = '65fa58235477f5d74517cfcb'
list_id = '66c8e799fafd5b925749197a'

# Seu dicionário de grupos e subgrupos
dicionario = {
    'acessorios_internos': {
        'codigo': '0076',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['PARAFUSO CINTO', 'PARAFUSO CINTO SEGURANÇA', 'PINO TAMPA PORTA LUVAS', 'BORRACHA MOLDURA INTERRUPTOR']},
            'botoes_plastico': {'codigo': '0295', 'itens': ['BOTAO DESEMBACADOR', 'BOTAO FALSO', 'BOTAO FIXACAO', 'BOTAO LIMITADOR', 'BOTAO MACACO', 'BOTAO MANOPLA', 'BOTAO MOLDURA RADIO', 'BOTAO PAINEL CINZEIRO', 'BOTAO REGULAGEM', 'BOTAO TAMPAO', 'BOTAO TRAVA BANCO', 'BOTAO/ACABAMENTO']},
            'molduras_internas': {'codigo': '0297', 'itens': ['MOLDURA ACABAMENTO CAIXA AR', 'MOLDURA ACABAMENTO BANCO', 'MOLDURA ACABAMENTO', 'MOLDURA ACABAMENTO INTERNO', 'MOLDURA ACABAMENTO TETO', 'MOLDURA BANCO', 'MOLDURA ALAVANCA BANCO', 'MOLDURA AR FORCADO', 'MOLDURA BOTAO', 'MOLDURA BOTAO TRAVA BANCO', 'MOLDURA BOTAO VIDRO', 'MOLDURA BRACO PORTA', 'MOLDURA CARPETE', 'MOLDURA CENTRAL', 'MOLDURA CENTRAL BOTOES', 'MOLDURA CENTRAL PAINEL', 'MOLDURA CINZERO', 'MOLDURA COBERTURA', 'MOLDURA COLUNA', 'MOLDURA COM LENTE PAINEL', 'MOLDURA DESCANSA BRACO', 'MOLDURA DIFUSOR AR', 'MOLDURA INTERRUPTOR VIDRO ELETRICO', 'MOLDURA LATERAL BANCO', 'MOLDURA LATERAL INTERNA PARABRISA', 'MOLDURA MACANETA INTERNA',' MOLDURA PAINEL', 'MOLDURA PUXADOR VIDRO', 'MOLDURA RADIO', 'MOLDURA DVD', 'MOLDURA VIDRO PORTA INTERNO', 'MOLDURA COLUNA INTERNA', 'MOLDURA ESPELHO INTERNO', 'MOLDURA CINTO SEGURANCA', 'MOLDURA DIFUSOR AR PAINEL', 'MOLDURA COIFA ALAVANCA CAMBIO']},
            'quebra_sol': {'codigo': '0277', 'itens': ['QUEBRA SOL']},
            'porta_luvas': {'codigo': '0249', 'itens': ['TAMPAO MACANETA PORTA LUVA']},
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
