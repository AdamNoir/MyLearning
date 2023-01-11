'use strict'

// plantillas de texto
/**
 * Para mostrar mas facilmente en un documento html.
 * Al usar corchetes no debemos de estar concatenando. Acepta
 * codigo HTML.
 */

var nombre = prompt("Ingresa nombre");
var apellidos = prompt("Ingresa apellidos");

var texto = `
    <h1>Hola</h1>
    <h3>Mi nombre es {nombre}</h3>
    <h3>Y mis apellidos {apellidos}</h3>
`;

document.write(texto)