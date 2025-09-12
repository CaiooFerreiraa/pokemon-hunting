export default function PokemonActions({ pokemonForCatch }) {
  const name = pokemonForCatch?.name;

  const handleCapture = () => {
    fetch(`http://127.0.0.1:5500/capture`)
      .then(responseBotPython => responseBotPython.json())
      .then(responseMenssage => console.log(responseMenssage))
      .catch(err => console.error(err))
  }

  const handleSend = () => {
    fetch(`http://127.0.0.1:5500/start-capture/${name}`)
      .then(responseBotPython => responseBotPython.json())
      .then(responseMenssage => console.log(responseMenssage))
      .catch(err => console.error(err))
  }

  const handleStop = () => {
      fetch(`http://127.0.0.1:5500/stop-capture`)
        .then(responseBotPython => responseBotPython.json())
        .then(responseMenssage => console.log(responseMenssage))
        .catch(error => console.error(error))
  }

  return (
    <div id="buttons-actions">
      <button onClick={handleCapture}>Start Hunting</button>
      <button onClick={handleSend}>Send to Bot</button>
      <button onClick={handleStop}>Mark Aound</button>
    </div>
  )
} 