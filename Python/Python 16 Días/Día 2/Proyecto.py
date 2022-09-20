# CONTADOR DE COMISIONES
"""Preguntar nombre al empleado y su total de ventas, esas ventas
sacarles el 13% e indicar en un mensaje su porcentaje.
Solo dos decimales
"""

nombre = input("Dime tu nombre: ")
ventas = input("Dime el total de ventas de este mes: ")
PORCENTAJE = 13 / 100
print(f"{nombre} tu comision por ${ventas} es: {round(int(ventas) * PORCENTAJE)}")
