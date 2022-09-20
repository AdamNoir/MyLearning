# VARIABLES Y TIPOS DE DATO
"""
- VARIABLES
Las variables en Python son espacios de memoria donde podemos almacenar informacion.

Esta informacion puede ir variando con el paso de la ejecucion. Las variables se identifican
con un nombre unico.

Una variable no es necesario que se cree con un valor, puede quedarse vacia. Cuando obtiene
un valor la variable pasa a pertencer un tipo de dato espesifico.

Estas variables se pueden invocar siempre que lo necesitemos para acceder a su
informacion.

- TIPOS DE DATO
En Python podemos encontrar varios tipos de datos, tambien conocidos como estructuras
de Datos, y son fundamentales en la programacion que determinan el tipo de informacion que
podemos almacenar y como manipularla.

Cada tipo de dato tiene sus metodos para trabajarlos. Y es posible convertir de un
tipo de dato a otro.

- Strings (str):
    Son cadenas de caracteres. Son textos. Es aquello que va entre comillias
    que abre y cierra. No importa si son numeros, letras, caracteres, si va entre comillas
    es un texto y sera tratao como tal.

- Numeros:
    - Integer (int):
        Son numeros enteros, ya sean negativos y positivos. Con ellos podemos realizar
        operaciones matemaricas.
    - Float:
        Son numeros con punto decimal, ya sean negativos o positivos. Igualmente podemos
        realizar operaciones matematicas.
    Podemos realizar operaciones usando numeros float e integer.
- Booleans (bool):
    Son valores binarios, 0 o 1, True o False.
- Listas:
    Conjunto ordenaro de elementos. Una lista se determina con corchetes [] y cada elemento
    tiene un indice, un lugar en la lista. La lista puede almacenar cualquier tipo de dato,
    incluso una mescolanza de ellos y hasta otras listas.
- Diccionarios:
    Un diccionario se determina por llaves {} y se compone por objetvos de clave-valor.
    Cada valor tiene una clave con el que podemos identificarlo. Cada calve debe ser unica.
- Tuples:
    Son un conjunto ordenado de elementos, donde cada elemento tiene un indice. Puede almacenar
    cualquier tipo de dato incluido otra tupla. La unica diferencia es que NO SE PUEDE
    MODIFICAR. Se determina con ().
- Sets:
    Se determina con llaves {} y admite cualquier tipo de dato, con la condicion
    QUE SOLO SEAN VALORES UNICOS, siendo esto lo que le diferencia de la lista o tuplas,
    que si puden tener elementos repetidos.
"""

# Strings
variable_string = "Hola Mundo"

# Integer
variable_integer = 123

# Float
variable_float = 10.223

# Booleans
variable_booleana = True

# Listas
variable_lista = ["Hola", 12, "Mundo", "Adios", 10.23, False, ["Hola", "Amigos", 23], "Fin"]

# Diccionario
variable_diccionario = {
    "Clave_1": "Valor1",
    "Clave_2": 10,
    "Clave_3": ["1", "2", 3, 4]
}

# Tupla
variable_tupla = ("Hola", 12, 9, ["4", "2"], 9)

# Set

variable_set = {'1', '2', '3'}
