# TIPOS DE METODOS
"""
Los metodos de insncia es lo que ya conocemos.

Los metodos de clase llevan el decoradaor classmethod:
    - Pueden modificar atributos de la clase
    - No pueden llamar metodos de intancia, solo se clase.
    - No requieren de una insncia para usarse
    - usan cls en lugar de self

Metodos estaticos llevan el decorador staticmethod:
    - No pueden modificar los atributos ni acceder a otros metodos de instancia o clase.

Una instancia puede acceder a todos los metodos.
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

    # Metodo de instancia que modifica los atrobutos
    # Puede llamar a otros metodos
    def pintar_negro(self):
        self.color = "Negro"
        print(f"Ahoa es de color {self.color}")
        self.piar()

    # Metodo de clase. No puede llamar a otros metodos de Instancia.
    # Puede modificar los atributos de clase o llamar otros metodos de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)

    # No puede acceder a otros metodos, mi modificar atributos.
    @staticmethod
    def mirar():
        print("El pajaro mira")


objeto_pajaro = Pajaro("amarillo", "canario")
objeto_pajaro.volar(10)
objeto_pajaro.mirar()
objeto_pajaro.poner_huevos(2)

Pajaro.poner_huevos(1)

Pajaro.mirar()
