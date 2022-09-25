# EXERCISE 9
"""
Pedir al usuaro cantidad a invertir, interes anual y el numero de años.
Mostrar por consula el capital obtenido de la inversion.
"""
cantidad_invertir = input("Ingresa la cantidad a Invertir: ")
interes_anual = input("Ingresa el interes anual: ")
numero_años = input("Ingrea el numero de años: ")
cantidad_invertir_float = float(cantidad_invertir)
interes_anual_float = float(interes_anual)
numero_años_int = int(numero_años)
capital_final = (round(cantidad_invertir_float * (interes_anual_float / 100 + 1) ** numero_años_int, 2))
print(f"El capital obtenido es: {capital_final}")
