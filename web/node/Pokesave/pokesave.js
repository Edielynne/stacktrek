const {Pokemons} = require ('./pokemon')
const {Ceil} = require ('./powerceiling');

const power = (n) => {
    return Ceil(Pokemons,n).map(function(pokemon){
        return pokemon.name
    });
}
console.log (power(51))
