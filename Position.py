import pyautogui
import time
import pyscreeze

print("Mova o mouse sobre o ponto desejado e espere...")
time.sleep(3)
current_position = pyautogui.position()
print(f"A posição do mouse é: {current_position}")

#Começo do campo (x=273)
#Fim do campo (x=731)
#Altura máxima do campo (y=742)
#Altura mínima do campo (y=755)
#Possível ponto central (x= 502) (y=748.5)

# time.sleep(3)
# screenshot = pyautogui.screenshot(region=(276, 743.5, 458, 15))
# screenshot.save('screenshot.png')