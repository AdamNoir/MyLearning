$(document).ready(function(){
    console.log("Evento click y doble click cargado.");

    var caja = $("#caja");

    caja.click(function(){
        $(this).css("background", "pink")
                .css("color", "white");

    });

    caja.dblclick(function(){
        $(this).css("background", "brown")
                .css("color", "red");
    });
});