# EXERCISE 10
"""
Cada payaso pesa 112g y cada muñeca 75g. Calcular el peso total del paquete en base al total
de payasos y muñecas vendidas.
"""
payasos = input("Ingresa la cantidad de payasos: ")
munnecas = input("Ingresa la cantidad de muñecas: ")
payasos_int = int(payasos)
munnecas_int = int(munnecas)
peso_final = (payasos_int * (0.112*1000)) + (munnecas_int * (0.075*1000))
print(f"El peso final es: {peso_final}")
