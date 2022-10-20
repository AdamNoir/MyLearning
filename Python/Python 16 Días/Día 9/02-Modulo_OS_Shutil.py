# MODULO OS & SHUTIL
"""
El modulo Shutil ofrece funcionalidades de alto nivel sobre archivos, tales como
copiar, crear, eliminar y mover entre directorios. Algunos modulos de OS tienen
objetivos similares.

- shutil.move(archivo, directorio): Muece un archivo desde el directorio actual hacia
el que se espesifica.
- os.unlink(directorio): elminina un ARCHIVO indicado.
- os.rmdir(directorio): elimina una CARPETA VACIA.
- shutil.rmtree(directorio): Elimina una carpeta indicada, incluyendo todo
lo que tenga dentro.
- send2trash: manda archivos a la papelera de reciclaje. Ocupa Pip
- os.walk(directorio): recorrer el directorio indicado y devuelve los nombres
delas carpetas y subcarpetas y archivos dentro de ellas en forma de tupa a traves
de un generador.
"""


import os
import shutil
import send2trash

# Imprimir Directorio actual
#print(os.getcwd())

# Crear Archivo y darle contenido
"""archivo = open("curso.txt", "w")
archivo.write("Texto de Prueba")
archivo.close()"""

# Mostrar en una lista los archivos y carpetas
#print(os.listdir())

# Usando SHUTIL movemos el archivo a el escritorio.
shutil.move("curso.txt","C:\\Users\\ivane\\Desktop")

# LAS SIGUENTES FORMAS DE ELIMINAR ARCHIVOS Y CARPETAS SON PELIGROSAS
# No manda los archivos a la papelera, los elimina sin posibilidad a recuperar

# os.unlink("C:\\Users\\ivane\\Desktop\\carpeta\\arch.txt")
# os.rmdir("C:\\Users\\ivane\\Desktop\\carpeta")
# shutil.rmtree("C:\\Users\\ivane\\Desktop\\carpeta")

# Metodo RECOMENDADO PARA ELIMINAR ARCHIVOS, pues los manda a la papelera
send2trash.send2trash("C:\\Users\\ivane\\Desktop\\carpeta\\arch.txt")

ruta = "C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 9\\Carpeta_Superior"

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son: ")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son: ")
    for arch in archivo:
        print(f"\t{arch}")
    print("\n")