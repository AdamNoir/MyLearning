$(document).ready(function(){
    console.log("jQuery cargado evento Hover");

    var caja = $("#caja");

    // Funcion
    function cambiaColor1(){
        $(this).css("background", "blue");
    }

    function cambiaColor2(){
        $(this).css("background", "grey");
    }

    caja.hover(cambiaColor1, cambiaColor2);
});