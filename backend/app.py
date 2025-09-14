import threading
from flask import Flask, jsonify
import os
import pyautogui
from PIL import Image
import time
import pytesseract
import mss
import webbrowser
import getCoordenadas

app = Flask(__name__)

# Configurações globais
namePokemon = None
pokemonSucessCaugth = None
cond = False
crop_area = getCoordenadas.load_coords()  # Carrega coords.json se existir

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pytesseract.pytesseract.tesseract_cmd = os.path.join(BASE_DIR, "Tesseract-OCR", "tesseract.exe")

# ========== Funções utilitárias ==========
def screenshot_region(crop_area):
    if crop_area is None:
        raise ValueError("crop_area não definido! Defina a área antes de iniciar a captura.")

    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        return img.crop(crop_area)

def captura():
    while True:
        img = screenshot_region(crop_area)
        text = pytesseract.image_to_string(img)
        normalized_text = text.lower().replace(" ", "")
        pyautogui.press('3')

        if pokemonSucessCaugth in normalized_text:
            break
        else:
            pyautogui.press('1')
        time.sleep(1)

def usarFalseSwipe():
    pyautogui.press('1')
    time.sleep(3)

    img = screenshot_region(crop_area)
    text = pytesseract.image_to_string(img)
    normalized_text = text.lower().replace(" ","")

    if "falseswipe" in normalized_text:
        pyautogui.press('3')
        captura()

def loop_captura():
    global crop_area

    if crop_area is None:
        print("[Loop] Erro: crop_area não definido!")
        return

    while cond:
        pyautogui.keyUp('a')
        pyautogui.keyDown('d')
        time.sleep(1)
        pyautogui.keyDown('a')

        img = screenshot_region(crop_area)
        text = pytesseract.image_to_string(img)
        normalized_text = text.lower().replace(" ", "")

        if namePokemon and namePokemon in normalized_text:
            pyautogui.press('1')
            usarFalseSwipe()
        else:
            pyautogui.press('4')
        time.sleep(0.5)

# ========== Endpoints ==========
@app.route("/define_pokemon/<name>", methods=["POST"])
def get_pokemon(name):
    global namePokemon
    namePokemon = name
    return jsonify({"status": "Pokemon definido", "pokemon": namePokemon})

@app.route("/define_area", methods=["GET"])
def define_area():
    global crop_area
    crop_area = getCoordenadas.select_area()
    return jsonify({"status": "Área definida", "coords": crop_area})

@app.route("/start-capture/<name>", methods=["POST"])
def start_capture(name):
    global cond, namePokemon, pokemonSucessCaugth
    if crop_area is None:
        return jsonify({"status": "Erro", "message": "Defina a área primeiro!"})

    namePokemon = name.lower()
    pokemonSucessCaugth = f"success!youcaught{namePokemon}"
    cond = True
    threading.Thread(target=loop_captura, daemon=True).start()
    return jsonify({"status": "captura iniciada", "pokemon": namePokemon})

@app.route("/stop-capture", methods=["GET"])
def stop_capture():
    global cond
    cond = False
    return jsonify({"status": "captura parada"})

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"running": cond, "pokemon": namePokemon, "crop_area": crop_area})

if __name__ == "__main__":
    def open_browser():
        time.sleep(1)
        webbrowser.open("https://pokemon-hunting.vercel.app/")

    threading.Thread(target=open_browser, daemon=True).start()
    app.run(debug=True, port=5500, use_reloader=False)
