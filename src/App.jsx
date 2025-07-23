import SearchBar from "./elements/SearchBar"
import MainCard from "./elements/MainCard"
import './index.css'
import { useState } from "react"

export default function App() {
  const [pokemonForCatch, setPokemonForCatch] = useState({});
  const [fetchError, setFerchError] = useState(null);

  function handleNextPokemon() {
    const nextPokemonId = pokemonForCatch.id + 1;
    if (nextPokemonId == null) return

    fetchPokemonById(nextPokemonId)
  }

  function fetchPokemonById(id) {
    fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
      .then(response => {
        if (!response.ok) throw new Error("O id não foi encontrado")
        
        return response.json();
      })
      .then(foundPokemon => {
        setPokemonForCatch(foundPokemon);
        setFerchError(null);
      })
      .catch(error => setFerchError(error));
  }

  return (
    <div id="grid-main">
        <SearchBar pokemonForCatch={pokemonForCatch} setPokemonForCatch={setPokemonForCatch} fetchError={fetchError} setFerchError={setFerchError}/>
        <div id="main-content">
          <MainCard pokemonForCatch={pokemonForCatch}/>
          <button id="next_pokemon" onClick={() => {handleNextPokemon()}}>Próximo Pokemon</button>
        </div>
    </div>
  )
}