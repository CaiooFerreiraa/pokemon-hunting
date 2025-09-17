import threading, time
from flask import Flask, jsonify
import webbrowser, getCoordenadas
from CapturePokemon import ActionsForCapturePokemon

botAplication = Flask(__name__)
actionsForCapturePokemon = ActionsForCapturePokemon()

# ========== Endpoints ==========
@botAplication.route("/define_pokemon/<name>", methods=["POST"])
def definePokemon(name):
    actionsForCapturePokemon.setNamePokemonBeighHunted(name)
    actionsForCapturePokemon.setPokemonSuccessfulyCaugth(name)
    return jsonify({"status": "Pokemon definido", "pokemon": actionsForCapturePokemon.getPokemonHunted()})

@botAplication.route("/define_area", methods=["GET"])
def defineArea():
    crop_area = getCoordenadas.select_area()
    return jsonify({"status": "Área definida", "coords": crop_area})

@botAplication.route("/start-capture/<name>", methods=["POST"])
def startCapture(name):
    actionsForCapturePokemon.checkCropAreaExists()
    actionsForCapturePokemon.setNamePokemonBeighHunted(name.lower())
    actionsForCapturePokemon.setConditionLoop(True)
    threading.Thread(target=actionsForCapturePokemon.loopCapture(), daemon=True).start()
    return jsonify({"status": "captura iniciada", "pokemon": actionsForCapturePokemon.getPokemonHunted()})

@botAplication.route("/stop-capture", methods=["GET"])
def stopCapture():
    actionsForCapturePokemon.setConditionLoop(False)
    return jsonify({"status": "captura parada"})

if __name__ == "__main__":
    def openBrowser():
        time.sleep(1)
        webbrowser.open("https://pokemon-hunting.vercel.app/")

    threading.Thread(target=openBrowser, daemon=True).start()
    botAplication.run(debug=True, port=5500, use_reloader=False)
