'use strict'

/*Utilizando un bucle, mostrar la suma, y media de los numeros introducids
hasta introducir un numero negativo y mostrar resultados*/

var suma = 0;
var contador = 0;

do{
    var numero = parseInt(prompt("Ingresa un numero: "));

    if(isNaN(numero)){
        numero = 0;
    }else if(numero > 0){
        suma = suma + numero;
        contador++;
    }
}while(numero >= 0);

alert("La suma es: " + suma);
alert("La media es: " + suma/contador);