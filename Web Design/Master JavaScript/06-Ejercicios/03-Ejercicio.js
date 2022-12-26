'use strict'
/** 
 * Pedir dos numeros y mostrar todos los numeros que hay entre ellos.
*/
var numero1 = parseInt(prompt("Ingresa un numero"));
var numero2 = parseInt(prompt("Ingresa un segundo numero"))

// Con document podemos escribir dese js en html
// Podemos escribir etiquetas para que trabaje como un elemento html
document.write("<h1>Del numero" + numero1 + " al numero " + numero2 + "</h1>")
for(var i = numero1 + 1; i < numero2; i++){
    //console.log(i);
    document.write(i + "<br/>")
}