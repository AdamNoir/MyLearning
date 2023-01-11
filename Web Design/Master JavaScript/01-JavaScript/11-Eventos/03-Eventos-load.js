'use stric'

/**
 * Este evento se prepara cuando los elementos del dom esten carcagos.
 * Asi podemo trabajarlos desde la etqieuta de head, siendo esta el lugar
 * mas recomendado para cargar todo el contenido de JS y no al final.
 */
// funciona con window
window.addEventListener("load", function(){
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
});