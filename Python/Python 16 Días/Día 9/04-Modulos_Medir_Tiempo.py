# MODULOS PARA MEDIR EL TIEMPO
"""
Con estos modulos podemos conocer el tiempo que tarda en ejecutarse el codigo para
encontrar la forma mas eficiente de resolver el problema.

- time: time.time() al principio y final del codigo que se ejecuta. Luego restamos
ambas variables. NO ES TAN PRECIOSO EN FUNCIONES CORTAS
- timeit:
    timeit.timeit(delcaracion, setup, numner=numero)
    - declaracion: recibe el codigo que queremos medir (es la invocacion)
    - setup: recibe las instrucciones (es la definicion, el codigo de funcion)
    - numner: cantidad de veces que se evaluara para tener una mejor respuesta.
"""

import time
import timeit

def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


# Uso de Time.
# Es bueno pero no es muy presicio.
inicio = time.time()
prueba_for(1000000)
final = time.time()
print(final - inicio)

inicio = time.time()
prueba_while(1000000)
final = time.time()
print(final - inicio)

print("*" * 50)
# Uso de Timeit
# Funcion For
declariacon = '''
prueba_for(10)
'''
mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''
duracion = timeit.timeit(declariacon, mi_setup, number=100000)
print(duracion)

# Funcion While
declariacon_while = '''
prueba_while(10)
'''
mi_setup_while= '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''
duracion_while = timeit.timeit(declariacon_while, mi_setup_while, number=100000)
print(duracion_while)