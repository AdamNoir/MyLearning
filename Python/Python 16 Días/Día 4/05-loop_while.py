# LOOP WHILE
"""
Los loop while resultan muy parecidos a las condicionales IF. Pertenecen al segunto tipo de Loop que se
ejecuta siempre y cuando se cumpla una determina condicion.

A estos ciclos se les puede agregar un ELSE al final, por si es que nunca se cumple la condicion y no se cumple
el ciclo.

Podemos hacer uso de demas palabras clave (Igualmente aplicables a un for)
- Break: termina el ciclo y ejecuta lo demas que haga falta del programa
- Continue: Interrumple la iteracion y regresa al principio del ciclo para iterar lo que sigue.
- Pass: no altera el programa, solo va donde debe ir una declaracion pero no se quiere relizar acciones.

Hay que ser  cuidadoso con los while ya que podemos entrar en un ciclo infinito y todo se jode. Asi que es bueno tener
una instruccion dentro que se asegure que algo cambie.

Este loop es perfecto para interactuar con los usuarios, pues depende si realiza ciertas acciones o no.
"""

coins = 5

while coins > 0:
    print(f"Tengo {coins} monedas")
    coins = coins - 1
else:
    print("No tienes monedas")

# Pedir valores al usuarios
answer = "s"
while answer == "s":
    answer = input("Ingresa una letra s o letra n: ")
else:
    print("Haz elegido n, gracias.")

# Palabras clave
# break

name = input("Ingresa un nombre: ")
for letra in name:
    if letra == "a":
        break
    print(letra)

# Continue
for letra in name:
    if letra == "a":
        continue
    print(letra)


