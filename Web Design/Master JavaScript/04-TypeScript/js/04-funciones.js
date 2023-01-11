// Indicamos el tipo de dato de los parametros
// Inciamos que devolvera, hasta el final, antes de las llaves
function getNumero(numero) {
    if (numero === void 0) { numero = 12; }
    return "El numero es: " + numero;
}
console.log(getNumero(100));
