# BOOLEANO
"""
Solo pueden tener dos valores: TRUE o FALSE
Se pueden crear de forma directa, igualando una variable a true o false; o de forma
indirecta haciendo una comparacion. Esto se hace con los operadores de comparacion.
"""

my_boolean_true = True
my_boolean_false = False
print(type(my_boolean_false))

number = 2 == 1
print(number)

# Forma mas explicita con la funcion Bool
# Si bool queda vacio sera falso
number2 = bool(2 > 10)
print(number2)

