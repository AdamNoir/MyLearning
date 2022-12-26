'use strict'

// Funciones Anonimas
// Funciones que no tienen nombre
var pelicula = function(nombre){
    return "La pelicula es: " + nombre;
}

// Callback
// Son funciones que llaman a otras funciones
function sumame(numero1, numero2, sumaYresta, sumaPorDos){
    var sumar = numero1 + numero2;

    sumaYresta(sumar);
    sumaPorDos(sumar);

    return sumar;
}

sumame(5, 7, function(dato){
    console.log("La suma es: " + dato)
},
function(dato){
    console.log("La suma por dos es: " + (dato*2))
});

// Funciones Flecha
/**
 * Son funciones anonimas pero usamos => en vez de funtion
 * - SI solo es un parametro puede ir sin parentesis
 * - SI tiene varios van entre parentesis
 * - Parentesis vacios cuadno no ocupa parametros
 * 
 */
sumame(10, 10, dato => {
    console.log("La suma es: " + dato)
},
dato => {
    console.log("La suma por dos es: " + (dato*2))
});