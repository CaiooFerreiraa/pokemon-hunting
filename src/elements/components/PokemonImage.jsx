import { formatName, getSpriteUrl } from "../../UtilFunctions";

export default function PokemonImage({pokemonForCatch}) {
  const name = formatName(pokemonForCatch?.name);
  const sprite = getSpriteUrl(pokemonForCatch?.sprites);

  return (
    <div className="componente-image">
        <div className="img-pokemon-container">
          <img src={sprite ? sprite : "/pokebola.png"} alt="" />
        </div>
        <h1>{name ? name : "Selecione um Pokemon"}</h1>
    </div>
  )
}