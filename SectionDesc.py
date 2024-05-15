
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
            'default':{'código': '0001', 'itens': ['VIDRO VIGIA', 'VIGIA']}}
    },
    'laterais': {
        'codigo': '0008',
        'subgrupos': {
            'ventarolas': {'codigo': '0004', 'itens': ['VENTAROLA', 'VIDRO LATERAL MOVEL', 'VIDRO VENTAROLA', 'VIDRO VENTAROLA OCULO']},
            'vidros_ocolus': {'codigo': '0005', 'itens': ['OCULO', 'OCULOS', 'VIDRO LATERAL DIANT', 'VIDRO LATERAL OCULO', 'VIDRO LATERAL TRAS OCULO', 'VIDRO FIXO DIANTEIRO']},
            'vidros_janela': {'codigo': '0006', 'itens': ['VIDRO JANELA', 'VIDRO LATERAL TRAS', 'VIDRO LATERAL', 'VIDRO LATERAL FIXO', 'VIDRO PORTA FIXO']},  
            'vidros_porta': {'codigo': '0007', 'itens': ['VIDRO PORTA']},

        }
    }
}


# Função para verificar o código do grupo e subgrupo de um item
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


print("---------------------------------------------------------------------------------------")
print("Bem-vindo ao SectionDescripted, o programa que classifica seções com base nas descrições de itens.") # Mensagem de boas vindas
option = "" # Variável que receberá a opção selecionada
while option != "4":
    print("Para começar, analise a opção desejada: \n 1 - Iniciar classificação \n 2 - Adicionar item regra \n 3 - Remover item de regra \n 4 - Sair do programa") # Mensagem de seleção de opções
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
            time.sleep(1) # Tempo de operação para segurança

            if watch in textwatcher or watch2 in textwatcher: # Se a palavra-chave 1 ou 2 estiverem no texto
                time.sleep(0.3) # Intervalo de segurança                
                screenshotdesc = pyautogui.screenshot(region=(280, 614, 458, 15)) # Captura a descrição do item
                screenshotdesc = screenshotdesc.convert("L")  # Converte para escala de cinza
                screenshotdesc.save('screenshotdesc.png') # Salva a imagem
                from PIL import Image
                screenshotdesc = Image.open('screenshotdesc.png') # Recebimento da imagem
                textdesc = pytesseract.image_to_string(screenshotdesc) # Converte para texto
                print(textdesc)
                grupoescolhido, subgrupo_escolhido = verificar_item(textdesc)

                if grupoescolhido:
                    pyautogui.typewrite(grupoescolhido)
                    if subgrupo_escolhido:
                        time.sleep(0.3) # Intervalo de segurança
                        pyautogui.press("tab")
                        time.sleep(0.1) # Intervalo de segurança
                        pyautogui.typewrite(subgrupo_escolhido)
                        subgrupoconfirm = True
                                
                time.sleep(0.3) # Intervalo de segurança
                pyautogui.press("down") # Pressiona a tecla de seta para baixo passando para o próximo item de modificação
                if subgrupoconfirm == True:
                    time.sleep(0.2) # Intervalo de segurança
                    pyautogui.press("left")

                time.sleep(0.3) # Intervalo de segurança
            else:
                exit()
    elif option == "2": # Se a opção for 2, inicia a operação de adição de item
        print("________________________________________________________________________________________")
        print("Você selecionou a opção de adicionar item regra.\n Primeiro, insira o nome do item.") # Mensagem de seleção de opção
        nome_item = input("Nome do item: ").upper() # Input para seleção de item a ser adicionado na lista de regras inserindo sempre com letras maiúsculas
        print("Agora, insira a qual seção ele pertence: \n 1 - Colorometria \n 2 - Tintas Vendas ") # Mensagem de seleção de opção
        secao_item = input("Seção do item: ") # Input para seleção de seção do item
        if int(secao_item) == 1: # Se a seção for 1, adiciona o item na lista de colorometria
            lista_colorometria.append(nome_item.upper)
            print("Item adicionado com sucesso.")
        elif int(secao_item) == 2: # Se a seção for 2, adiciona o item na lista de tintas vendas
            lista_tintasvendas.append(nome_item.upper)
            print("Item adicionado com sucesso.")
        else:
            print("Opção inválida.")

    elif option == "3": # Se a opção for 3, inicia a operação de remoção de item
        print("Você selecionou a opção de remover item regra.\n Primeiro, insira o nome do item.")
        nome_item = input("Nome do item: ").upper() # Input para seleção de item a ser removido da lista de regras buscando sempre com letras maiúsculas    
        print("Agora, insira a qual seção ele pertence: \n 1 - Colorometria \n 2 - Tintas Vendas ")
        secao_item = input("Seção do item: ")
        if secao_item == 1:
            lista_colorometria.remove(nome_item) # Remove o item da lista de colorometria
        elif secao_item == 2:
            lista_tintasvendas.remove(nome_item) # Remove o item da lista de tintas vendas
        else:
            print("Opção inválida.")
    
    elif option == "4": # Se a opção for 4, sai do programa
        print("Saindo do programa...") # Mensagem de saída
        break # Quebra o loop

# Salva os arquivos ao final do programa, encontra-se em fase de testes
with open('lista_colorometria.pkl', 'wb') as f: 
        pickle.dump(lista_colorometria, f)
with open('lista_tintasvendas.pkl', 'wb') as f:
        pickle.dump(lista_tintasvendas, f)
