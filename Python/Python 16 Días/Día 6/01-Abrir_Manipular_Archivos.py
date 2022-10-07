# ABRIR Y MANIPUÑAR ARCHIVOS
"""
La manipulacion de archivos en Python se engloban bajo las funciones de E/S o entrada y salida.

- open: Abre un archivo y devuele un objeto de tipo archivo sobre el cual pueden aplicarse metodos.
- read: Devuelve un numero espesificado de bytes archivo. Devolvera el archivo completo.
- readline: Devuelve una linea de archivo, limitada por el numero indicado en el parametro.
- readlines: Devuelve una lista con cada una de las lineas de archivo. 
- close: Cierra el archivo. No puede ser leeido o modificado una vez cerrado. 
"""

# No hara nada, solo abrira el archivo.
my_file = open("C:\Programming\MyLearning\Python\Python 16 Días\Día 6\Prueba.txt")

# No mostrara contenido, solo el tipo de objeto y en que modo se encuentra el archivo.
print(my_file)

# Para poder leer usamos el metodo read(). Y este deberia ir en un print para mostrar contenido.
#print(my_file.read())
# Podemos almacenar el contenido en una variable de tipo STRING
#todo_texto = my_file.read()
#print(todo_texto)

# Podemos obtener el contenido de una linea
# Esta linea igual podemos almacenarla en variable o imprimirla
una_linea = my_file.readline()
print(una_linea)

# Para poder todas las lineas debemos ir colocando varias veces el readline.
# Esto es porque se guarda un punto hasta donde se leyo y apartir de ahi continua.
una_linea = my_file.readline()
print(una_linea)

# Read Lineas almacena las lineas en una lista
# Sobre esta lista podemos usar todos los metodos de listas.
lista = my_file.readlines()
print(lista)



# Se recomienda al final colocar CLOSE() para reservar espacio en memoria.
my_file.close()