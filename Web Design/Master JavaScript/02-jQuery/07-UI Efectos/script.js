$(document).ready(function(){
    console.log("07-UI Efectos")

    // Efectos
    $("#mostrar").click(function(){
        // $(".caja-efectos").fadeToggle();
        
        // $(".caja-efectos").effect("explode");
        
        // $(".caja-efectos").toggle("explode");
        // $(".caja-efectos").toggle("blind");
        // $(".caja-efectos").toggle("slide");
        // $(".caja-efectos").toggle("drop");
        // $(".caja-efectos").toggle("fold");
        // $(".caja-efectos").toggle("puff");
        // $(".caja-efectos").toggle("scale");
        $(".caja-efectos").toggle("shake", 4000);
    });
});