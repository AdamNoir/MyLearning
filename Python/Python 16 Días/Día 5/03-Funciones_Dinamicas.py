# FUNCIONES DINAMICAS
"""
Dentro de una funciones podemos integrar diferentes herramientas como el control de flujo,
permitiendo crear funciones dinamicas y existentes.
Todo puede entrar, como otras funciones, condicionales, loops, palabras clave como
break, continue...
"""

# Usar Funcion range
# Determina si un numero es de tres cifras
def chequear_3_cifras(numero):
    return numero in range(100, 1000)
resultado = chequear_3_cifras(100)
print(resultado)

# Chequear si los elementos de una lista son de 3 cifras
def chequear_3_cifras_lista(lista):
    """
    Puede haber varios return en una misma funcion. Cuando se ejecute uno la funcion termina.
    Si no encuentra nada devolvera false, pero si encuentra al menos uno dara true.
    """
    for n in lista:
        if n in range(100, 1000):
            return True
        else:
            pass
    # Esta es la ultima linea. Solo pasara por aqui si no encuentra nada.
    return False

resultado = chequear_3_cifras_lista([33, 120, 13])
print(resultado)

# Misma idea que el anterior, solo que devuelve una lista con los numeros que cumplen la condicion.
def chequear_3_cifras_lista_devolver(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100, 1000):
            lista_3_cifras.append(n)
        else:
            pass
    # Esta es la ultima linea. Solo pasara por aqui si no encuentra nada.
    return lista_3_cifras
resultado = chequear_3_cifras_lista([33, 120, 13])
print(resultado)

