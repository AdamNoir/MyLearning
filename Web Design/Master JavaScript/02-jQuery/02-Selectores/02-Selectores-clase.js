$(document).ready(function(){
    console.log("jQuery Cargado!");

    // Selectores de Clase
    var mi_clase = $(".zebra");
    
    console.log(mi_clase);

    //mi_clase.css("border", "5px dashed black");

    // Agregara la clase al elemento al darle click.
    // Lo estilos que debe cargar estan el html
    $(".sin_borde").click(function(){
        console.log("Has dado click");
        $(this).addClass("zebra");
    });
});