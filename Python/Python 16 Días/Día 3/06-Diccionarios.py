# DICCIONARIOS
"""
Los diccionarios son estructuras de Datos que almacenan informacion en base a 'Clave:valor'
Los elementos de un diccionario no estan ordenados por un indice, no tienen orden, sino que podemos
acceder a ellos buscando en base a su clave.

Son mutables, los valores PUEDEN SER REPEDITOS, pero las CLAVES NO PUDEN REPETIRSE.
"""

diccionario = {"C1": "Valor1", "C2": "Valor2"}
print(type(diccionario))

print(diccionario)

# Acceder a los valores en base a su clave
valor = diccionario["C1"]
print(valor)

cliente = {
    "Nombre": "Ivan",
    "Edad": 24,
    "Nacionalidad": "Mexicano"
}
print(cliente["Edad"])

# Acceder a elementos de lista u otros diccionarios desde un diccionario
new_dic = {"Clave1": [1, 2, 3], "Clave2": {"C1": "Valor1", "C2": "Valor2"}}
print(new_dic["Clave1"][1])
print(new_dic["Clave2"]["C1"])

# Sobre Escribir elemento
new_dic["Clave1"] = "Hola"
print(new_dic)

# METODOS DEL DICCIONARIO - Lo hace en una Lista de T
# uplas
# Muestra solo las claves
print(new_dic.keys())
# Muestra todos los valores
print(new_dic.values())
# Muestra el contenido
print(new_dic.items())