import pyautogui
import mouse
import keyboard
import time

print("Pressione 'ctrl + alt + s' para iniciar a seleção da área.")

keyboard.wait('ctrl+alt+s')
print("Seleção iniciada. Clique e arraste o mouse para selecionar a área.")


mouse.wait(button='left', target_types=('down',))
start_x, start_y = pyautogui.position()
print("Com o botão esquerdo pressionado, arraste o mouse até a posição desejada, então, solte o botão esquerdo do mouse")

mouse.wait(button='left', target_types=('up',))
end_x, end_y = pyautogui.position()

# Calcula a largura e a altura da área selecionada
width = end_x - start_x
height = end_y - start_y

print(f"|Canto superior esquerdo: ({start_x}, {start_y})|\n|Dimensões: ({width}, {height}) pixels|\nLembre-se de que os valores serão sempre inteiros, a vírgula serve para diferenciar um termo do próximo")
