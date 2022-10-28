
import Proyecto_Generadores_Decoradores


def inicio():
    print("-" * 40)
    farmacia = Proyecto_Generadores_Decoradores.mi_generador_farmacia()
    perfumeria = Proyecto_Generadores_Decoradores.mi_generador_perfumeria()
    cometicos = Proyecto_Generadores_Decoradores.mi_generador_cosmeticos()
    print("[1] Farmacia")
    print("[2] Perfumeria")
    print("[3] Cosmeticos")
    print("[4] Salir.")
    while True:
        eleccion = int(input("Elige opcion: "))
        if eleccion == 1:
            print(next(farmacia))
        elif eleccion == 2:
            print(next(perfumeria))
        elif eleccion == 3:
            print(next(cometicos))
        elif eleccion == 4:
            print("Gracias por usar.")
            break


inicio()
