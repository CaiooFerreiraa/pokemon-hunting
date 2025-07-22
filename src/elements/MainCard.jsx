import CardPokemon from "./CardPokemon"
import "./css/MainCard.css"

export default function MainCard({ pokemonForCatch }) {
  return (
    <div id="main-card">
      <div className="img-container">
        <img src="/src/assets/avatar.png" alt="Aqui é a imagem do personagem" id="img-trainner"/>
      </div>
      <CardPokemon pokemonForCatch={pokemonForCatch}/>
    </div>
  )
}