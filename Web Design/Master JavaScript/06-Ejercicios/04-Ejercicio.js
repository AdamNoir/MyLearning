'use stric'

/**
 * Mostar todos los numeros imparaes dentro del rango de dos numeros
 */
var numero1 = parseInt(prompt("Ingresa un numero"));
var numero2 = parseInt(prompt("Ingresa un segundo numero"));

document.write("<h1>Impares del numero " + numero1 + "hasta el " + numero2 + "</h1>");
for(var i = numero1 + 1; i < numero2; i++){
    if(i%2 != 0){
        document.write(i + "<br/>");
    }
}