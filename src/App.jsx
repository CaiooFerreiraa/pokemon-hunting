import SearchBar from "./elements/SearchBar"
import MainCard from "./elements/MainCard"
import './index.css'
import { useState } from "react"

export default function App() {
  const [pokemonForCatch, setPokemonForCatch] = useState({});

  function handleNextPokemon() {
    const nextPokemonId = pokemonForCatch.id + 1;
    if (nextPokemonId == null) return

    fetchPokemonById(nextPokemonId)
  }

  function fetchPokemonById(id) {
    fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
      .then(response => response.json())
      .then(foundPokemon => setPokemonForCatch(foundPokemon))
      .catch(error => console.error("Houve um erro ao procurar o pokemon: " + error))
  }

  return (
    <div id="grid-main">
        <SearchBar pokemonForCatch={pokemonForCatch} setPokemonForCatch={setPokemonForCatch}/>
        <div id="main-content">
          <MainCard pokemonForCatch={pokemonForCatch}/>
          <button id="next_pokemon" onClick={() => {handleNextPokemon()}}>Próximo Pokemon</button>
        </div>
    </div>
  )
}