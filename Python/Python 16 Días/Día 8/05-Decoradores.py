# DECORADORES
"""
Los decoradores son patrones de diseño usados para dar nuevas funcionalidades a los objetos (en este caso funciones),
modificando su comportamiento sin alterar la estructura: SON FUNCIONES QUE MODIFICAN FUNCIONES.

- Las funciones en Python pueden ser asignadas a una variable, de este modo los argumentos pasan a la variable
para poder ejecutar la funcion.
    mi_variable = funcion
    mi_variable(argumentos_funcion)

- Podemos definir funciones dentro de otras funciones
- Podemos definir funciones que reciban otras funciones.
"""


# Funcion que se usara de decorador.
# el argumento que recibe es una funcion.
def decorar_saludo(funcion):

    # Acciones extra que dotara a la siguente funcion. Ocupa los mismos argumentos.
    def otra_funcion(palabra):
        print("HOLA")
        # Esta linea indica cuando se ejecutra la funcion a la que se aplicara el decorador.
        funcion(palabra)
        print("ADIOS")
    # Retornamos la funcion para poder usarla.
    return otra_funcion


@decorar_saludo
def mayusculas(texto):
    print(texto.upper())


@decorar_saludo
def minusculas(texto):
    print(texto.lower())


mayusculas("ivan")
minusculas("IVAN")
