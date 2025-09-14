import threading, os
from flask import Flask, jsonify
import pyautogui, time, pytesseract
from PIL import Image
import mss, webbrowser, getCoordenadas

botAplication = Flask(__name__)

# Configurações globais
namePokemonBeingHunted = None
pokemonSuccessfulyCaugth = None
conditionLoop = False
useMove = "falseswipe"
crop_area = getCoordenadas.loadCoords()  # Carrega coords.json se existir

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pytesseract.pytesseract.tesseract_cmd = os.path.join(BASE_DIR, "Tesseract-OCR", "tesseract.exe")

# ========== Funções utilitárias ==========
def screenshot_region(crop_area):
    if crop_area is None:
        raise ValueError("crop_area não definido! Defina a área antes de iniciar a captura.")

    with mss.mss() as screenPrint:
        screenshot = screenPrint.grab(screenPrint.monitors[1])
        imageScreen = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        return imageScreen.crop(crop_area)

def catchPokemon():
    while True:
        pyautogui.press('3')
        if pokemonSuccessfulyCaugth in normalizedText():
            break
        else:
            pyautogui.press('1')
        time.sleep(1)

def useFalseSwipe():
    pyautogui.press('1')
    time.sleep(3)
    if useMove in normalizedText():
        pyautogui.press('3')
        catchPokemon()

def loopCapture():
    global crop_area
    if crop_area is None:
        return
    
    while conditionLoop:
        botMovement()
        if namePokemonBeingHunted and namePokemonBeingHunted in normalizedText():
            pyautogui.press('1')
            useFalseSwipe()
        else:
            pyautogui.press('4')
        time.sleep(0.5)

def botMovement():
    pyautogui.keyUp('a')
    pyautogui.keyDown('d')
    time.sleep(1)
    pyautogui.keyDown('a')

def normalizedText():
    image = screenshot_region(crop_area)
    text = pytesseract.image_to_string(image)
    return text.lower().replace(" ", "")

# ========== Endpoints ==========
@botAplication.route("/define_pokemon/<name>", methods=["POST"])
def getPokemon(name):
    global namePokemonBeingHunted
    namePokemonBeingHunted = name
    return jsonify({"status": "Pokemon definido", "pokemon": namePokemonBeingHunted})

@botAplication.route("/define_area", methods=["GET"])
def defineArea():
    global crop_area
    crop_area = getCoordenadas.select_area()
    return jsonify({"status": "Área definida", "coords": crop_area})

@botAplication.route("/start-capture/<name>", methods=["POST"])
def startCapture(name):
    global conditionLoop, namePokemonBeingHunted
    if crop_area is None:
        return jsonify({"status": "Erro", "message": "Defina a área primeiro!"})

    namePokemonBeingHunted = name.lower()
    conditionLoop = True
    threading.Thread(target=loopCapture, daemon=True).start()
    return jsonify({"status": "captura iniciada", "pokemon": namePokemonBeingHunted})

@botAplication.route("/stop-capture", methods=["GET"])
def stopCapture():
    global conditionLoop
    conditionLoop = False
    return jsonify({"status": "captura parada"})

@botAplication.route("/status", methods=["GET"])
def status():
    return jsonify({"running": conditionLoop, "pokemon": namePokemonBeingHunted, "crop_area": crop_area})

if __name__ == "__main__":
    def openBrowser():
        time.sleep(1)
        webbrowser.open("https://pokemon-hunting.vercel.app/")

    threading.Thread(target=openBrowser, daemon=True).start()
    botAplication.run(debug=True, port=5500, use_reloader=False)
