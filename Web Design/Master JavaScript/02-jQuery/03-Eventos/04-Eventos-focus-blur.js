$(document).ready(function(){
    console.log("Eventos focus y blur");

    // focus y blur
    var nombre = $("#nombre");


    nombre.focus(function(){
        $(this).css("border", "2px solid green");
    });

    nombre.blur(function(){
        $(this).css("boder", "2px solid red");
        // Mostrar div con datos ingresados al hacer blur (salir focus)
        $("#datos").text($(this).val()).show();
    });

});