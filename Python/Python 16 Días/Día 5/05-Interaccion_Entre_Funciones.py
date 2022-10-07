# INTERACCION ENTRE FUNCIONES
"""
Las salidas de una determinada funcion puede convertirse en entradas de otras funciones.
De esta manera cada funcion realiza una tarea difernete y se contruye el programa
apartir de la interaccion entre funciones.
"""
from random import *

# Lista Inicial
palitos = ["-", "--", "---", "----"]

# Mexclar Palitos
def mezclar(lista):
    shuffle(lista)
    return lista

# Pedirle Intento
def probar_suerte():
    intento = ""

    while intento not in ["1", "2", "3", "4"]:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)

# Comprobar Intento
def checar_intento(lista, intento):
    if lista[intento - 1] == "-":
        print("Has perdido")
    else:
        print("Te has salvado")
    print(f"Te ha tocado {lista[intento - 1]")

# Interactuar entre Funciones
palitos_mezclados = mezclar(palitos)
seleccion = probar(suerte)  # Almacena el intento del usuario
chequear_intento(palitos_mezclados, seleccion)
