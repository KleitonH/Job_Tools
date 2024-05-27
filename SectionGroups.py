
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
            'default': {'codigo': '0001', 'itens': []},
            'radiadores': {'codigo': '0008', 'itens': []},
            'bombas_agua': {'codigo': '0009', 'itens': []},
            'ventiladores': {'codigo': '0010', 'itens': []},

        }
    },
    'cabos': {
        'codigo': '0021',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'cabos_acelerador': {'codigo': '0011', 'itens': []},
            'cabos_embreagem': {'codigo': '0012', 'itens': []},
            'cabos_freio': {'codigo': '0013', 'itens': []},
            'cabos_capo': {'codigo': '0014', 'itens': []},
            'cabos_velocimetro': {'codigo': '0015', 'itens': []},
            'cabos_tampa_traseira': {'codigo': '0016', 'itens': []},
            'cabos_afogador': {'codigo': '0017', 'itens': []},
            'cabos_cambio': {'codigo': '0018', 'itens': []},
            'cabos_fechadura': {'codigo': '0019', 'itens': []},
            'cabos_trava_banco': {'codigo': '0020', 'itens': []},
        }
    },
    'carburacao': {
        'codigo': '0022',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'carburadores': {'codigo': '0021', 'itens': []},
            'componentes_carburadores': {'codigo': '0022', 'itens': []},
        }
    },
    'correias': {
        'codigo': '0023',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'correias_alternador': {'codigo': '0023', 'itens': []},
            'correias_comando': {'codigo': '0024', 'itens': []},
        }
    },
    'direcao': {
        'codigo': '0024',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'caixas_direcao': {'codigo': '0025', 'itens': []},
            'sistemas_direcao_mecanica': {'codigo': '0026', 'itens': []},
            'sistemas_direcao_hidraulica': {'codigo': '0027', 'itens': []},
        }
    },
    'filtros': {
        'codigo': '0025',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'filtros_ar': {'codigo': '0028', 'itens': []},
            'filtros_combustivel': {'codigo': '0029', 'itens': []},
            'filtros_de_oleo': {'codigo': '0030', 'itens': []},
        }
    },
    'freios': {
        'codigo': '0026',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'pastilhas_freio': {'codigo': '0031', 'itens': []},
            'discos_freio': {'codigo': '0032', 'itens': []},
            'tambores_freio': {'codigo': '0033', 'itens': []},
            'flexiveis_freio': {'codigo': '0034', 'itens': []},
            'pincas_freio': {'codigo': '0035', 'itens': []},
            'cilindros_roda_freio': {'codigo': '0036', 'itens': []},
            'cilindros_mestre_freio': {'codigo': '0037', 'itens': []},
            'lonas_freio': {'codigo': '0038', 'itens': []},
            'sapatas_freio': {'codigo': '0039', 'itens': []},
        }
    },    
    'juntas_retentores': {
        'codigo': '0027',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
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
            'default': {'codigo': '0001', 'itens': []},
            'bombas_oleo': {'codigo': '0049', 'itens': []},
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
        }
    },    
    'motor': {
        'codigo': '0030',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'cabecotes': {'codigo': '0055', 'itens': []},
            'virabrequins': {'codigo': '0056', 'itens': []},
            'carteres': {'codigo': '0057', 'itens': []},
        }
    },
    'reparos': {
        'codigo': '0031',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'kit_reparo_homocinetica': {'codigo': '0058', 'itens': []},
            'kit reparo_trambulador': {'codigo': '0059', 'itens': []},
            'kit_reparo_alavanca': {'codigo': '0060', 'itens': []},
        }
    },
    'rolamentos_tensores_polias': {
        'codigo': '0032',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'rolamentos_roda': {'codigo': '0061', 'itens': []},
            'rolamentos_motor': {'codigo': '0062', 'itens': []},
            'tensores': {'codigo': '0063', 'itens': []},
            'polias': {'codigo': '0064', 'itens': []},
        }
    },
    'suspensao': {
        'codigo': '0033',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'buchas': {'codigo': '0065', 'itens': []},
            'amortecedores': {'codigo': '0066', 'itens': []},
            'pivos': {'codigo': '0067', 'itens': []},
            'homocineticas': {'codigo': '0068', 'itens': []},
        }
    },
    'terminais': {
        'codigo': '0034',
        'subgrupos': {
            'default': {'codigo': '0001', 'itens': []},
            'terminais_barra_axial': {'codigo': '0069', 'itens': []},
            'terminais_cabo_comando': {'codigo': '0070', 'itens': []},
            'terminais_cabo_engate': {'codigo': '0071', 'itens': []},
            'terminais_direcao': {'codigo': '0072', 'itens': []},
            'terminais_suspensao': {'codigo': '0073', 'itens': []},
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

def corrigir_descricao(item):
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
            screenshotwatcher = pyautogui.screenshot(region=(0, 10, 150, 45)) # Primeira variável de segurança, captura a tela no tamanho e posição definidos (x, y, largura e altura)
            screenshotwatcher = screenshotwatcher.convert("L") # Converte a captura para escala monocromática, permitindo uma melhor conversão de dados
            screenshotwatcher.save('screenshotwatcher.png') # Salva a captura com o nome do arquivo .png dado
            from PIL import Image # Importa a biblioteca PIL para interpretação de imagens
            screenshotwatcher = Image.open('screenshotwatcher.png') # A variável recebe o arquivo de imagem dado
            textwatcher = pytesseract.image_to_string(screenshotwatcher) # Cria uma variável que recebe dados strings transformados pelo pytesseract, o qual interpreta a imagem e localiza textos.
            watch = 'Livre' # Define uma palavra-chave que deve ser encontrada no conjunto de textos convertidos
            watch2 = 'campos' # Define uma segunda palavra-chave
            time.sleep(0.8) # Tempo de operação para segurança

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