# DIRECTORIOS
"""
Para trabajar con archivos que se encuentran en directorios diferentes a los de nuestro codigio, requiere
el uso del modulo OS, el cual tiene funciones para interacutuar con el sistema operativo.

- os.getcwd(): Obtiene y devuelve el directorio actual sobre el que estamos trabajando.
- os.chdir(ruta): Cambia el directorio de trabajao a la ruta espesificada
- os.makedirs(ruta): Crea una carpeta, asi como todas las intermedias necesarias, de acuerdo a una ruta
espesifica.
-  os.path.basename(ruta): Dada una ruta, obtiene el nombre del archivo.
- os.path.split(ruta): Devuelve una tupla que contiene el directorio y el nombre del al base, el archivo.
- rmdir(ruta): Elimina el directorio indicado en la ruta.
"""

import os

ruta = os.getcwd()
print(ruta)

nueva_ruta = os.chdir("C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 6\\Prueba")
archivo = open("hola.txt")
print(archivo.read())

# Crea una carpeta
# Si la carpeta ya la creo dara error.
# nueva_carpeta = os.mkdir("C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 6\\Prueba\\otra_prueba")

# Crea una carpeta y sus sub carpetas
# nueva_carpeta = os.makedirs("C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 6\\Prueba\\otra_prueba\\otra_prueba\\otra_prueba\\hola.txt")

# La base seria seria el nombre del archivo que busco en una ruta
# El dir name es la ruta hacia un directorio que contiene ese archivo
ruta_base = os.path.basename("C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 6\\Prueba\\hola.txt")
print(ruta_base)
ruta_dir = os.path.dirname("C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 6\\Prueba")
print(ruta_dir)
ruta_tupla = os.path.split("C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 6\\Prueba\\hola.txt")
print(ruta_tupla)

# Remueve una carpeta SI ESTA VACIA
#os.rmdir("C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 6\\Prueba\\otra_prueba")