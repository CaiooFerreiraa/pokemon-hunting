export function extractTypes(types = []) {
  return types.map(t => capitalize(t.type?.name ?? ""));
}

export function capitalize(str = "") {
  return str[0]?.toUpperCase() + str.slice(1);
}

export function formatName(name) {
  return name ? capitalize(name) : "Selecione um Pokemon";
}

export function getSpriteUrl(sprite) {
  return sprite?.front_default ?? "/pokebola.png";
}

export function extractAbilities(abilities = []) {
  return abilities.map(a => capitalize(a.ability?.name ?? ""));
}