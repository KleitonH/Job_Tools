# interruptor.py
import keyboard
import threading
import tkinter as tk
import time

# Variável de controle para a execução
running = True

def monitorar_interrupcao(forcar_parada = None):
    global running
    if forcar_parada is not None:
        running = False
        print("Operação finalizada automaticamente")
        exibir_janela_interrompido(True)
    elif forcar_parada is None:
        while running:
            if keyboard.is_pressed('alt+k'):
                running = False
                print("Interrompido via ALT + K pelo usuário")
                time.sleep(2)
                exibir_janela_interrompido()
                break
            time.sleep(0.1) 
    else:
        print("Parâmetro de inserção incorreto")

def iniciar_monitoramento(forcar_parada = None):
    global running
    running = True
    monitor_thread = threading.Thread(target=monitorar_interrupcao, args=(forcar_parada,))
    monitor_thread.start()
    return monitor_thread

def verificar_interrupcao():
    global running
    return running

def reiniciar_monitoramento():
    global running
    running = True

def exibir_janela_interrompido(forcar_parada = None):
    root = tk.Tk()
    if forcar_parada is not None:
        declarar_texto = "Operação finalizada automaticamente"
    elif forcar_parada is None:
        declarar_texto="A operação foi interrompida!"
    root.title("Operação Finalizada")
    root.geometry("300x100+520+260")
    
    root.attributes("-topmost", True)
    
    label = tk.Label(root, text=declarar_texto, font=("Arial", 12))
    label.pack(pady=20)
    
    button = tk.Button(root, text="OK", command=root.destroy)
    button.pack()
    
    root.mainloop()