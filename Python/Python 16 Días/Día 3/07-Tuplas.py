# TUPLAS
"""
Las tuplas son estructuras de datos ordenadas, similares a las listas, contiene indeices
y admite valores duplicados, PERO SON INMUTABLES, el contenido de una tupla no puede cambiar.

Acepta cualquier tipo de elementos, incluso otros tuples. Podemos acceder a ellos por medio de su indice.

- Ocupan menos memoria
- Al no ser mutables son a prueba de daños, es decir, podemos almacenar valores que no queremos
que cambien.
"""

my_tuple = (1, 2, 3, 4, 5)
print(type(my_tuple))

print(my_tuple)

my_new_tuple = (1, 2, "Hola", True, [0, 1, 2])
print(my_new_tuple)

# Acceder al contenido de un Tuple por su indice
print(my_new_tuple[2])

# Podemos acceder a los elementos de otro tuples o una lista dentro de un tuple.
print(my_new_tuple[4][2])

# Podemos convertir un tuple en una lista
my_list_from_tuple = list(my_new_tuple)
print(my_list_from_tuple)

# Podemos almacenar los elementos de un tuple en variables
# La unica ciondicion es que la cantidad de variables y elementos sea la misma
other_tuple = (1, 2, 3, 1)
a, b, c, d = other_tuple
print(a, b, c)

# Largo de tuple
print(len(other_tuple))

# Metodos de Tupla
# Cuanta cuantas veces hay un elemento en la tuple
print(other_tuple.count(1))

# Muestra el indice de un elemento en la tupla
print(other_tuple.index(2))