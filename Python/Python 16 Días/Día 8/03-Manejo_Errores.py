# MANEJO DE ERRORES
"""
Existen estrategias para capturar y gestionar los errores que pueden presentarse
al ejecutar un programa, a fines de evitar una falla.

- Try:
    El codigo que se encuentra se ejecutara hasta finalizar o hasta presentar algun error.
- except:
    Contiene el manejador de erroes (respuesta del programa ante un error) atrapando las
    excepciones que ocurren durante la ejecucion.
- else:
    Engloba el codigo que se ejecutara cuando no haya ocurrido ninguna excepcion. 
- finally:
    Es el codigo que se ejecutara siempre, haya o no errores.
"""


def sumar():
    numero1 = int(input("Ingresa un numero: "))
    numero2 = int(input("Ingresa un segundo numero: "))
    print(numero1 + numero2)
    print("Gracias por sumar")


def pedir_numero():
    while True:
        try:
            numero = int(input("Pedir numero: "))
        except:
            print("Ese no es un numero.")
        else:
            print(f"TU numero es: {numero}")
            break
    print("Fin")


pedir_numero()

try:
    sumar()
except ValueError:
    print("Ese no es un numero")
except TypeError:
    print("No puedes concatenar tipos distintos de ese modo")
else:
    print("Ha salido todo bien")
finally:
    print("Hemos acabao.")

