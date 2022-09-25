# EXERCISE 3
"""
Pedir dos numeros y mostrar en pantalla su division. Si el divisor es 0 mostrar un
numero.
"""

number_1 = int(input("Ingrea un numero: "))
number_2 = int(input("Ingrea otro numero: "))

if number_2 == 0:
    print("ERROR! NO PUEDES DIVIDIR ENTRE 0")
else:
    print(f"El resultado de la divison es: {number_1 / number_2}")