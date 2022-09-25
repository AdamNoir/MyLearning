# EXCERCISE 11
"""
Pedir inversion y sacar valance por tres meses. El interes es de 4%
"""
inversion = float(input("Ingresa la inversion: "))
interes = 0.04
balance_1 = (inversion * (1 + interes))
print(f"El primer balance es: {round(balance_1, 2)}")
balance_2 = (balance_1 * (1 + interes))
print(f"El segundo balance es: {round(balance_2, 2)}")
balance_3 = (balance_2 * (1 + interes))
print(f"El tercer balance es: {round(balance_3, 2)}")
