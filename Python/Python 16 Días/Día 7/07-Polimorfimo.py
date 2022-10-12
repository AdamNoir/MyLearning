# POLIMORFISMO
"""
Es el pilar de la POO mediante el cual un mismo metodo puede comportarse de diferentes maneras
segun el objeto sobre el cual esta actuando, en fundion de como dicho metodo haya sido creado
para la clase en particular.
"""


class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muu")


class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")


objeto_vaca = Vaca("Manchas")
objeto_oveja = Oveja("Esponjosa")

lista_objeto = [objeto_vaca, objeto_oveja]

for animal in lista_objeto:
    animal.hablar()


def animal_habla(animal):
    animal.hablar()


print("----")
animal_habla(objeto_vaca)
animal_habla(objeto_oveja)
