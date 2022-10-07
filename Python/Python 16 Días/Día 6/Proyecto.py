# PRYECTO

# Importar Modulos
import os
from pathlib import Path
from os import system

menu_int = 0
# Establecer ruta de acceso
ruta = Path(Path.home(), "Recetas")

# Funcion para contar recetas
def contar_recetas(ruta):
    contador = 0
    for receta in Path(ruta).glob("**/*.txt"):
        contador = contador + 1
    return contador

def inicio():
    system("cls")
    print("*" * 50)
    print("Bienvenido al control de recetas")
    print(f"Las recetas se encuentran en: {ruta}")
    print(f"En total hay: {contar_recetas(ruta)} recetas")
    print("*" * 50)

def menu():
    while menu != 6:
        if menu == 1:
            pass
            # Mostrar Categorias
            # Elegir Categoria
            # mostrar recetas
            # elegir recetas
            # leer receta
            # volver al inicio
        elif menu == 2:
            pass
            # Mostrar Categorias
            # Elegir Categoria
            # Crear receta
            # volver al inicio
        elif menu == 3:
            pass
            # Crear Categoria 
            # volver al inicio
        elif menu == 4:
            pass
            # Mostrar Categorias
            # Elegir Categoria
            # mostrar recetas
            # elegir recetas
            # eliminar receta
            # volver al inicio
        elif menu == 5:
            pass
            # Mostrar Categorias
            # Elegir Categoria
            # Eliminar Categoria
            # volver al inicio
        elif menu == 6:
            pass
            # Salir
# -------------------------------

def inicio_usuario():
    """
    - Dar bienvenida al usuario
    - Ruta donde estan las carpetas
    - Cantidad de recetas que hay dentro de la carpeta
    """
    # Bienvenida al usuario
    name = input("Ingresa tu nombre: ")
    system("cls")
    # Ruta de carpetas
    ruta = Path(Path.home(), "Recetas")
    # Cantidad de recetas
    contador = 0
    for receta in ruta.glob("**/*.txt"):
        # print(f"La ruta de acceso es: {receta}")
        contador = contador + 1
    print(f"Bienvenido {name}")
    print(f"La ruta de acceso es: {ruta}")
    print(f"La cantidad de Recetas es: {contador}")
    menu_principal(name)
    

# Funcion While
def menu_principal(name):
    """
    Mostrar Menu y llamar Funciones.
    """
    while (True):
        print("1) Elige una Categoria Para Leer Recetas")
        print("2) Elige una Categoria Para Crear Recetas")
        print("3) Elige una Categoria Que Quieras Crear")
        print("4) Elige una Categoria Para Eliminar una Receta")
        print("5) Elige una Categoria Para Eliminarla Por Completo")
        print("6) Salir.")
        respuesta = input("Ingresa una opcion: ")
        if respuesta == "1":
            print("1")
        elif respuesta == "2":
            print("2")
        elif respuesta == "3":
            print("3")
        elif respuesta == "4":
            print("4")
        elif respuesta == "5":
            print("5")
        elif respuesta == "6":
            print(f"GRACIAS POR USAR EL PROGRAMA {name}")
            break
        else:
            print("No entiendo que quieres hacer. Intenta de Nuevo.")

# Funcion Leer Receta
def categoria_leer_receta():
    """
    En base a la categoria Elegida lee una receta
    """
    print("LEER RECETA")

# Ejecucion
inicio()