'use strict'

// Metodos textos

// Tranformacion de textos
var numero = 444;
var texto1 = "Bienvenidos a js";
var texto2 = "es buen lenguaje";

var dato = numero.toString(); // Convierete a un string
    dato = texto1.toUpperCase(); // todo a mayusculas
    dato = texto2.toLowerCase(); // todo a minusculas

// calcular longitud
var nombre = "Ivan";
console.log(nombre.length);
var nombres = ["Ivan", "Fer"];
console.log(nombres.length);

// concatenar textos
var textoTotal = texto1.concat(" " + texto2);
console.log(textoTotal)