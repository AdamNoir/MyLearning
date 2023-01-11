'use strict'

//EVENTOS
/**
 * Los eventos son funciones que se ejecutan cada que sucede algo, como dar click, hacer scroll,
 * escribir en un input.
 */

// Eventos del raton
/**
 * Aunque existe el atributo onclick y el ondblclik en html,
 * lo mejor es tener todo eso en un archivo JS usando un eventListener
 */

function cambiarColorBoton(){
    console.log("Me has presionado");
    var bg = boton.style.background;
    if(bg == "green"){
        boton.style.background = "red";
    }else{
        boton.style.background = "green";
    }
    boton.style.padding = "10px";
    boton.style.border = "1ox solid #ccc";

    return true;
}

var boton = document.querySelector("#boton");
// Estara atento a cualquier click se se le d al boton seleccionado"
// Evento click - cuando damos click al elemento
boton.addEventListener("click", function(){
    cambiarColorBoton();
});

// Evento mouse over - cuando pasamos el mouse por encima
boton.addEventListener("mouseover", function(){
    boton.style.background = "#ccc";
})

// Evento mouseOut - cuando el mouse sale del elemento
boton.addEventListener("mouseout", function(){
    boton.style.background = "yellow";
})
