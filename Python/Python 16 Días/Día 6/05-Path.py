# PATH
"""
Permite repsentar rutas de archivos en el sistema de archivos de nuestros sistema
operativo. Se destaca por su legibilidad frente a alternativas semejantes.
"""

from pathlib import Path

# Devuelve un objeto Path repsesentado por el directorio base del usuario
base = Path.home()
print(base)

# Crea la ruta Path, relativa o absoluta
guia = Path(base, "Bacelona", "Sagrada_Familia.txt")
print(guia)

# Crea otra ruta cambiando unicamente el nombre del archivo
# guia2 = guia.with_name("La_Pedrera.txt")
#print(guia2)

# Devulve la ruta de la jerarquia inmediata superior
# Podemos colocar varios Parent
#print(guia.parent.parent)

# Obtiene los archivos que coinciden con un patron
print(base.glob("*.txt"))
# De esto modo devuelve TODOS los archivos que se encuentran 
# Tambien en subcarpetas
print(base.glob("**/*.txt"))

# Permite crear rutas relavias indicando desde que punto hacia abajo
#ruta_relativa_1 = guia.relative_to("Europa")
#ruta_relativa_2 = guia.relative_to("Europa", "Españada")