'use strict';

// FETCH(ajax) Y PETICIONES a servicios / apis rest

var div_usuarios = document.querySelector("#usuarios");

var usuarios = []

// Llamar a servicio rest
fetch("https://reqres.in/api/users")
    // Capurar datos a JSON
    .then(data => data.json())
    // tenemos los datos recodigos y los almacenamos en la variable
    .then(users => {
        usuarios = users.data;
        console.log(usuarios);

        usuarios.map((user, i) =>{
            let nombre = document.createElement("h3");

            nombre.innerHTML = i + ". " + user.first_name + " " + user.last_name;

            div_usuarios.appendChild(nombre);

            document.querySelector(".loading").style.display = "none";
        });
    });
