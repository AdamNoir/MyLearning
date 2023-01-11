'use strict'

// Metodos reemplazar
var numero = 444;
var texto1 = "Bienvenidos a js";
var texto2 = "       es buen lenguaje             ";

// Remplaza un texto por otro
var reemplazar = texto1.replace("js", "JavaScript")
console.log(reemplazar);

// Corta a partir de un indice indidcado
var cortar = texto1.slice(5)
console.log(cortar);

// Haace un array separando elementos por el caracter indicado
var hacerSplit = texto1.split(" ");
console.log(hacerSplit);

// Borra espacios al principio o final del texto
// Remplaza un texto por otro
var quitarEspacios = texto2.trim();
console.log(quitarEspacios);