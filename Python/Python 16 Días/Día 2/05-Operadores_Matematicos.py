# OPERADORES MATEMATICOS
"""
Son los simbolos clasicos con los que podemos realizar operaciones con numeros, ya sean de tipo
integer o float.

- Suma (+)
- Resta (-)
- Multiplicacion (*)
- Division (/)
- Modulo (%) El residuo de una division
- Potencia (**) Eleva a un numero
- Raiz Cuadrada (**0.5)
-- Division al Piso (//) Solo devuelve enteros sin decimales en el resultado
"""

first_number = 10
second_number = 2
third_number = 7

print(f"{first_number} + {second_number} = {first_number + second_number}")
print(f"{first_number} - {second_number} = {first_number - second_number}")
print(f"{first_number} * {second_number} = {first_number * second_number}")
print(f"{first_number} / {second_number} = {first_number / second_number}")

print(f"{first_number} dividido al piso de {second_number} = {first_number // second_number}")

print(f"{first_number} modulo de {second_number} = {first_number % second_number}")

print(f"{first_number} elevado a la {second_number} = {first_number ** second_number}")

print(f"Raiz cuadrada de {first_number}= {first_number ** 0.5}")
