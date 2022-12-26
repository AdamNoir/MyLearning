'use strict'

/**
 * Calculadora
 * - Pedir dos numeros
 * - Si metemos mas el numero nos los pide again
 * - Mostrar en el cuerpo, alerta y consola los resultados de la suma,
 * resta, multiplicacion y division.
 */

var numero1 = parseInt(prompt("Ingresa un numero"));
var numero2 = parseInt(prompt("Ingresa un segundo numero"));

while(isNaN(numero1) || isNaN(numero2)){
    var numero1 = parseInt(prompt("Ingresa un numero"));
    var numero2 = parseInt(prompt("Ingresa un segundo numero"));
}

var suma = "La suma de los numeros es: " + (numero1 + numero2);
var resta = "La resta de los numeros es: " + (numero1 - numero2);
var multiplicacion = "La multiplicacion de los numeros es: " + (numero1 * numero2);
var divison = "La suma de los numeros es: " + (numero1 / numero2);

var todo = suma + " " + resta + " " + multiplicacion + " " + divison;

document.write(todo);
alert(todo);
console.log(todo);