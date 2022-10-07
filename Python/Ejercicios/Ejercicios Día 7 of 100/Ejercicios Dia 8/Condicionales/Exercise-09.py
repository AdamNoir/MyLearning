# EXERCISE 9
"""
"""
edad = int(input("Ingresa tu edad: "))
if edad < 4:
    print("GRATIS")
elif edad >= 4 and edad <= 18:
    print("PAGAS 5 EUROS")
else:
    print("PAGAS 10 EUROS")