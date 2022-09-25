# EXCERCISE 7
"""
Pedir al usuario el peso en kilos, y la estatura en metors. Sacas el IMC, indice de masa corporal.
La formula es:
    peso / altura en metros cuadrados.
"""
peso = input("Ingresa tu peso: ")
altura = input("Ingresa tu altura: ")
altura_float = float(altura)
peso_float = float(peso)
imc = round(peso_float / (altura_float**2),2)
print(f"Tu IMC es: {imc}")

