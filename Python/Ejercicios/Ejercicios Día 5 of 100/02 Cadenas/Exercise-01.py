# EXERCISE 1
"""
Pedir al usuario su nombre y un numero entero. Mostrar en linas distintas
el nombre el total de veces que el numero indique.
"""
name = input("Ingresa tu nombre: ")
number = int(input("Ingresa un numero entero: "))
print(f"{name}\n" * number)
