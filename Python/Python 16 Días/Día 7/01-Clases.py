# CLASES
"""
Las clases son herramientas que nos permiten crear objetos, que "empaquetan" datos y
funcionalidad juntos.

Podemos pensar a las clases como el plan o plantilla a partir del cual podemos crear
pbjetos individuales, con propiedades y metodos asociados.
"""
from builtins import type


class Pajaro:
    pass


objeto_pajaro = Pajaro()
objeto_pajaro_2 = Pajaro()

print(objeto_pajaro)
print(type(objeto_pajaro))
print(objeto_pajaro_2)
print(type(objeto_pajaro_2))
