
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
            'coxins': {'codigo': '0078', 'itens': ['COXIM SILENCIOSO', 'COXIM ESCAPAMENTO ']},

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
    'ar_condicionado': {
        'codigo': '0037',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['CONJUNTO EMBREAGEM COMPRESSOR']},
        }
    },
    'arrefecimento': {
        'codigo': '0020',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['BRUCUTU', 'BUCHA BOMBA ESGUICHO']},
            'buchas_arrefecimento': {'codigo': '0001', 'itens': ['BUCHA RADIADOR', 'BUCHA BOMBA ESGUICHO', 'BUCHA RESERVATORIO GAS PARTIDA']},
            'radiadores': {'codigo': '0008', 'itens': []},
            'bombas_agua': {'codigo': '0009', 'itens': ['BOMBA AGUA', 'BOMBA D.HIDR', 'BOMBA DAGUA']},
        }
    },
    'cabos': {
        'codigo': '0021',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['CABO ACIONADOR PORTINHOLA', 'CABO AR FORCADO', 'CABO PORTA CORRER', 'CABO PORTA MALA', 'CABO PORTINHOLA', 'CABO TEMPERATURA']},
            'cabos_acelerador': {'codigo': '0011', 'itens': ['CABO ACEL', 'CABO ACELERADO', 'CABO DE ACELERADOR', 'CABO PARADA MOTOR']},
            'cabos_embreagem': {'codigo': '0012', 'itens': ['CABO EMB', 'CABO EMBR', 'CABO EMBREAGE', 'CABO FLEX EMBR', 'CABO TRANSMISSAO', 'FLEXIVEL EMBREAGEM']},
            'cabos_freio': {'codigo': '0013', 'itens': ['CABO DE FREIO', 'CABO FREIO', 'CABO LIBERACAO FREIO']},
            'cabos_capo': {'codigo': '0014', 'itens': ['CABO CAPO', 'CABO PUXADOR CAPO']},
            'cabos_velocimetro': {'codigo': '0015', 'itens': ['CABO DE VELOCIMETRO', 'CABO TACOGRAFO', 'CABO TACOMETRO', 'CABO VELOCIMETRO', 'CABO VELOC']},
            'cabos_tampa_traseira': {'codigo': '0016', 'itens': ['CABO LIMITADOR DA TAMPA TRAS', 'CABO PUXADOR TAMPA', 'CABO TAMPA TRAS']},
            'cabos_afogador': {'codigo': '0017', 'itens': ['CABO AFOGADOR', 'CABO ESTRANGULADOR']},
            'cabos_cambio': {'codigo': '0018', 'itens': ['CABO CAMBIO', 'CABO COMANDO', 'CABO COMANDO MARCHA', 'CABO ENGATE COMANDO', 'CABO ENGATE', 'CABO ENGATE MARCHA', 'CABO MARCHA', 'CABO REDUZIDA', 'CABO SELECAO CAMBIO', 'CABO SELECAO MARCHA', 'CABO SELECAO COMANDO']},
            'cabos_fechadura': {'codigo': '0019', 'itens': []},
            'cabos_trava_banco': {'codigo': '0020', 'itens': ['CABO ENCOSTO BANCO', 'CABO REGULAGEM BANCO', 'CABO TRAVA BANCO', 'CABO BANCO']},
        }
    },
    'carburacao': {
        'codigo': '0022',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['AVANCO DISTRIBUIDOR', ' BOIA CARBURADOR', 'AFOGADOR', 'AVANCO DO DISTRIBUIDOR',   'CONJUNTO VALVULA BOIA CARBURADOR']},
            'carburadores': {'codigo': '0021', 'itens': ['CARBURADOR']},
            'componentes_carburadores': {'codigo': '0022', 'itens': ["AGULHA CARBURADOR", 'BASE CARB', 'BASE CARBURADOR', 'BASE VEDACAO CARB', 'BENGALA CARB', 'BENGALA INJETOR CARBURAD', 'BORBOLETA CARBURADOR', 'ESGUICHO CARB']},
            'diafragmas_carburadores': {'codigo': '0122', 'itens': ['DIAFRAGMA CARBURADO', 'DIAFRAGMA ACELERA']},
        }
    },
    'carcacas_tubos': {
        'codigo': '0035',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'antichama': {'codigo': '0105', 'itens': ['ANTICHAMA', 'ANTI CHAMA', 'DEFLETOR ANTICHAMA']},
            'cavaletes': {'codigo': '0106', 'itens': ['CAVALETE', 'FLANGE CAVALETE AGUA']},
            'tubos': {'codigo': '0107', 'itens': []},
            'conectores': {'codigo': '0108', 'itens': ['CONECTOR LIGACAO MANGUEIRA', 'CONECTOR MANGUEIRA', 'CONECTOR 3/8', 'CONECTOR AGUA', 'CONECTOR CAMB', 'CONECTOR DUPLO UNIVE', 'CONECTOR GASOLINA', 'CONECTOR QUICK', 'CONECTOR SELADO', 'CONECTOR UNIVERSAL', 'CONEXAO RESERVATORIO', 'CONEXAO AGUA', 'CONEXAO CARC VALV', 'CONEXAO COM REGISTRO', 'CONEXAO DUPLA MANG', 'CONEXAO ESGUICHO', 'CONEXAO INF', 'CONEXAO MANG', 'CONEXAO RAPIDA', 'CONEXAO RADIADOR', 'CONEXAO Y DUPLO', 'EMENDA CONEXAO']},
            'cotovelos': {'codigo': '0109', 'itens': ['CONEXAO (COTOVELO)', 'COTOVELO', 'COTOVELO CAVALETE']},
            'capas_correias': {'codigo': '0110', 'itens': ['CAPA CORREIA']},
            'carcacas': {'codigo': '0111', 'itens': ['CARCACA', 'CAIXA FILTRO AR', 'CAIXA FILTRO AR CARB', 'CAMARA VALVULA TERMOS']},
            'flanges': {'codigo': '0131', 'itens': ['FLANGE  MOTOR', 'FLANGE MANG CABECOTE', 'FLANGE AGUA', 'FLANGE BOMBA DAGUA', 'FLANGE CONEXAO', 'FLANGE ROLAMENTO CAIXA CAMBIO', 'FLANGE SEMI EIXO', 'FLANGE TERMOSTATO', 'FLAGE TUBO MANGUEIRA', 'FLANGE VALV TERMOST']},
            'kits_carcacas': {'codigo': '0112', 'itens': []},
        }
    },
    'combustivel': {
        'codigo': '0034',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ["ADAPTADOR TAMPA TANQUE", 'BORRACHA FLANGE COM', 'CANO COMBUSTIVEL']},
            'flanges_combustivel': {'codigo': '0089', 'itens': ["ADAPTADOR FLANGE CAIXA", "FLANGE", 'FLANGE COMBUSTIVEL', 'FLANGE MODULO COMBUSTIVEL']},
            'boia_combustivel': {'codigo': '0098', 'itens': ['BOIA COMBUSTIVEL',"BOIA TANQUE", 'BOIA TANQUE']},
        }
    },
    'correias': {
        'codigo': '0023',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['CORREIA VENTOINHA']},
            'correias_dentadas': {'codigo': '0023', 'itens': ['CORREIA COMANDO', 'CORREIA DENTADA']},
            'correias_polyv': {'codigo': '0024', 'itens': ['CORREIA ALT', 'CORREIA ALTERNADOR', 'CORREIA AR COND', 'CORREIA MICRO V', 'CORREIA POLY V', 'CORREIA MULTI V']},
            'correias_em_v': {'codigo': '0119', 'itens': ['CORREIA EM V', 'CORREIA EM V AR COND', 'CORREIA EM V ALT']},
        }
    },
    'direcao': {
        'codigo': '0024',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ["ADAPTADOR VOLANTE", 'BORRACHA FIXADORA CAIXA DIRE', 'BORRACHA FIXACAO SETOR']},
            'buchas_direcao': {'codigo': '0102', 'itens': ["BUCHA COLUNA DIRECAO", 'BUCHA SETOR DIRECAO', 'BUCHA BRACO', 'BUCHA INF BRACO', 'BUCHA CAIXA DIRECAO', 'BUCHA COLUNA DIRECAO', 'BUCHA CAIXA DIRECAO', 'BUCHA FIX SETOR DIRECAO', 'BUCHA NUCLEO ARTIC', 'BUCHA TERMINAL DIRECAO']},
            'bombas_direcao': {'codigo': '0099', 'itens': ['BOMBA DIRECAO HIDRAULICA', 'BOMBA HIDRAULICA']},
            'caixas_direcao': {'codigo': '0025', 'itens': []},
            'setor_direcao': {'codigo': '0026', 'itens': []},
            'barras_axiais': {'codigo': '0027', 'itens': ['BARRA AXIAL', 'BARRA BRACO TENSOR', 'BARRA DIRECAO', 'BARRA LATERAL', 'BRACO AUXILIAR', 'BRACO DIANT INF', 'BRACO OSCILANT', 'BRACO PITMAN', 'BRACO SETOR', 'BRACO SUSP', 'BRACO TENSOR']},
            'pivos': {'codigo': '0067', 'itens': ['PIVO', 'PIVO INFERIOR', 'PIVO', 'PIVO SUSP']},
            'terminal_direcao': {'codigo': '0093', 'itens': ['TERMINAL DIR', 'TERMINAL DIRECAO', 'TERMINAL SUSPENSAO']},
            'colunas_direcao': {'codigo': '0124', 'itens': ['COLUNA DIR', 'COLUNA DIRECAO']},
            'cubos_direcao': {'codigo': '0126', 'itens': ['CUBO DIRECAO', 'CUBO VOLANTE']},
        }
    },
    'filtros': {
        'codigo': '0025',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['FILTRO DAGUA']},
            'filtros_ar': {'codigo': '0028', 'itens': ['FILTRO AR']},
            'filtros_combustivel': {'codigo': '0029', 'itens': ['FILTRO BOMB COMB', 'FILTRO COMBUSTIVEL', 'FILTRO DIESEL']},
            'filtros_de_oleo': {'codigo': '0030', 'itens': ['FILTRO OLEO', 'FILTRO DE OLEO', 'FILTRO RETORNO']},
            'filtros_de_ar_condicionado': {'codigo': '0074', 'itens': ['FILTRO AR CONDICIONADO']},
            'filtros_de_cabine': {'codigo': '0075', 'itens': []},
            'filtros_cambio': {'codigo': '0130', 'itens': ['FILTRO CAIXA AUTOMATICA', 'FILTRO CAMB', 'FILTRO CAMBIO', ]}
        }
    },
    'freios': {
        'codigo': '0026',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ["ACIONADOR FREIO", "ACIONADOR/GATILHO FREIO"]},
            'pastilhas_freio': {'codigo': '0031', 'itens': ['PASTILHA FREIO']},
            'coifas_freio': {'codigo': '0128', 'itens': ['COIFA FREIO']},
            'canos_freio': {'codigo': '0116', 'itens': ['CANO DE FREIO', 'CANO FREIO']},
            'discos_freio': {'codigo': '0032', 'itens': ['DISCO FREIO', 'DISCO FREIO DIANT', "DISCO FREIO TRAS"]},
            'tambores_freio': {'codigo': '0033', 'itens': []},
            'flexiveis_freio': {'codigo': '0034', 'itens': ['BIFURCACAO AO FLEXIVEL', 'FLEXIVEL', 'FLEXIVEL FREIO', 'FLEX DIANT', 'FLEXIVEL TRAS']},
            'pincas_freio': {'codigo': '0035', 'itens': []},
            'cilindros_roda_freio': {'codigo': '0036', 'itens': ['CILINDRO RODA']},
            'cilindros_mestre_freio': {'codigo': '0037', 'itens': ['CILINDRO MESTRE', 'CILINDRO MESTRE FREIO']},
            'lonas_freio': {'codigo': '0038', 'itens': []},
            'sapatas_freio': {'codigo': '0039', 'itens': []},
            'servofreios': {'codigo': '0087', 'itens': ["ACIONADOR FREIO", "ALAVANCA ACIONAMENTO FREIO", "GATILHO FREIO"]},
        }
    },    
    'juntas_retentores': {
        'codigo': '0027',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'aneis': {'codigo': '0091', 'itens': ['ANEIS PISTAO', 'ANEL PISTAO', 'ANEL BUJAO', 'ANEL AJUSTE ROLAMENTO', 'ANEL ALAVANCA', 'ANEL AMORTECEDOR', 'ANEL ANTI RUIDO', 'ANEL BOCAL TANQUE', 'ANEL BORRACHA', 'ANEL BRACO SUSP', 'ANEL CARCACA', 'ANEL CEBOLAO', 'ANEL CILINDRO', 'ANEL COLETOR', 'ANEL VEDACAO', 'ANEL EIXO TRAS', 'ANEL IMPULSOR ARV', 'ANEL INFERIOR CARRO', 'ANEL INTERMEDIARIO', 'ANEL JUNTA', 'ANEL MALHA ACO', 'ANEL MOTOR', 'ANEL RADIADOR', 'ANEL RODA', 'ANEL SILENCIOSO', 'ANEL SINCRONIZ', 'ANEL TAMPA VALV', 'ANEL TIRANTE SUSP', 'ANEL TRASEIRO', 'ANEL TRAVA', 'ANEL VEDACAO', 'ANEL VEDADOR', 'ANEL JUNTA DISTRI', 'ANEL TOMADA FORCA', 'BORRACHA BOCAL ']},
            'diafragmas_tampa': {'codigo': '0127', 'itens': ['DIAFRAGMA TAMPA VALVU']},
            'juntas_cabecote': {'codigo': '0040', 'itens': []},
            'juntas_coletor': {'codigo': '0041', 'itens': []},
            'juntas_carter': {'codigo': '0042', 'itens': []},
            'juntas_tampa_valvula': {'codigo': '0043', 'itens': []},
            'juntas_tampa_distribuidor': {'codigo': '0044', 'itens': []}, 
            'retentores_eixo': {'codigo': '0045', 'itens': []},
            'retentores_virabrequim': {'codigo': '0046', 'itens': []},
            'retentores_comando_valvula': {'codigo': '0047', 'itens': []},
            'retentores_caixa_cambio': {'codigo': '0048', 'itens': []},
            'vedacao': {'codigo': '0048', 'itens': ["BUCHA VEDACAO"]},
        }
    },
    'lubrificacao': {
        'codigo': '0028',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['ALONGADOR VARETA']},
            'bombas_oleo': {'codigo': '0049', 'itens': ['BOMBA OLEO', 'CORPO BOMBA OLEO']},
            'engrenagem': {'codigo': '0129', 'itens': ['ENGRENAGEM BOMBA OLEO']},
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
            'mangueiras_ar_motor': {'codigo': '0085', 'itens': ['DUTO FILTRO AR', 'MANGUEIRA FILTRO AR', 'DUTO AR ADMISSAO']},
            'mangueiras_oleo': {'codigo': '0086', 'itens': []},
            'bocais': {'codigo': '0097', 'itens': ['BOCAL TANQUE']},
        }
    },    
    'motor': {
        'codigo': '0030',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['BUCHA ARRANQUE', 'BALANCIM', 'DEFLETOR CARTER', 'CAPA TUCHO']},
            'cabecotes': {'codigo': '0055', 'itens': ['CABECOTE', 'CABECOTE MOTOR']},
            'comandos': {'codigo': '0118', 'itens': ['COMANDO', 'EIXO COMANDO']},
            'coxins': {'codigo': '0078', 'itens': ['COXIM MOTOR', 'COXIM DIANT MOTOR', 'COXIM CENTRAL MOTOR']},
            'engrenagem': {'codigo': '0129', 'itens': ['ENGRENAGEM VIRABREQUIM', 'ENGRENAGEM CORPO BORBOLETA']},
            'virabrequins': {'codigo': '0056', 'itens': []},
            'carteres': {'codigo': '0057', 'itens': ['CARTER']},
            'bronzinas': {'codigo': '0100', 'itens': ['BRONZINA','BRONZINA DE BIEL', 'BRONZINA MANCAL']},
            'tuchos': {'codigo': '0103', 'itens': ['BUCHA POSTERIOR ARVORE']},
            'parafuso_cabecote': {'codigo': '0105', 'itens': ['BUCHA PRISIONEIRO CABECOTE','PARAFUSO CABECOTE', 'PARAFUSO PRISIONEIRO']},
            'corpo_borboleta': {'codigo': '0123', 'itens': ['CORPO BORBOLETA']}
        }
    },
    'reparos': {
        'codigo': '0031',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ["ACOPLAMENTO COLETOR ADMISSAO", "ACOPLAMENTO DIRECAO", "ACOPLAMENTO VISOCOSO", "ADAPTADOR COLETOR ADMISSAO", "REPARO COLETOR ADMISSAO", "REPARO DIRECAO", "ADAPTADOR MOTOR MAQ VIDRO", 'BUCHA RETORNO PEDAL']},
            'kit_reparo_homocinetica': {'codigo': '0058', 'itens': []},
            'kit reparo_cambio': {'codigo': '0059', 'itens': ['ACOPLAMENTO HASTE TRAMBULADOR', 'ACOPLAMENTO HASTE LIGACAO',"ACOPLAMENTO VARAO CAMBIO", 'ARTICULACAO CABO ENGATE', 'ARTICULADOR CABO ENGATE', "REPARO VARAO CAMBIO", 'BUCHA ALAVANCA CAMBIO', 'BUCHA REPARO ALAVANCA', 'BORRACHA/REPARO TRAMBULADOR', 'CACHORRINHO REPARO ANEIS', 'BUCHA CABO MARCHA', 'BUCHA PEDAL EMBREAGEM', 'BUCHA PRETA TRAMBULADOR', 'BUCHA SELETOR MARCHA', 'BUCHA TRAMBULADOR', 'BUCHA VARAO CAMBIO', 'CONJUNTO KIT REPARO PEDAL', 'CATRACA ACIONADOR EMBREAGEM', 'CONJUNTO AGULHA MOLA MARCHA', 'COROA VELOCIMETRO']},
            'kit_reparo_pincas': {'codigo': '0077', 'itens': ['BUCHA PINCA']},
            'kit_reparo_setor': {'codigo': '0088', 'itens': ['ACOPLAMENTO SETOR']},
            'alavancas': {'codigo': '0090', 'itens': ['ALAVANCA ACIONADORA', 'ALAVANCA CAMBIO', 'ALAVANCA EMB', 'ALAVANCA EMBREAGEM', 'ALAVANCA ENGATE', 'ALAVANCA ENGRENAGEM', 'ALAVANCA FREIO MAO', 'ALAVANCA FREIO TRAS', 'ALAVANCA INIBIDORA', 'ALAVANCA LIGACAO', 'ALAVANCA MARCHA', 'ALAVANCA PATIM', 'ALAVANCA REG', 'ALAVANCA REGULADO', 'ALAVANCA SELETORA', 'ALAVANCA TRAMBULADOR', 'BUCHA LATERAL ALAVANCA']},
        }
    },
    'rolamentos_tensores_polias': {
        'codigo': '0032',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['ROLAMENTO CAMBIO', 'BUCHA AGULHA', 'BUCHA AGULIA']},
            'rolamentos_roda': {'codigo': '0061', 'itens': ['BUCHA ROLAMENTO DIRECAO']},
            'rolamentos_motor': {'codigo': '0062', 'itens': []},
            'tensores': {'codigo': '0063', 'itens': []},
            'polias': {'codigo': '0064', 'itens': []},
        }
    },
    'suspensao': {
        'codigo': '0033',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['EMBUCHAMENTO', 'CALCO AJUSTE', 'CALCO AMORT', 'CALCO BATENT']},
            'buchas_suspensao': {'codigo': '0065', 'itens': ['BARRA TORCAO', 'BUCHA BAND SUSP', 'BUCHA BARRA ESTAB', 'BUCHA BANDEJA DIANT', 'BUCHA AGREGADO', 'BUCHA ALGEMA BARRA', 'BUCHA ALT SUP', 'BUCHA ALTERNADOR', 'BUCHA AMORT', 'BUCHA AMORT DIANT', 'BUCHA AMORTEC', 'BUCHA AMORTECEDOR', 'BUCHA AR COND', 'BUCHA ARTIC EIXO', 'BUCHA ARTICULACAO', 'BUCHA BAND', 'BUCHA BANDEJA', 'BUCHA BARR ESTAB', 'BUCHA BARRA ESTAB', 'BUCHA BARRA LIGACAO', 'BUCHA BARRA TENS SUSP', 'BUCHA BARRA TORCAO' 'BUCHA BIELA', 'BUCHA CALCO TRAVESSA', 'BUCHA CENTRAL BANDEJA', 'BUCHA COXIM', 'BUCHA EIXO', "BUCHA ESTAB", 'BUCHA ESTABILIZADORA', 'BUCHA FEIXE MOLA', 'BUCHA MANGA EIXO', 'BUCHA HAST BAND', 'BUCHA INF AMOR', 'BUCHA INFERIOR BANDE', 'BUCHA INFERIOR AMORT', 'BUCHA INFERIOR JUMELO', 'BUCHA JUMELO', 'BUCHA MAIOR', 'BUCHA MENOR', 'BUCHA MOLA', 'BUCHA OVAL EIXO', 'BUCHA TRAS BAND', 'BUCHA PONTA BANDEJA', 'BUCHA SUP ALGEMA', 'BUCHA SUP AMOR', 'BUCHA SUPERIOR BAND', 'BUCHA SUPERIOR JUMELO', 'BUCHA SUSP', 'BUCHA SUSPEN', 'BUCHA SUSPENSAO', 'BUCHA TENSO', 'BUCHA TENSOR SUS', 'BUCHA TERMINAL EIXO', 'BUCHA TIRANTE', 'BUCHA TARS BAND', 'BUCHA TRAS BRAC', 'BUCHA TRAS EIXO', 'BUCHA TRAS FEIXE MOLA', 'BUCHA TRAS SUSP', 'BUCHA TRAS BAND', 'BUCHA TRASEIRA BANDEJA', 'BUCHA TRAV EIXO', 'BUCHA QUADRO', 'BUCHA SUPERIOR QUADRO', 'BUCHA TRAS QUADRO', 'CAPA AMORTECE DIAN', 'FLUTOBLOC']},
            'amortecedores': {'codigo': '0066', 'itens': ["AMORT DIANT", "AMORTECEDOR DIANT", "AMORTECEDOR REMAN", "AMORTECEDOR TRAS", "AMORTECEDOR TRASEIRO", 'COXIM COM ROLAMENTO AMORT']},
            'coifas': {'codigo': '0128', 'itens': ['COIFA AMORT']},
            'coxins': {'codigo': '0078', 'itens': ['CALCO AMORTECE', 'COXIM AMORT', 'COXIM AMORTECEDOR', 'COXIM BR OSCI', 'COXIM BRACO OSCIL', ' COXIM CABINE', 'COXIM LIMITADOR TORCAO', 'COXIM ESTABILIZADOR', 'COXIM SUSP', 'CAPA SUSPENSAO', 'COXIM CABINE']},
            'bieletas': {'codigo': '0079', 'itens': ['BIELETA', 'BIELETA BARRA ESTAB', 'BIELETA BARRA ESTABILIZADORA', 'BIELETA DIANT', 'BIELETA ESTAB', 'BIELETA ESTABILIZADORA', 'BIELETA SUSP', 'BIELETA SUSPENSAO', 'BIELETA TRAS']},
            'bandejas': {'codigo': '0080', 'itens': ['BAND SUSP SUP', 'BANDEJA', "BANDEJA DIANT", 'BANDEJA DIANTEIRA', 'BANDEJA INFERIOR', 'BANDEJA SUS', 'BANDEJA SUSPENSAO']},
            'kit_amortecedor': {'codigo': '0081', 'itens': ['BATENTE AMORT', 'BATENTE AMORTECEDOR', 'BATENTE BANDEJA', 'BATENTE BRACO', 'BATENTE DE MOLA', 'BATENTE DIANT', 'BATENTE EIXO', 'BATENTE FEIXE MOLA', 'BATENTE INF', 'BATENTE INFERIOR', 'BATENTE MOLA', 'BATENTE SUP', 'BATENTE SUSP', 'BATENTE COIFA', 'BOLACHA SANTA FE', 'BORRACHA BARRA ESTA', 'BORRACHA HASTE VALVULA', 'BORRACHA LIGACAO BARRA EST']},
            'molas': {'codigo': '0115', 'itens': ['MOLA SUSPENSAO', 'FEIXE MOLA']},
            'pratos': {'codigo': '0104', 'itens': ['ASSENTO SUPERIOR MOLA']},
            'barra_estabilizadora': {'codigo': '0095', 'itens': ['BARRA ESTABILIZADORA']},
            'kit_barra_estabilizadora': {'codigo': '0096', 'itens': []},
            'cubos_roda': {'codigo': '0076', 'itens': ['CUBO RODA', 'CUBO RODA DIANTEIR', 'CUBO RODA TRASEIR']},
        }
    },
    'transmissao': {
        'codigo': '0036',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': ['BALENCEIRO EMBREAGEM', 'BARRA DE LIGACAO', 'CAIXA SATELITE', 'CANO EMBREAGEM', 'CAPA ROLAMENTO CARDAN', 'CANO GUIA CABO EMB', ]},
            'buchas_transmissao': {'codigo': '0101', 'itens': ['BUCHA CAMBIO', 'BUCHA OLEO', 'BUCHA GARFO EMBR', 'BUCHA ADAPTADOR COMANDO EMBREAG', 'BUCHA LATERAL CAMBIO', 'BUCHA REFIL SUPORTE CAMBIO AUTO']},
            'embreagens': {'codigo': '0082', 'itens': ['DISCO EMBREAGEM', 'EMBREAGEM']},
            'engrenagem': {'codigo': '0129', 'itens': ['ENGRENAGEM MARCHA', 'ENGRENAGEM PLANETARIA']},
            'coifas': {'codigo': '0128', 'itens': ['COIFA CAMBIO', 'COIFA GUARDA PO', 'COIFA HASTE SELETORA', 'COIFA HOMOCINETICA', 'COIFA LADO CAMBIO', 'COIFA LADO RODA', 'COIFA RODA', 'COIFA SETOR']},
            'cilindros_embreagem': {'codigo': '0083', 'itens': ['CILINDRO EMBRAGEM', 'CILINDRO EMB', 'CILINDRO AUXILIAR EMB', 'CILINDRO ESCRAVO']},
            'cilindros_mestre_embreagem': {'codigo': '0117', 'itens': ['CILINDRO MESTRE EMBREAGEM', 'CILINDRO MESTRE EMB']},
            'atuadores_embreagem': {'codigo': '0084', 'itens': ['ATUADOR EMBREAGE']},
            'homocineticas': {'codigo': '0068', 'itens': ['HOMOCINETICA', 'HOMOCINETICA DESLIZANTE', 'HOMOCINETICA RODA', 'JUNTA HOMOCINETICA', 'KIT JUNTA HOMOCINETICA']},
            'kit_coifa_homocinetica': {'codigo': '0092', 'itens': ['KIT COIFA HOMOCINETICA']},
            'trizetas': {'codigo': '0094', 'itens': ['TRIZETA']},
            'cruzeta': {'codigo': '0125', 'itens': ['CRUZETA']},
            'coxins': {'codigo': '0078', 'itens': ['COXIM CAMBIO', 'COXIM TRANSMISSAO', 'COXIM LADO CAMBIO', 'COXIM RETO CAMBIO', 'COXIM AMORTECEDOR CAMBIO', 'COXIM CARDAN', 'COXIM EXT EIXO']}
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
while option != "2":
    print("Para começar, analise a opção desejada: \n 1 - Iniciar classificação \n 2 - Sair do programa") # Mensagem de seleção de opções
    option = input("Digite o número da opção desejada: ") 
    if option == "1":
        print("_____________________________________________________________________________")
        print("Iniciando operação de classificação de itens em 5 segundos...") 
        time.sleep(1) #
        print("4 segundos...")
        time.sleep(1)
        print("3 segundos...")
        time.sleep(1)
        print("2 segundos...")
        time.sleep(1)
        print("1 segundo...")
        time.sleep(1)
        print("Iniciando operação...") 
        tempo_inicial = time.time() # Regra para definir o período de tempo
        contadorverificados = -1 
        while(time.time() - tempo_inicial) < tempo_de_execucao: # Loop de execução enquanto o contador de tempo estiver ativo
            subgrupoconfirm = False # Define a seleção de código para subgrupo como indefinida até a possível necessidade
            contadorverificados += 1
            print(f"_______________________________")
            print(f"Número de verificações: {contadorverificados}") 
            screenshotwatcher = pyautogui.screenshot(region=(0, 24, 150, 20)) # Primeira variável de segurança, captura a tela no tamanho e posição definidos (x, y, largura e altura)
            screenshotwatcher = screenshotwatcher.convert("L") # Converte a captura para escala monocromática, permitindo uma melhor conversão de dados
            screenshotwatcher.save('screenshotwatcher.png') 
            from PIL import Image # Importa a biblioteca PIL para interpretação de imagens
            screenshotwatcher = Image.open('screenshotwatcher.png')
            textwatcher = pytesseract.image_to_string(screenshotwatcher) # Cria uma variável que recebe dados strings transformados pelo pytesseract, o qual interpreta a imagem e localiza textos.
            watch = 'Livre' 
            watch2 = 'campos' 
            time.sleep(0.8) 
            print(textwatcher)

            if watch in textwatcher or watch2 in textwatcher: 
                time.sleep(0.2)              
                screenshotdesc = pyautogui.screenshot(region=(280, 614, 458, 15)) # Captura a descrição do item
                screenshotdesc = screenshotdesc.convert("L")
                screenshotdesc.save('screenshotdesc.png')
                from PIL import Image
                screenshotdesc = Image.open('screenshotdesc.png')
                textdesc = pytesseract.image_to_string(screenshotdesc) 
                print(textdesc)
                grupoescolhido, subgrupo_escolhido = verificar_item(textdesc)

                # if "ESCAPAMENTO" and "TRAS" or "ESCAPAMENTO" and "TRASEIRO" in textdesc: # Complemento de situação específica
                #     corrigir_descricao(textdesc)
                #     time.sleep(0.5)
                #     pyautogui.doubleClick(x=1124, y=622)
                #     time.sleep(0.2)

                if grupoescolhido:
                    pyautogui.typewrite(grupoescolhido)
                    if subgrupo_escolhido:
                        time.sleep(0.2) 
                        pyautogui.press("tab")
                        time.sleep(0.1)
                        pyautogui.typewrite(subgrupo_escolhido)
                        subgrupoconfirm = True
                                
                time.sleep(0.2) 
                pyautogui.press("down")
                # time.sleep(0.2) # Caso haja necessidade de correção de itens do sistema quanto as suas descrições
                # pyautogui.press("down")
                # time.sleep(0.2)
                # pyautogui.click(x=1344, y=79)
                if subgrupoconfirm == True: # Uso do booleano para quando o subgrupo for alterado
                    time.sleep(0.2)
                    pyautogui.press("left")
                time.sleep(0.1)
            else:
                exit()
    elif option == "2": # Se a opção for 4, sai do programa
        print("Saindo do programa...")
        break