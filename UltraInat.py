
from email.mime import text
import pyautogui
import time
import re
from pyscreeze import screenshot
from pytesseract import pytesseract
caminho_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.tesseract_cmd = caminho_tesseract

tempo_de_execucao = 10000
tempo_inicial = time.time()
contadorinativos = 0

while(time.time() - tempo_inicial) < tempo_de_execucao:
    print(f'Numéro de itens inativados = {contadorinativos}') # Apresenta na tela a quantidade de itens que foram inativados
    screenshotwatcher = pyautogui.screenshot(region=(38, 22, 150, 45))
    screenshotwatcher = screenshotwatcher.convert("L")
    screenshotwatcher.save('screenshotwatcher.png')
    from PIL import Image
    screenshotwatcher = Image.open('screenshotwatcher.png')
    textwatcher = pytesseract.image_to_string(screenshotwatcher)
    watch = 'Livre'
    watch2 = 'campos'
    time.sleep(1)

    if watch in textwatcher or watch2 in textwatcher:
        time.sleep(0.3)
        screenshotcod = pyautogui.screenshot(region=(37, 743.5, 59, 15))
        screenshotcod = screenshotcod.convert("L")  # Converte para escala de cinza
        screenshotcod.save('screenshotcod.png')

        from PIL import Image
        screenshootcod = Image.open('screenshotcod.png')
        textcod = pytesseract.image_to_string(screenshotcod)
        time.sleep(2)
        pyautogui.click(559, 873)
        time.sleep(0.9)
        pyautogui.click(470, 809)
        time.sleep(1)

        screenshotwatcher2 = pyautogui.screenshot(region=(77, 769, 280, 25))
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
                    screenshooterror2 = pyautogui.screenshot(region=(450, 371, 692, 141))
                    screenshooterror2 = screenshooterror2.convert("L")  # Converte para escala de cinza
                    screenshooterror2.save('screenshoterror2.png')
                    from PIL import Image
                    screenshooterror2 = Image.open('screenshoterror2.png')
                    texterror2 = pytesseract.image_to_string(screenshooterror2)
                    errorname2 = "inativar"
                    errorname3 = "nativo"
                    
                    if errorname2 in texterror2 or errorname3 in texterror2:
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
        pyautogui.press("down")
    else:
        exit()