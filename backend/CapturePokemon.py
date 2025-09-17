import getCoordenadas, pyautogui, time
import os, pytesseract, mss
from flask import jsonify
from PIL import Image

class ActionsForCapturePokemon:
  namePokemonBeingHunted = None
  pokemonSuccessfulyCaugth = None
  conditionLoop = False
  useMove = "falseswipe"
  crop_area = getCoordenadas.loadCoords()
  BASE_DIR = os.path.dirname(os.path.abspath(__file__))
  pytesseract.pytesseract.tesseract_cmd = os.path.join(BASE_DIR, "Tesseract-OCR", "tesseract.exe")

  def loopCapture():
    if ActionsForCapturePokemon.crop_area is None:
        return
    
    while ActionsForCapturePokemon.conditionLoop:
        ActionsForCapturePokemon.botMovement()
        if ActionsForCapturePokemon.namePokemonBeingHunted in ActionsForCapturePokemon.normalizedText():
            pyautogui.press('1')
            ActionsForCapturePokemon.useFalseSwipe()
        else:
            pyautogui.press('4')
        time.sleep(0.2)

  def botMovement():
      pyautogui.keyUp('a')
      pyautogui.keyDown('d')
      time.sleep(1)
      pyautogui.keyDown('a')

  def normalizedText():
    image = ActionsForCapturePokemon.screenshot_region(ActionsForCapturePokemon.crop_area)
    text = pytesseract.image_to_string(image)
    return text.lower().replace(" ", "")
  
  def screenshot_region(crop_area):
    if crop_area is None:
        raise ValueError("crop_area não definido! Defina a área antes de iniciar a captura.")

    with mss.mss() as screenPrint:
        screenshot = screenPrint.grab(screenPrint.monitors[1])
        imageScreen = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        return imageScreen.crop(crop_area)

  def useFalseSwipe():
    pyautogui.press('1')
    time.sleep(3)
    if ActionsForCapturePokemon.useMove in ActionsForCapturePokemon.normalizedText():
      pyautogui.press('3')
      ActionsForCapturePokemon.catchPokemon()

  def catchPokemon():
    while True:
        pyautogui.press('3')
        if ActionsForCapturePokemon.pokemonSuccessfulyCaugth in ActionsForCapturePokemon.normalizedText():
            break
        else:
            pyautogui.press('1')
        time.sleep(1)
  
  def getCropArea():
    return getCoordenadas.loadCoords()
  
  def getPokemonHunted():
    return ActionsForCapturePokemon.namePokemonBeingHunted

  def setNamePokemonBeighHunted(name):
    ActionsForCapturePokemon.namePokemonBeingHunted = name

  def setPokemonSuccessfulyCaugth(msgPokemon):
    ActionsForCapturePokemon.pokemonSuccessfulyCaugth = f"success!youcaught{msgPokemon.lower()}"
  
  def setConditionLoop(condition):
    ActionsForCapturePokemon.conditionLoop = condition

  def checkCropAreaExists():
    if ActionsForCapturePokemon.getCropArea() is None:
      return jsonify({"status": "Erro", "message": "Defina a área primeiro!"})