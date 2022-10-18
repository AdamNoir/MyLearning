# GENERADORES
"""
Los generadores son un tipo especial de funciones que devuelven un iterador que no almacena su contenido completo en memoria.
Sino que "demora la ejecucion de una expresion hasta que su valor se solicita.

- En lugar de return usamos YIELD.
    - Puede haber varuis yield en un generador y este no interrumpira la ejecucion.
"""


def mi_funcion():
    return 4


def mi_generador():
    yield 4


print(mi_funcion())
print(mi_generador())
g = mi_generador()
print(next(g))

# Otro Ejemplo con Listas
def funcion_lista():
    lista = []
    for numero in range(1, 5):
        lista.append(numero * 10)
    return lista


def generador_lista():
    for numero in range(1, 5):
        yield numero * 10


print(funcion_lista())
generador = generador_lista()
print(next(generador))
print(next(generador))
