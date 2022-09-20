# CONVERSION DE TIPOS
"""
Python realiza conversion de tipos de datos de forma implicita para tabajar con
numeros. Esto lo vemos al sumar un integer con un float.

En otros casos, para convertir un String a un Int o visecenrsa, necesitamos ocupar
la conversion explicita. Esta se consigue escribiendo el tipo de dato que quieres tener y
entre parentesis la variable.
int(var)
str(var)
floar(var)

La conversion no es permanente. Solo funciona en el momento cuando usamos el metodo, por lo demas, sigue
siendo el mismo tipo. Por eso es mejor almacenar el nuevo tipo en una nueva variable.
"""

# Input devuelve Strings aunque el usuario ingrese numeros
age = input("Ingres tu edad: ")
print(type(age))

# Convertir variable age en int
suma = int(age) + 1
print(suma)

# Float a Integer
# No redondea, solo quita los decimales.
my_float = 10.9
my_integer = int(my_float)
print(my_integer)
