// Lo primero que se hace con jQuery es ver que toda la pagina esta cargada
// document es toda la pagina, ready es un evento y con la funcion ejecutamos lo que queramos

// $ y jQuery es lo mismo.
$(document).ready(function(){
    console.log("JQUERY LISTO!!")

    // SELECTORES
    var rojo = $("#rojo").css("background", "red")
        .css("color", "white");
    
    // Podemos igualmente almacenar el contenido en una variable
    console.log(rojo);

    $("#amarillo").css("background", "yellow")
        .css("color", "green");

    $("#verde").css("background", "green")
        .css("color", "white");
});