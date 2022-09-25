# ENUMERATE

"""
Facilita llevar las cuentas de las iteraciones, a traves de un contador de indices de un iterable que puede usarse de forma directa
en un loop, o convertirse en una lista de tuples.
"""

# Forma clasica de obtener indice de elementos en lista
lista = ["A", "B", "C",  "D"]
indice = 0

for item in lista:
    print(indice, item)
    indice = indice + 1

# Forma mas efectiva utilizando enumerate
# Aqui obtendremos una serie de tuplas
for item in enumerate(lista):
    print(item)

# De este modo podremos usar el indice como variable individual
for indice, item in enumerate(lista):
    print(indice, item)

# Crear lista de tuples de indice
# Podemos trabajar y accder a sus elementos como ya se vio con anterioridad. 
lista_tuples = list(enumerate(lista))
print(lista_tuples)





