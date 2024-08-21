#Algoritmo de atribuição de código de seção fixo
import pyautogui # Importação da biblioteca Pyautogui para controle do mouse e teclado 
import time # Importação da biblioteca time para intervalos de tempo 
from pytesseract import pytesseract # Importação da biblioteca pytesseract para conversão de imagens em strings
caminho_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # Caminho para o executável do pytesseract
pytesseract.tesseract_cmd = caminho_tesseract # Define o caminho para o pytesseract
tempo_de_execucao = 40000
tempo_inicial = time.time() # Regra para definir o período de tempo
while(time.time() - tempo_inicial) < tempo_de_execucao:
    time.sleep(1)
    pyautogui.typewrite("5073")
    time.sleep(0.2) 
    pyautogui.press("tab")
    pyautogui.typewrite("0001")
    time.sleep(0.2)
    pyautogui.press("tab")
    pyautogui.typewrite("0001")
    time.sleep(0.2)
    pyautogui.press("down")
    time.sleep(0.1)
    pyautogui.press("left")
    time.sleep(0.1)
    pyautogui.press("left")

