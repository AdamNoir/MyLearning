# SETS
"""
Los set son una estructura de datos similares a las listas.
Los sets se definen de dos maneras:
    - La palabra clave set seguida de parentesis () y dentro con llaves o corchetes el contenido
    - Entre llaves sin la palabra set.

En los sets no se pueden agregar listas ni diccionarios. Pero si Tuples. Esto es porque los tuples
son inmutables y el set requeire que sus elementos no se puedan repetir.

Los sets no tienen orden establecido. No podemos acceder por medio de indice.

LOS SETS NO ACEPTAN ELEMENTOS DUPLICADOS. Si agregamos duplicado no pasa nada, no dara error, solo eliminara
esa repeticion.
"""

mi_set = set([1, 2, 3, 4, 5])
print(type(mi_set))

otro_set = {1, 2, 3, 4, 5, 6, 7}

print(type(otro_set))

print(mi_set)
print(otro_set)

# Podemos calcular su largo
print(len(mi_set))

# Podemos preguntar si un elemento se encuentra o no
print(2 in otro_set)

# Union de Sets
nuevo_set = mi_set.union()
print(nuevo_set)

# Agregar nuevo elemento
# Si agregamos repetido no pasa nada, solo no lo agrega
nuevo_set.add(9)

# Eliminar Elemento
nuevo_set.remove(1)

# Elimina un elemento, pero si no lo encuentra no dara error como lo hace remove
nuevo_set.discard(1)

# Elimina un elemento PERO DE FORMA ALEATORIA si no pasamos argumentos
nuevo_set.pop()

print(nuevo_set)

# Vacia el Set
nuevo_set.clear()
print(nuevo_set)

