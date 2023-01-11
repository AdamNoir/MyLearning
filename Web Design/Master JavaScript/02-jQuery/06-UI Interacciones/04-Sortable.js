$(document).ready(function(){
    $(".lista-seleccionable").sortable({
        update: function(event, ui){
            console.log("Ha cambiado la lista");
        }
    });
});