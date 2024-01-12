
from email.mime import text
import pyautogui 
import time
import re
from pyscreeze import screenshot
from pytesseract import pytesseract
caminho_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.tesseract_cmd = caminho_tesseract #Importação das bibliotecas utilizadas no código, 'Pyautogui' para controle, 'time' para intervalos, 're' para modificação da string para localização de valores numéricos e pytesseract para converter a imagem da captura em uma string 

tempo_de_execucao = 40000 # Tempo de execução máximo da operação 
tempo_inicial = time.time() # Regra para definir o período de tempo
contadorinativos = 0 # Variável que receberá o número de itens inativados na operação
contadorverificados = -1 # Variável que define a quantidade de itens verificados, começa com -1 pois o loop inicia adicionando 1 a contagem
while(time.time() - tempo_inicial) < tempo_de_execucao: # Loop de execução enquanto o contador de tempo estiver ativo
    contadorverificados += 1 # Adiciona uma verificação para o ciclo, aumentado o contador de itens verificados
    print(f"_______________________________")
    print(f"Número de verificações: {contadorverificados}") # Exibe a quantidade de verificações feitas
    print(f'Número de itens inativados : {contadorinativos}') # Apresenta na tela a quantidade de itens que foram inativados
    screenshotwatcher = pyautogui.screenshot(region=(38, 22, 150, 45)) # Primeira variável de segurança, captura a tela no tamanho e posição definidos (x, y, largura e altura)
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
        screenshotcod = pyautogui.screenshot(region=(37, 743.5, 59, 15)) # Variável para receber código da célula do item da tabela
        screenshotcod = screenshotcod.convert("L")  # Converte para escala de cinza
        screenshotcod.save('screenshotcod.png') # Salva a imagem

        from PIL import Image # Interpretação de imagem
        screenshootcod = Image.open('screenshotcod.png') # Recebimento da imagem
        textcod = pytesseract.image_to_string(screenshotcod) # Converte para texto
        time.sleep(2) # Intervalo
        pyautogui.click(559, 873) # Clica na posição do ícone da barra de tarefas do sistema
        time.sleep(0.9) 
        pyautogui.click(470, 809) # Clica na outra aba de sistema aberta
        time.sleep(1)

        screenshotwatcher2 = pyautogui.screenshot(region=(77, 769, 280, 25)) # Segundo método de verificação, segue a mesma lógica do primeiro, buscando outras palavras. Garante que esteja na tela correta de operação
        screenshotwatcher2 = screenshotwatcher2.convert("L")
        screenshotwatcher2.save('screenshotwatcher2.png')
        from PIL import Image
        screenshotwatcher2 = Image.open('screenshotwatcher2.png')
        textwatcher2 = pytesseract.image_to_string(screenshotwatcher2)
        watch3 = "sistan"
        time.sleep(0.3)

        if watch3 in textwatcher2:
            time.sleep(0.2)
            pyautogui.press("f5")
            time.sleep(0.5)
            pyautogui.typewrite(textcod)
            time.sleep(1)
            
            screenshoterror = pyautogui.screenshot(region=(680, 402, 235, 60))
            screenshoterror = screenshoterror.convert("L")
            screenshoterror.save('screenshoterror.png')
            from PIL import Image
            screenshooterror = Image.open('screenshoterror.png')
            texterror = pytesseract.image_to_string(screenshoterror)
            errorname = 'registro'

            if errorname in texterror:
                pyautogui.click(790, 486)
                time.sleep(0.8)
                pyautogui.press("esc")
                time.sleep(0.5)
                pass
            else:
                time.sleep(1)
                pyautogui.press("enter")
                pyautogui.press("enter")
                time.sleep(0.8)
                pyautogui.click(403, 190)
                time.sleep(1.3)
                screenshotdate = pyautogui.screenshot(region=(195, 510, 56, 17))
                screenshotdate = screenshotdate.convert("L")  # Converte para escala de cinza
                screenshotdate.save('screenshotdate.png')
                from PIL import Image
                screenshootdate = Image.open('screenshotdate.png')
                textdate = pytesseract.image_to_string(screenshotdate)
                screenshotdate2 = pyautogui.screenshot(region=(385, 510, 56, 17))
                screenshotdate2 = screenshotdate2.convert("L")  # Converte para escala de cinza
                screenshotdate2.save('screenshotdate2.png')
                from PIL import Image
                screenshootdate2 = Image.open('screenshotdate2.png')
                textdate2 = pytesseract.image_to_string(screenshotdate2)
                padrao_numerico = r'\b\d+\.\d+|\b[0-9]+\b'
                numeros_textdate = [float(match.group()) for match in re.finditer(padrao_numerico, textdate)]
                numeros_textdate2 = [float(match.group()) for match in re.finditer(padrao_numerico, textdate2)]
                time.sleep(1)
                
                if any(numero >= 1 for numero in numeros_textdate) or any(numero >= 1 for numero in numeros_textdate2):
                    pyautogui.press("esc")
                    pyautogui.press("esc")
                    time.sleep(0.2)
                else:
                    pyautogui.press("esc")
                    pyautogui.press("esc")
                    time.sleep(0.5)
                    pyautogui.press("f3")
                    time.sleep(0.5)
                    pyautogui.typewrite(textcod)
                    time.sleep(0.5)
                    pyautogui.press("enter")
                    pyautogui.press("enter")
                    time.sleep(1)
                    pyautogui.click(945, 566)
                    time.sleep(0.5)
                    pyautogui.click(650, 660)
                    time.sleep(0.5)
                    screenshoterror2 = pyautogui.screenshot(region=(450, 371, 692, 141))
                    screenshoterror2 = screenshoterror2.convert("L")  # Converte para escala de cinza
                    screenshoterror2.save('screenshoterror2.png')
                    from PIL import Image
                    screenshoterror2 = Image.open('screenshoterror2.png')
                    texterror2 = pytesseract.image_to_string(screenshoterror2)
                    errorname2 = "inativar"
                    errorname3 = "nativo"
                    errorname4 = "duplicado"
                    
                    if errorname2 in texterror2 or errorname3 in texterror2 or errorname4 in texterror2:
                        pyautogui.click(802, 483)
                        time.sleep(0.6)
                        pyautogui.press("esc")
                        time.sleep(0.6)
                        pyautogui.click(744, 483)
                        time.sleep(0.6)
                        pyautogui.press("esc")
                        time.sleep(0.6)
                    else:
                        pyautogui.press("esc")
                        time.sleep(0.2)
                        contadorinativos += 1
        else:
            exit()

        pyautogui.click(559, 883)
        time.sleep(0.5)
        pyautogui.click(674, 809)
        time.sleep(1.5)
        
        screenshotdesc = pyautogui.screenshot(region=(276, 743.5, 458, 15))
        screenshotdesc = screenshotdesc.convert("L")  # Converte para escala de cinza
        screenshotdesc.save('screenshotdesc.png')
        from PIL import Image
        screenshotdesc = Image.open('screenshotdesc.png')
        textdesc = pytesseract.image_to_string(screenshotdesc)

        secaoescolhida = ""
        lista_latarias = ["PONTEIRA", "ASSOALHO", "CHAPA", "CAPO", "CAIXA AR", "CAIXA DE AR", "LONGARINA", "ALMA", "PAINEL TRAS", "ALOJAMENTO FAROL"]
        item_encontrado = next((item for item in lista_latarias if item in textdesc), None)
        if item_encontrado:
            if len(item_encontrado) > len(secaoescolhida):
                secaoescolhida = "latarias"

        lista_alimentos = ["PICOLE", "CHICLETE", "SALGADINHO", "BOMBOM", "BALA FREEGELLS", "BARRA CHOCOLATE", "WAFER", "PIPOCA", "YOKITOS", "BATATA", "BALA DE GOMA", "AMENDOIM JAPONES", "PACOQUINHA", "SORVETE", "TRENTO", "PIRULITO", "BISCOITO", "TORTUGUITA", "COOKIES", "CEREAL BARRA", "BARRA CEREAL", "BIS LACTA", "AGUA MINERAL", "REFRIGERANTE", "SUCO"]
        item_encontrado = next((item for item in lista_alimentos if item in textdesc), None)
        if item_encontrado:
            if len(item_encontrado) > len(secaoescolhida):
                secaoescolhida = "alimentos"

        lista_mecanica = []
        item_encontrado = next((item for item in lista_mecanica if item in textdesc), None)
        if item_encontrado:
            if len(item_encontrado) > len(secaoescolhida):
                secaoescolhida = "mecanica"

        lista_plasticos = ["MANIVELA VIDRO", "GRAMPO VERSAILLES", "ALCA TETO", "TAMPA RESERV", "TAMPA CAPA VENTIL", "BOLA CAMBIO", "TAMPA OLEO", "MANIVELA REGULADORA" "SUPORTE MACANETA", "CALCO MACANETA", "APOIA BRACO", "MOLDURA MACANETA"]
        item_encontrado = next((item for item in lista_plasticos if item in textdesc), None)
        if item_encontrado:
            if len(item_encontrado) > len(secaoescolhida):
                secaoescolhida = "plasticos"

        lista_eletrica = ["CILINDRO IGNICAO", "COMUTADOR IGNICAO"]
        item_encontrado = next((item for item in lista_eletrica if item in textdesc), None)
        if item_encontrado:
            if len(item_encontrado) > len(secaoescolhida):
                secaoescolhida = "eletrica"

        lista_escapamentos = ["PONTEIRA ESCAPAMENTO"]
        item_encontrado = next((item for item in lista_escapamentos if item in textdesc), None)
        if item_encontrado:
            if len(item_encontrado) > len(secaoescolhida):
                secaoescolhida = "escapamentos"

        lista_ferragens = ["DOBRADICA", "AMORTECEDOR", "GRAMPO TRAVA MANIVELA", "PRESILHA FECHADURA", "MOTOR MAQUINA VIDRO", "PORCA", "ARRUELA", "PARAFUSO", "SUPORTE VIDRO", "VARETA TRAVA", "CABO DESTRAVA PORTA", "TRAVA DIRECAO", "TRAVA IGNICAO", "PINO TRAVA", "PINO SUPORTE", "GATILHO MACANETA", "COMANDO MACANETA", "TAMPA RADIADOR", "ROLDANA MAQUINA VIDRO", "ROLDANA MAQUINA DE VIDRO", "MAQUINA VIDRO", "MAQUINA DE VIDRO", "LIMITADOR PORTA", "MACANETA INTERNA", "MACANETA EXTERNA", "TRAVA SEGURANCA PORTA", "CILINDRO PORTA", "KIT MACANETA", "BATENTE", "FECHO PORTA", "FECHO CILINDRO PORTA", "CABO ACION", "CABO FECH", "FECHADURA", "FECHO PORTA", "TRINCO JANELA", "TRINCO VIDRO", "TRINCO QUEBRA VENTO"]
        item_encontrado = next((item for item in lista_ferragens if item in textdesc), None)
        if item_encontrado:
            if len(item_encontrado) > len(secaoescolhida):
                secaoescolhida = "ferragens"

        if item_encontrado == "latarias":
            pyautogui.typewrite(5039)
        elif item_encontrado == "alimentos":
            pyautogui.typewrite(5042)
        elif item_encontrado == "mecanica":
            pyautogui.typewrite(5048)
        elif item_encontrado == "plasticos":
            pyautogui.typewrite(5049)
        elif item_encontrado == "eletrica":
            pyautogui.typewrite(5058)
        elif item_encontrado == "escapamentos":
            pyautogui.typewrite(5062)
        elif item_encontrado == "ferragens":
            pyautogui.typewrite(5066)
    
        time.sleep(0.3)
        pyautogui.press("down")
    else:
        exit()