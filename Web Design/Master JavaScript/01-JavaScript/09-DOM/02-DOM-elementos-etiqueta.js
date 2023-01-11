'use strict'

// DOM - Document Object Model

// Conseguir todos los elementos por su etiqueta
// Seria un array de elementos pues hay muchos
var todosDiv = document.getElementsByTagName("div");
var contenidoDiv = todosDiv[2].textContent; // Permite ver el contenido del Elemento
console.log(contenidoDiv)

var seccion = document.querySelector("#seccion");
var hr = document.createElement("hr");

// REcorrer listado de divs
var valor;
for(valor in todosDiv){
    // Preguntamos si todos los valore son texto (hay cosas propias del dom)
    if(typeof(todosDiv[valor].textContent) == "string"){
        // Creamos un elemento parrafo
        var parrafo = document.createElement("p");
        // Creamos el texto apartir de el contenido de la iteracion actuakl
        var texto = document.createTextNode(todosDiv[valor].textContent);
        // Agregamos el texto al parrafo
        parrafo.appendChild(texto);
        // Añadimos el prrafo a la seccion por su ID
        document.querySelector("#seccion").appendChild(parrafo);
        // Puede usarse append prepend(antes) o appenChild
    }
}
seccion.append(hr);