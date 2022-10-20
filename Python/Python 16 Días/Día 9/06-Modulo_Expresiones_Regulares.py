# MODULO EXPRESIONES REGULAES
"""
Una expresion regular es una secuencia de caracteres que forman un patron de busqueda
determinado. Pueden ser utilizadas para verificar String en busqueda de un contenido
espesifico.

- search(): devuelve un objeto "match" que contiene informacion acerca del
hallazgo si se encuentra en algun punto del string.
- findall(): devuelve una lista que contiene todos los hallazgos del patron.

Para formar patrones usamos los siguentes caracteres especiales y cauntificadores
- Cracteres especiales:
    - \d digito numerocio
    - \D NO numerico
    - \w caracter alfanumerico
    - \W NO alfanumerico
    - \s especio en blanco
    - \S NO espacio en blanco
- Cuantificadores
    - + 1 o mas veces 
    - {n} se repite n veces
    - {n ,m} se repite de n hasta m veces
    - {n ,} desde n hacia arriba
    - * 0 o mas veces
    - ? 1 o 0 veces
"""
import re

# Modo clasico
texto = "Si necesitas ayuda llama al  (658)-598-9977 las 24 horas al servicio de ayuda online"
palabra = "ayuda" in texto
print(palabra)

# Expresiones regulares
# Mostrara solo la primer coicidencia
patron = "ayuda"
busqueda = re.search(patron, texto)
# Objeto de tipo Regular Expresion
# Dice que encontro y el span (de que caracter a que caracter)
print(busqueda)
# Podemos acceder a propieades en concreto
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())

# Encontrar TODO
busqueda_todo = re.findall(patron, texto)
# Dara una lista con todo aquello que coincida
print(busqueda_todo)


# Busquedas con expresiones regulares
nuevo_texto = "Llama al 564-525-6588"

patron = r"\d\d\d-\d\d\d-\d\d\d\d"
resultado = re.search(patron, nuevo_texto)
print(resultado)
# Mostrara lo que encontro
print(resultado.group())

# Usando cuantificadores
patron_cuantificador = r"\d{3}-\d{3}-\d{4}"
resultado = re.search(patron_cuantificador, nuevo_texto)
print(resultado)

# Ejemplo con Claves
# Una calve que NO comience con dijito y tenga otros 7 alfanumericos
clave = input("Ingresa una Clave: ")
patron_clave = r"\D{1}\w{7}"
chequear = re.search(patron_clave, clave)
print(chequear)

# Una conicidencia u otra. Es como un or.
aviso = "No atendemos los martes por la tade"
buscar = re.search(r"lunes|martes", aviso)
print(buscar)

# Caracter cualquiera, al principio o final, digito, espacio, lo que sea
buscar = re.search(r"...demos...", aviso)
print(buscar)

# Caracter al principio
buscar = re.search(r"^\D", aviso)
print(buscar)

# Caracter al final
buscar = re.search(r"\D$", aviso)
print(buscar)

# Excluir
buscar = re.findall(r"[^\s]", aviso)
print(buscar)


