import threading, time
from flask import Flask, jsonify
import webbrowser, getCoordenadas
from CapturePokemon import CapturePokemon

botAplication = Flask(__name__)

# ========== Endpoints ==========
@botAplication.route("/define_pokemon/<name>", methods=["POST"])
def definePokemon(name):
    CapturePokemon.setNamePokemonBeighHunted(name)
    CapturePokemon.setPokemonSuccessfulyCaugth(name)
    return jsonify({"status": "Pokemon definido", "pokemon": CapturePokemon.getPokemonHunted()})

@botAplication.route("/define_area", methods=["GET"])
def defineArea():
    crop_area = getCoordenadas.select_area()
    return jsonify({"status": "Área definida", "coords": crop_area})

@botAplication.route("/start-capture/<name>", methods=["POST"])
def startCapture(name):
    CapturePokemon.checkCropAreaExists()
    CapturePokemon.setNamePokemonBeighHunted(name.lower())
    CapturePokemon.setConditionLoop(True)
    threading.Thread(target=CapturePokemon.loopCapture(), daemon=True).start()
    return jsonify({"status": "captura iniciada", "pokemon": CapturePokemon.getPokemonHunted()})

@botAplication.route("/stop-capture", methods=["GET"])
def stopCapture():
    CapturePokemon.setConditionLoop(False)
    return jsonify({"status": "captura parada"})

if __name__ == "__main__":
    def openBrowser():
        time.sleep(1)
        webbrowser.open("https://pokemon-hunting.vercel.app/")

    threading.Thread(target=openBrowser, daemon=True).start()
    botAplication.run(debug=True, port=5500, use_reloader=False)
