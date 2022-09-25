# EXERCISE 6
"""
Pedir una frase y una vocal, devolver la frase con la vocal en mayuscula
"""
frase = input("Ingresa una Frase: ")
vocal = input("Ingresa una vocal: ")
print(f"{frase.lower().replace(vocal, vocal.upper())}")
