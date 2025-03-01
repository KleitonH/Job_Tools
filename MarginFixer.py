import pandas as pd
import pyautogui
import time
import re # Importação da biblioteca re para modificação de strings
import Breaker
from pytesseract import pytesseract # Importação da biblioteca pytesseract para conversão de imagens em strings
caminho_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # Caminho para o executável do pytesseract
pytesseract.tesseract_cmd = caminho_tesseract # Define o caminho para o pytesseract

monitor_thread = Breaker.iniciar_monitoramento()

# Função para executar o script PyAutoGUI (essa função pode ser personalizada)
def executar_script_pyautogui(codigo_interno, codigo_fabricante, situacao):
    screenshotwatcher = pyautogui.screenshot(region=(4, 40, 222, 25)) # Primeira variável de segurança, captura a tela no tamanho e posição definidos (x, y, largura e altura)
    screenshotwatcher = screenshotwatcher.convert("L") # Converte a captura para escala monocromática, permitindo uma melhor conversão de dados
    screenshotwatcher.save('./screenshots/screenshotwatcher.png') # Salva a captura com o nome do arquivo .png dado
    from PIL import Image # Importa a biblioteca PIL para interpretação de imagens
    screenshotwatcher = Image.open('./screenshots/screenshotwatcher.png') # A variável recebe o arquivo de imagem dado
    textwatcher = pytesseract.image_to_string(screenshotwatcher) # Cria uma variável que recebe dados strings transformados pelo pytesseract, o qual interpreta a imagem e localiza textos.
    watch = 'Data do balanco' # Define uma palavra-chave que deve ser encontrada no conjunto de textos convertidos

    if watch in textwatcher and Breaker.verificar_interrupcao():
        if situacao == "Negativo":
            # Exemplo: Simular uma ação do PyAutoGUI para situação "Negativo"
            pyautogui.alert(f"Item {codigo_fabricante}: Situação é 'Negativo'")
        elif situacao == "Exorbitante":
            pyautogui.typewrite(str(codigo_interno))
            pyautogui.press("enter")
            time.sleep(1.4)

            screenshotsimilarwatcher = pyautogui.screenshot(region=(23, 24, 109, 14)) # Primeira variável de segurança, captura a tela no tamanho e posição definidos (x, y, largura e altura)
            screenshotsimilarwatcher = screenshotsimilarwatcher.convert("L") # Converte a captura para escala monocromática, permitindo uma melhor conversão de dados
            screenshotsimilarwatcher.save('./screenshots/screenshotsimilarwatcher.png') # Salva a captura com o nome do arquivo .png dado
            from PIL import Image # Importa a biblioteca PIL para interpretação de imagens
            screenshotsimilarwatcher = Image.open('./screenshots/screenshotsimilarwatcher.png') # A variável recebe o arquivo de imagem dado
            screenshotsimilarwatcher = pytesseract.image_to_string(screenshotsimilarwatcher) # Cria uma variável que recebe dados strings transformados pelo pytesseract, o qual interpreta a imagem e localiza textos.
            print(screenshotsimilarwatcher)
            time.sleep(1.8)

            def screenshotSimilar():
                screenshotquantidade = pyautogui.screenshot(region=(561, 106, 70, 19)) # Primeira variável de segurança, captura a tela no tamanho e posição definidos (x, y, largura e altura)
                screenshotquantidade = screenshotquantidade.convert("L") # Converte a captura para escala monocromática, permitindo uma melhor conversão de dados
                screenshotquantidade.save('./screenshots/screenshotquantidade.png') # Salva a captura com o nome do arquivo .png dado
                from PIL import Image # Importa a biblioteca PIL para interpretação de imagens
                screenshotquantidade = Image.open('./screenshots/screenshotquantidade.png') # A variável recebe o arquivo de imagem dado
                quantidade = pytesseract.image_to_string(screenshotquantidade) # Cria uma variável que recebe dados strings transformados pelo pytesseract, o qual interpreta a imagem e localiza textos.
            
                screenshotvalorvenda = pyautogui.screenshot(region=(636, 107, 75, 18)) # Primeira variável de segurança, captura a tela no tamanho e posição definidos (x, y, largura e altura)
                screenshotvalorvenda = screenshotvalorvenda.convert("L") # Converte a captura para escala monocromática, permitindo uma melhor conversão de dados
                screenshotvalorvenda.save('./screenshots/screenshotvalorvenda.png') # Salva a captura com o nome do arquivo .png dado
                from PIL import Image # Importa a biblioteca PIL para interpretação de imagens
                screenshotvalorvenda = Image.open('./screenshots/screenshotvalorvenda.png') # A variável recebe o arquivo de imagem dado
                valor_venda = pytesseract.image_to_string(screenshotvalorvenda) # Cria uma variável que rec
                
                return quantidade, valor_venda

            def screenshotReserva():
                screenshot_reserva = pyautogui.screenshot(region=(684, 436, 249, 15)) # Primeira variável de segurança, captura a tela no tamanho e posição definidos (x, y, largura e altura)
                screenshot_reserva = screenshot_reserva.convert("L") # Converte a captura para escala monocromática, permitindo uma melhor conversão de dados
                screenshot_reserva.save('./screenshots/screenshot_reserva.png') # Salva a captura com o nome do arquivo .png dado
                from PIL import Image # Importa a biblioteca PIL para interpretação de imagens
                screenshot_reserva = Image.open('./screenshots/screenshot_reserva.png') # A variável recebe o arquivo de imagem dado
                reservado = pytesseract.image_to_string(screenshot_reserva) # Cria uma variável que recebe dados strings transformados pelo pytesseract, o qual interpreta a imagem e localiza textos.
                
                return reservado

            if "Produtos Similares" in screenshotsimilarwatcher:
                quantidade, valor_venda = screenshotSimilar()
            else:
                pyautogui.press('enter')
                time.sleep(0.8)
                quantidade, valor_venda = screenshotSimilar()

            time.sleep(1.4)
            pyautogui.press('enter')
            time.sleep(0.4)

            screenshotsimilarwatcher = pyautogui.screenshot(region=(24, 24, 108, 13)) # Primeira variável de segurança, captura a tela no tamanho e posição definidos (x, y, largura e altura)
            screenshotsimilarwatcher = screenshotsimilarwatcher.convert("L") # Converte a captura para escala monocromática, permitindo uma melhor conversão de dados
            screenshotsimilarwatcher.save('./screenshots/screenshotsimilarwatcher.png') # Salva a captura com o nome do arquivo .png dado
            from PIL import Image # Importa a biblioteca PIL para interpretação de imagens
            screenshotsimilarwatcher = Image.open('./screenshots/screenshotsimilarwatcher.png') # A variável recebe o arquivo de imagem dado
            screenshotsimilarwatcher = pytesseract.image_to_string(screenshotsimilarwatcher) # Cria uma variável que recebe dados strings transformados pelo pytesseract, o qual interpreta a imagem e localiza textos.
            print(screenshotsimilarwatcher)
            time.sleep(1.4)

            if "Produtos Similares" in screenshotsimilarwatcher:
                pyautogui.press('enter')
            time.sleep(0.4)
            quantidade = re.sub(r'[^\d,]', '', quantidade)
            pyautogui.write(str(quantidade))
            time.sleep(0.4)
            valor_venda_limpo = re.sub(r'[^\d,]', '', valor_venda).replace(',', '.')
            try:
                valor_venda_float = float(valor_venda_limpo)
                pyautogui.write(str(round(valor_venda_float / 1.7, 2)).replace('.', ','))
            except ValueError:
                print(f"Erro ao converter valor de venda para o item {codigo_fabricante}: '{valor_venda}'")
            time.sleep(0.4)

            reservado = screenshotReserva()
            if "Produto possui saldo" in reservado:
                pyautogui.click(1076, 584)
                time.sleep(1)
            pyautogui.press("down")
            time.sleep(0.4)
            pyautogui.press("left")

            print(f"Item {codigo_fabricante}: Situação é 'Exorbitante'")
        elif situacao == "Igual":
            print(f"Item {codigo_fabricante} está normal")
        time.sleep(1)
    else:
        Breaker.monitorar_interrupcao(True)
        exit()

# Função para aplicar a fórmula personalizada na coluna I
def verificar_situacao(d, f):
    if d > f:
        return "Negativo"
    elif f > d and d == 0:
        return "Exorbitante"
    else:
        return  "Igual"

# Ler a planilha Excel (exemplo)
arquivo_excel = "C:\\Planilha_Margens_Erradas.xlsx"
df = pd.read_excel(arquivo_excel)

# Iterar por cada linha da planilha
for index, row in df.iloc[1:].iterrows():
    print(f"\nVerificando linha {index + 2}")
    codigo_interno = row['Codigo_Interno']  # Coluna B (código do fabricante)   
    
    codigo_fabricante = row['Codigo_Fabricante']  # Coluna B (código do fabricante)
    valor_d = row['Custo_Gerencial'] # Coluna D (valor D)
    valor_f = row['Vlr_Preco_Venda'] # Coluna F (valor F)

    # Aplicar a fórmula na coluna I
    situacao = verificar_situacao(valor_d, valor_f)

    # Executar o script PyAutoGUI para essa linha
    executar_script_pyautogui(codigo_interno, codigo_fabricante, situacao)
