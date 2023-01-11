$(document).ready(function(){
    console.log("04-Ajax.js");

    //  Ajax con fumulario
    $("#formulario").submit(function(e){
        e.preventDefault(); // Para no redirigr

        var usuario = {
            name: $('input[name="name"]').val(),
            job: $('input[name="job"]').val()
        }

        $.ajax({
            type: "POST", // Metodo http
            dataType: "json", // Tipo de dato que recibe
            contentType: "application/json", // Tipo de dato recibimos
            url: $(this).attr("action"), // a donde se enviara
            beforeSend: function(){ // Se ejecuta antes de inicar la peticion
                console.log("Enviando...");
            },
            success: function(response){ // Se ejecuta cuando haya terminado con exito
                console.log(response)
            },
            error: function(){ // Se ejecuta si da un error
                console.log("Error.");
            },
            timeout: 10000 // Cuanto tiempo puede demorar
        });

        return false;
    });
});