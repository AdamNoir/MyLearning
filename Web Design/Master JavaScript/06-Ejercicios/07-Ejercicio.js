'use strict'
/**
 * Tabla de multiplicar de un numero ingresado
 */

var numero = parseInt(prompt("Ingresa un numero entero"));
var resultado = 0;
document.write("<h1>Tabla del " + numero + "</h1>");

for(var i = 0; i <= 10; i++){
    resultado = numero * i;
    document.write("<p>" + numero + "X" + i + " = " + resultado + "</p>");
}