import pyautogui # Importação da biblioteca Pyautogui para controle do mouse e teclado 
import time # Importação da biblioteca time para intervalos de tempo
import Breaker
from pytesseract import pytesseract # Importação da biblioteca pytesseract para conversão de imagens em strings
caminho_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # Caminho para o executável do pytesseract
pytesseract.tesseract_cmd = caminho_tesseract # Define o caminho para o pytesseract
tempo_de_execucao = 40000
tempo_inicial = time.time() # Regra para definir o período de tempo
monitor_thread = Breaker.iniciar_monitoramento()

time.sleep(3)
while(time.time() - tempo_inicial) < tempo_de_execucao and Breaker.verificar_interrupcao():
    # pyautogui.click(27, 705)
    # time.sleep(0.1)
    # pyautogui.click(24, 682)

    time.localtime()