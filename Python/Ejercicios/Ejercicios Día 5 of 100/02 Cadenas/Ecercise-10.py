# EXERCISE 10
"""
Pedir una cesta de productos separados por coma y mostrar cada producto
en una linea distinta.
"""
productos = input("Ingresa Productos: ")
productos = productos.split(", ")
for producto in productos:
    print(producto)
#print(productos)
