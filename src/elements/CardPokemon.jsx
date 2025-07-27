import PokemonActions from "./components/PokemonActions";
import PokemonForm from "./components/PokemonForm";
import PokemonImage from "./components/PokemonImage";
import PokemonLog from "./components/PokemonLog";
import "./css/CardPokemon.css"


export default function CardPokemon({ pokemonForCatch }) {
  return (
    <div id="main-card-pokemon">
      <div id="card-pokemon">

        <PokemonImage pokemonForCatch={pokemonForCatch}/>
        <div id="body-pokemon">
          <PokemonForm pokemonForCatch={pokemonForCatch}/>
          <PokemonActions />
        </div>
      </div>
      <PokemonLog />
    </div>
  )
}