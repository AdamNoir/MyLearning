'use strict'

//
function mostrarConsola(numero1, numero2){
    console.log(numero1 + numero2);
    console.log(numero1 - numero2);
    console.log(numero1 * numero2);
    console.log(numero1 / numero2);
}

function mostrarPantalla(numero1, numero2){
    document.write((numero1 + numero2) + "<br>");
    document.write((numero1 - numero2) + "<br>");
    document.write((numero1 * numero2) + "<br>");
    document.write((numero1 / numero2) + "<br>");
}

// Funcion principal
function calculadora(numero1, numero2, mostrar = false){
    if(mostrar == false){
        mostrarConsola(numero1, numero2);
    }else{
        mostrarPantalla(numero1, numero2);
    }
}

calculadora(1, 23);