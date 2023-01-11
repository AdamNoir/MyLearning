'use strict'

/*Pedir dos numeros y decir cual es mayor, el menor o si son iguales
Si los numero no son un numero o son 0, volverlos a pedir*/

// ParseInt para convertir de string a numero.
var numero1 = parseInt(prompt("Ingresa un numero: "));
var numero2 = parseInt(prompt("Ingrersa otro numero: "));

//isNaN (not a number) determina si es un numero u otra cosa. True cuando no es numero.
while(numero1 <= 0 || numero2 <= 0 || isNaN(numero1) || isNaN(numero2)){
    var numero1 = parseInt(prompt("Ingresa un numero: "));
    var numero2 = parseInt(prompt("Ingrersa otro numero: "));
}

if(numero1 > numero2){
    alert("Numero 1 es mayor");
}else if(numero2 > numero1){
    alert("Numero 2 es mayor")
}else if(numero1 == numero2){
    alert("Los numeros son iguaes");
}else{
    alert("Algo no salio bien.")
}