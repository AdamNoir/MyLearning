# RANDOM
"""
Random es una libreria que debemos importar, y con ella podemos acceder a distintos metodos que nos permiten crear aleatorios.
 
-randint
    Devuelve un integer entre dos rangos dados.
-uniform
    Devuelve un float entre un valor minimo y uno maximo.
    Podemos combinarlo con round para tener menos decimales.
-random
    Sin parametros devuelve un float entre 0 y 1
-choice
    Devuelve un aleatorio de una secuencia (listas, tuplas, etc)
-shuffle
    Toma una secuencia como una lista y ordena aleatoriamente sus elementos.
"""

from random import *

# randint
aleatorio = randint(10, 20)
print(aleatorio)

# uniform
aleatorio = round(uniform(10, 15), 1)
print(aleatorio)

# random
aleatorio = random()
print(aleatorio)

# choice
colores = ["Azul", "Verde", "Naranja", "Morado"]
print(choice(colores))

# Shuffle
# No devuelve nada. No puede almacenarse en una variable
lista_numeros = list(range(5, 51, 5))
print(lista_numeros)

shuffle(lista_numeros)
print(lista_numeros)
