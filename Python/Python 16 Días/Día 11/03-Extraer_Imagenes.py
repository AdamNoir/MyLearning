import bs4
import requests

resultado = requests.get("https://www.escueladirecta.com/courses")

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

imagenes = sopa.select("img")
#print(imagenes)

#for i in imagenes:
#    print(i)

# Obtener Imagenes por clase
imagenes_cursos = sopa.select(".course-box-image")
# Iterar Lista de Imagenes
for i in imagenes_cursos:
    print(i)

# Obtener SOLO el enlace de la imagen
# Esto se puede poner en un Loop para scar todas las imagenes
descargar_imagen = sopa.select(".course-box-image")[0]["src"]
print(descargar_imagen)

# Descargamos la imagen PERO SOLO EL TIPO BINARIO
imagen_curso_descarga = requests.get(descargar_imagen)  # type: ignore
print(imagen_curso_descarga.content)

# De este modo tomamos el Binario y lo almacenamos en un archivo usable para los mortales
f = open("Mi_Imagen.jpg", "wb")
f.write(imagen_curso_descarga.content)
f.close()