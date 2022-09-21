# METODO INDEX
"""
En Python existen mas de 30 metodos para los Strings.

El metodo index() nos permite explorar los Strings, ya que encuentra el indice
de un caracter o varios caracteres dentro de un texto.

Podemos saber que caracter hay en una posicion indicada, o podemos saber que posicion ocupa
cierto caracter.

Toda cadena comienza por el indice 0. Los espacios vacios tambien son un caracter y tienen su indice.
"""

my_string = "Esto es una Prueba"

# Ver el caracater que se encuentra en determinado indice
print(my_string[0])
print(my_string[5])

# Podemos realizar la busqueda inversa usando numeros negativos
print(my_string[-1])

# Metodo index
# Encontrar el indice de determinado caracter
print(my_string.index("s"))

# Al buscar palabras completas nos dice DESDE QUE INDICE COMIENZA
print(my_string.index("Prueba"))

# Al no encontrar el indice dara una excepion
# print(my_string.index("x"))

# Al agregar mas valores al index establecemos DESDE DONDE BUSQUE, HASTA DONDE
print(my_string.index("a", 5, 11))

# Rindex es index pero al reves, busca desde el ultimo caracter
print(my_string.rindex("a"))
