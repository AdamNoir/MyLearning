# EJEMPLO FUNCIONES
"""
Tomar una lista de tuplas y ver cual es el precio mas caro.
"""

precios_cafe = [('capuchino', 1.5), ('expresso', 2.5), ('Moka', 1.9)]

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ""
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return (cafe_mas_caro, precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El mas caro es {cafe}, cuesta {precio}")
