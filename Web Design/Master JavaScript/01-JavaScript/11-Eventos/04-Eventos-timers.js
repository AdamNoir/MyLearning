'use strict'

window.addEventListener("load", function(){
    // Timers

    // Interval - ejecuta codigo cada cierto tiempo indicado
    var tiempo = this.setInterval(function(){
        console.log("Set interval ejecutado.");
        var encabezado = document.querySelector("h1");
        if(encabezado.style.fontSize == "50px"){
            encabezado.style.fontSize = "30px";
        }else{
            encabezado.style.fontSize = "50px";
        }
    }, 500);

    //Time Out - se ejecuta una sola vez pasado el tiempo indicado
    var tiempoOut = this.setTimeout(function(){
        console.log("Time out ejecutado.");
        var encabezado = document.querySelector("h1");
        if(encabezado.style.color != "red"){
            encabezado.style.color = "red";
        }else{
            encabezado.style.color = "blue";
        }
    }, 3000);

    // Detener Invervalo
    var stop = this.document.querySelector("#stop");
    stop.addEventListener("click", function(){
        alert("Has parado el intervalo en bucle");
        clearInterval(tiempo);
    });

});