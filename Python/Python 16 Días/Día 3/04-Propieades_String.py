# PROPIEADES DE LOS STRINGS
"""
- INMUTABLES: Una vez creado el String NO PUEDE MODIFICARSE SU CONTENIDO, pero si puede reasignarse
el valor de la variable por un nuevo STRING, o crear un nuevo String en base a lo que necesitemos.
- CONCATENABLES: Podemos unir varios strings usando el simbolo: +
- MULTIPLICABLES: Se concatenara una determinada repetision de Strings usando el simbolo * y un valor
numerico.
- DETERMINAR LONGITUD: Con el metodo len() podemos saber el largo total de un string.
- VERIFICAR CONTENIDO: con las palabras clave in y not in podemos saber si algun caracter, o cadena de
caracteres se encuentran en un string.
"""

my_string = "Hola Mundo"
# No se podra cambiar el string, pero le asignare otro a la variable
# my_string[0] = "h"
my_string2 = my_string.lower()

valor1 = "Hola"
valor2 = "Como estan"
print(valor1 + " " + valor2)

print(valor1 * 5)

print(len(my_string))

print("adios" in my_string2)
print("mesa" not in my_string)



