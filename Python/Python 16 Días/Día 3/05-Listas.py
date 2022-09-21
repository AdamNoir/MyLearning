# LISTAS
"""
Las Listas son secuencias ordenadas de objetos. Estos objetos pueden ser de cualquier tipo,
incluso otras listas. Estas listas son mutables, es decir, podemos modificarlas.

"""

my_list = ["A",  "B", "C"]
print(type(my_list))

print(my_list)

# Podemos buscar por indices como en los String
print(my_list[0])
print(my_list[:1])

# Podemos ver el largo de una lista
print(len(my_list))

# Podemos concatenar listas
my_second_list = ["D", "E", "F"]
print(my_list + my_second_list)

my_third_list = my_list + my_second_list

# Podemos sobre escribir elementos
my_third_list[1] = "Z"
print(my_third_list)

# METODOS DE LISTA

# append agrega un nuevo elemento al final de la lista
my_third_list.append("Y")
print(my_third_list)

# Eliminar elementos de Lista
# Sin parametros POP elimina el ultimo, podemos pasarle el indice
# Este valor se puede almacenar en una variable
eliminado = my_third_list.pop()
eliminado2 = my_third_list.pop(2)

print(eliminado, eliminado2)

# Ordenar listas
# Este metodo no devuelve nada, modifica la lista original
new_list = ["O", "K", "B", "S", "A", "N"]
new_list.sort()
print(new_list)

# Invertir orden de Lista
new_list.reverse()
print(new_list)
