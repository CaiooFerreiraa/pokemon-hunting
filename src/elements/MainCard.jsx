import CardPokemon from "./CardPokemon"
import "./css/MainCard.css"

export default function MainCard({ pokemonForCatch }) {
  return (
    <div id="main-card">
      <img src="..." alt="Aqui é a imagem do personagem" id="img-trainner"/>
      <CardPokemon pokemonForCatch={pokemonForCatch}/>
    </div>
  )
}