$(document).ready(function(){
    
    console.log("01 Dom y textos cargado");
    reloadLinks();

    $("#add_button").click(function(){
        //console.log($("#add_link").val());
        /**
         * HTML - agrega contenido html encima de lo demas. Borrando.
         * prepend - agrega al inicio de la lista
         * before - agrega antes de que comience el elemento html
         * after - agrega despues de terminar el elemento HTML
         */
        $("#menu").append('<li><a href="' + $("#add_link").val() + '"></a></li>');

        // Limpiar input con contenido vacio
        $("#add_link").val("");

        reloadLinks();
    })

});

function reloadLinks(){
    $("a").each(function(index){
        //console.log($(this))
        var that = $(this);
        // Obtener contenido del attributo
        var enlace = that.attr("href");
        // Agregar atributo
        that.attr("target", "_blank");
        // Eliminar atributi
        that.removeAttr("target");
        that.text(enlace);
    });
}