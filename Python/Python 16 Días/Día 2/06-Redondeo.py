# REDONDEO
"""
Facilita la interpretacion de valores numericos al limitar la cantidad de decimales.
Tambien, aproxima al decimal mas cercano. Al redondear obviamente pasa a ser un int.

De .5 para arriba redondea hacia arriba.

De .4 para abajo redonde hacia abajo.
"""

print(f"Valor sin redondeo: {90/7}, valor con redondeo {90/7}")

# Podemos almacenar el resultado de Round en una variable
redondeo = round(90/7)
print(redondeo)

# Con round podemos decir cuando decimales queremos mostrar.
valor = 97.897677777123
print(round(valor, 3))

