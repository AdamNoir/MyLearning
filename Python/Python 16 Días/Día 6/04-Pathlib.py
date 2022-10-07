# PATHLIB
"""
Modulo Pathlib disponoble desde 3.4

Perimite crear objetos Path, enerando rutas que permiten ser interpetadas
por diferentes sistemas operativos.

Es posible concatenear objetos Path y String con un delimitador / para contruir 
rutas completas.

- read_text(): lee el contenido de un archivo sin necesidad de abrirlo o cerrarlo
- name: devuelve el nombre y extension del archivo
- suffix: devuelve la extension del archivo (sufijo)
- steam: devuelve el nombre del archivo sin extension
- existis: verifica si el directorio o archivo existe. Devuelve true o false.
"""

from pathlib import Path, PureWindowsPath

carpeta = Path("/home/ivannyva/Documentos/All My Test/Dot Py/Día 6/pathlib.py")

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if carpeta.exists():
    print("EXISTE")
else:
    print("No existe")

# Convierte a una ruta de Windows
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)