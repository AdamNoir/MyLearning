# LIMPIAR CONSOLA
"""
Podemos controlar la informacion mostrada al usuario por consola, limpiandola,
eliminado los diferentes mensajes que han aparecido mientras se ejecuta
el programa.

- Windows: system("cls")
- Mac/Linux: system("clear")
"""

# EN ALGUNOS IDE COMO PYCHARM SE DEBE HACER CONFIGURACION EXTRA. EN VS CODE NO
# VIDEO 82 SECCION 6

from os import system

nombre = input("Ingres tu nombre: ")

system("clear")

print(f"Tu nombre es: {nombre}")