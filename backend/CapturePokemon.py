import getCoordenadas, pyautogui, time
import os, pytesseract, mss
from flask import jsonify
from PIL import Image

class CapturePokemon:
  namePokemonBeingHunted = None
  pokemonSuccessfulyCaugth = None
  conditionLoop = False
  useMove = "falseswipe"
  crop_area = getCoordenadas.loadCoords()
  BASE_DIR = os.path.dirname(os.path.abspath(__file__))
  pytesseract.pytesseract.tesseract_cmd = os.path.join(BASE_DIR, "Tesseract-OCR", "tesseract.exe")

  @staticmethod
  def loopCapture():
    if CapturePokemon.crop_area is None:
        return
    
    while CapturePokemon.conditionLoop:
        CapturePokemon.botMovement()
        if CapturePokemon.namePokemonBeingHunted in CapturePokemon.normalizedText():
            pyautogui.press('1')
            CapturePokemon.useFalseSwipe()
        else:
            pyautogui.press('4')
        time.sleep(0.2)

  def botMovement():
      pyautogui.keyUp('a')
      pyautogui.keyDown('d')
      time.sleep(1)
      pyautogui.keyDown('a')

  @staticmethod
  def normalizedText():
    image = CapturePokemon.screenshot_region(CapturePokemon.crop_area)
    text = pytesseract.image_to_string(image)
    return text.lower().replace(" ", "")
  
  def screenshot_region(crop_area):
    if crop_area is None:
        raise ValueError("crop_area não definido! Defina a área antes de iniciar a captura.")

    with mss.mss() as screenPrint:
        screenshot = screenPrint.grab(screenPrint.monitors[1])
        imageScreen = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        return imageScreen.crop(crop_area)

  @staticmethod  
  def useFalseSwipe():
    pyautogui.press('1')
    time.sleep(3)
    if CapturePokemon.useMove in CapturePokemon.normalizedText():
      pyautogui.press('3')
      CapturePokemon.catchPokemon()

  @staticmethod
  def catchPokemon():
    while True:
        pyautogui.press('3')
        if CapturePokemon.pokemonSuccessfulyCaugth in CapturePokemon.normalizedText():
            break
        else:
            pyautogui.press('1')
        time.sleep(1)
  
  @staticmethod
  def getCropArea():
    return getCoordenadas.loadCoords()
  
  @staticmethod
  def getPokemonHunted():
    return CapturePokemon.namePokemonBeingHunted

  @staticmethod
  def setNamePokemonBeighHunted(name):
    CapturePokemon.namePokemonBeingHunted = name

  @staticmethod
  def setPokemonSuccessfulyCaugth(msgPokemon):
    CapturePokemon.pokemonSuccessfulyCaugth = f"success!youcaught{msgPokemon.lower()}"
  
  @staticmethod
  def setConditionLoop(condition):
    CapturePokemon.conditionLoop = condition

  @staticmethod
  def checkCropAreaExists():
    if CapturePokemon.getCropArea() is None:
      return jsonify({"status": "Erro", "message": "Defina a área primeiro!"})