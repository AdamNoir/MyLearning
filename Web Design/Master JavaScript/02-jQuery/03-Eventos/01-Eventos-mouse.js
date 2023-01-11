$(document).ready(function(){
    console.log("jQuery Cargado 01-Eventos-Mouse.js")

    // Mouse over y moue out

    var caja = $("#caja");

    // MouseOver
    caja.mouseover(function(){
        $(this).css("background", "red");
    });

    // MouseOut
    caja.mouseout(function(){
        $(this).css("background", "green");
    });

    // MouseDown y MouseUP
    var datos = $("#datos");

    // MouseDown - Cuando presiono
    datos.mousedown(function(){
        $(this).css("border-color", "green")
    });

    // MouseUp - Cuando suelto
    datos.mouseup(function(){
        $(this).css("border-color", "black")
    });

    //MouseMove
    $(document).mousemove(function(){
        console.log("En X: " + event.clientX);
        console.log("En Y: " + event.clientY);

        $("body").css("cursor", "none");

        var sigueme = $("#sigueme");
        sigueme.css("left", event.clientX);
        sigueme.css("top", event.clientY);
    });
});