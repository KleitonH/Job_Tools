
from email.mime import text 
import pyautogui # Importação da biblioteca Pyautogui para controle do mouse e teclado 
import time # Importação da biblioteca time para intervalos de tempo 
import re # Importação da biblioteca re para modificação de strings
import pickle # Importação da biblioteca pickle para salvar arquivos
from pyscreeze import screenshot # Importação da biblioteca pyscreeze para captura de tela
from pytesseract import pytesseract # Importação da biblioteca pytesseract para conversão de imagens em strings
caminho_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # Caminho para o executável do pytesseract
pytesseract.tesseract_cmd = caminho_tesseract # Define o caminho para o pytesseract
tempo_de_execucao = 40000 # Tempo de execução máximo da operação 


grupos = {
    'colorometria': {
        'codigo': '0006',
        'subgrupos': {
            'default':{'código': '0001', 'itens': []}

        }
    },
    'parabrisas': {
        'codigo': '0005',
        'subgrupos': {
            'sem_sensor': {'codigo': '0002', 'itens': ["PARABRISA", "PARABRISA S/SENSOR", "PARABRISA S/ SENSOR", "PARABRISA SISENSOR", "PARABRISA SEM SENSOR"]},
            'com_sensor': {'codigo': '0003', 'itens': ["PARABRISA C/SENSOR", "PARABRISA C/ SENSOR", "PARABRISA COM SENSOR", "PARABRISA SENSOR", "PARABRISA CISENSOR"]}
        }
    },
    'vigias': {
        'codigo': '0003',
        'subgrupos': {
            'default':{'codigo': '0001', 'itens': ['VIDRO VIGIA', 'VIGIA']}}
    },
    'laterais': {
        'codigo': '0008',
        'subgrupos': {
            'ventarolas': {'codigo': '0004', 'itens': ['VENTAROLA', 'VIDRO LATERAL MOVEL', 'VIDRO VENTAROLA', 'VIDRO VENTAROLA OCULO']},
            'vidros_ocolus': {'codigo': '0005', 'itens': ['OCULO', 'OCULOS', 'VIDRO LATERAL DIANT', 'VIDRO LATERAL OCULO', 'VIDRO LATERAL TRAS OCULO', 'VIDRO FIXO DIANTEIRO']},
            'vidros_janela': {'codigo': '0006', 'itens': ['VIDRO JANELA', 'VIDRO LATERAL TRAS', 'VIDRO LATERAL', 'VIDRO LATERAL FIXO', 'VIDRO PORTA FIXO']},  
            'vidros_porta': {'codigo': '0007', 'itens': ['VIDRO PORTA']},
        }
    },
    'baterias_startstop': {
        'codigo': '0009',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['BATERIA START STOP', 'BATERIA START STOP', 'BATERIA START-STOP']},

        }
    },
    'baterias_nobreak': {
        'codigo': '0010',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['BATERIA NOBREAK', 'BATERIA NOOBREAK']},

        }
    },
    'escapamentos_completos': {
        'codigo': '0011',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},

        }
    },
    'escapamentos_silenciosos': {
        'codigo': '0012',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['ESCAPAMENTO TRAS', 'ESCAPAMENTO TRASEIRO', 'ESCAPAMENTO SILENC', 'ESCAPAMENTO SILENCIOSO TRAS', 'ESCAPAMENTO SIL TRAS', 'ESCAPAMENTO SILENCIOSO TRAS', 'ESCAPAMENTO ABAF', 'ESCAPAMENTO ABAFADOR', 'ESCAPAMENTO CONJUNT', 'ESCAPAMENTO TURBINHO', 'ESCAPAMENTO TURBINHO']},

        }
    },
    'escapamentos_catalisadores': {
        'codigo': '0013',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['CATALISADOR ESCAP', 'ESCAPAMENTO CATALISA']},

        }
    },
    'escapamentos_coletores': {
        'codigo': '0014',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['ESCAPAMENTO COLETOR', 'ESCAPAMENTO COLETOR TUBULAR']},

        }
    },
    'escapamentos_coletores_catalisador': {
        'codigo': '0015',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['CATALISADOR C/TB', 'CATALISADOR C/TUBO', 'COLETOR COM CATALIS']},

        }
    },
    'escapamentos_intermediarios': {
        'codigo': '0016',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['BENGALA ESCAPAMENTO', 'CURVA ESCAPAMENTO', 'ESCAPAMENTO INTER', 'ESCAPAMENTO INTERM', 'ESCAPAMENTO INTEMEDIARIO', 'ESCAPAMENTO ABAF INTER', 'ESCAPAMENTO ABAFADOR INTERM', 'ESCAPAMENTO SIL INTER', 'ESCAPAMENTO TUBO INTER', 'TUBO INTER' ]},

        }
    },
    'escapamentos_ponteiras': {
        'codigo': '0017',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['PONTEIRA', 'PONTEIRA ESCAP']},

        }
    },
    'escapamentos_tubos': {
        'codigo': '0018',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['TUBO ESCAP', 'ESCAPAMENTO TUBO', 'LUVA ESCAP', 'TUBO MOTOR']},

        }
    },
    'escapamentos_flexiveis': {
        'codigo': '0019',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['ESCAPAMENTO C/FLEX', 'ESCAPAMENTO COM FLEXIVEL', 'ESCAPAMENTO FLEXIVEL', 'FLEXIVEL ESCAP']},

        }
    },
    'arrefecimento': {
        'codigo': '0020',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['BRUCUTU', 'BUCHA BOMBA ESGUICHO']},
            'radiadores': {'codigo': '0008', 'itens': []},
            'bombas_agua': {'codigo': '0009', 'itens': ['BOMBA AGUA', 'BOMBA D.HIDR', 'BOMBA DAGUA']},
            'ventiladores': {'codigo': '0010', 'itens': []},

        }
    },
    'cabos': {
        'codigo': '0021',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['CABO ACIONADOR PORTINHOLA', 'CABO AR FORCADO', 'CABO PORTA CORRER', 'CABO PORTA MOLA', 'CABO PORTINHOLA', 'CABO TEMPERATURA']},
            'cabos_acelerador': {'codigo': '0011', 'itens': ['CABO ACEL', 'CABO ACELERADO', 'CABO DE ACELERADOR', 'CABO PARADA MOTOR']},
            'cabos_embreagem': {'codigo': '0012', 'itens': ['CABO EMB', 'CABO EMBR', 'CABO EMBREAGE', 'CABO FLEX EMBR', 'CABO TRANSMISSAO']},
            'cabos_freio': {'codigo': '0013', 'itens': ['CABO DE FREIO', 'CABO FREIO', 'CABO LIBERACAO FREIO']},
            'cabos_capo': {'codigo': '0014', 'itens': ['CABO CAPO', 'CABO PUXADOR CAPO']},
            'cabos_velocimetro': {'codigo': '0015', 'itens': ['CABO DE VELOCIMETRO', 'CABO TACOGRAFO', 'CABO TACOMETRO', 'CABO VELOCIMETRO', 'CABO VELOC']},
            'cabos_tampa_traseira': {'codigo': '0016', 'itens': ['CABO LIMITADOR DA TAMPA TRAS', 'CABO PUXADOR TAMPA', 'CABO TAMPA TRAS']},
            'cabos_afogador': {'codigo': '0017', 'itens': ['CABO AFOGADOR', 'CABO ESTRANGULADOR']},
            'cabos_cambio': {'codigo': '0018', 'itens': ['CABO CAMBIO', 'CABO COMANDO', 'CABO COMANDO MARCHA', 'CABO ENGATE COMANDO', 'CABO ENGATE', 'CABO ENGATE MARCHA', 'CABO MARCHA', 'CABO REDUZIDA', 'CABO SELECAO CAMBIO', 'CABO SELECAO MARCHA', 'CABO SELECAO COMANDO']},
            'cabos_fechadura': {'codigo': '0019', 'itens': []},
            'cabos_trava_banco': {'codigo': '0020', 'itens': ['CABO ENCOSTO BANCO', 'CABO REGULAGEM BANCO', 'CABO TRAVA BANCO']},
        }
    },
    'carburacao': {
        'codigo': '0022',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'carburadores': {'codigo': '0021', 'itens': []},
            'componentes_carburadores': {'codigo': '0022', 'itens': ["AGULHA CARBURADOR", 'BASE CARB', 'BASE CARBURADOR', 'BASE VEDACAO CARB', 'BENGALA CARB', 'BENGALA INJETOR CARBURAD', 'BORBOLETA CARBURADOR']},
        }
    },
    'combustivel': {
        'codigo': '0035',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ["ADAPTADOR TAMPA TANQUE", 'BORRACHA FLANGE COM']},
            'flanges': {'codigo': '0089', 'itens': ["ADAPTADOR FLANGE CAIXA", "FLANGE"]},
        }
    },
    'correias': {
        'codigo': '0023',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'correias_dentadas': {'codigo': '0023', 'itens': []},
            'correias_polyv': {'codigo': '0024', 'itens': []},
        }
    },
    'direcao': {
        'codigo': '0024',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ["ADAPTADOR VOLANTE", 'BUCHA SETOR DIRECAO', 'BUCHA COLUNA DIRECAO', 'BUCHA BRACO', 'BUCHA INF BRACO',]},
            'caixas_direcao': {'codigo': '0025', 'itens': []},
            'setor_direcao': {'codigo': '0026', 'itens': []},
            'barras_axiais': {'codigo': '0027', 'itens': ['BARRA AXIAL', 'BARRA DIRECAO', 'BARRA LATERAL', 'BRACO AUXILIAR', 'BRACO DIANT INF', 'BRACO OSCILANT', 'BRACO PITMAN', 'BRACO SETOR', 'BRACO SUSP', 'BRACO TENSOR']},
            'pivos': {'codigo': '0067', 'itens': ['PIVO', 'PIVO INFERIOR', 'PIVO', 'PIVO SUSP']},
            'terminal_direcao': {'codigo': '0093', 'itens': ['TERMINAL DIR', 'TERMINAL DIRECAO', 'TERMINAL SUSPENSAO']}
        }
    },
    'filtros': {
        'codigo': '0025',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'filtros_ar': {'codigo': '0028', 'itens': ['FILTRO AR']},
            'filtros_combustivel': {'codigo': '0029', 'itens': []},
            'filtros_de_oleo': {'codigo': '0030', 'itens': []},
            'filtros_de_ar_condicionado': {'codigo': '0074', 'itens': []},
            'filtros_de_cabine': {'codigo': '0075', 'itens': []},
        }
    },
    'freios': {
        'codigo': '0026',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ["ACIONADOR FREIO", "ACIONADOR/GATILHO FREIO"]},
            'pastilhas_freio': {'codigo': '0031', 'itens': ['PASTILHA FREIO']},
            'discos_freio': {'codigo': '0032', 'itens': ['DISCO FREIO', "DISCO FREIO TRAS"]},
            'tambores_freio': {'codigo': '0033', 'itens': []},
            'flexiveis_freio': {'codigo': '0034', 'itens': ['BIFURACACAO AO FLEXIVEL']},
            'pincas_freio': {'codigo': '0035', 'itens': []},
            'cilindros_roda_freio': {'codigo': '0036', 'itens': ['CILINDRO RODA']},
            'cilindros_mestre_freio': {'codigo': '0037', 'itens': []},
            'lonas_freio': {'codigo': '0038', 'itens': []},
            'sapatas_freio': {'codigo': '0039', 'itens': []},
            'servofreios': {'codigo': '0087', 'itens': ["ACIONADOR FREIO", "ALAVANCA ACIONAMENTO FREIO", "GATILHO FREIO"]},
        }
    },    
    'juntas_retentores': {
        'codigo': '0027',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'aneis': {'codigo': '0091', 'itens': ['ANEIS PISTAO', 'ANEL PISTAO', 'ANEL BUJAO', 'ANEL AJUSTE ROLAMENTO', 'ANEL ALAVANCA', 'ANEL AMORTECEDOR', 'ANEL ANTI RUIDO', 'ANEL BOCAL TANQUE', 'ANEL BORRACHA', 'ANEL BRACO SUSP', 'ANEL CARCACA', 'ANEL CEBOLAO', 'ANEL CILINDRO', 'ANEL COLETOR', 'ANEL VEDACAO', 'ANEL EIXO TRAS', 'ANEL IMPULSOR ARV', 'ANEL INFERIOR CARRO', 'ANEL INTERMEDIARIO', 'ANEL JUNTA', 'ANEL MALHA ACO', 'ANEL MOTOR', 'ANEL RADIADOR', 'ANEL RODA', 'ANEL SILENCIOSO', 'ANEL SINCRONIZ', 'ANEL TAMPA VALV', 'ANEL TIRANTE SUSP', 'ANEL TRASEIRO', 'ANEL TRAVA', 'ANEL VEDACAO', 'ANEL VEDADOR', 'ANEL JUNTA DISTRI', 'BORRACHA BOCAL ']},
            'juntas_cabecote': {'codigo': '0040', 'itens': []},
            'juntas_coletor': {'codigo': '0041', 'itens': []},
            'juntas_carter': {'codigo': '0042', 'itens': []},
            'juntas_tampa_valvula': {'codigo': '0043', 'itens': []},
            'juntas_tampa_distribuidor': {'codigo': '0044', 'itens': []}, 
            'retentores_eixo': {'codigo': '0045', 'itens': []},
            'retentores_virabrequim': {'codigo': '0046', 'itens': []},
            'retentores_comando_valvula': {'codigo': '0047', 'itens': []},
            'retentores_caixa_cambio': {'codigo': '0048', 'itens': []},
        }
    },
    'lubrificacao': {
        'codigo': '0028',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['ALONGADOR VARETA']},
            'bombas_oleo': {'codigo': '0049', 'itens': ['BOMBA OLEO']},
            'reservatorios_oleo': {'codigo': '0050', 'itens': []},
        }
    },
    'mangueiras': {
        'codigo': '0029',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'mangueiras_ar_condicionado': {'codigo': '0051', 'itens': []},
            'mangueiras_aquecimento': {'codigo': '0052', 'itens': []},
            'mangueiras_combustivel': {'codigo': '0053', 'itens': []},
            'mangueiras_agua': {'codigo': '0054', 'itens': []},
            'mangueiras_ar_motor': {'codigo': '0085', 'itens': []},
            'mangueiras_oleo': {'codigo': '0086', 'itens': []},
        }
    },    
    'motor': {
        'codigo': '0030',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['BUCHA ARRANQUE', ]},
            'cabecotes': {'codigo': '0055', 'itens': ['CABECOTE', 'CABECOTE MOTOR']},
            'virabrequins': {'codigo': '0056', 'itens': []},
            'carteres': {'codigo': '0057', 'itens': []},
        }
    },
    'reparos': {
        'codigo': '0031',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ["ACOPLAMENTO COLETOR ADMISSAO", "ACOPLAMENTO DIRECAO", "ACOPLAMENTO VISOCOSO", "ADAPTADOR COLETOR ADMISSAO", "REPARO COLETOR ADMISSAO", "REPARO DIRECAO", "ADAPTADOR MOTOR MAQ VIDRO"]},
            'kit_reparo_homocinetica': {'codigo': '0058', 'itens': []},
            'kit reparo_trambulador': {'codigo': '0059', 'itens': ['ACOPLAMENTO HASTE TRAMBULADOR', 'ACOPLAMENTO HASTE LIGACAO', 'BORRACHA/REPARO TRAMBULADOR', 'CACHORRINHO REPARO ANEIS']},
            'kit_reparo_alavanca': {'codigo': '0060', 'itens': ["ACOPLAMENTO VARAO CAMBIO", "REPARO VARAO CAMBIO", 'BUCHA ALAVANCA CAMBIO', 'BUCHA REPARO ALAVANCA']},
            'kit_reparo_pincas': {'codigo': '0077', 'itens': []},
            'kit_reparo_setor': {'codigo': '0088', 'itens': ['ACOPLAMENTO SETOR']},
            'alavancas': {'codigo': '0090', 'itens': ['ALAVANCA ACIONADORA', 'ALAVANCA CAMBIO', 'ALAVANCA EMB', 'ALAVANCA EMBREAGEM', 'ALAVANCA ENGATE', 'ALAVANCA ENGRENAGEM', 'ALAVANCA FREIO MAO', 'ALAVANCA FREIO TRAS', 'ALAVANCA INIBIDORA', 'ALAVANCA LIGACAO', 'ALAVANCA MARCHA', 'ALAVANCA PATIM', 'ALAVANCA REG', 'ALAVANCA REGULADO', 'ALAVANCA SELETORA', 'ALAVANCA TRAMBULADOR', ]},
        }
    },
    'rolamentos_tensores_polias': {
        'codigo': '0032',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['ROLAMENTO CAMBIO']},
            'rolamentos_roda': {'codigo': '0061', 'itens': ['BUCHA ROLAMENTO DIRECAO']},
            'rolamentos_motor': {'codigo': '0062', 'itens': []},
            'tensores': {'codigo': '0063', 'itens': []},
            'polias': {'codigo': '0064', 'itens': []},
            'cubos_roda': {'codigo': '0076', 'itens': ['CUBO RODA', 'CUBO RODA DIANTEIR', 'CUBO RODA TRASEIR']},
        }
    },
    'suspensao': {
        'codigo': '0033',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'buchas': {'codigo': '0065', 'itens': ['BUCHA BAND SUSP', 'BUCHA BARRA ESTAB', 'BUCHA BANDEJA DIANT', 'BUCHA AGREGADO', 'BUCHA ALGEMA BARRA', 'BUCHA ALT SUP', 'BUCHA ALTERNADOR', 'BUCHA AMORT', 'BUCHA AMORT DIANT', 'BUCHA AMORTEC', 'BUCHA AMORTECEDOR', 'BUCHA AR COND', 'BUCHA ARTIC EIXO', 'BUCHA ARTICULACAO', 'BUCHA BAND', 'BUCHA BANDEJA', 'BUCHA BARR ESTAB', 'BUCHA BARRA ESTAB', 'BUCHA BARRA LIGACAO', 'BUCHA BARRA TENS SUSP', 'BUCHA BARRA TORCAO' 'BUCHA BIELA', 'BUCHA CALCO TRAVESSA', 'BUCHA CENTRAL BANDEJA', 'BUCHA COXIM', 'BUCHA EIXO', "BUCHA ESTAB", 'BUCHA ESTABILIZADORA', 'BUCHA FEIXE MOLA', 'BUCHA MANGA EIXO', 'BUCHA HAST BAND', 'BUCHA INF AMOR', 'BUCHA INFERIOR BANDE', 'BUCHA INFERIOR AMORT', 'BUCHA INFERIOR JUMELO', 'BUCHA JUMELO', 'BUCHA MAIOR', 'BUCHA MENOR', 'BUCHA MOLA', 'BUCHA OVAL EIXO', 'BUCHA TRAS BAND', 'BUCHA PONTA BANDEJA', 'BUCHA SUP ALGEMA', 'BUCHA SUP AMOR', 'BUCHA SUPERIOR BAND', 'BUCHA SUPERIOR JUMELO', 'BUCHA SUSP', 'BUCHA SUSPEN', 'BUCHA SUSPENSAO', 'BUCHA TENSO', 'BUCHA TENSOR SUS', 'BUCHA TERMINAL EIXO', 'BUCHA TIRANTE', 'BUCHA TARS BAND', 'BUCHA TRAS BRAC', 'BUCHA TRAS EIXO', 'BUCHA TRAS FEIXE MOLA', 'BUCHA TRAS SUSP', 'BUCHA TRAS BAND', 'BUCHA TRASEIRA BANDEJA', 'BUCHA TRAV EIXO']},
            'amortecedores': {'codigo': '0066', 'itens': ["AMORT DIANT", "AMORTECEDOR DIANT", "AMORTECEDOR REMAN", "AMORTECEDOR TRAS", "AMORTECEDOR TRASEIRO", ]},
            'coxins': {'codigo': '0078', 'itens': ['COXIM MOTOR']},
            'bieletas': {'codigo': '0079', 'itens': ['BIELETA', 'BIELETA BARRA ESTAB', 'BIELETA BARRA ESTABILIZADORA', 'BIELETA DIANT', 'BIELETA ESTAB', 'BIELETA ESTABILIZADORA', 'BIELETA SUSP', 'BIELETA SUSPENSAO', 'BIELETA TRAS']},
            'bandejas': {'codigo': '0080', 'itens': ['BAND SUSP SUP', 'BANDEJA', "BANDEJA DIANT", 'BANDEJA DIANTEIRA', 'BANDEJA INFERIOR', 'BANDEJA SUS', 'BANDEJA SUSPENSAO']},
            'kit_amortecedor': {'codigo': '0081', 'itens': ['BATENTE AMORT', 'BATENTE AMORTECEDOR', 'BATENTE BANDEJA', 'BATENTE BRACO', 'BATENTE DE MOLA', 'BATENTE DIANT', 'BATENTE EIXO', 'BATENTE FEIXE MOLA', 'BATENTE INF', 'BATENTE INFERIOR', 'BATENTE MOLA', 'BATENTE SUP', 'BATENTE SUSP', 'BATENTE COIFA', 'BOLACHA SANTA FE', 'BORRACHA BARRA ESTA', 'BORRACHA HASTE VALVULA', 'BORRACHA LIGACAO BARRA EST']},

        }
    },
    'transmissao': {
        'codigo': '0034',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['BALENCEIRO EMBREAGEM', 'BARRA DE LIGACAO']},
            'embreagens': {'codigo': '0082', 'itens': []},
            'cilindros_embreagem': {'codigo': '0083', 'itens': []},
            'atuadores_embreagem': {'codigo': '0084', 'itens': ['ATUADOR EMBREAGE']},
            'homocineticas': {'codigo': '0068', 'itens': ['HOMOCINETICA', 'HOMOCINETICA DESLIZANTE', 'HOMOCINETICA RODA', 'JUNTA HOMOCINETICA', 'KIT JUNTA HOMOCINETICA']},
            'kit_coifa_homocinetica': {'codigo': '0092', 'itens': ['KIT COIFA HOMOCINETICA']},
            'trizetas': {'codigo': '0094', 'itens': ['TRIZETA']}
        }
    },
}



# Função para verificar o código do grupo e subgrupo de um item
def verificar_item(item):
    maior_item_subgrupo = ""
    for grupo, dados_grupo in grupos.items():
        for subgrupo, info_subgrupo in dados_grupo['subgrupos'].items():
            for item_subgrupo in info_subgrupo['itens']:
                termos_subgrupo = item_subgrupo.split()
                if all(termo in item for termo in termos_subgrupo) and len(item_subgrupo) > len(maior_item_subgrupo):
                    maior_item_subgrupo = item_subgrupo

    if maior_item_subgrupo:
        for grupo, dados_grupo in grupos.items():
            for subgrupo, info_subgrupo in dados_grupo['subgrupos'].items():
                if maior_item_subgrupo in info_subgrupo['itens']:
                    return dados_grupo['codigo'], info_subgrupo['codigo']

    return None, None  # Retorna None se nenhum subgrupo for encontrado no item

def corrigir_descricao(item): # Função de situação específica, o objetivo era acrescentar à descrição a informação de silencioso
        if "ESCAPAMENTO" and "TRAS" not in item:
            exit()
        pyautogui.click(x=374, y=623)
        time.sleep(0.5)
        pyautogui.press("space")
        time.sleep(0.5)
        pyautogui.typewrite("SILENCIOSO")
        time.sleep(0.5)

print("---------------------------------------------------------------------------------------")
print("Bem-vindo ao SectionDescripted, o programa que classifica grupos e subgrupos com base nas descrições de itens.") # Mensagem de boas vindas
option = "" # Variável que receberá a opção selecionada
while option != "4":
    print("Para começar, analise a opção desejada: \n 1 - Iniciar classificação \n 4 - Sair do programa") # Mensagem de seleção de opções
    option = input("Digite o número da opção desejada: ") # Input para seleção de opção
    if option == "1": # Se a opção for 1, inicia a operação
        print("_____________________________________________________________________________")
        print("Iniciando operação de classificação de itens em 5 segundos...") # Mensagem de início de operação
        time.sleep(1) # Intervalo de 1 segundo
        print("4 segundos...")
        time.sleep(1)
        print("3 segundos...")
        time.sleep(1)
        print("2 segundos...")
        time.sleep(1)
        print("1 segundo...")
        time.sleep(1)
        print("Iniciando operação...") # Mensagem de início de operação
        tempo_inicial = time.time() # Regra para definir o período de tempo
        contadorverificados = -1 # Variável que define a quantidade de itens verificados, começa com -1 pois o loop inicia adicionando 1 a contagem
        while(time.time() - tempo_inicial) < tempo_de_execucao: # Loop de execução enquanto o contador de tempo estiver ativo
            subgrupoconfirm = False # Define a seleção de código para subgrupo como indefinida até a possível necessidade
            contadorverificados += 1 # Adiciona uma verificação para o ciclo, aumentado o contador de itens verificados
            print(f"_______________________________")
            print(f"Número de verificações: {contadorverificados}") # Exibe a quantidade de verificações feitas
            screenshotwatcher = pyautogui.screenshot(region=(0, 16, 150, 45)) # Primeira variável de segurança, captura a tela no tamanho e posição definidos (x, y, largura e altura)
            screenshotwatcher = screenshotwatcher.convert("L") # Converte a captura para escala monocromática, permitindo uma melhor conversão de dados
            screenshotwatcher.save('screenshotwatcher.png') # Salva a captura com o nome do arquivo .png dado
            from PIL import Image # Importa a biblioteca PIL para interpretação de imagens
            screenshotwatcher = Image.open('screenshotwatcher.png') # A variável recebe o arquivo de imagem dado
            textwatcher = pytesseract.image_to_string(screenshotwatcher) # Cria uma variável que recebe dados strings transformados pelo pytesseract, o qual interpreta a imagem e localiza textos.
            watch = 'Livre' # Define uma palavra-chave que deve ser encontrada no conjunto de textos convertidos
            watch2 = 'campos' # Define uma segunda palavra-chave
            time.sleep(0.8) # Tempo de operação para segurança
            print(textwatcher)

            if watch in textwatcher or watch2 in textwatcher: # Se a palavra-chave 1 ou 2 estiverem no texto
                time.sleep(0.2) # Intervalo de segurança                
                screenshotdesc = pyautogui.screenshot(region=(280, 614, 458, 15)) # Captura a descrição do item
                screenshotdesc = screenshotdesc.convert("L")  # Converte para escala de cinza
                screenshotdesc.save('screenshotdesc.png') # Salva a imagem
                from PIL import Image
                screenshotdesc = Image.open('screenshotdesc.png') # Recebimento da imagem
                textdesc = pytesseract.image_to_string(screenshotdesc) # Converte para texto
                print(textdesc)
                grupoescolhido, subgrupo_escolhido = verificar_item(textdesc)

                # if "ESCAPAMENTO" and "TRAS" or "ESCAPAMENTO" and "TRASEIRO" in textdesc:
                #     corrigir_descricao(textdesc)
                #     time.sleep(0.5)
                #     pyautogui.doubleClick(x=1124, y=622)
                #     time.sleep(0.2)

                if grupoescolhido:
                    pyautogui.typewrite(grupoescolhido)
                    if subgrupo_escolhido:
                        time.sleep(0.2) # Intervalo de segurança
                        pyautogui.press("tab")
                        time.sleep(0.1) # Intervalo de segurança
                        pyautogui.typewrite(subgrupo_escolhido)
                        subgrupoconfirm = True
                                
                time.sleep(0.2) # Intervalo de segurança
                pyautogui.press("down")
                # time.sleep(0.2) # Caso haja necessidade de correção de itens do sistema quanto as suas descrições
                # pyautogui.press("down") # Pressiona a tecla de seta para baixo passando para o próximo item de modificação
                # time.sleep(0.2)
                # pyautogui.click(x=1344, y=79)
                if subgrupoconfirm == True:
                    time.sleep(0.2) # Intervalo de segurança
                    pyautogui.press("left")

                time.sleep(0.1) # Intervalo de segurança
            else:
                exit()
    elif option == "4": # Se a opção for 4, sai do programa
        print("Saindo do programa...") # Mensagem de saída
        break # Quebra o loop