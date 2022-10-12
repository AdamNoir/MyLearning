# HERENCIA EXTENDIDA
"""
Las clases hijas que heredan de las clases superiroes pueden crear nuevos metodos o sobreescribir
los de la clase padre.

Asimismo, una clase hija puede heredar de una o mas clases, y a su vez trasmitir herencia
a clases nietas.


"""


class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("El animal ha nacido")

    def hablar(self):
        print("El animal emite un sonido")


class Pajaro(Animal):
    # Sobre escribir metodo constructor
    def __init__(self, edad, color, altura):
        # Para no repetir todos los atributos de la clase padre
        super(Pajaro, self).__init__(edad, color)
        self.altura = altura

    def hablar(self):
        print("Pio, Pio")

    def volar(self, metros):
        print(f"Volo {metros} metros")


objeto_pajaro = Pajaro(2, "Amarillo", 10)
objeto_pajaro.hablar()
objeto_pajaro.volar(10)


# Herencia multiple
"""
Si un metodo o atributo se repetie en dos clases, y una clase hereda de ambas,
buscara primero en la clase de la que hereda primera, de la que primero se pasa entre
parentesis. Y despues en la que sigue, y la que sigue.

Si hereda directamente de una clase, buscara en esa, y despues ira subiendo como en un arbol
genialogico.
"""


class Padre:
    def hablar(self):
        print("Hola")


class Madre:
    def reir(self):
        print("Jajaja")

    def hablar(self):
        print("Saludos")


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


objeto_nieto = Nieto()
objeto_nieto.hablar()
# Orden de herencia
print(Nieto.__mro__)
