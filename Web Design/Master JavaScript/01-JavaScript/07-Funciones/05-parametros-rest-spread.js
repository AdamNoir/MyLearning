'use strict'

// Parametros REST y SPREAD

// rest
/**Es como varargs de java, o los kwarg de python.
 * Resiven muchos parametros y los almacenan en un array.
 */

function listadoFrutas(fruta1, fruta2, ...resto_frutas){
    console.log("Fruta 1: " + fruta1);
    console.log("Fruta 2: " + fruta2);
    console.log(resto_frutas);
}

listadoFrutas("Naranja", "Manzana", "Sandia", "Pera", "Melon", "Coco");

// SPREAD
/**
 * Toma un array y lo separa para que cada elemento sea un parametro unico
 */
var frutas = ["Naranja", "Manzana"];
listadoFrutas(...frutas, "Sandia", "Pera", "Melon", "Coco");