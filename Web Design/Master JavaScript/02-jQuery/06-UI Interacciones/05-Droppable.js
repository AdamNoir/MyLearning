$(document).ready(function(){

    $("#elemento-movido").draggable();

    $("#area").droppable({
        drop: function(){
            console.log("Dropeado");
        }
    });
});