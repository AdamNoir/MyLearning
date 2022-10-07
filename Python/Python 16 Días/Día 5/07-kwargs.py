# KWARGS
"""
Keyword arguments, sirven para identificar el argumento por su nombre, indepedientemente
de la posicion en la que se encuentra a la hora de pasarlo a la funcion. Si no se 
conoce de antemano su cantidad, el parametro **kwargs los agrupara en un
dicconario.

kwargs es una buena practica, aunque puede usarse cualquier palabra que vaya depues
de dos astericos.
"""

def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x = 3, y = 5, z = 2))

# Funcion que recibe todo los tipos de argumentos.
def prueba(num1, num2, *args, **kwargs):
    print(num1)
    print(num2)

    for arg in args:
        print(arg)
    
    for clave, valor in kwargs.items():
        print(clave, valor)
    
"""
Los primeros valores seran los argumentos normales.
    Le siguen los *args
Y para que sepa que son los valores del **kwargs pasamos argumentos
que se compongan de calve valor.
"""
prueba(1, 2, 10, 20, 30, 40, x = 100, y = 200, z = 300)

# Podemos pasarlo por variables usando * o ** en el nombre de la variabl
args = [10, 20, 30, 40]
kwargs = {"x": "100", "y": "200", "z": "300"}