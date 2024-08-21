import pyautogui # Importação da biblioteca Pyautogui para controle do mouse e teclado 
import time # Importação da biblioteca time para intervalos de tempo 
import re # Importação da biblioteca re para modificação de strings
import pickle # Importação da biblioteca pickle para salvar arquivos
from pyscreeze import screenshot # Importação da biblioteca pyscreeze para captura de tela
from pytesseract import pytesseract # Importação da biblioteca pytesseract para conversão de imagens em strings
caminho_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # Caminho para o executável do pytesseract
pytesseract.tesseract_cmd = caminho_tesseract # Define o caminho para o pytesseract
keywords = ['BOMBA COMB', 'BOIA COMB', 'BOMBA INJECAO COMB']

print("---------------------------------------------------------------------------------------")
print("Bem-vindo ao SectionFixer, o programa que insere a seção com base na descrição do item.") # Mensagem de boas vindas
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
            screenshotwatcher = pyautogui.screenshot(region=(0, 20, 150, 15)) # Primeira variável de segurança, captura a tela no tamanho e posição definidos (x, y, largura e altura)
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
                
                for item in keywords:
                    if item in textdesc:
                        pyautogui.typewrite("5058")
                time.sleep(0.2) # Intervalo de segurança
                pyautogui.press("down")
                time.sleep(0.1) # Intervalo de segurança
            else:
                exit()
    elif option == "4": # Se a opção for 4, sai do programa
        print("Saindo do programa...") # Mensagem de saída
        break # Quebra o loop
