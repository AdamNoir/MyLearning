# EXERCISE 5
"""
Para tributar un impuesto debes tener mas de 16 años y tener ingresos iguales
o superiores a 1000.
Escribir un programa que pregunete edad e ingresos y determinar si debe
tributar o no.
"""
age = int(input("Ingresa tu edad: "))
money = float(input("Ingrea tus ingresos mensuales: "))

if age > 16 and money >= 1000:
    print("Debes tributar")
else:
    print("No debes tributar")