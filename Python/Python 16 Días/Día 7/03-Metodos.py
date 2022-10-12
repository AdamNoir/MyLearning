# METODOS
"""
Los objetos creados a apartir de una clase tambien contienen metodos.
Dicho de otra manera, los metodos son las funciones que petenecen al objeto.

Cada vez que un atributo de objeto sea indovado debemos incluir self, que se
refiere a la instancia misma, indicando la pertenencia de atributo.
"""


class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"Pio y mi color {self.color}")

    def volar(self, metros):
        print(f"volo {metros} metros")


objeto_pajaro = Pajaro("Negro", "Dodo")
objeto_pajaro.piar()
objeto_pajaro.volar(30)
