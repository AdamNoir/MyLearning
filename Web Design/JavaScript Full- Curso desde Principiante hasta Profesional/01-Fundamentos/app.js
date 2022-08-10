//console.log("Hola a Todos mis Amigos!!");

/************************************************************************
 * DECLARACION DE VARIABLES EN JAVASCRIPT
 ************************************************************************
--JS es de tipado dinamico, pero debemos usar VAR para indicar que vamos 
a declarar una variable.
--JS usa camelCase
--Una variable es indefinida debido a que JS es tipado dinamico, y al
no inicializar una variable, solo declararla, no sabe que tipo de dato
asgingar.
--MUTACION: al ser JS de tipado dinamico, podemos cambiar el tipo de
dato de una variable tan facil como solo asignarle el nuevo valor
con otro tipo de dato.
*************************************************************************/ 

//VARIABLES
//String
var primerNombre = "Ivan";
//Numericas
var edad = 24;
var sueldo = 1800.90;
//Booleanos
var tieneTrabajo = true;
//Indefinidas
var puestoTrabajo;
//Nulas
var amigosTrabajo = null;

//Imprimir variables
console.log(primerNombre);
console.log(edad);
console.log(sueldo);
console.log(tieneTrabajo);
console.log(puestoTrabajo);
console.log(amigosTrabajo)

//Mutacion
//Edad es originalmente de tipo numerio y pasara a ser String
edad = "Veinticuatro";
console.log("Mi edad es: " + edad + " años.");

/************************************************************************
 * OPERADORES JS
 ************************************************************************
--MATEMATICOS: para matematica basca (+. -, *, /, %)
--RELACIONALES: relacionar operandos (>, <, >=, ==, etc.) 
--En JS existe el operador === 'Igualdad Estricta' que revisa si los 
operandos son del mismo tipo de dato. Si no son devuelve falso.
Por su parte el operador de 'Igualdad Regular' == a quien lo le importa
el tipo de dato de los operadores (los convierte). 
--TYPEOF: devuelve el tipo de dato al que pertenece una variable
--UNARIOS: Ocupan un unico unario para aumentar o restar su valor en uno.
--COMPUESTOS: Abreviaturas de operaciones aritmeticas.
--LOGICOS: ||, &&, ! 
*************************************************************************/ 

//Operadores Matematicos - Aritmeticos
var suma = 2 + 5;
console.log("La suma es: " + suma);
var resta = 12 - 8;
console.log("La resta es: " + resta);
var multiplicacion = 4 * 70;
console.log("La muliplicacion es: " + multiplicacion);
var division = 5 / 2;
console.log("La division es: " + division);
var modulo = 10 % 2;
console.log("El modulo es: " + modulo);

//Operadores Relacionales
var mayor = 5 > 6;
console.log(mayor);
var menor = 6 < 9;
console.log(menor);
var igual = 7 == 7;
console.log(igual);
var mayorIgual = 5 >= 5;
console.log(mayorIgual);
var menorIgual = 5 <= 10;
console.log(menorIgual);
var diferente = 1 != 4;
console.log(diferente);

//Igualdad Regular
var igualRegular = 1 == '1';
console.log("Igualdad Regular: " + igualRegular);
//Igualdad Estricta
var igualdadEstricta = 2 === '2';
console.log("Igualdad Estricta: "+ igualdadEstricta);

//Type Of
console.log("El tipo de dato es: " + typeof igualdadEstricta);
console.log("El tipo de dato es: " + typeof "Saludos");
console.log("El tipo de dato es: " + typeof 34); 

//Unarios
var edadPersona1 = 19;
var edadPersona2 = 14;
console.log("Edad Persona 1: " + edadPersona1);
console.log("Edad Persona 2: " + edadPersona2);
//Pre Incremento y Pre Decremento
//Primero aumenta o resta despues usa la variable
console.log("Pre Incremento: " + ++edadPersona1);
console.log("Pre Decremento: " + --edadPersona2);

//Post Incremento y Post Decremento
//Primero usa la variable despues aumenta o resta valor
console.log("Post Incremento: " + edadPersona1++);
console.log("Post Decremento: " + edadPersona2--);
console.log("Resultado Post Incremento: " + edadPersona1++);
console.log("Resultado Post Decremento: " + edadPersona2--);

//Compuestos
var a = 10;
var b = 23;
console.log("Valor de a: " + a);
console.log("Valor de b: " + b);
console.log(a += b);
console.log(b -= a);
console.log(a *= b);
console.log(b/= a);
console.log(a %= b);

//Logicos
console.log("¿Es 5 > 4 && 3 < 4? " + (5 > 4 && 3 < 4));
console.log("¿Es 5 == 4 && 10 > 2? " + (5 == 4 && 10 > 2));
console.log("¿Es !true? " + (!true));

/************************************************************************
 * VALORES VERDADEROS Y FALSOS EN JAVASCRIPT
 ************************************************************************
-- Son valores que sin ser Booleanos, para JS serian falsos o verdaderos
dependindo del contenido que tengan.
-- FALSOS: indefinidos, nullos, 0, ''
-- VERDADEROS: NOT FALSOS (todo lo contrario a falso)
*************************************************************************/ 
//Indefinido, por lo que es falso
console.log("##### VALORES VERDADEROS Y FALSOS #####") 
var variable;
variable ? console.log("DEFINIDA") : console.log("NO DEFINIDA");
//Nulo es falso
variable = null;
variable ? console.log("Verdadero") : console.log("Falso");
//0 es falso
variable = 0;
variable ? console.log("Verdadero") : console.log("Falso");
//cadena vacia es falso
variable = '';
variable ? console.log("Verdadero") : console.log("Falso");
/************************************************************************
 * EJERCICIO
 ************************************************************************
Utiliza la siguente formula para calcular el IMC (Indice de Masa
Corporal) de Luis y Carlos.
IMC se obtiene dividiendo el peso entre la altura al cuadrado. 
Compara si el IMC de carlos es superior al de Luis.
*************************************************************************/ 
//Datos
//Luis
var pesoLuis = 72;
var alturaLuis = 1.72;
//Carlos
var pesoCarlos = 89;
var alturaCarlos = 1.75;

//Operaciones
var imcLuis = pesoLuis/(alturaLuis**2);
var imcCarlos = pesoCarlos/(alturaCarlos**2);

console.log("IMC de Luis: " + imcLuis);
console.log("IMC de Carlos: " + imcCarlos);
console.log("¿Es el IMC de carlos mayor al de Luis? " + (imcCarlos > imcLuis));