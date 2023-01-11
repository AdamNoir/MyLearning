'use strict'

// Localstorage

// Comprobar disponiblidad del localstorage

if(typeof(Storage) != 'undefined'){
    console.log("Localstorage disponible");
}else{
    console.log("Incompatible con localstorage");
}

// Guardar datos 
localStorage.setItem("titulo", "contenido de titulo en localstorage");

// recuperar dato
var titulo = localStorage.getItem("titulo");
console.log(titulo);

// REcuperar dato y mostrarlo en pagina
//document.querySelector("#dato").innerHTML = localStorage.getItem("titulo");

// Guardar json
var usuario = {
    nombre: "Ivan",
    edad: 24,
    correo: "correo@correo.com"
}

// Usamos stringify para volver el json un string
localStorage.setItem("usario", JSON.stringify(usuario));

// Recuperar JSON
// usamos parse para pasarlo de string a un objeto json usanble
var miJson = JSON.parse(localStorage.getItem("usuario"));

// borra una variable delo localstoraga
localStorage.removeItem("usuario");
// borra todo el local strogae
localStorage.clear();