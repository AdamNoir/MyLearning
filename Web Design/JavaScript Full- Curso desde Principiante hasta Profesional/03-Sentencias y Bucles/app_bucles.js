/************************************************************************
 * BUCLE FOR
 ************************************************************************

*************************************************************************/
console.log("########BUCLE FOR########")
for (var i = 0; i <= 10; i++){
    console.log("El numero es: " + i);
}
console.log("########BUCLE FOR INVERSIO########");
for(var i = 10; i >= 1; i--){
    console.log("El numero hacia atras es: " + i);
}

/************************************************************************
 * BUCLE WHILE
 ************************************************************************
-- Se ejecuta siempre que se cumpla una condicion.
-- Importante colocar el incremento o sera un while infinito.
*************************************************************************/
console.log("########BUCLE WHILE########");
var i = 0;
while(i <= 10){
    console.log("El numero en While es: " + i);
    i++ //Importante nunca olvidar.
}

/************************************************************************
 * BUCLE DO - WHILE
 ************************************************************************
-- Identico al Bucle While, con la diferencia que garantiza que la logica
se ejecutara al menos una vez. Primero ejecuta despues comprueba si la condicion es true.
*************************************************************************/
console.log("########BUCLE DO - WHILE########");
var j = 12;
do {
    console.log("El numero en Do - While es: " + j);
    j++
}while(i <= 10);
