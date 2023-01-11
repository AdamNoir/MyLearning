$(document).ready(function(){
    console.log("02 Efectos cargado.");

    $("#mostrar").hide();

    $("#mostrar").click(function(){
        $(this).hide();
        $("#ocultar").show();
        
        // Efecto de recogido
        //$("#caja").show("fast");

        // Velocidades - fast, slow, normal. O con milisegundos
        // Difumiado
        //$("#caja").fadeIn("slow");
        //$("#caja").fadeIn("slow", 0.9);
        $("#caja").slideDown("slow");
    });

    $("#ocultar").click(function(){
        $(this).hide();
        $("#mostrar").show();
        
        //$("#caja").hide("fast");
        
        // Difumiado
        //$("#caja").fadeOut("slow");
        //$("#caja").fadeOut("slow", 0.2);

        // Se ejcuta justo al acabar la animacion
        $("#caja").slideUp("slow", function(){
            console.log("Cartel oculato");
        });
    });

    // Usar un unico Boton
    // Efecto toggle
    $("#unico").click(function(){
        //$("#caja").toggle("fast");
        //$("#caja").fadeToggle("fast");
        $("#caja").slideToggle("fast");
    });
});