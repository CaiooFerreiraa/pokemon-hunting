import { useEffect, useState } from "react"
import "./css/SearchBar.css"

export default function SearchBar({ setPokemonForCatch }) {
  const [pokemonList, setPokemonList] = useState([]);
  let [offSetPokemon, setOffSetPokemon] = useState(0);

  useEffect(() => {
    fetch(`https://pokeapi.co/api/v2/pokemon?limit=12&offset=${offSetPokemon}`)
      .then(res => res.json())
      .then(data => setPokemonList(data.results))
      .catch(error => console.error("Erro ao buscar pokémons:", error));
  }, [offSetPokemon]);

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
      <div id="search-container">
        <div>
        <form onSubmit={handleSearchPokemon}>
          <input
            type="text"
            id="search-input"
            placeholder="Search a Pokemon..."
            autoComplete="off"
          />
          <button type="submit" className="material-symbols-outlined">search</button>
        </form>
      </div>
        {
          pokemonList.map((pokemon, index) => {
            const nameFormated = pokemon.name[0].toUpperCase() + pokemon.name.substring(1);
            return (
              <button key={index} onClick={() => fetchPokemonByName(pokemon.name)} className="search_button">{nameFormated}</button>
            )
          })
        }
        <div className="buttons_navigate"> 
          {
            offSetPokemon >= 12 && <button onClick={() => {setOffSetPokemon(prev => prev - 12)}} className="material-symbols-outlined previous">line_start_arrow_notch</button>
          }
          <button onClick={() => {setOffSetPokemon(prev => prev + 12)}} className="material-symbols-outlined next">line_end_arrow_notch</button>
        </div>
      </div>
    </div>
  )
}