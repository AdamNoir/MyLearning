# DECORADOR
def decorador_saludo(funcion):
    def saludos():
        print("Su turno no: ")
        funcion()
        print("En breve sera atendido")

    yield saludos


@decorador_saludo
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

