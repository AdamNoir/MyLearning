# CONTROL DE FLUJO
"""
Determina el orden en el que el codigo de un programa se va ejecutando.
Esto se maneja con las condicionales, los loops y las funciones.

Las CONDICIONALES if, revisan que si una determinada comparacion se cumple se ejecute un bloque de codigo,
sino se comple se ejecute otro.

- IF compara si una condicion es verdadera, y si lo es ejecuta su bloque de codigo.
- ELIF es una combinacion y se usa cuando una comparacion no se cumple, evalue otra.
- ELSE se usa cuando todas las comparaciones dieron falso. 

Podemos anidar if. Es decir, colocar condiconales if dentro de otras. Esto es para cuando si una condicion se cumple, ocupemos
realizar otra comparacion. Podemos anidar tantas como queramos.
"""

# IF
if 10 == 10:
    print("Son iguales")

if True:
   print("Es verdadero")

# Si la condicion no se cumple no ejecutara nada.
if False:
   print("Esto no se va a cumplir")

# ELSE
if "Animal" == "Persona":
    print("Esto no se va a cumplir")
else:
    print("Animal no es lo mismo que persona")

# ELIF
my_pet = "Conejo"
if my_pet == "Perro":
    print("Tienes de mascota un perro")
elif my_pet == "Pez":
    print("Tienes de mascota a un pez")
elif my_pet == "Conejo":
    print("Tienes de mascota a un conejo")
else:
    print("No se que mascota tienes")

# CONDICIONALES IF ANIDADAS
age = 18
score = 98
if age >= 18:
    print("Eres mayor de edad")
    if score >= 70:
        print("Haz pasado la materia")
    else: 
        print("Has reprobado la materia")
else:
    print("Eres menor de edad")

