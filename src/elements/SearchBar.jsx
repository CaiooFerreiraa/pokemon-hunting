import { useEffect, useState } from "react"
import "./css/SearchBar.css"

export default function SearchBar({ setPokemonForCatch }) {
  const [pokemonList, setPokemonList] = useState([]);
  let [offSet, setOffSet] = useState(0);

  useEffect(() => {
    fetch(`https://pokeapi.co/api/v2/pokemon?limit=12&offset=${offSet}`)
      .then(res => res.json())
      .then(data => setPokemonList(data.results))
      .catch(error => console.error("Erro ao buscar pokémons:", error));
  }, [offSet]);

  function handleSearchPokemon(event) {
    event.preventDefault()
    const namePokemonForSearch = getPokemonNameFromEvent(event);
    if (!namePokemonForSearch) return

    fetchPokemonByName(namePokemonForSearch)
  }

  function getPokemonNameFromEvent(event) {
    const input = event.target.querySelector("input");
    return input?.value.trim().toLowerCase();
  }

  function fetchPokemonByName(name) {
    fetch(`https://pokeapi.co/api/v2/pokemon/${name}`)
      .then(res => res.json())
      .then(foundPokemon => {
        setPokemonForCatch(foundPokemon)
      })
      .catch((error) => console.error("Houve um erro ao buscar o pokemon: " + error))
  }

  return (
    <div id="search-main">
      <div>
        <form onSubmit={handleSearchPokemon}>
          <input
            type="text"
            id="search-input"
            placeholder="Search a Pokemon..."
            autoComplete="off"
          />
          <button type="submit">Search</button>
        </form>
      </div>
      <div>
        {
          pokemonList.map((pokemon, index) => {
            return (
              <button key={index} onClick={() => fetchPokemonByName(pokemon.name)}>{pokemon.name}</button>
            )
          })
        }
        <div> 
          <button onClick={() => {setOffSet(prev => prev + 12)}}>Mais</button>
          {
            offSet >= 12 && <button onClick={() => {setOffSet(prev => prev - 12)}}>Menos</button>
          }
          
        </div>
      </div>
    </div>
  )
}