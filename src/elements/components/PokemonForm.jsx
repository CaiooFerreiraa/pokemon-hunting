import { extractTypes, extractAbilities } from "../../UtilFunctions"

export default function PokemonForm({pokemonForCatch}) {
  const types = extractTypes(pokemonForCatch?.types)
  const abilities = extractAbilities(pokemonForCatch?.abilities)

  return (
    <div className="component-form">
      <div id="content-type">
        <label>Type: </label>
        <span className="type">{
          types.map((type, index) => {
            return (<span key={index}>{type}</span>)
          })}
        </span>
      </div>

      <div>
        <label htmlFor="abilitys">Abilities: </label>
        <select name="abilitys" id="abilitys">
          {
            abilities.map((ability, index) => {
              return (
                <option value={ability} key={index}>{ability}</option>
              )
            })
          }
        </select>
      </div>
    </div>
  )
}