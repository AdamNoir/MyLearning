'use strict'

// condicional switch
var edad = 18;
var imprime = "";

switch(edad){
    case 18:
        imprime = "Acabas de cumplir mayoria de edad";
    break;
    case 25:
        imprime = "Ya eres adulto";
    break;
    case 40:
        imprime = "Crisis de los cuarente";
    break;
    case 75:
        imprime = "Eres un anciano";
    break;
    default:
        imprime = "Tu edad es neutra";
    break;
}

console.log(imprime)