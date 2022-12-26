'use strict'
/**
 * Pedir un numero y mostrar todos los numeros divisiores de ese numero.
 */

var numero = parseInt(prompt("Ingresa un numero"));

for(var i = 1; i <= numero; i++){
    if(numero % i == 0){
        console.log(i);
    }
}