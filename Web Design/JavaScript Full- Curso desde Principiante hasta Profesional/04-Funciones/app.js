/************************************************************************
 * FUNCIONES
 ************************************************************************
-- Es codigo que se ejecuta cada que las llamemos. 
 -- Partes de una Funcion:
    -- Entradas (Parametros)
    -- Bloque de codigo (Logica de la Funcion)
    -- Salida (Return)
-- Una funcion puede mandar llamar otras funciones.
*************************************************************************/ 
//Funcion
function bienvenido(){
    console.log("Bienvenido! Este texto solo se muestra. No podemos hacer nada con el.");
}
//Llamar Funcion
bienvenido();

/************************************************************************
 * RETURN
 ************************************************************************
-- Una funcion sin Return no devuelve valores. Podemos realizar 
codigo e imprimirlo, PERO NO ALMACENAR ALGUN RESULTADO EN VARIABLES.
-- Una funcion con Return si puede almacenar un valor en una variable
para posteriormente hacer uso de ella.
-- RETURN no muestra informacion, solo la devuelve.
*************************************************************************/ 
function bienvenidoReturn(){
    return "Bienvenido! Este texto si se puede almacenar y trabajar con el."
}
//Variable con el valor que regresa la funcion.
var mensajeFuncion = bienvenidoReturn();
console.log("El mensaje de la funcion fue: " + mensajeFuncion);

/************************************************************************
 * ARGUMENTOS DE FUNCIONES
 ************************************************************************
-- Son valores que enviamos a una funcion para que realice logica con ellos.
-- Podemos enviar argumentos indefindidos. No darar error al entrar a la variable,
pero puede haber problmeas de logica. Por lo que sera bueno validar con typeof.
-- Si enviamos un NUll como argumento no dara error. Lo trabajara, pero
es mejor, para no tener problemas, utilizar validaciones.
*************************************************************************/ 
function argumentos(argumento){
    console.log("Lo que usten envio fue: " + argumento);
}
argumentos(10);
var argumento = 15;
argumentos(argumento);
var contenido = "Hola";
argumentos(contenido);

function numeroCuadrado(numero){
    var resultado = numero * numero;
    return resultado;
}

var miNumero = numeroCuadrado(10);
console.log("El numero cuadrado es: " + miNumero);

//Argumentos Indefinidos
var mascota;
function argumentoIndefinido(mascota){
    //Este condicional lo suluciona todo.
    if (typeof mascota == "undefined"){
        console.log("No se puede trabajar indefinido")
    }else{
        console.log("Tu mascota es un: " + mascota);
    }
}
argumentoIndefinido(mascota);

//Argumentos Nulos
var comida = null;
function argumentoNulo(comida){
    //Esa condicional lo resuelve todo.
    if(comida == null){
        console.log("No se puede trabajar con Nulos");
    }else{
        console.log("La comida de hoy es: " + comida);
    }
}
argumentoNulo(comida);

/************************************************************************
 * ARGUMENTOS POR DEFECTO
 ************************************************************************
-- Podeos asignar un valor por defecto a las argumentos de las funciones,
los cuales los tomara si no envianos nada, o si el contenido de un argumento
envidado es undefind.
-- Si los argumentos tienen valores correctos, los valores por defecto son 
ignorados y trabajamos con los proporcionados.
*************************************************************************/ 
function sumar(a = 10, b = 1, c = 3){
    return a + b + c;
}
console.log(sumar());
/************************************************************************
 * FUNCIONES COMO EXPRESIONES
 ************************************************************************
-- Tambien se le conoce como: Funciones como Expesiones.
-- Es una sintaxis distinta pero es basicamente la misma funcionalidad 
de una funcion.
-- Se almacenan en memoria, es decir, el contenido de una funcion se 
almacena en variable y se incova con ese mismo nombre de variable.
-- Igual puede usar argumentos.
*************************************************************************/ 
var funcionAnonima = function(nombre){
    console.log("Saludos " + nombre + ". Soy anonima.")
}

funcionAnonima("Pepe");

/************************************************************************
 * TEMPLATE STRING
 ************************************************************************
-- `
*************************************************************************/ 

var variable = "Soy una variable.";
console.log(`El contenido de la variable es ${variable}`);

/************************************************************************
 * EJERCICIOS FUNCIONES
 ************************************************************************
-- 1. Convertir de Fahrenhein a Celsius
    Formula: C = (F - 32) * 5/9
-- 2. Calcular edad 
-- 3. Calcular cuanto le falta a una persona para jubilarse.
    -- Una persona se jubila a los 65
    -- Pasar como argumento año de nacimiento y nombre
*************************************************************************/ 
//1. 
function gradosCelsius(fahrenhein){
    var celcius = (fahrenhein - 32) * (5/9);
    return celcius;
}
var resultadoConversion = gradosCelsius(32);
console.log("Los grados son: " + resultadoConversion);

//2.
function calcularEdad(yearNacimiento){
    var edad = (2022 - yearNacimiento);
    return edad;
}
var resultadoEdad = calcularEdad(2003);
console.log("Tu edad es: " + resultadoEdad);

//3. Primer Caso
function calcularJubilamiento(nombre, yearNacimiento){
    var edad = (2022 - yearNacimiento);
    var jubilamiento = 65 - edad;
    return "A " + nombre + " le faltan " +  jubilamiento + " años para su retiro.";
}
var resultadoJubilamiento = calcularJubilamiento("Ivan", 1998);
console.log(resultadoJubilamiento);

//3. Segundo caso -- llamando otra funcion
function calcularJubilamientoSegundoCaso(nombre, yearNacimiento){
    //Llamar Funcion edad para alcular la edad de la persona
    var edad = calcularEdad(yearNacimiento);
    var jubilamiento = 65 - edad;
    return "A " + nombre + " le faltan " +  jubilamiento + " años para su retiro. (Segundo Caso)";
}
var resultadoJubilamientoSegundoCaso = calcularJubilamientoSegundoCaso("Ivan", 1998);
console.log(resultadoJubilamientoSegundoCaso);

