'use strict'

// DOM - Document Object Model

// Conseguir todos los elementos por su clase
var divRojos = document.getElementsByClassName("rojo");
var divAmarillos = document.getElementsByClassName("amarillo");
divAmarillos[0].style.background = "yellow";
// No se puede aplicar estilos en conjunto, pues un array
// recorremos elementos y cambiamos estilos uno por uni
for(var div in divRojos){
    // Verifica que sea un div, pues trae cosas propias del dom
    if(divRojos[div].className == "rojo"){
        divRojos[div].style.background = "red";
    }
}

console.log(divRojos);
