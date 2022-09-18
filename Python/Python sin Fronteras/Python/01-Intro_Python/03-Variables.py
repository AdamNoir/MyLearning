# VARIABLES

"""Una variable es un espacio en memoria que alcena informacion en algun tipo de dato valido.

Una variable puede tener cualquier nombre, pero exsten varias reglas para ello:
    - No puede comenzar con numeros, pero si puede llevar numeros al final o enmedio del nombre.
    - No puede ser palabras reservadas del lenduaje como if, for, etc...
    - No puede comenzar con simbolos.
    - Los unicos simbolos validos son _ o $
    - No puede haber espacio entre palabras
    - Las palabras se separan con Camel Case o Snake Case
        - Ejemplo Camel Case: miPrimeraVariable
        - Ejemplo Snake Case: mi_primvera_variable
    - Las variables en mayusuclas se usan para las constantes, osea, que su valor no cambia."""

# Ejemplos de Variables
mi_primera_variable = 12
mi_segunda_variable = "Esta es una cadaena de texto"

# Una vez creada podemos invocarla y hacer uso de su contenido cuando queramos.
print(mi_primera_variable)
print(mi_segunda_variable)
