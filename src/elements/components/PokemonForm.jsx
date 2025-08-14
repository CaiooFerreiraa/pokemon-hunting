import { extractTypes, extractAbilities } from "../../UtilFunctions"
import Form from 'react-bootstrap/Form';

export default function PokemonForm({ pokemonForCatch }) {
  const types = extractTypes(pokemonForCatch?.types)
  const abilities = extractAbilities(pokemonForCatch?.abilities)

  return (
    <div className="component-form">
      <div id="content-type">
        <label>Type: </label>
        <span className="type">{
          types.map((type, index) => {
            return (<span key={index}>|{type}|</span>)
          })}
        </span>
      </div>

      <div id="content-abilities">
        <label htmlFor="abilitys">Abilities: </label>
        <Form.Select aria-label="Default select example">
          {
            abilities.map((ability, index) => {
              return (
                <option value={ability} key={index}>{ability}</option>
              )
            })
          }
        </Form.Select>
      </div>
    </div>
  )
}