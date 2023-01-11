// Indicamos el tipo de dato de los parametros
// Inciamos que devolvera, hasta el final, antes de las llaves
function getNumero(numero:number = 12):string{
    return "El numero es: " + numero;
}

console.log(getNumero(100));