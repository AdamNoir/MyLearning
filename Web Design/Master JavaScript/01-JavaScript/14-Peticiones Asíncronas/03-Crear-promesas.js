'use strict'


var div_usuarios = document.querySelector("#usuarios");
var div_janet = document.querySelector("#janet");
var div_profesor = document.querySelector("#profesor");

// Al ser una funcion que devuelve como resultado una peticion fetch pues podemos usar promeas directamente.
getUsuarios()
    .then(data => data.json())
    .then(users => {
        // La data se la pasamos a el metoo, para que liste en pantalla.
        listadoUsuarios(users.data);
        // Al acabar la funcion de callback mandara llamar la otra funcion
        return getInfo();
    })
    .then(data => {
        div_profesor.innerHTML = data;

        return getJanet();
    })
    .then(data => data.json())
    .then(user => {
        mostrarJanet(user.data);
    });


function getUsuarios(){
    return fetch("https://reqres.in/api/users");
}

function getJanet(){
    return fetch("https://reqres.in/api/users/2");
}

function getInfo(){
    var profesor = {
        nombre: "Ivan",
        apellido: "Ibarra",
        url: "https://web.com"
    };

    return new Promise((resolve, reject) => {
        var profesor_string = "";
        setTimeout(function(){
            profesor_string = JSON.stringify(profesor);
            if(typeof profesor_string != "string"){
                return reject("Error");
            }else{
                return resolve(profesor_string);
            }
        }, 3000);
    });
}


function listadoUsuarios(users){
    users.map((user, i) =>{
        let nombre = document.createElement("h3");

        nombre.innerHTML = i + ". " + user.first_name + " " + user.last_name;

        div_usuarios.appendChild(nombre);

        document.querySelector(".loading").style.display = "none";
    });
}

function mostrarJanet(user){
    let nombre = document.createElement("h4");
    let avatar = document.createElement("img");
    nombre.innerHTML = user.first_name + " " + user.last_name;
    avatar.src = user.avatar;
    avatar.width = "100";

    div_janet.appendChild(nombre);
    div_janet.appendChild(avatar);

    document.querySelector("#janet .loading").style.display = "none";
}