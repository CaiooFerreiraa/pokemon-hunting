import getCoordenadas, pyautogui, time
import os, pytesseract, mss
from flask import jsonify
from PIL import Image

class ActionsForCapturePokemon:
  def __init__(self):
        self.namePokemonBeingHunted = None
        self.pokemonSuccessfulyCaugth = None
        self.conditionLoop = False
        self.useMove = "falseswipe"
        self.crop_area = getCoordenadas.loadCoords()
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        pytesseract.pytesseract.tesseract_cmd = os.path.join(self.BASE_DIR, "Tesseract-OCR", "tesseract.exe")


  def loopCapture(self):
    if self.crop_area is None:
        return
    
    while self.conditionLoop:
        self.botMovement()
        if self.namePokemonBeingHunted in self.normalizedText():
            pyautogui.press('1')
            self.useFalseSwipe()
        else:
            pyautogui.press('4')
        time.sleep(0.2)

  def botMovement():
      pyautogui.keyUp('a')
      pyautogui.keyDown('d')
      time.sleep(1)
      pyautogui.keyDown('a')

  def normalizedText(self):
    image = self.screenshot_region(self.crop_area)
    text = pytesseract.image_to_string(image)
    return text.lower().replace(" ", "")
  
  def screenshot_region(self, crop_area):
    if crop_area is None:
        raise ValueError("crop_area não definido! Defina a área antes de iniciar a captura.")

    with mss.mss() as screenPrint:
        screenshot = screenPrint.grab(screenPrint.monitors[1])
        imageScreen = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        return imageScreen.crop(crop_area)

  def useFalseSwipe(self):
    pyautogui.press('1')
    time.sleep(3)
    if self.useMove in self.normalizedText():
      pyautogui.press('3')
      self.catchPokemon()

  def catchPokemon(self):
    while True:
        pyautogui.press('3')
        if self.pokemonSuccessfulyCaugth in self.normalizedText():
            break
        else:
            pyautogui.press('1')
        time.sleep(1)
  
  def getCropArea():
    return getCoordenadas.loadCoords()
  
  def getPokemonHunted(self):
    return self.namePokemonBeingHunted

  def setNamePokemonBeighHunted(self, name):
    self.namePokemonBeingHunted = name

  def setPokemonSuccessfulyCaugth(self, msgPokemon):
    self.pokemonSuccessfulyCaugth = f"success!youcaught{msgPokemon.lower()}"
  
  def setConditionLoop(self, condition):
    self.conditionLoop = condition

  def checkCropAreaExists(self):
    if self.getCropArea() is None:
      return jsonify({"status": "Erro", "message": "Defina a área primeiro!"})