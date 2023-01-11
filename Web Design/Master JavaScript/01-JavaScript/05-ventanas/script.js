'use strict'

//Ventanas y alertas

// Alerta
alert("Esta es mi alerta!");

// Confirmacion
confirm("¿Continuar?");
// El resultado booleano se puede almacenar en variable
var resultado = confirm("¿Desea continuar?");
console.log(resultado, typeof(resultado));

// Ingreso de informacion
// Primero el mensaje y un valor por defecto
// Puede qudar vacio y no hara nada.
prompt("¿Edad?");
// El resultado puede almacenarse en una variable. Siempre sera string.
var resultado_prompt = prompt("Pais", "Mexico");
console.log(resultado_prompt, typeof(resultado_prompt));