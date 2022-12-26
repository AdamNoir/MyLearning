'use strict'

var categorias = ["Accion", "Terror", "Comedia"];
var peliculas = ["La verdad duele", "La vida es bella", "Totoro"];
var numeros = [10, 8, 100, 23, 1, 512, 6];
var lenguajes = new Array("Php", "js", "go", "java");

// Agrega un elemento
peliculas.push("Annie Hall");
// Quita el ultimo elemento
categorias.pop();

// Borra desde un indice el numero de elementos que le indiquemos
peliculas.splice(0, 1);

// Convierte un array a string
var miArray = peliculas.join();

// COnvierte un texto en array en base al caracter que pasemos
var texto = "esto tiene varias palabras";
var cadenaArray = texto.split(" ");

// Ordena un array de menor a mayor
console.log(numeros.sort());

// Invierte el orden de array
console.log(numeros.reverse());
  
console.log(categorias);
console.log(peliculas);
console.log(miArray);
console.log(cadenaArray);


// Recorre un arrya como en python
for(let numero in numeros){
    console.log(numeros[numero]);
}

// Busquedas en Array
var precios = [10, 20, 50, 80, 12];
// Pregunt si hay elementos mayores a 10
var busqueda  = precios.some(precio => precio > 10);
// Muestra el indice del elemento que coincida con la busqueda
var busqueda2  = precios.findIndex(precio => precio > 20);
console.log(busqueda);
console.log(busqueda2)