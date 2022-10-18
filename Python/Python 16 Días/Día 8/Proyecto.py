# PROYECTO

"""
- Turnero de farmacia con tres distintas areas:
    - Perfumeria
    - Farmacia
    - Cosmeticos
- Preguntar al usuario a que harea quiere ir
- Usar generadores para mantener la cuenta.
- Usar decoradores para agregar mensaje: Su turno es y sera atendido en cada funcion.
- Separar en Dos modulos
    - numeros donde estaran los generadores y decoradores
    - principal donde estaran las funciones (importar numeros)
"""


# DECORADOR
def decorador_saludo(funcion):
    def saludos():
        print("Su turno no: ")
        funcion()
        print("En breve sera atendido")

    yield saludos



def mi_generador_perfumeria():
    numero = 0
    while True:
        yield "P-" + str(numero)
        numero += 1



def mi_generador_farmacia():
    numero = 0
    while True:
        yield "P-" + str(numero)
        numero += 1



def mi_generador_cosmeticos():
    numero = 0
    while True:
        yield "C-" + str(numero)
        numero += 1


"""farmacia = mi_generador_farmacia()

print(next(farmacia))
print(next(farmacia))
print(next(farmacia))
print(next(farmacia))"""
def inicio():
    print("-" * 40)
    farmacia = mi_generador_farmacia()
    perfumeria = mi_generador_perfumeria()
    cometicos = mi_generador_cosmeticos()
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
