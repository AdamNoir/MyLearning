# LOOP FOR
"""
Lo Loops son ciclos, repeticiones que hacen que algo vuelva a ejecutarse una y otra vez.
Estos loops pueden estar condicionados a una cantidad definidad de iteraciones, y los que estan sujetos a que se cumpla alguna condicion.

Algunos elementos como las listas o los string sin iterables, es decir, que con un ciclo podemos recorrer uno a uno sus elementos.

-FOR
    A diferencia de otros lenguajes, en Python el For no es necesario indicar la cantidad de veces que se reccorrera, sino que actua en base a los elementos
    que contiene un iterable. Esto lo hace con una variable interna (que podemos llamar y usar) que contendra cada uno de los elementos durante la ejecucion.
Es importante saber que esta variable interna SOLO PODEMOS USARLA DENTRO DEL CICLO FOR.
"""

list = ["A", "B", "C", "D"]

# letter es la variable interna del ciclo, con cada iteracion su valor cambira.
for letter in list:
    print("La letra es: " + letter)

# Podemos saber el indice de cada elemento
for letter in list:
    letter_index = list.index(letter)
    print(f"La letra es: {letter} y su indice es: {letter_index}")

# Podemos dentro de los Loops agregar codigo como Condicionales, para ir filtrando los elementos si es necesario.
names_list = ["Ivan", "Fernando", "Maria", "Jose", "Ivone"]
for name in names_list:
    if name.startswith("I"):
        print(name)
    else:
        print("No comienza con I")

# Podemos iterar Strings
word = "Python"
for letter in word:
    print(letter)

# Podemos iterar contenido como listas o strings directamente, y no solo pasando variables
for element in "Hola mis bellos amigos como estan":
    print(element)
for elemento in [1, 2, 3, 4, 5]:
    print(elemento)

# Podemos iterar diccionarios
diccionario = {"Clave1": "valor1", "Clave2": "valor2"}

# De este modo solo muestra las calves
for dicc in diccionario:
    print(dicc)
# Agregando el metodo values, keys o items podemos definir que queremos iterar
for dicc in diccionario.values():
    print(dicc)


# Itear dentro de otra lista
for elemento_a, elemento_b in [[1, 2], [3, 4], [5, 6]]:
    print(elemento_a)
    print(elemento_b)




