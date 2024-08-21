# interruptor.py
import keyboard
import threading
import tkinter as tk
import time

# Variável de controle para a execução
running = True

def monitorar_interrupcao():
    global running
    keyboard.wait('alt+k')
    running = False
    print("Interrompido via ALT + K pelo usuário")
    time.sleep(2)
    exibir_janela_interrompido()

def iniciar_monitoramento():
    monitor_thread = threading.Thread(target=monitorar_interrupcao)
    monitor_thread.start()
    return monitor_thread

def verificar_interrupcao():
    global running
    return running

def reiniciar_monitoramento():
    global running
    running = True

def exibir_janela_interrompido():
    root = tk.Tk()
    root.title("Operação Finalizada")
    root.geometry("300x100+520+260")
    
    root.attributes("-topmost", True)
    
    label = tk.Label(root, text="A operação foi interrompida!", font=("Arial", 12))
    label.pack(pady=20)
    
    button = tk.Button(root, text="OK", command=root.destroy)
    button.pack()
    
    root.mainloop()