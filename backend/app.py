import threading
from flask import Flask, jsonify
import pyautogui
import pyscreenshot as imageGrab
from PIL import Image
import time
import pytesseract

app = Flask(__name__)

pyautogui.FAILSAFE = False

# Configurações
namePokemon = None  # Inicialmente sem alvo
pokemonSucessCaugth = None
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
cond = False  # Bot parado até receber comando

def captura():
    time.sleep(5)
    # Tirar nova screenshot
    screenshot = imageGrab.grab()
    screenshot.save("test.jpeg", "JPEG")

    img = Image.open("test.jpeg")
    crop_area = (645, 500, 1093, 750)
    cropped_image = img.crop(crop_area)

    text = pytesseract.image_to_string(cropped_image)
    normalized_text = text.lower().replace(" ", "")

    while True:
        pyautogui.press('3')
        print(f"[Captura] Texto encontrado: {text.strip()}")
        #caught Charmander
        if pokemonSucessCaugth in normalized_text:
            print("[Captura] A captura terminou.")
            break
        else:
            print("[Captura] Capturando...")
            pyautogui.press('1')
        screenshot = imageGrab.grab()
        screenshot.save("test.jpeg", "JPEG")
        img = Image.open("test.jpeg")
        cropped_image = img.crop(crop_area)
        text = pytesseract.image_to_string(cropped_image)
        normalized_text = text.lower().replace(" ", "")

def usarFalseSwipe():
    time.sleep(3)
    pyautogui.press('1')

    screenshot = imageGrab.grab()
    screenshot.save("test.jpeg", "JPEG")
    img = Image.open("test.jpeg")
    crop_area = (645, 500, 1093, 750)
    cropped_image = img.crop(crop_area)

    text = pytesseract.image_to_string(cropped_image)
    normalized_text = text.lower().replace(" ","")
    print(f"[usarFalseSwipe] Texto: {text.strip()}")

    if "falseswipe" in normalized_text:
        print("[usarFalseSwipe] False Swipe detectado, chamando captura()...")
        pyautogui.press('3')
        captura()
    else:
        print("[usarFalseSwipe] False Swipe não encontrado.")

# API para iniciar a captura
@app.route("/start-capture/<name>", methods=["GET"])
def start_capture(name):
    global cond, namePokemon, pokemonSucessCaugth
    namePokemon = name.lower()
    pokemonSucessCaugth = f"success!youcaught{namePokemon}"
    cond = True
    return jsonify({"status": "Captura iniciada", "pokemon": namePokemon})

# Cria o loop de captura
@app.route("/capture", methods=["GET"])
def loop_captura():
    global cond, namePokemon, pokemonSucessCaugth
    time.sleep(3)
    while cond:
        if not namePokemon:
            time.sleep(1)
            continue

        screenshot = imageGrab.grab()
        screenshot.save("test.jpeg", "JPEG")
        img = Image.open("test.jpeg")
        crop_area = (645, 500, 1093, 750)
        cropped_image = img.crop(crop_area)
        text = pytesseract.image_to_string(cropped_image)
        print(f"[Main Loop] Texto: {text.strip()}")

        normalized_text = text.lower().replace(" ", "")

        if namePokemon in normalized_text:
            print(f"[Main Loop] {namePokemon} detectado!")
            pyautogui.press('1')
            usarFalseSwipe()
        else:
            print(f"[Main Loop] {namePokemon} não encontrado...")
            pyautogui.press('4')

# API para parar a captura
@app.route("/stop-capture", methods=["GET"])
def stop_capture():
    global cond
    cond = False
    return jsonify({"status": "Captura parada"})

if __name__ == "__main__":
    threading.Thread(target=loop_captura, daemon=True).start()
    app.run(debug=True, host="127.0.0.1", port=5500)