'use strict'

var formulario = document.querySelector("#formMovies");

formulario.addEventListener("submit", function(){
    console.log("Entra");
    var titulo = document.querySelector("#addMovie").value;
    localStorage.setItem(titulo, titulo);
});

var ul = document.querySelector("#pelisList");

for(var i in localStorage){
    if(typeof localStorage[i] == "string"){
        var li = document.createElement("li");
        li.append(localStorage[i]);
        ul.append(li);
    }
}

var formularioDelete = document.querySelector("#formMoviesDelete");

formularioDelete.addEventListener("submit", function(){
    console.log("Entra");
    var titulo = document.querySelector("#deleteMovie").value;
    localStorage.removeItem(titulo);
});