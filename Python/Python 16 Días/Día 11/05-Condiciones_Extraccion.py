import bs4
import requests

url_base = "http://books.toscrape.com/catalogue/page-{}.html"

resultado = requests.get(url_base.format('1'))

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# Nos dimos cuenta que cada elemento se encentra dentro de un article
# Y este lleva por nombre product_pod
print(sopa.select(".product_pod"))

