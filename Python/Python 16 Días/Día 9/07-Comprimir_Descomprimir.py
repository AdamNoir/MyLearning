# COMPRIMIR Y DESCOMPRIMIR
"""
El formato .zip permite comprimir archivos sin perdida de informacion, ahorrando espacio de almacenamiento
y manteniento documenos relacionados en un mismo archivo de extension .zip.
"""

import zipfile
import shutil

# Comprimir archivos
mi_zip = zipfile.ZipFile("archivo_comprimido.zip", 'w')

# Seleccionar archivos para comprimir
mi_zip.write("mi_texto_A.txt")
mi_zip.write("mi_texto_B.txt")

mi_zip.close()

# Descomprimir archivos
zip_abierto = zipfile.ZipFile("archivo_comprimido.zip", "r")
zip_abierto.extractall()

# Comprimir con Shutil
"""carpeta_origen = "C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 9\\Carpeta_Superior"
archivo_destino = "Todo_Comprimido"
shutil.make_archive(archivo_destino, "zip", carpeta_origen)"""

# Descomprimir con Shutil
shutil.unpack_archive("Todo_Comprimido.zip", "Extracion Terminada", "zip")
