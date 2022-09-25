# PROYECTO
"""
JUEGO DE ADIVINA EL NUMERO.

- PEDIR NOMBRE DE USUARIO

- ELEGIR NUMERO AL AZAR ENTRE 1 Y 100
- DAR 8 INTENTOS AL JUGADOR PARA ENCONTRARLO
    - SI EL NUMERO QUE INGRESA EL USUARIO ES MENOR A 1 Y MAYOR A 100 INDICARLO
    - SI EL NUMERO ES MENOR AL ELEGIDO INDICARLO
    - SI ES MAYOR INDICARLO
    - SI ACIERTA SE DICE QUE HA GANADO Y CUANTOS INTENTOS LE QUEDARON.
"""
from random import randint

# Pedir nombre al usuario
name = input("Ingresa tu nombre: ")
print(f"Muy bien, {name}. He elegido un numero entre 1 y 100, y tienes 8 intentos para encontrarlo. Vamos.")

# Generar Numero random
numero_encontrar = randint(1, 100)
print(numero_encontrar)

numero_intentos = 8


while numero_intentos > 0:
    numero_jugador = int(input("Ingresa un numero: "))
    if numero_jugador < 1 or numero_jugador > 100:
        print("El numero esta fuera del rango de 1 y 100. Pierdes una vida.")
        numero_intentos = numero_intentos - 1
        print(f"Te quedan: {numero_intentos} intentos")
        continue
    elif numero_jugador < numero_encontrar:
        print("El numero es menor al numero a encontrar. Pierdes una vida.")
        numero_intentos = numero_intentos - 1
        print(f"Te quedan: {numero_intentos} intentos")
        continue
    elif numero_jugador > numero_encontrar:
        print("El numero es mayor al numero al encontrar. Pierdes una vida.")
        numero_intentos = numero_intentos - 1
        print(f"Te quedan: {numero_intentos} intentos")
    elif numero_jugador == numero_encontrar:
        print(f"FELICIDADES HAS GANADO! te quedaron {numero_intentos} intentos.")
        break
else:
    print(f"HAS PERIDO. El numero a encontrar era {numero_encontrar}")
