const Ceil = (arr,ceiling)  => {
   return arr.filter(function (pokemon){
      return pokemon.power >= ceiling
        
    })
}
module.exports = {Ceil}