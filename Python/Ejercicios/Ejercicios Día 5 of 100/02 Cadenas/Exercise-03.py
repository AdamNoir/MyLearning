# EXERCISE 3
"""
Pedir a al usuario su nombre y despues mostrar el nombre y el total de letras que tiene.
"""
name = input("Ingresa tu Nombre: ")
name_sin_espacios = name.replace(" ", "")
print(f"{name} tiene {len(name_sin_espacios)}")
