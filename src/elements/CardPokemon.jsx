import "./css/CardPokemon.css"

export default function CardPokemon({ pokemonForCatch }) {
  const namePokemon = configureNamePokemon()
  const spritePokemon = checkSpritePokemon()

  function configureNamePokemon() {
    return pokemonForCatch.name != null && pokemonForCatch.name[0].toUpperCase() + pokemonForCatch.name.substring(1);
  }

  function checkSpritePokemon() {
    return pokemonForCatch.sprites != null ? pokemonForCatch.sprites.front_default : null;
  }

  return (
    <div id="main-card-pokemon">
      <div id="card-pokemon">
        <div className="img-pokemon-container">
          <img src={spritePokemon ? spritePokemon : "/pokebola.png"} alt="" />
        </div>
        <h1>{namePokemon ? namePokemon : "Selecione um Pokemon"}</h1>

        <div id="body-pokemon">
          <div>
            <label htmlFor="">Type: </label>
            <span>Aqui vai o tipo do pokemon</span>
          </div>
          <div>
            <label htmlFor="ability">Abilities: </label>
            <input type="text" name="ability" id="ability" />
          </div>
          <div>
            <label htmlFor="rota">Rota: </label>
            <input type="text" name="rota" id="rota" />
          </div>
          <div id="botoes">
            <button>Start Hunting</button>
            <button>Send to Bot</button>
            <button>Mark Aound</button>
          </div>
        </div>
      </div>
      <div id="log">
        aqui é o console.log
      </div>
    </div>
  )
}