import bs4
import requests

# Tomamos la url de la pagina, dandos cuenta que lo unico que cambia es el numero de pagina
url_base = "http://books.toscrape.com/catalogue/page-{}.html"

#print(url_base.format('4'))

# Con un ciclo vamos aumentando el numero de paginas
for n in range(1, 11):
    # Al string se lo colocamos con el metodo format para ir sacando varias urls de una
    print(url_base.format(n))
    