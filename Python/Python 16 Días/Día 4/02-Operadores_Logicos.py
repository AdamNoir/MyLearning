# OPERADORES LOGICOS
"""
Nos permieten tomar decisiones basadas en mutiples comparaciones.
- AND 
    Solo devuelve true su ambas comparaciones son verdaderas
- OR
   Devuelve true cuando al menos una de las dos condiciones es verdadera
- NOT
    Devuelve true cuando la condicion no se cumple.
"""

# Aunque no es necesario, por temas de legibilidad se recomienda usar parentesis en las comparaciones
print((10 == 10) and (2 > 1))

# Podemos realizar operaciones logicas con varios tipos
print((19 + 1 > 30) and ("Hola" == "Adios"))

print((10 > 1) or ("Saludo" == "Saludo"))

# Podemos buscar en varios string a la vez
text = "Esto es una frase epica"
print(("Esto" in text) and ("es" in text))
print(("Esto" in text) or ("Amigos" in text))

print(not(10 > 1))
