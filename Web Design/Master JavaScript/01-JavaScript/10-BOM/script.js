'use strict'

// BOM - Broswer Object Model
/**
 * Permite trabajar con elementos que da el navegador web. Cosas como tamaño de ventana
 * del navegador, redigir etc.
 */

// Con el objeto window accedemos a las propiedades de la ventana del navegador
function getBoom(){
    // Valores que cambiaran dependiendo de como este acomodada la ventana
    // Incluso la consola del browser le quita tamaño
    console.log(window.innerWidth);
    console.log(window.innerHeight);
}

function getBoomScreen(){
    console.log(screen.width);
    console.log(screen.height);
}

// Ver url (traer muchas propiedades mas)
console.log(window.location);
// Url clickeable
console.log(window.location.href);

// FUncion para redirigir
function redirect(url){
    window.location.href = url;
}

// Funcion para abrir nueva ventana
function abrirVentana(url){
    window.open(url);
}

function abrirVentanaTamaño(url){
    window.open(url,"","width=400,height=300");
}