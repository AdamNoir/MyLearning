import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")

# Imprimira el codigo de la pagina en formato string, texto
#print(resultado.text)

# Podemos buscar en los diferentes ingrediente (Elementos) del codigo.
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
#print(sopa)

# De este modo podemos seleccionar una etiqueta del codigo de la pagina
print(sopa.select("title"))

# Al haber muchas estiquetas iguales nos traera una lista con todas ellas
# Podemos manipularla como una lista normal
print(sopa.select("h1"))

# Usando [0] y el metodo gettext podemos poder el contenido sin las etiquetas
# Podemos colocar entre corchetes cualquier indide [i]
print(sopa.select("title")[0].get_text())

parrafo_especial = sopa.select("p")
print(parrafo_especial)
