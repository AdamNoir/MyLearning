# *args
"""
En aquellos casos en los que no se conoce la cantidad de argumentos que debe pasar a una
funcion se utiliza *args.

La funcion recibira los argumentos indefinidos y los almacenara en una tupla.
Esta tupla se puede iterar y trabajar sobre ella del modo habitual.

*args no es un nombre mandatorio, puede ser cualquier palabra despues de un asterico.
Solo es una buena practica usarlo.
"""

def sumar(*args):
    total = 0
    for arg in args:
        total = total + arg
    return total
print(suma(1, 2, 3, 4, 5))
