# MODULO COLLECTIONS
"""
El modulo de Collection amplia los tipos de contendores en Python. Un contenedor almacena diferentes objetos y
proporciona una nueva forma de acceder e iterar.

- Counter: Subclase del diccionario usado para contar las repeticiones de cada elemento en un iterable en
forma de diccionario.

- DefaultDict: subclase del diccionario usado para proporcionar valores por defecto PARA LAS CLAVES QUE NO EXISTEN,
evitando errores. El valor puede ser un int, lista o una funcion lambda que proporcione el valor directamente.

- NamedTuple: devuelve una tupla donde las posiciones de sus elementos tienen un nombre, ademas de un numero de
indice como las tuplas tradicionales.
"""

from collections import Counter
from collections import defaultdict
from collections import namedtuple

# COUNTER
# Cada elemento se volvera una clave del diccionario y su valor ser el total de repeticiones de dicho elemento.
numeros = [1, 2, 2, 1, 2, 3, 4, 1, 2, 6, 5, 6, 7, 4, 1, 1, 8, 5, 8, 9, 9, 8]
print(Counter(numeros))

# Contara cara elemento y nos dira cuantas vedes se repite
print(Counter("mississipi"))

# Tomara cada palabra (por eso usar split) para dejar en claro cuanto se repite cada una de ellas.
frase = "al pan pan y al vino vino"
print(Counter(frase.split()))

# Podemos asignar el valor de counter a  una variable y hacer uso de sus metodos al ser un objeto.
serie = Counter([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4])
# Muestra el elemento mas comun. Al no pasar nada muestra todos los elementos. Podemos pasar de argumento 1, 2, 3,
# dependiendo.
print(serie.most_common())

# DEFAULD DIC
# Cada que llamemenos a una clave que no existe dara este mensaje.
mi_dic = defaultdict(lambda: "No hay nada aqui.")

mi_dic["uno"] = "valor 1"
print(mi_dic["dos"])

print(mi_dic)

# NAMED TUPLE
# Podemos acceder a los elementos de la tupla como si fuera propieades de objeto.
Persona = namedtuple("Persona", ["nombre", "altura", "peso"])
ariel = Persona("Ariel", 1.50, 45)
print(ariel.peso)

