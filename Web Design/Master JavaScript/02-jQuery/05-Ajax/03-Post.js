$(document).ready(function(){
    console.log("03-Post.js");

    // POST
    usuario = {
        name: "name",
        job: "job"
    }

    $.post("https://reqres.in/api/users", usuario, function(response){
        console.log(response)
    });

    // POST con formulario
    $("#formulario").submit(function(e){
        e.preventDefault(); // Para no redirigr

        var usuario = {
            name: $('input[name="name"]').val(),
            job: $('input[name="job"]').val()
        }

        $.post($(this).attr("action"), usuario, function(response){
            console.log(response);
        }).done(function(){ // Se reliza una vez finalizado el metodo.
            alert("Creado");
        });

        return false;
    });
});