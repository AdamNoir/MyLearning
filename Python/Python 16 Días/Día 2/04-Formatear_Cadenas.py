# FORMATEAR CADENAS
"""
El formateo de cadneas nos ayuda a la concatenacion de variable de distintos tipos de datos y
texto, para asi ahorranos la necesidad de estar conviertiendo las variables a string para poder concatenar.

- Funcion Format
    Encierras las posiciones de las variables entre llaves vacias {}, y el final agregas .format() y entre
    los parentesis colocas de FORMA ORDENADA las variables que llenaran esos espacios.
- Cadena Literal
    Colocas una f antes de la comilla que dara inicio a la cadena, y entre llaves {} colocas las variables.

Tanto en format como en la cadena literal podemos realizar operaciones con la variables.
"""

my_name = "Ivan"
age = 24

# Funcion Format
print("Mi nombre es {} y mi edad {}".format(my_name, age))
print("Mi nombre es {} y mi edad mas un año es {}".format(my_name, age + 1))

# Cadena Literal
print(f"Mi nombre es {my_name} y mi edad {age}")
print(f"Mi nombre es {my_name} y mi edad mas un año es {age + 1}")
