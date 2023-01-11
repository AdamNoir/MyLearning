'use strict'

window.addEventListener("load", function(){
    this.alert("Dom cargado.");

    var formulario = this.document.querySelector("#formulario");

    var box_dashed = this.document.querySelector(".dashed");
    box_dashed.style.display = "none";
    
    // Capurar evento sumbit
    formulario.addEventListener("submit", function(){
        console.log("Evento submit capturado");

        //
        var nombre = document.querySelector("#nombre").value;
        var apellidos = document.querySelector("#apellidos").value;
        var edad = parseInt(document.querySelector("#edad").value);
        console.log(nombre, edad, apellidos);


        // Validar formulario
        if(nombre.trim() == null || nombre.trim().length == 0){
            alert("EL nombre no es valido");
            document.querySelector("#error_nombre").innerHTML = "El nombre no es valido";
            return false;
        }else{
            document.querySelector("#error_nombre").style.display = "none";
        }

        if(apellidos.trim() == null || apellidos.trim().length == 0){
            alert("Los apellidos no son validos");
            document.querySelector("#error_apellidos").innerHTML = "Los apellidos no son validos";
            return false;
        }else{
            document.querySelector("#error_apellidos").style.display = "none";
        }

        if(edad == null || edad <= 0 || isNaN(edad)){
            alert("La edad no es valida");
            document.querySelector("#error_edad").innerHTML = "La edad no es valida";
            return false;
        }else{
            document.querySelector("#error_edad").style.display = "none";
        }

        box_dashed.style.display = "block";

        var datos_usuario = [nombre, apellidos, edad];

        var indice;
        for(indice in datos_usuario){
            var parrafo = document.createElement("p");
            parrafo.append(datos_usuario[indice]);
            box_dashed.append(parrafo);
        }

        /*var parrafo = document.createElement("p");
        parrafo.append(nombre);
        parrafo.append(apellidos);
        parrafo.append(edad);
        box_dashed.append(parrafo);*/
    });


});