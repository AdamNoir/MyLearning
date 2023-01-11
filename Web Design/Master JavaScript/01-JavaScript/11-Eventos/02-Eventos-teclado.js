'use strict'

//EVENTOS
/**
 * Los eventos son funciones que se ejecutan cada que sucede algo, como dar click, hacer scroll,
 * escribir en un input.
 */


// Eventos teclado
var input = document.querySelector("#campo_nombre");

// Focus - seleccionar el input
input.addEventListener('focus', function(){
    console.log("[focus] - Estas dentro del input");
});

// Blur - salir del input
input.addEventListener("blur", function(){
    console.log("[blur] - Estas fuera del input");
});

// Keydown
input.addEventListener("keydown", function(event){
    console.log("[keydown] - Pulsando la tecla: ", String.fromCharCode(event.keyCode));
});

// Keypress
input.addEventListener("keypress", function(event){
    console.log("[keypress] - Tecla presionada: ", String.fromCharCode(event.keyCode));
});

// Keyup
input.addEventListener("keyup", function(event){
    console.log("[Keyup] - Tecla soltada: ", String.fromCharCode(event.keyCode));
});