# INPUT
"""
Funcion que permite al usuario introducir informacion a traves del teclado.
Se espesifica un mensaje indicando que informacion debe ingresar, edad, nombre, etc.
Esta informacion puede almacenarse en una variable y poder trabjarse con ella despues.

El codigo quedara suspendido hasta que el usuario ingrese informacion y continuara su
ejecucion normal despues de ella.

Input puede ir dentro de una funcion print para mostrar el contenido ingresado por el
usuario inmediatamente.
"""

# Esto no mostrara contenido, pues no se almacena ni se indica que se debe imprimir.
input("Ingresa tu nombre: ")
input("Ingresa tu apellido: ")

# Aqui almacenamos el contenido en variable y lo imprimirmos despues.
nombre = input("Dime tu nombre: ")
apellido = input("Dime tu apellido: ")
print(nombre, apellido)

# Imprimir contenido de funcion input
print(input("¿Cual es tu nombre?: "), input("¿Cual es tu apellido?: "))

# Se puede concatenar texto para tener salida personalizada
# Para incluir espacio entre resultados concatenamos espacio entre Inputs
print("Tu nombre es: " + input("¿Cual es tu nombre?: ") + " " + input("¿Cual es tu apellido?: "))
