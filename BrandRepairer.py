#Algoritmo de correção de marca em alteração em massa
import pyautogui # Importação da biblioteca Pyautogui para controle do mouse e teclado 
import time # Importação da biblioteca time para intervalos de tempo
import Breaker
from pytesseract import pytesseract # Importação da biblioteca pytesseract para conversão de imagens em strings
caminho_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # Caminho para o executável do pytesseract
pytesseract.tesseract_cmd = caminho_tesseract # Define o caminho para o pytesseract
tempo_de_execucao = 40000
tempo_inicial = time.time() # Regra para definir o período de tempo
time.sleep(3.5)
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
        
def screenshot():
    screenshotdesc = pyautogui.screenshot(region=(220, 86, 59, 17)) # Captura a descrição do item
    screenshotdesc = screenshotdesc.convert("L")
    screenshotdesc.save('./screenshots/screenshotdesc.png')
    from PIL import Image
    screenshotdesc = Image.open('./screenshots/screenshotdesc.png')
    textdesc = pytesseract.image_to_string(screenshotdesc)
    return textdesc

monitor_thread = Breaker.iniciar_monitoramento()
while(time.time() - tempo_inicial) < tempo_de_execucao and Breaker.verificar_interrupcao():
    textdesc = screenshot()
    print(textdesc)
    if '' in textdesc or "---" in textdesc:
        pass
    else:
        exit()
    time.sleep(1.4)
    pyautogui.tripleClick(249, 91)
    time.sleep(1)
    pyautogui.typewrite('INDET')
    time.sleep(0.5)
    pyautogui.click(248, 75)
    time.sleep(0.5)
    pyautogui.click(248, 75)
    time.sleep(0.5)
