# HERENCIA
"""
La herencia es el proceso mediante el cual una clase puede tomar metodos y atributos de una clase
superior, evitando asi la repeticion de codigo cuando varias clases tienen atributos o
metodos en comun.

Para crear una clase hia tan solo basta con pasar como parametro la clase a la que queremos heredad.

Las clases hijas pueden sobreescribir los metodos o atributos o definir nuevos.
"""


class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("El animal ha nacido")


class Pajaro(Animal):
    pass


# Ver subsclases
print(Animal.__subclasses__())
# Ver de donde hereda
print(Pajaro.__bases__)

objeto_pajaro = Pajaro(2, "Amarillo")
objeto_pajaro.nacer()
print(objeto_pajaro.color)
