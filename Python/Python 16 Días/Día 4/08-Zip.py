# ZIP
"""
Crea una lista a partir de dos listas. La lista resultante es una lista compuesta por tuples.

Zip solo une, para poder usarla como lista debemos de usar la funcion list().

Zip llega hasta el largo de la lista mas corta, por lo que no habra error si combinamos listas de tamaños distintos.

Podemos combinar cuantas listas nos sea necesario
"""
names = ["Ivan", "Fernando", "Maria"]
ages = [24, 25, 30]

combinados = list(zip(names, ages))
print(combinados)

# Agregar una tercer lista
city = ["Manhattan", "Paris", "Madrid"]

combinados = list(zip(names, ages, city))
print(combinados)

# Podemos iterar esta lista como cualquier otra
for name, age, city in combinados:
    print(f"El nombre es {name} su edad es {age} y es de la ciudad de {city}")





