# LA BASE DE PYTHON: LA IDENTACION

"""La diferencia de Python con otros lenguajes, es que no cuenta con {} que abren y cierran para establecer
bloques de codigo. En su lugar, hace uso de la identacion, que no es mas que una tabulacion, sangria o tres espeacios
en las lineas de codigo que dependen de alguna instruccion como puede ser un condicional IF, o una funcion.

La identacion puede tener varios niveles, asi como existen bloques de codigo delimitados por {} que abren
y cierran dentro de otros, es posible tener lineas identadas dentro de otras."""


# Ejemplo Identacion:

# Esto es correcto:
if 5 > 3:
    print("5 Es mayor a 3")

# Esto es Incorrecto:
# Este codigo se comenta porque dara error.
# if 6 < 10:
# print("6 es menor a 10")"""


# EJEMPLO IDENTACION SUB NIVELES
if 5 > 3:
    if 9 == 9:
        print("Amabas se cumplen")