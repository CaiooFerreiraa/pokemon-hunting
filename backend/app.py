import threading
from flask import Flask, jsonify
import requests
import pyautogui
import pyscreenshot as imageGrab
from PIL import Image
import time
import pytesseract

app = Flask(__name__)

# Configurações
namePokemon = "charmander"
pokemonSucessCaugth = f"success!youcaught{namePokemon}"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
cond = True

def captura():
    time.sleep(5)
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

def loop_captura():
    """Loop infinito de detecção do Pokémon"""
    time.sleep(5)
    while cond:
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

# Rota da API
@app.route("/pokemon/<name>")
def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "name": data["name"],
            "sprite": data["sprites"]["front_default"],
            "types": [t["type"]["name"] for t in data["types"]]
        })
    else:
        return jsonify({"error": "Pokémon não encontrado"}), 404

if __name__ == "__main__":
    # Inicia o loop de captura em segundo plano
    threading.Thread(target=loop_captura, daemon=True).start()
    # Inicia o servidor Flask
    app.run(debug=True)
