import tkinter as tk
import json
import os
import sys

# Define o diretório base corretamente
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

save_path = os.path.join(BASE_DIR, "coords.json")
coords = ()

def select_area():
    """Abre a tela para o usuário selecionar a área e retorna as coordenadas (x1, y1, x2, y2)."""
    global coords

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-alpha", 0.3)  # transparente
    root.config(bg="black")
    root.title("Selecione a área e solte o mouse")

    start_x = start_y = None
    rect = None

    def on_mouse_down(event):
        nonlocal start_x, start_y, rect
        start_x, start_y = event.x, event.y
        rect = canvas.create_rectangle(start_x, start_y, start_x, start_y, outline="red", width=2)

    def on_mouse_drag(event):
        nonlocal rect
        canvas.coords(rect, start_x, start_y, event.x, event.y)

    def on_mouse_up(event):
        global coords
        x1, y1, x2, y2 = start_x, start_y, event.x, event.y
        coords = (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))

        # Salvar as coordenadas em JSON
        with open(save_path, "w") as f:
            json.dump(coords, f)

        print("Coordenadas selecionadas:", coords)
        print("Arquivo salvo em:", save_path)
        root.destroy()

    canvas = tk.Canvas(root, cursor="cross")
    canvas.pack(fill="both", expand=True)

    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_drag)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)

    root.mainloop()
    return coords

def loadCoords():
    """Carrega coords.json se existir."""
    if os.path.exists(save_path):
        with open(save_path, "r") as f:
            loaded = tuple(json.load(f))
            print(f"[Init] Área carregada de coords.json: {loaded}")
            return loaded
    return None

if __name__ == "__main__":
    area = select_area()
    print("Área retornada:", area)
