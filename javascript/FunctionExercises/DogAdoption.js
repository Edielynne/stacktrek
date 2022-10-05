
let dog = ["Peipei", "Sherky", "Panpan"]
let age = [6 , 2 , 1]
let images = ["1.jpg", "2.jpg", "3.jpg"]
let toys = [["bone", "water", "ball"], ["shoes","duck", "tissue"], ["slippers", "wire", "stufftoy"]]
let name = ""
let dog_age = ""
let dog_image = ""
let dog_toy = ""
let adoption = ""


for (let i = 0; i < dog.length; i++){
        name = dog[i] 
        dog_age = age[i]
        dog_image = images[i]
        dog_toy = toys [i].join(",");
        adoption = ` <div id="box">
        Name:${name} <br> Age:Your doggie is ${dog_age} years old in dog years <br> 
        <img src="${dog_image}"> <br> fave toys: ${dog_toy}
        </div><br>`

        document.getElementById("data").innerHTML += adoption;
    }
    



