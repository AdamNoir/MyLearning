# Integers and Floats
"""
- Integer:
    Numero entero positivo o negativo.
- Float:
    Numero con decimales positivo o negativo.

La funcion type() nos permite saber el tipo de dato de una variable.
"""

# Integers
my_integer = 19
print(my_integer)

# Funcion Type para ver el tipo de dato de la variable
print(type(my_integer))

# Podemos almacenar resultados de operaciones literales o con variables.
my_integer_add = 9 + 1
print(my_integer_add)
my_integer_add = my_integer_add + my_integer
print(my_integer_add)

# Floats
my_float = 10.90
print(my_float)

# Funcion Type
print(type(my_float))

# Podemos Operar con distintos tipos de datos
my_result = my_float + my_integer
print(my_result)
# Lo que importa es el resultado, no los operadores
print(type(my_result))
