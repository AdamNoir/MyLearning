'use strict'

// DOM - Document Object Model

// Conseguir elementos con un ID

//Funcion para cambiar el color
function cambiaColor(color){
    caja.style.background = color;
}

// tomar valores por su id
//var caja = document.getElementById("caja");

// Podemos seleccionar todos los elementos como si se CSS se tratara
var caja = document.querySelector("#caja");
console.log(caja.innerHTML);

// innerHTML permite obtener el contenido HTML y cambiarlo
caja.innerHTML = "TEXTO DESDE JS";
// Se le pueden modificar los colores usando propiedades css
caja.style.background = "red";
caja.style.padding = "20px";
caja.style.color = "white";
// Podemos agregar atributos como nombres de clase
caja.className = "className";

console.log(caja)