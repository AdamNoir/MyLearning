'use strict'

// OPERADORES LOGICOS
var year = 2018;

// negacion
if(year != 2016){
    console.log("No es 2016");
}

// and
if(year >= 2000 && year <= 2022){
    console.log("Era actual");
}else{
    console.log("Era post moderna")
}

// or
if(year == 2008 || (year >= 2018 && year == 2028)){
    console.log("El año acaba en 8");
}else{
    console.log("Año no registrado")
}