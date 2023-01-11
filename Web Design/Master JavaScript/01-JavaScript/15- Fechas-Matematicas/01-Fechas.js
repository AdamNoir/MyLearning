'use strict'

// Fechas
var fecha = new Date();
console.log(fecha);

var year = fecha.getFullYear();
var mes = fecha.getMonth(); // contando desde 0
var dia = fecha.getDate();
var hora = fecha.getHours();

var textoHora = `
    año: ${year}
    mes: ${mes}
    dia: ${dia}
    hora: ${hora}
`;

console.log(textoHora);