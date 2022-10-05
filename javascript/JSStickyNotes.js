let text_data = []
let color = ["pink","blue","yellow"]

function addnote(){
    let t = document.getElementById ("text").value
    text_data.push(t);
    console.log(text_data);

    let note = ""

    for (let i = 0; i<text_data.length; i++){
        note += `<div id= innerdiv>${text_data[i]} </div><br>`
    }
    document.getElementById("text_data").innerHTML = note;
}


