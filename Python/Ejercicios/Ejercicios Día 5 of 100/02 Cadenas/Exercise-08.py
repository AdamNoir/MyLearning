# EXERCISE 8
"""
Preguntar por consola el precio e algo con dos decimales y mostrar
en pantalle el total y sus decimales por separado.
"""
precio = input("Ingresa un precio con dos decimales: ")
decimal = precio.find(".")
print(f"Euros: {precio[:decimal]} centimos: {precio[decimal + 1:]}")
