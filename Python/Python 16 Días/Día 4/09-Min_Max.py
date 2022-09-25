# MIN AND MAX
"""
Min es una funcion que devuelve el valor minumo de un iterable (lista, tuple, string) y max devuelve el valor maximo.

Si se trata de un string, devuelve los valores ALFABETICAMENTE.
Esto quiere decir que ira comparando si es una a, luego una b, y asi. 

"""
minimo = min(10, 7, 11, 24, 1, 2)
maximo = max(10, 81, 2, 100 , 1231)
print(minimo)
print(maximo)

# Maximo de una lista
lista = [57, 90, 12, 13, 1, 8, 45, 12]
print(max(lista))
print(min(lista))

# Lista de Strings
names = ["Fernando", "Maria", "Alicia", "Alberto", "Macario"]
print(min(names))
print(max(names))

# Primero busca en las letras mayuculas luego minusculas
name = "Maria"
print(max(name))

# En un diccionario buscara por defecto en sus claves
dicc = {"c1": 45, "c2": 30}
print(max(dicc))
# Con values podemos ver el valor mas grande o mas pequeño
print(min(dicc.values()))



