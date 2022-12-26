'use strict'

var nombre = "Ivan";
// Puede tener todo tipo de elementos
var nombres = ["Ivan", "Fer", "Kenia", 12, true]; //Crear array

var lenguajes = new Array("Php", "js", "go", "java"); //crear array

console.log(nombres);
console.log(lenguajes);

console.log(nombres[3]);
console.log(lenguajes[1]);

// Longitud de arrya
console.log(nombres.length);

// Hacer lista con arrays en HTML
document.write("<h1>Lenguajes</h1>");
document.write("<ul>");
for(var i = 0; i < lenguajes.length; i++){
    document.write("<li>" + lenguajes[i] + "</li>");
}
document.write("</ul>");