'use strict'

// IF
var edad1 = 10;
var edad2 = 12;

if(edad1 > edad2){
    console.log("Edad uno es mayor")
}else{
    console.log("Edad uno es inferior")
}

var edad = 33;
var nombre = "pepe"
if(edad >= 18){
    console.log("Mayor");
    if(edad == 33){
        console.log("Estas muy viejo")
    }else if(edad > 70){
        console.log("Anciano")
    }else{
        console.log("Joven")
    }
}else{
    console.log("Menor")
}