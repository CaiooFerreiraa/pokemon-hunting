import threading
from flask import Flask, jsonify
import requests
import os
import pyautogui
from PIL import Image
import time
import pytesseract
import mss
import webbrowser

app = Flask(__name__)

# Configurações globais
namePokemon = None
pokemonSucessCaugth = None
cond = False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pytesseract.pytesseract.tesseract_cmd = os.path.join(BASE_DIR, "Tesseract-OCR", "tesseract.exe")

# ========== Funções utilitárias ==========
def screenshot_region(crop_area):
    """Captura a tela e retorna apenas a região cortada"""
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        return img.crop(crop_area)

def captura():
    crop_area = (645, 500, 1093, 750)
    while True:
        img = screenshot_region(crop_area)
        text = pytesseract.image_to_string(img)
        normalized_text = text.lower().replace(" ", "")

        print(f"[Captura] Texto: {text.strip()}")
        pyautogui.press('3')

        if pokemonSucessCaugth in normalized_text:
            print("[Captura] Captura concluída!")
            break
        else:
            print("[Captura] Ainda capturando...")
            pyautogui.press('1')
        time.sleep(1)

def usarFalseSwipe():
    crop_area = (645, 500, 1093, 750)
    pyautogui.press('1')
    time.sleep(3)

    img = screenshot_region(crop_area)
    text = pytesseract.image_to_string(img)
    normalized_text = text.lower().replace(" ","")
    print(f"[usarFalseSwipe] Texto: {text.strip()}")

    if "falseswipe" in normalized_text:
        print("[usarFalseSwipe] False Swipe detectado → captura()")
        pyautogui.press('3')
        captura()
    else:
        print("[usarFalseSwipe] False Swipe não encontrado.")

def loop_captura():
    crop_area = (645, 500, 1093, 750)

    pyautogui.keyUp('a')
    pyautogui.keyDown('d')
    time.sleep(1)
    pyautogui.keyDown('a')

    while cond:
        img = screenshot_region(crop_area)
        text = pytesseract.image_to_string(img)
        normalized_text = text.lower().replace(" ", "")

        print(f"[Loop] Texto: {text.strip()}")

        if namePokemon and namePokemon in normalized_text:
            print(f"[Loop] {namePokemon} detectado!")
            pyautogui.press('1')
            usarFalseSwipe()
        else:
            print(f"[Loop] {namePokemon} não encontrado.")
            pyautogui.press('4')
        time.sleep(1)

# ========== Endpoints ==========
@app.route("/define_pokemon/<name>", methods=["POST"])
def get_pokemon(name):
    global namePokemon
    namePokemon = name

    return jsonify({"status": "Pokemon definido", "pokemon": namePokemon})

@app.route("/start-capture/<name>", methods=["POST"])
def start_capture(name):
    global cond, namePokemon, pokemonSucessCaugth
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
    return jsonify({"running": cond, "pokemon": namePokemon})

if __name__ == "__main__":
    def open_browser():
        time.sleep(1)
        webbrowser.open("https://pokemon-hunting.vercel.app/")

    threading.Thread(target=open_browser, daemon=True).start()

    app.run(debug=True, port=5500, use_reloader=False)
