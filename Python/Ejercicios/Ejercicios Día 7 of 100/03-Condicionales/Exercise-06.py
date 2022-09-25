# EXERCISE 6
"""
Grupo A Y B estan conformado por: 
Grupo A: Mujeres con letra anterior a letra M y hombres con letra N posterior.
El b son todos los demas.
Preguntar sexo y nombre e indicar que grupo es.
"""
sex = input("¿Eres hombre o mujer?: ")
name = input("Ingresa tu nombre: ")

if (sex.lower == "mujer" and name.lower() < "m") or (sex.lower == "hombre" and name.lower() > "n"):
    print("ERES DE A")
else:
    print("Eres del B")
