$(document).ready(function(){
    console.log("jQuery cargado desde 05");

    // Selecciona varios elementos por etiqueta
    $("p, a").addClass("margen-superior");

    // Busca un elemento en el dom
    var busqueda = $("#caja").find(".resaltado");
    console.log(busqueda);

    // parren va subiendo niveles en el dom
    var busqueda2 = $("#elemento").parent().parent().find(".resaltado");
    console.log(busqueda2);
});