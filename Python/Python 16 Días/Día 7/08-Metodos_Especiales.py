# METODOS ESPECIALES
"""
Pueden encontrarse como metodos magicos o dunder methods (dunder = double undersoce, doble guion bajo)
Ayudan a sobreescribir metodos incorporados de Python sobre nuestras clases para controlar el
resultado devuelto.
"""

class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    # Modifica como se imprime el objeto
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"

    # Permite establecer que tamaño o largo mostrara
    def __len__(self):
        return self.canciones

    # Establece un mensje cuando eliminamos el objeto
    def __del__(self):
        print("Se elimino.")


mi_cd = CD("Pink Floyd", "The Wall", 24)

print(mi_cd)
print(len(mi_cd))

del mi_cd
