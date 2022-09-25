# EXERCISE 2
"""
Preguntar nombre completo al usuario.
Mostrar el nombre tres veces:
    1) todo en minusculas
    2) todo en mayusculas
    3) La primera letra en mayuscula
Puede ingresarse como sea
"""
name = input("Ingresa tu nombre: ")
print(name.lower())
print(name.upper())
lista = name.split()
for indice, letter in enumerate(lista):
    letter.lower()
    new = letter.capitalize()
    lista[indice] = new
print(" ".join(lista))

