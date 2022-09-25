# EXERCISE 10
"""
Pedir fecha de cumpleaños al usuario.
Adaptar para cuando dijite dia o mes un solo digito tenga un 0 delante.
"""
fecha = input("Ingresa una Fecha: ")
lista_fecha = fecha.split("/")
if int(lista_fecha[0]) < 10:
    if len(lista_fecha[0]) < 2:
        lista_fecha[0] = "0" + lista_fecha[0]
if int(lista_fecha[1]) < 10:
    if len(lista_fecha[1]) < 2:
        lista_fecha[1] = "0" + lista_fecha[1]
print("/".join(lista_fecha))
