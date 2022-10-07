# RETURN
"""
Para que una funcion devuelva un valor y este pueda almacenarce en una variable usamos
return.
- Todo lo que este debajo de un RETURN no se ejecutara.
- Una variable almacenara lo que devuelva un return.
"""
def operacion(valor1, valor2):
    return valor1 * valor2

print(operacion(10, 2))

resultado = operacion(5, 8)
print(resultado)

def operacion_variable(valor1, valor2):
    suma = valor1 + valor2
    return suma
print(operacion_variable(2, 9))
suma = operacion_variable(2, 10)
print(suma)
