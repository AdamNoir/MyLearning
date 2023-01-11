// String
let cadena: string = "Esto es un string---";
console.log(cadena);

// Number
let numero: number = 12;
let numero2: number = 12.3;
console.log(numero);
console.log(numero2);

// Booleano
let booleano: boolean = true;
console.log(booleano);

// Any - Cualquier tipo de dato
let cualquiera: any = "Hola";
cualquiera = 12;
console.log(cualquiera);

// Arrays
var lenguajes: Array<string> = ["uno", "dos", "tres"];

let numeros: number[] = [1, 2, 3]

let cualquier_tipo: any = ["uno", 1, "dos", 2];

console.log(lenguajes);
console.log(numeros);
console.log(cualquier_tipo);

// Multiples tipos
// Usando | podemos colocarle a una variable varios tipos de datos

let varios: string | number = "Esto puede ser un string";
console.log(varios);
varios = 100;
console.log("O tambien un numero: ", varios);

// Mi propio tipo de dato
// Podemos crear un nuevo tipo, usando type, el nombre y que tipos de datos puede contener.
type miNuevoTipo = boolean | number;
let nuevoTipo: miNuevoTipo = 12;
console.log("Mi tipo de dato propio puede ser un numero ", nuevoTipo);
nuevoTipo = false;
console.log("O un booleano ", nuevoTipo);