# RANGE
"""
La funcion range devuelve una secuencia de numeros dados por 3 parametros. Se utiliza fundamentalmente para controlar el 
numero de ejecuciones de un loop o crear una secuencia rapida de valores.

Solo adminte valores integer. Si solo agregamos un valor establecemos que ira desde 0 hasta ese valor - 1.

Si colocamos un dos valores deparados por coma, el primero indica desde donde comenzar y el segundo hasta donde, recordando
que es n-1

Y un tercer argumento indica el paso, de cuanto en cuanto hara la secuencia, de dos en dos, tres en tres, etc.
"""

for numero in range(5):
    print(numero)

for numero in range(1, 6):
    print(f"---{numero}")

for numero in range(2, 21, 2):
    print(numero)


# Podemos usarlo para crear listas 
lista = list(range(1, 101))
print(lista)



