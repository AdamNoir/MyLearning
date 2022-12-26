'use strict'

//Funciones

function miFuncion(){
    console.log("Hola soy una funcion");
    console.log("Si soy una funcion");

    return "Hola funcion1";
}

// Las funciones pueden llamarse de varios modos
// Guardando en variable (si devuelve algo)
var laFuncion = miFuncion();
console.log(laFuncion)
// Imprimir en consola (si tiene logs)
console.log(miFuncion);
// Llamar directamente.
miFuncion();