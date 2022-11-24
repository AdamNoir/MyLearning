# Extraer Elementos de una Clase
"""
 - " Todos los Elementos con la etiqueta
 - # Elementos que contengan un id
 - . elementos que contengan una clase
 - (espacio) Cualquier Elemento espesificado dentro de otro elemento espesificado
 - > Cualquier elemento espesificado dentro de un elemento espesificado sin nada en el medio
"""
import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

# Obtener Clases
columna_lateral = sopa.select(".skip-navigation")
print(columna_lateral)

# Obtender todos los elementos espesificados dentro de otro elementos
columna_lateral2 = sopa.select(".skip-navigation a")
print(columna_lateral2)


