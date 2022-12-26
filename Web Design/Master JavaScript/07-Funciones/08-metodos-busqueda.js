'use strict'

// Metodos buscar
var numero = 444;
var texto1 = "Bienvenidos a js";
var texto2 = "es buen lenguaje";

// Desde que indice empieza
var busqueda = texto2.indexOf("buen");
console.log(busqueda);

var busquedaUltimo = texto2.lastIndexOf("buen");
console.log(busquedaUltimo);

// Otro metodo para buscar
var busquedaSearch = texto2.search("buen");
console.log(busquedaSearch);

// Muestra un array con informacion de todas las coincidencias
var busquedaMatch = texto2.match("buen");
console.log(busquedaMatch);

// Substraer String
var subtraer = texto1.substring(2, 10);
console.log(subtraer)

// En base a un indice saca un caracter
var caracter = texto2.charAt(2);
console.log(caracter);

// Revisa si un texto comienza con el string (true o false)
var comenzar = texto1.startsWith("Bien");
console.log(comenzar);

// Revisa si un texto termina con el string (true o false)
var terminar = texto1.endsWith("Bien");
console.log(terminar);

// revisa si se incluye o no el string (true, false)
// Revisa si un texto comienza con el string (true o false)
var incluye = texto1.includes("js");
console.log(incluye);