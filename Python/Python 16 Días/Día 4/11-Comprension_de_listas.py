# COMPRENSION DE LISTAS
"""
Es una sintacis mas brebe en la creacion de una nueva lista basada en valores disponibles
en otra secuencia como un string u otro lista. Es un poco menos legible aunque puede ayudar
a ahorrar lineas de codigo.

Es como usar un For en una sola linea.
"""

# Llenar una lista con las letras de una plabra.
# Este es un codigo basico y funcional para ello.
palabra = "Python"
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

# Usando Compresion de Listas quedaria asi:
# Aqui letra es la variable interna.
lista2 = [letra for letra in palabra]
print(lista2)

# Funciona con valores literales
lista3 = [letra for letra in "Hola Amigos"]

# Funciona con rangos. 
lista_rango = [number for number in range(0 ,21)]
print(lista_rango)

# Incluso podemos agregar mas codigo como operaciones o hasta condicionales.
lista_pares = [number for number in range(0, 21) if number % 2 == 0]
print(lista_pares)

# Para agregar concionales con ELSE va antes del for
lista_pares_no = [number if number % 2 == 0 else "NO ES PAR" for number in range(0, 21)]
print(lista_pares_no)
