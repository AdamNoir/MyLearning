'use strict'

// LET Y VAR
/*La diferencia es el alcanze.
Var define una variable global o local sin importar donde este. Es decir que su contenido puede cambiar desde cualquier sitio.
Let define una variable limitada al alcance de su bloque. 
-- La buena practica es usar let en variables que solo usaremos dentro de bloques.*/
//VAR
var numero = 40;
console.log(numero); //40

if(true){
    var numero = 50;
    console.log(numero); // 50
}

console.log(numero); // 50

// LET
let texto = "Hola let";
console.log(texto); //hola let

if(true){
    let texto = "Adios let"; //adios let
    console.log(texto);
}

console.log(texto); // hola let

// Otro ejemplo var let
var a = 5;
var b = 10;
 
if (a === 5) {
  let a = 4; // El alcance es dentro del bloque if
  var b = 1; // El alcance es dentro de la función
 
  console.log(a);  // 4
  console.log(b);  // 1
}
 
console.log(a); // 5
console.log(b); // 1