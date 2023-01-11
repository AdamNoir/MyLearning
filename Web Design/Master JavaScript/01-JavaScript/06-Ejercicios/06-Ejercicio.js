'use strict'

/**
 * Pedir un numero por promt y ver si es par o impar
 * si no es valido volver a pedir el numero
 */

var numero = parseInt(prompt("Ingresa un numero"));

while(numero < 0 || isNaN(numero)){
    var numero = parseInt(prompt("Ingresa un numero"));
}

if(numero % 2 == 0){
    alert("Numero es par");
}else{
    alert("Numero No es par");
}