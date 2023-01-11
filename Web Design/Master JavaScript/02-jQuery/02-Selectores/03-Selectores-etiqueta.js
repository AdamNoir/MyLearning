$(document).ready(function(){
    console.log("jQuery Cargado en 03-Selectores-etiqueta")

    var parrafos = $("p").css("cursor", "pointer");

    parrafos.click(function(){
        // Ayuda a optimizar al almacenar el valor del dom en una variable
        var mi_this = $(this);

        // Si no tiene clase
        if(!mi_this.hasClass("grande")){
            // agregamos
            mi_this.addClass("grande");
        }else{
            // si la tiene la removemos.
            mi_this.removeClass("grande");
        }
    });
});