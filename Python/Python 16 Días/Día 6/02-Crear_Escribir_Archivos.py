# CREAR Y ESCRIBIR ARCHIVOS
"""
Para poder escribir en un archivo de Python debemos de tener bien espesificado el modo de apertura.

- r (read, lectura): Modo por defecto. Permite leer el contenido pero no escribir. Da error si el archivo
no existe.
- a (añadir, append): Abre el archivo y permite escribir debajo de la ultima linea. Crea el archivo si este
no existe.
- w (write, escribir): Abre o crea un archivo si no existe. Sobre escribir el contenido.
- x (create, crear): Crea un archivo y da error si ya existe. 
"""

# Modo escritura
# Como no existe el archivo lo creara.
my_file = open("Día 6\Prueba1.txt", "w")
# No incluye salto de linea, debemos de establecerlo con los caracteres de escape
my_file.write("Soy otro contenido ")
my_file.write("Soy otro contenido")

# writelines agrega una lista de string, PERO NO AGREA SALTO DE LINEAS NI ESPACIOS. Todo pegado.
my_file.writelines(["Hola", "Somos", "Mas", "Contenido"])

my_file.close()

# Abrir con este metodo añade texto PERO NO REMPLAZA, continua desde la ultima linea
my_file2 = open("Día 6\Prueba1.txt", "a")
my_file2.write("Jajajaja xD")
my_file2.write("Jajajaja xD")
my_file2.close()