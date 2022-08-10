/************************************************************************
 * SENTENCIA IF / ELSE
 ************************************************************************

*************************************************************************/
var nombre = "Ivan";
var estadoCivil = "Soltero";
var estaCasado = true;

if(estaCasado){
    console.log("Esta casado");
}else{
    console.log("No esta casado");
}

if(estadoCivil === "Casado"){
    console.log("Su estaso civil es casado");
}else{
    console.log("Su estado civil es soltero");
}

/************************************************************************
 * OPERADOR TERNARIO
 ************************************************************************
-- CONDICION ? ACCION SI ES TRUE : ACCION SI ES FALSE;
    -- No puede funcionar si no tene los dos escenarios, true y false.
*************************************************************************/
estaCasado == true ? console.log("Esta casado(Ternario)") : console.log("Esta soltero(Ternario)"); 

var numero = 10;
numero < 11 ? console.log("Menor a 11") : console.log("Mayor a 11");

/************************************************************************
 * SENTENCIA SWITCH
 ************************************************************************
--Compara el valor de una variable con posibles casos, y ejecuta cierta logica
dependiendo del caso.
--Basta con que se cumpla un caso para ejecutar todos los bloques que le siguen.
Por ello usar Break.
--Tiene un Default para ejecutar una logica si no se cumple ningun caso.
*************************************************************************/
var mes = "Mayo";
switch(mes){
    case "Enero": 
        console.log("Es el primer mes del año");
        break;
    case "Febrero": 
        console.log("Es el segundo mes del año");
        break;
    case "Marzo": 
        console.log("Es el tercer mes del año");
        break;
    case "Abril":
        console.log("Es el cuarto mes del año");
        break;
    case "Mayo":
        console.log("Es el quinto mes del año");
        break;
    case "Junio":
        console.log("Es el sexto mes del año");
        break;
    default:
        console.log("EL MES NO PERTENECE AL PRIMER SEMESTRE DEL AÑO.")
}

/************************************************************************
 * EJERCICO DE SENTENCIAS
 ************************************************************************
-- Tienes dos alumnos, Pablo y Maria. 
Pablo tiene las siguentes calificaciones en JS: 14, 8, 16. 
Maria tiene las siguentes calificaciones en JS: 12, 18, 10.

-- Calcular el promedio de cada alumno, ademas, inficar quien tiene el 
promedio mas alto.
-- Indicar si el alumno esta aprobado, para ello el promedio debe ser mayor 
a 13. 
*************************************************************************/
console.log("##### EJERCICIO #####");
var promedioPablo = (14 + 8 + 16) / 3;
var promedioMaria = (12 + 18 + 10) / 3;

//primedioMaria > primedioPablo ? console.log("El promedio de Maria es mayor.") : console.log("El primedio de Pablo es mayor.");

if (promedioMaria > promedioPablo){
    console.log("El promedio de Maria es Mayor.");
    if(promedioMaria >= 13){
        console.log("Esta aprobada con: " + promedioMaria);
    }else{
        console.log("Esta reprobada con: " + promedioMaria)
    }
}else{
    console.log("El promedio de Pablo es Mayor")
    if(promedioPablo >= 13){
        console.log("Esta aprobada con: " + promedioPablo);
    }else{
        console.log("Esta reprobada con: " + promedioPablo)
    }
}
//LA SOLUCION DEL CURSO SIMPLEMENTE NO ME CONVENSE.