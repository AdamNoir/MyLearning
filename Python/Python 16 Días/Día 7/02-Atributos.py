# ATRIBUTOS
"""
Los atributos son variables que petenecen a la clase.
Existen atributos de clase (compartidos por todas las instancias de clase)
y atributos de instancia (que pertenencen a cada instancia de la clase)

- Self es el equivalente a This en java. Hace referncia a el atributo.
    - Self es una convencion y puede usarse cualquier otra palabra.
- Los atributos y parametros que recibe el constructor no deben llamarse necesariamente
iguales. Pero es una convension y es mas faciles identificarlos.
"""


class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


objeto_pajaro = Pajaro("Negro", "Tucan")
print(objeto_pajaro.color, objeto_pajaro.especie, objeto_pajaro.alas)
