'use strict'

// Parametros Opciones
// Parametros que ya estan inicializados y no son necesarios. 
function calculadoraOpcional(numero1, numero2, mostrar = false){
    if(mostrar == false){
        console.log(numero1 + numero2);
        console.log(numero1 - numero2);
        console.log(numero1 * numero2);
        console.log(numero1 / numero2);
    }else{
        document.write((numero1 + numero2) + "<br>");
        document.write((numero1 - numero2) + "<br>");
        document.write((numero1 * numero2) + "<br>");
        document.write((numero1 / numero2) + "<br>");
    }
}
calculadoraOpcional(1, 2);
calculadoraOpcional(8, 9, true);