export default function PokemonActions({ pokemonForCatch }) {
  const name = pokemonForCatch?.name;

  const handleCapture = () => {
    fetch(`http://127.0.0.1:5500/capture`)
      .then((res) => res.json())
      .then((res) => console.log(res))
      .catch(err => console.error(err))
  }

  const handleSend = () => {
    fetch(`http://127.0.0.1:5500/start-capture/${name}`)
      .then((res) => res.json())
      .then((res) => console.log(res))
      .catch(err => console.error(err))
  }

  const handleStop = () => {
      fetch(`http://127.0.0.1:5500/stop-capture`)
        .then((res) => res.json())
        .then((res) => console.log(res))
        .catch(err => console.error(err))
  }

  return (
    <div id="buttons-actions">
      <button onClick={handleCapture}>Start Hunting</button>
      <button onClick={handleSend}>Send to Bot</button>
      <button onClick={handleStop}>Mark Aound</button>
    </div>
  )
} 