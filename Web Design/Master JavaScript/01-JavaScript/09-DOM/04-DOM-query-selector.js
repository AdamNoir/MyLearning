'use strict'

var id = document.querySelector("#encabezado");
console.log(id);

// Query selector devuelve solo un valor al selcccionr ya sea por clase
// aun cuando haya muchos
var claseRojo = document.querySelector(".rojo");
console.log(claseRojo);

// query selector all devuelve todos los elementos en una NodeList
var claseRojoArray = document.querySelectorAll(".rojo");
console.log(claseRojoArray)