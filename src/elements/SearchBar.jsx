import { useEffect, useState } from "react"
import "./css/SearchBar.css"
import { capitalize } from "../UtilFunctions";

export default function SearchBar({ setPokemonForCatch, fetchError, setFerchError }) {
  const [pokemonList, setPokemonList] = useState([]);
  const [offSetPokemon, setOffSetPokemon] = useState(0);

  useEffect(() => {
    fetch(`https://pokeapi.co/api/v2/pokemon?limit=12&offset=${offSetPokemon}`)
      .then(responseApi => responseApi.json())
      .then(data => setPokemonList(data.results))
      .catch(error => setFerchError(error));
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
      .then(responseApi => {
        if (!responseApi.ok) throw new Error("Pokemon não encontrado ou nome incorreto");
        return responseApi.json();  
      })
      .then(foundPokemon => {
        setPokemonForCatch(foundPokemon);
        setFerchError(null);
      })
      .catch((error) => setFerchError(error));
  }

  return (
    <div id="search-main">
      <div id="search-container">
        <div className="search-form">
          <form onSubmit={handleSearchPokemon}>
            <input
              type="text"
              id="search-input"
              placeholder="Search a Pokemon..."
              autoComplete="off"
            />
            <button type="submit" className="material-symbols-outlined">search</button>
          </form>
          {
            fetchError != null && <div className="error-container">{fetchError.message}</div>
          }
        </div>
        {
          pokemonList.map((pokemon, index) => {
            return (
              <button key={index} onClick={() => fetchPokemonByName(pokemon.name)} className="search_button">{capitalize(pokemon.name)}</button>
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